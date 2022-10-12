

import subprocess
from datetime import datetime, timedelta
from threading import Lock

from flask import current_app


class PasswordExec:

    lock = Lock()

    def __init__(self, cmd, expiration_seconds = None, timeout = 60):
        self.cmd = str(cmd)
        self.expiration_seconds = int(expiration_seconds)
        self.timeout = int(timeout)
        self.password = None
        self.last_result = None

    def get(self):
        current_app.logger.info(f'passexec {type(self.expiration_seconds)}:{self.expiration_seconds} GET {self.cmd}')
        with self.lock:
            if not self.password or self.is_expired():
                if not self.cmd:
                    return None
                current_app.logger.info(f'Calling passexec')
                now = datetime.utcnow()
                p = subprocess.run(
                    self.cmd,
                    shell = True,
                    timeout = self.timeout,
                    capture_output = True,
                    text = True,
                    check = True,
                )
                self.last_result = now
                self.password = p.stdout.strip()
                current_app.logger.info(f'passexec generated {self.password}')
            return self.password

    def is_expired(self):
        if self.expiration_seconds == None:
            return False
        return self.last_result is not None and datetime.utcnow() - self.last_result >= timedelta(seconds=self.expiration_seconds)


