"""Update column of the name for the group by removing unique=True

Revision ID: d002752d1c0e
Revises: bad9a54563cc
Create Date: 2017-11-06 17:11:35.827462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd002752d1c0e'
down_revision = 'bad9a54563cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('groups_name_key', 'groups', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('groups_name_key', 'groups', ['name'])
    # ### end Alembic commands ###
