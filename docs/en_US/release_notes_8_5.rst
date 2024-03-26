***********
Version 8.5
***********

Release date: 2024-04-04

This release contains a number of bug fixes and new features since the release of pgAdmin 4 v8.5.

Supported Database Servers
**************************
**PostgreSQL**: 12, 13, 14, 15, and 16

**EDB Advanced Server**: 12, 13, 14, 15, and 16

Bundled PostgreSQL Utilities
****************************
**psql**, **pg_dump**, **pg_dumpall**, **pg_restore**: 16.1


New features
************

  | `Issue #5611 <https://github.com/pgadmin-org/pgadmin4/issues/5611>`_ -  Added support for provider, deterministic, version and RULES parameter while creating collation.
  | `Issue #7098 <https://github.com/pgadmin-org/pgadmin4/issues/7098>`_ -  Added support for EDB Job Scheduler.
  | `Issue #7221 <https://github.com/pgadmin-org/pgadmin4/issues/7221>`_ -  Added support for UNIX socket in entrypoint.sh for Docker implementation.

Housekeeping
************


Bug fixes
*********

  | `Issue #4413 <https://github.com/pgadmin-org/pgadmin4/issues/4413>`_ -  Fixed an issue in Schema Diff where Columns with sequences get altered unnecessarily.
  | `Issue #7116 <https://github.com/pgadmin-org/pgadmin4/issues/7116>`_ -  Bug fixes and improvements in pgAdmin CLI.
  | `Issue #7165 <https://github.com/pgadmin-org/pgadmin4/issues/7165>`_ -  Fixed schema diff wrong query generation for table, foreign table and sequence.
  | `Issue #7229 <https://github.com/pgadmin-org/pgadmin4/issues/7229>`_ -  Fix an issue in table dialog where changing column name was not syncing table constraints appropriately.
  | `Issue #7255 <https://github.com/pgadmin-org/pgadmin4/issues/7255>`_ -  Fixed an issue where taking backup of a shared server was using server owner's user name.
  | `Issue #7262 <https://github.com/pgadmin-org/pgadmin4/issues/7262>`_ -  Fix an issue in editor where replace option in query tool edit menu is not working on non-Mac OS.
  | `Issue #7268 <https://github.com/pgadmin-org/pgadmin4/issues/7268>`_ -  Fix an issue in editor where Format SQL shortcut and multiline selection are not working.
  | `Issue #7269 <https://github.com/pgadmin-org/pgadmin4/issues/7269>`_ -  Fix an issue in editor where "Use Spaces?" Preference of Editor is not working.
  | `Issue #7271 <https://github.com/pgadmin-org/pgadmin4/issues/7271>`_ -  Fixed an issue where Triggers, Rules, Indexes were absent from the Schema Diff when comparing views.
  | `Issue #7277 <https://github.com/pgadmin-org/pgadmin4/issues/7277>`_ -  Fix an issue in query tool where toggle case of selected text loses selection.
  | `Issue #7299 <https://github.com/pgadmin-org/pgadmin4/issues/7299>`_ -  Fix query tool autocomplete results when cursor is in between the SQL query.
  | `Issue #7305 <https://github.com/pgadmin-org/pgadmin4/issues/7305>`_ -  Fix an issue in query tool where custom keyboard shortcuts are not working for some.
  | `Issue #7308 <https://github.com/pgadmin-org/pgadmin4/issues/7308>`_ -  Fixed issue related to email authentication of Two-factor authentication.
