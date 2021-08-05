"""empty message

Revision ID: d46e7ff1b1f2
Revises: 
Create Date: 2021-08-04 17:33:51.191722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd46e7ff1b1f2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('NFL', sa.Column('team_name', sa.VARCHAR(length=30), nullable=True))
    op.drop_column('NFL', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('NFL', sa.Column('name', sa.VARCHAR(length=30), autoincrement=False, nullable=True))
    op.drop_column('NFL', 'team_name')
    # ### end Alembic commands ###
