***********
Version 7.5
***********

Release date: 2023-07-27

This release contains a number of bug fixes and new features since the release of pgAdmin 4 v7.4.

Supported Database Servers
**************************
**PostgreSQL**: 11, 12, 13, 14 and 15

**EDB Advanced Server**: 11, 12, 13, 14 and 15

Bundled PostgreSQL Utilities
****************************
**psql**, **pg_dump**, **pg_dumpall**, **pg_restore**: 15.3


New features
************

  | `Issue #6369 <https://github.com/pgadmin-org/pgadmin4/issues/6369>`_ -  Added support to detach partitions using concurrently and finalize.
  | `Issue #6416 <https://github.com/pgadmin-org/pgadmin4/issues/6416>`_ -  Added new/missing parameters to pg_dumpall (Backup Server).
  | `Issue #6417 <https://github.com/pgadmin-org/pgadmin4/issues/6417>`_ -  Added new/missing parameters to pg_dump (Backup Objects).

Housekeeping
************

  | `Issue #6295 <https://github.com/pgadmin-org/pgadmin4/issues/6295>`_ -  Remove Bootstrap and jQuery from authentication pages and rewrite them in ReactJS.
  | `Issue #6423 <https://github.com/pgadmin-org/pgadmin4/issues/6423>`_ -  Clarify the LICENSE file to indicate that it is the PostgreSQL Licence.
  | `Issue #6532 <https://github.com/pgadmin-org/pgadmin4/issues/6532>`_ -  Remove unsupported PostgreSQL versions from the container.

Bug fixes
*********

  | `Issue #6163 <https://github.com/pgadmin-org/pgadmin4/issues/6163>`_ -  Fix an issue where queries can't complete execution.
  | `Issue #6165 <https://github.com/pgadmin-org/pgadmin4/issues/6165>`_ -  Fixed an issue where Import Export not working when using pgpassfile.
  | `Issue #6317 <https://github.com/pgadmin-org/pgadmin4/issues/6317>`_ -  Fix an issue where queries longer than 1 minute get stuck - Container 7.1
  | `Issue #6356 <https://github.com/pgadmin-org/pgadmin4/issues/6356>`_ -  Fix an issue where queries get stuck with auto-completion enabled.
  | `Issue #6364 <https://github.com/pgadmin-org/pgadmin4/issues/6364>`_ -  Fixed Query Tool/ PSQL tool tab title not getting updated on database rename.
  | `Issue #6501 <https://github.com/pgadmin-org/pgadmin4/issues/6501>`_ -  Fix the query tool auto-complete issue on the server reconnection.
  | `Issue #6502 <https://github.com/pgadmin-org/pgadmin4/issues/6502>`_ -  Fix the query tool restore connection issue.
  | `Issue #6509 <https://github.com/pgadmin-org/pgadmin4/issues/6509>`_ -  Fix the reconnecton issue if the PostgreSQL server is restarted from the backend.
  | `Issue #6514 <https://github.com/pgadmin-org/pgadmin4/issues/6514>`_ -  Fix the connection and stability issues since v7, possibly related to background schema changes.
  | `Issue #6515 <https://github.com/pgadmin-org/pgadmin4/issues/6515>`_ -  Fixed an issue where the query tool is unable to execute a query on Postgres 10 and below versions.
  | `Issue #6524 <https://github.com/pgadmin-org/pgadmin4/issues/6524>`_ -  Fix the lost connection error in v7.4.
