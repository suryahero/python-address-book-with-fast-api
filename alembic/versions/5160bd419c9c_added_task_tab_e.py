"""Added Task tab;e

Revision ID: 5160bd419c9c
Revises: c53f84c817a5
Create Date: 2022-08-06 13:15:35.441572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5160bd419c9c'
down_revision = 'c53f84c817a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
