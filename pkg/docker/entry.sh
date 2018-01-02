#!/usr/bin/env bash

########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2017, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
#########################################################################

export PGADMIN_SETUP_EMAIL=${PGADMIN_DEFAULT_EMAIL}
export PGADMIN_SETUP_PASSWORD=${PGADMIN_DEFAULT_PASSWORD}

j2 /templates/pgadmin4.conf.j2 > /etc/httpd/conf.d/pgadmin4.conf

rm /run/httpd/httpd.pid

/usr/sbin/httpd -D FOREGROUND
