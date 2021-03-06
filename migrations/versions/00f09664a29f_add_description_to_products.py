"""add description to products

Revision ID: 00f09664a29f
Revises: 1f8fb5c3b8d6
Create Date: 2021-04-01 14:26:05.520984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00f09664a29f'
down_revision = '1f8fb5c3b8d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'description')
    # ### end Alembic commands ###
