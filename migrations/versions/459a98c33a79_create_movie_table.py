"""Create Movie table

Revision ID: 459a98c33a79
Revises: e9a3fe89483a
Create Date: 2015-12-24 21:04:26.724200

"""

# revision identifiers, used by Alembic.
revision = '459a98c33a79'
down_revision = 'e9a3fe89483a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('movies',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('tmdb_id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(), nullable=False),
                    sa.Column('release_year', sa.Integer(), nullable=True),
                    sa.Column('poster_url', sa.String(), nullable=True),
                    sa.Column('movievent_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['movievent_id'],
                                            ['nightly.movievents.id']),
                    sa.PrimaryKeyConstraint('id'),
                    schema='nightly')
    op.create_index(op.f('ix_nightly_movies_release_year'), 'movies',
                    ['release_year'], unique=False, schema='nightly')
    op.create_index(op.f('ix_nightly_movies_title'), 'movies', ['title'],
                    unique=False, schema='nightly')
    op.create_index(op.f('ix_nightly_movies_tmdb_id'), 'movies', ['tmdb_id'],
                    unique=False, schema='nightly')


def downgrade():
    op.drop_index(op.f('ix_nightly_movies_tmdb_id'), table_name='movies',
                  schema='nightly')
    op.drop_index(op.f('ix_nightly_movies_title'), table_name='movies',
                  schema='nightly')
    op.drop_index(op.f('ix_nightly_movies_release_year'), table_name='movies',
                  schema='nightly')
    op.drop_table('movies', schema='nightly')
