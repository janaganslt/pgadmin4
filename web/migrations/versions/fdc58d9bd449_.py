##########################################################################
#
# pgAdmin 4 - PostgreSQL Tools
#
# Copyright (C) 2013 - 2023, The pgAdmin Development Team
# This software is released under the PostgreSQL Licence
#
##########################################################################

"""Initial database creation

Revision ID: fdc58d9bd449
Revises:
Create Date: 2017-03-13 11:15:16.401139

"""
import base64
import os

import config
import sqlalchemy as sa
from alembic import op
from flask import current_app
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.utils import hash_password
from pgadmin.model import db, User, Role
from pgadmin.setup import user_info

# revision identifiers, used by Alembic.
revision = 'fdc58d9bd449'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    email, password = user_info()

    version_table = op.create_table(
        'version', sa.Column('name', sa.String(length=32), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint('name'))

    user_table = op.create_table(
        'user',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('email', sa.String(length=256), nullable=False),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=False),
        sa.Column('confirmed_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'))

    with op.batch_alter_table("user") as batch_op:
        batch_op.create_unique_constraint('user_unique_constraint', ['email'])

    role_table = op.create_table(
        'role',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('description', sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'))

    op.create_table(
        'setting', sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('setting', sa.String(length=256), nullable=False),
        sa.Column('value', sa.String(length=1024), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('user_id', 'setting'))

    roles_users_table = op.create_table(
        'roles_users', sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'))

    server_group_table = op.create_table(
        'servergroup',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('user_id', 'name'))

    op.create_table(
        'server',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('servergroup_id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('host', sa.String(length=128), nullable=False),
        sa.Column('port', sa.Integer(), nullable=False),
        sa.Column('maintenance_db', sa.String(length=64), nullable=False),
        sa.Column('username', sa.String(length=64), nullable=False),
        sa.Column('ssl_mode', sa.String(length=16), nullable=False),
        sa.ForeignKeyConstraint(['servergroup_id'], ['servergroup.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id'))

    current_salt = getattr(
        config, 'SECURITY_PASSWORD_SALT', base64.urlsafe_b64encode(
            os.urandom(32)
        ).decode()
    )

    secret_key = getattr(
        config, 'SECRET_KEY', base64.urlsafe_b64encode(
            os.urandom(32)
        ).decode()
    )
    if current_app.extensions.get('security') is None:
        current_app.config['SECURITY_PASSWORD_SALT'] = current_salt
        current_app.config['SECRET_KEY'] = secret_key
        user_datastore = SQLAlchemyUserDatastore(db, User, Role)
        Security(current_app, user_datastore, register_blueprint=False)
    else:
        current_app.config['SECURITY_PASSWORD_SALT'] = current_salt
        current_app.config['SECRET_KEY'] = secret_key

    setattr(config, 'SECURITY_PASSWORD_SALT', current_salt)
    setattr(config, 'SECRET_KEY', secret_key)
    password = hash_password(password)

    op.bulk_insert(user_table,
                   [{'email': email, 'password': password,
                     'active': 1, 'confirmed_at': None}])

    op.bulk_insert(version_table,
                   [{'name': 'ConfigDB', 'value': 2}])

    op.bulk_insert(role_table,
                   [{'name': 'Administrators',
                     'description': 'pgAdmin Administrators Role'}])

    op.bulk_insert(roles_users_table,
                   [{'user_id': 1, 'role_id': 1}])

    op.bulk_insert(server_group_table,
                   [{'user_id': 1, 'name': 'Servers'}])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('server')
    op.drop_table('servergroup')
    op.drop_table('roles_users')
    op.drop_table('setting')
    op.drop_table('role')
    op.drop_table('user')
    op.drop_table('version')
    # ### end Alembic commands ###
