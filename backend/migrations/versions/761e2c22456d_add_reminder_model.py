"""Add Reminder model

Revision ID: 761e2c22456d
Revises: 4a5358d81eb6
Create Date: 2025-02-07 02:41:29.742453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '761e2c22456d'
down_revision = '4a5358d81eb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reminder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.String(length=200), nullable=False),
    sa.Column('time', sa.String(length=50), nullable=False),
    sa.Column('frequency', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reminder')
    # ### end Alembic commands ###
