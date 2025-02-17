"""empty message

Revision ID: 312e938df670
Revises: 21f185cc44c4
Create Date: 2023-01-19 20:40:50.956276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '312e938df670'
down_revision = '21f185cc44c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('facts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('facts', sa.Text(), nullable=True))
        batch_op.drop_column('fact')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('facts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fact', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.drop_column('facts')

    # ### end Alembic commands ###
