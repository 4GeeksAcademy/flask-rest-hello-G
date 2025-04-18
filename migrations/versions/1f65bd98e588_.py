"""empty message

Revision ID: 1f65bd98e588
Revises: 337ed5ba7741
Create Date: 2025-04-15 21:28:47.885685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f65bd98e588'
down_revision = '337ed5ba7741'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=200), nullable=True))
        batch_op.add_column(sa.Column('content', sa.Text(), nullable=False))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('bio',
               existing_type=sa.TEXT(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('bio',
               existing_type=sa.TEXT(),
               nullable=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('content')
        batch_op.drop_column('image_url')

    op.drop_table('comment')
    op.drop_table('followers')
    # ### end Alembic commands ###
