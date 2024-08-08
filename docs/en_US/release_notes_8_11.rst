************
Version 8.11
************

Release date: 2024-08-25

This release contains a number of bug fixes and new features since the release of pgAdmin 4 v8.10.

Supported Database Servers
**************************
**PostgreSQL**: 12, 13, 14, 15, 16 and 17

**EDB Advanced Server**: 12, 13, 14, 15, and 16

Bundled PostgreSQL Utilities
****************************
**psql**, **pg_dump**, **pg_dumpall**, **pg_restore**: 16.3


New features
************


Housekeeping
************

  | `Issue #7776 <https://github.com/pgadmin-org/pgadmin4/issues/7776>`_ -  Introduce custom React Hook useSchemaState to simplify SchemaView component.

Bug fixes
*********

  | `Issue #7499 <https://github.com/pgadmin-org/pgadmin4/issues/7499>`_ -  Fixed an issue where refreshing the Schema Diff tool opened in a new tab caused an error.
  | `Issue #7540 <https://github.com/pgadmin-org/pgadmin4/issues/7540>`_ -  Fix server heartbeat logging error after deleting the server.
  | `Issue #7682 <https://github.com/pgadmin-org/pgadmin4/issues/7682>`_ -  Fixed an issue where the Generate Script ignored filter conditions when a parent node was selected.
  | `Issue #7683 <https://github.com/pgadmin-org/pgadmin4/issues/7683>`_ -  Fixed an issue where delete object(shortcut key) affecting both text and Object Explorer items.
  | `Issue #7728 <https://github.com/pgadmin-org/pgadmin4/issues/7728>`_ -  Updated the documentation for web server authentication.
  | `Issue #7737 <https://github.com/pgadmin-org/pgadmin4/issues/7737>`_ -  Fixed an issue where the REVOKE statement in the create script was throwing an error if the role contained special characters.
  | `Issue #7754 <https://github.com/pgadmin-org/pgadmin4/issues/7754>`_ -  Fix an issue where the wheel package is not getting installed on the arm64-based macOS version < 14.
  | `Issue #7775 <https://github.com/pgadmin-org/pgadmin4/issues/7775>`_ -  Fixed an issue where the value in the find box is not updating with selected text in editor if find is already open and re-triggered.
