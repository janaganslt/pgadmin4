CREATE PUBLICATION test_publication_create
   FOR  TABLES IN SCHEMA test_schema_publication
   WITH (publish = 'insert, update, delete, truncate', publish_via_partition_root = false);