"""empty message

Revision ID: 9ad04d9c6dde
Revises: c51757b2b32c
Create Date: 2022-02-15 17:06:02.766950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ad04d9c6dde'
down_revision = 'c51757b2b32c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('timestamp', sa.DateTime(), nullable=False))
    op.alter_column('comments', 'post_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    op.alter_column('comments', 'post_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('comments', 'timestamp')
    # ### end Alembic commands ###