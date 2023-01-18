##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2023, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
#########################################################################

"""Server heartbeat manager."""


import threading
import datetime
import config
from flask import session, current_app


def log_server_heartbeat(data):
    """Log Server Heartbeat."""
    from config import PG_DEFAULT_DRIVER
    from pgadmin.utils.driver import get_driver
    manager = get_driver(PG_DEFAULT_DRIVER).connection_manager(int(data['sid'])
                                                               )

    _server_heartbeat = getattr(current_app, '_pgadmin_server_heartbeat', {})

    if session.sid not in _server_heartbeat:
        _server_heartbeat[session.sid] = {}

    _server_heartbeat[session.sid][data['sid']] = {
        'timestamp': datetime.datetime.now(),
        'conn': manager.connections
    }

    setattr(current_app, '_pgadmin_server_heartbeat', _server_heartbeat)

    current_app.logger.debug(
        "Heartbeat logged for the server id : %s" % data['sid'])


def get_server_heartbeat(server_id):
    _server_heartbeat = getattr(current_app, '_pgadmin_server_heartbeat', {})

    if session.sid in _server_heartbeat and server_id in _server_heartbeat[
            session.sid]:
        return _server_heartbeat[session.sid][server_id]
    else:
        return None


class startServerHeartbeatTimer():
    def __init__(self, sec, _app):
        def func_wrapper():
            self.t = threading.Timer(sec, func_wrapper)
            self.t.start()
            self.release_server_heartbeat()
        self.t = threading.Timer(sec, func_wrapper)
        self.t.start()
        self._app = _app

    def release_server_heartbeat(self):
        with self._app.app_context():
            _server_heartbeat = getattr(self._app,
                                        '_pgadmin_server_heartbeat', {})
            if len(_server_heartbeat) > 0:
                for sess_id in list(_server_heartbeat):
                    for sid in list(_server_heartbeat[sess_id]):
                        last_heartbeat_time = _server_heartbeat[sess_id][sid][
                            'timestamp']
                        current_time = datetime.datetime.now()
                        diff = current_time - last_heartbeat_time

                        # Wait for 4 times then the timeout
                        if diff.total_seconds() > (
                                config.SERVER_HEARTBEAT_TIMEOUT * 4):
                            server_conn = _server_heartbeat[sess_id
                                                            ][sid]['conn']
                            for d in server_conn:
                                server_conn[d]._release()
                                current_app.logger.debug(
                                    "Heartbeat not received. Released"
                                    " connection for the server id : %s" % sid)
                            _server_heartbeat[sess_id].pop(sid)
                            if len(_server_heartbeat[sess_id]) == 0:
                                _server_heartbeat.pop(sess_id)
                setattr(self._app, '_pgadmin_server_heartbeat',
                        _server_heartbeat)

    def cancel(self):
        self.t.cancel()


def init_app(app):
    setattr(app, '_pgadmin_server_heartbeat', {})
    startServerHeartbeatTimer(sec=config.SERVER_HEARTBEAT_TIMEOUT,
                              _app=app)
