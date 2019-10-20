"""History model

Revision ID: e4483aedc097
Revises: 80c52c6a5d6f
Create Date: 2019-10-17 09:46:38.626218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4483aedc097'
down_revision = '80c52c6a5d6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('command', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_history_command'), 'history', ['command'], unique=False)
    op.create_index(op.f('ix_history_username'), 'history', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_history_username'), table_name='history')
    op.drop_index(op.f('ix_history_command'), table_name='history')
    op.drop_table('history')
    # ### end Alembic commands ###