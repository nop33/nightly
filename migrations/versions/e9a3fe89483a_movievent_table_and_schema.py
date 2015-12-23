"""Movievent table and schema

Revision ID: e9a3fe89483a
Revises: None
Create Date: 2015-12-23 12:22:38.940536

"""

# revision identifiers, used by Alembic.
revision = 'e9a3fe89483a'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.execute('CREATE SCHEMA nightly')
    op.create_table('movievents',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('date', sa.Date(), nullable=False),
                    sa.Column('time', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    schema='nightly')


def downgrade():
    op.drop_table('movievents', schema='nightly')
    op.execute('DROP SCHEMA events')
