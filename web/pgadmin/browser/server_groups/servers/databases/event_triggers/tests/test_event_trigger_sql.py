##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2023, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################

import uuid
from pgadmin.browser.server_groups.servers.databases.schemas.tests import \
    utils as schema_utils
from pgadmin.browser.server_groups.servers.databases.tests import \
    utils as database_utils
from pgadmin.utils import server_utils
from pgadmin.utils.route import BaseTestGenerator
from regression import parent_node_dict
from regression import trigger_funcs_utils
from regression.python_test_utils import test_utils as utils
from . import utils as event_trigger_utils
from unittest.mock import patch


class EventTriggerGetSqlTestCase(BaseTestGenerator):
    """ This class will fetch added event trigger  sql under test database. """
    scenarios = utils.generate_scenarios('get_event_trigger_sql',
                                         event_trigger_utils.test_cases)

    def setUp(self):
        self.schema_data = parent_node_dict['schema'][-1]
        self.server_id = self.schema_data['server_id']
        self.db_id = self.schema_data['db_id']
        self.schema_name = self.schema_data['schema_name']
        self.schema_id = self.schema_data['schema_id']
        self.extension_name = "postgres_fdw"
        self.db_name = parent_node_dict["database"][-1]["db_name"]
        self.db_user = self.server["username"]
        self.func_name = "trigger_func_%s" % str(uuid.uuid4())[1:8]
        self.trigger_name = "event_trigger_get_%s" % (str(uuid.uuid4())[1:8])
        server_con = server_utils.connect_server(self, self.server_id)
        if not server_con["info"] == "Server connected.":
            raise Exception("Could not connect to server to add resource "
                            "groups.")
        server_version = 0
        if "type" in server_con["data"]:
            if server_con["data"]["version"] < 90300:
                message = "Event triggers are not supported by PG9.2 " \
                          "and PPAS9.2 and below."
                self.skipTest(message)
        self.function_info = trigger_funcs_utils.create_trigger_function(
            self.server, self.db_name, self.schema_name, self.func_name,
            server_version)
        self.event_trigger_id = event_trigger_utils.create_event_trigger(
            self.server, self.db_name, self.schema_name, self.func_name,
            self.trigger_name)

    def get_event_trigger_sql(self):
        """
        this function fetch event trigger sql
        :return: event trigger sql details
        """
        return self.tester.get(
            self.url +
            str(utils.SERVER_GROUP) + '/' + str(self.server_id) + '/' +
            str(self.db_id) + '/' + str(self.event_trigger_id),
            content_type='html/json'
        )

    def get_event_trigger_msql(self):
        """
        This function returns the modified sql
        :return: event trigger msql details
        """
        return self.tester.get(
            self.url +
            str(utils.SERVER_GROUP) + '/' + str(self.server_id) + '/' +
            str(self.db_id) + '/',
            content_type='html/json'
        )

    def runTest(self):
        """ This function will fetch added event trigger under test database.
        """
        db_con = database_utils.connect_database(self, utils.SERVER_GROUP,
                                                 self.server_id, self.db_id)
        if not db_con['data']["connected"]:
            raise Exception("Could not connect to database.")
        schema_response = schema_utils.verify_schemas(self.server,
                                                      self.db_name,
                                                      self.schema_name)
        if not schema_response:
            raise Exception("Could not find the schema.")
        func_name = self.function_info[1]
        func_response = trigger_funcs_utils.verify_trigger_function(
            self.server,
            self.db_name,
            func_name)
        if not func_response:
            raise Exception("Could not find the trigger function.")

        actual_response_code = True,
        expected_response_code = False
        if self.is_positive_test or hasattr(self, "msql"):
            response = self.get_event_trigger_sql()
            actual_response_code = response.status_code
            expected_response_code = self.expected_data['status_code']
        else:
            if hasattr(self, "error_fetching_event_trigger"):
                with patch(self.mock_data["function_name"],
                           return_value=eval(self.mock_data["return_value"])):
                    response = self.get_event_trigger_sql()
                    actual_response_code = response.status_code
                    expected_response_code = self.expected_data['status_code']
            if hasattr(self, "error_fetching_event_trigger_db"):
                with patch(self.mock_data["function_name"],
                           return_value=eval(self.mock_data["return_value"])):
                    response = self.get_event_trigger_sql()
                    actual_response_code = response.status_code
                    expected_response_code = self.expected_data['status_code']
            if hasattr(self, "error_fetching_event_trigger_msql"):
                response = self.get_event_trigger_msql()
                actual_response_code = response.status_code
                expected_response_code = self.expected_data['status_code']

        self.assertEqual(actual_response_code, expected_response_code)

    def tearDown(self):
        # Disconnect the database
        database_utils.disconnect_database(self, self.server_id, self.db_id)
