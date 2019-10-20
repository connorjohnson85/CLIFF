"""history model

Revision ID: f94c14924b1b
Revises: 307947ee6fb3
Create Date: 2019-10-17 09:53:10.647684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f94c14924b1b'
down_revision = '307947ee6fb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'history', 'user', ['user_id'], ['id'])
    op.drop_column('history', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('history', sa.Column('username', sa.VARCHAR(length=64), nullable=True))
    op.drop_constraint(None, 'history', type_='foreignkey')
    # ### end Alembic commands ###