"""empty message

Revision ID: 0b2483085a84
Revises: f4b72ae50c22
Create Date: 2024-06-26 15:22:32.868186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b2483085a84'
down_revision = 'f4b72ae50c22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('address', sa.String(), nullable=True))
    op.drop_column('departments', 'location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('departments', sa.Column('location', sa.VARCHAR(), nullable=True))
    op.drop_column('departments', 'address')
    # ### end Alembic commands ###
