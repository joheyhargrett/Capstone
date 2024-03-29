"""upgraded nullable value on product table

Revision ID: 3fa38ec061e7
Revises: 020a4fa693fb
Create Date: 2024-01-08 23:07:48.075864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fa38ec061e7'
down_revision = '020a4fa693fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('stock_quantity',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.alter_column('stock_quantity',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
