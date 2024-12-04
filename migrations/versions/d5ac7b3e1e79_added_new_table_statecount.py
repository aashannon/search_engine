"""Added new table StateCount

Revision ID: d5ac7b3e1e79
Revises: cdf0a60c522d
Create Date: 2024-10-26 01:48:50.766522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5ac7b3e1e79'
down_revision = 'cdf0a60c522d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('state_count',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('state', sa.String(length=200), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('list_of_ids', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('state_count')
    # ### end Alembic commands ###
