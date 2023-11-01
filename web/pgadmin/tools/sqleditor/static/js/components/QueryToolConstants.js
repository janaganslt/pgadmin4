/////////////////////////////////////////////////////////////
//
// pgAdmin 4 - PostgreSQL Tools
//
// Copyright (C) 2013 - 2023, The pgAdmin Development Team
// This software is released under the PostgreSQL Licence
//
//////////////////////////////////////////////////////////////
import gettext from 'sources/gettext';

export const QUERY_TOOL_EVENTS = {
  TRIGGER_STOP_EXECUTION: 'TRIGGER_STOP_EXECUTION',
  TRIGGER_EXECUTION: 'TRIGGER_EXECUTION',
  TRIGGER_LOAD_FILE: 'TRIGGER_LOAD_FILE',
  TRIGGER_SAVE_FILE: 'TRIGGER_SAVE_FILE',
  TRIGGER_SAVE_DATA: 'TRIGGER_SAVE_DATA',
  TRIGGER_DELETE_ROWS: 'TRIGGER_DELETE_ROWS',
  TRIGGER_COPY_DATA: 'TRIGGER_COPY_DATA',
  TRIGGER_ADD_ROWS: 'TRIGGER_ADD_ROWS',
  TRIGGER_RENDER_GEOMETRIES: 'TRIGGER_RENDER_GEOMETRIES',
  TRIGGER_SAVE_RESULTS: 'TRIGGER_SAVE_RESULTS',
  TRIGGER_SAVE_RESULTS_END: 'TRIGGER_SAVE_RESULTS_END',
  TRIGGER_PASTE_ROWS: 'TRIGGER_PASTE_ROWS',
  TRIGGER_QUERY_CHANGE: 'TRIGGER_QUERY_CHANGE',
  TRIGGER_INCLUDE_EXCLUDE_FILTER: 'TRIGGER_INCLUDE_EXCLUDE_FILTER',
  TRIGGER_REMOVE_FILTER: 'TRIGGER_REMOVE_FILTER',
  TRIGGER_SET_LIMIT: 'TRIGGER_SET_LIMIT',
  TRIGGER_FORMAT_SQL: 'TRIGGER_FORMAT_SQL',

  COPY_DATA: 'COPY_DATA',
  SET_LIMIT_VALUE: 'SET_LIMIT_VALUE',
  SET_CONNECTION_STATUS: 'SET_CONNECTION_STATUS',
  EXECUTION_START: 'EXECUTION_START',
  EXECUTION_END: 'EXECUTION_END',
  STOP_QUERY: 'STOP_QUERY',
  CURSOR_ACTIVITY: 'CURSOR_ACTIVITY',
  SET_MESSAGE: 'SET_MESSAGE',
  ROWS_FETCHED: 'ROWS_FETCHED',
  SELECTED_ROWS_COLS_CELL_CHANGED: 'SELECTED_ROWS_COLS_CELL_CHANGED',
  DATAGRID_CHANGED: 'DATAGRID_CHANGED',
  HIGHLIGHT_ERROR: 'HIGHLIGHT_ERROR',
  FOCUS_PANEL: 'FOCUS_PANEL',
  LOAD_FILE: 'LOAD_FILE',
  LOAD_FILE_DONE: 'LOAD_FILE_DONE',
  SAVE_FILE: 'SAVE_FILE',
  SAVE_FILE_DONE: 'SAVE_FILE_DONE',
  QUERY_CHANGED: 'QUERY_CHANGED',
  API_ERROR: 'API_ERROR',
  SAVE_DATA_DONE: 'SAVE_DATA_DONE',
  TASK_START: 'TASK_START',
  TASK_END: 'TASK_END',
  RENDER_GEOMETRIES: 'RENDER_GEOMETRIES',
  PUSH_NOTICE: 'PUSH_NOTICE',
  PUSH_HISTORY: 'PUSH_HISTORY',
  HANDLE_API_ERROR: 'HANDLE_API_ERROR',
  SET_FILTER_INFO: 'SET_FILTER_INFO',
  FETCH_MORE_ROWS: 'FETCH_MORE_ROWS',

  EDITOR_LAST_FOCUS: 'EDITOR_LAST_FOCUS',
  EDITOR_FIND_REPLACE: 'EDITOR_FIND_REPLACE',
  EDITOR_EXEC_CMD: 'EDITOR_EXEC_CMD',
  EDITOR_SET_SQL: 'EDITOR_SET_SQL',
  EDITOR_TOGGLE_CASE: 'EDITOR_TOGGLE_CASE',
  COPY_TO_EDITOR: 'COPY_TO_EDITOR',

  WARN_SAVE_DATA_CLOSE: 'WARN_SAVE_DATA_CLOSE',
  WARN_SAVE_TEXT_CLOSE: 'WARN_SAVE_TEXT_CLOSE',
  WARN_TXN_CLOSE: 'WARN_TXN_CLOSE',

  RESET_LAYOUT: 'RESET_LAYOUT',
  FORCE_CLOSE_PANEL: 'FORCE_CLOSE_PANEL',
  RESET_GRAPH_VISUALISER: 'RESET_GRAPH_VISUALISER',

  GOTO_LAST_SCROLL: 'GOTO_LAST_SCROLL',
};

export const CONNECTION_STATUS = {
  TRANSACTION_STATUS_IDLE: 0,
  TRANSACTION_STATUS_ACTIVE: 1,
  TRANSACTION_STATUS_INTRANS: 2,
  TRANSACTION_STATUS_INERROR: 3,
  TRANSACTION_STATUS_UNKNOWN: 4,
};

export const CONNECTION_STATUS_MESSAGE = {
  [CONNECTION_STATUS.TRANSACTION_STATUS_IDLE]: gettext('The session is idle and there is no current transaction.'),
  [CONNECTION_STATUS.TRANSACTION_STATUS_ACTIVE]: gettext('A command is currently in progress.'),
  [CONNECTION_STATUS.TRANSACTION_STATUS_INTRANS]: gettext('The session is idle in a valid transaction block.'),
  [CONNECTION_STATUS.TRANSACTION_STATUS_INERROR]: gettext('The session is idle in a failed transaction block.'),
  [CONNECTION_STATUS.TRANSACTION_STATUS_UNKNOWN]: gettext('The connection with the server is bad.')
};

export const PANELS = {
  QUERY: 'id-query',
  MESSAGES: 'id-messages',
  SCRATCH: 'id-scratch',
  DATA_OUTPUT: 'id-dataoutput',
  EXPLAIN: 'id-explain',
  GEOMETRY: 'id-geometry',
  NOTIFICATIONS: 'id-notifications',
  HISTORY: 'id-history',
  GRAPH_VISUALISER: 'id-graph-visualiser',
};

export const MAX_QUERY_LENGTH = 1000000;