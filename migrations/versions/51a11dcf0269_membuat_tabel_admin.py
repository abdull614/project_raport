"""membuat tabel admin

Revision ID: 51a11dcf0269
Revises: 6caca7333a61
Create Date: 2024-11-04 13:34:05.287573

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51a11dcf0269'
down_revision = '6caca7333a61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id_admin', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('id_guru', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['id_guru'], ['guru.id_guru'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_admin'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    # ### end Alembic commands ###
