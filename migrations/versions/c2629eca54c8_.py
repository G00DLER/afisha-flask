"""empty message

Revision ID: c2629eca54c8
Revises: a355a7b1c32c
Create Date: 2022-12-15 22:27:58.704937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2629eca54c8'
down_revision = 'a355a7b1c32c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticket_name', sa.String(length=64), nullable=True),
    sa.Column('ticket_body', sa.String(length=600), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket')
    # ### end Alembic commands ###
