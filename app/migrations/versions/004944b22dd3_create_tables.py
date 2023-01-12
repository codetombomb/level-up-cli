"""create tables

Revision ID: 004944b22dd3
Revises: 
Create Date: 2023-01-11 23:17:46.697916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '004944b22dd3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('fact_type', sa.String(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('month_day', sa.String(), nullable=True),
    sa.Column('year', sa.String(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fact_users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('fact_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fact_id'], ['facts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'fact_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fact_users')
    op.drop_table('users')
    op.drop_table('facts')
    # ### end Alembic commands ###