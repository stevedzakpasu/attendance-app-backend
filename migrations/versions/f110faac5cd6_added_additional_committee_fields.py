"""added additional committee fields

Revision ID: f110faac5cd6
Revises: e8faa782fa11
Create Date: 2023-01-08 21:25:54.766854

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'f110faac5cd6'
down_revision = 'e8faa782fa11'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('committee_1', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('member', sa.Column('committee_2', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('member', sa.Column('committee_3', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.drop_constraint('member_committee_fkey', 'member', type_='foreignkey')
    op.create_foreign_key(None, 'member', 'committee', ['committee_3'], ['name'])
    op.create_foreign_key(None, 'member', 'committee', ['committee_1'], ['name'])
    op.create_foreign_key(None, 'member', 'committee', ['committee_2'], ['name'])
    op.drop_column('member', 'committee')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('committee', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'member', type_='foreignkey')
    op.drop_constraint(None, 'member', type_='foreignkey')
    op.drop_constraint(None, 'member', type_='foreignkey')
    op.create_foreign_key('member_committee_fkey', 'member', 'committee', ['committee'], ['name'])
    op.drop_column('member', 'committee_3')
    op.drop_column('member', 'committee_2')
    op.drop_column('member', 'committee_1')
    # ### end Alembic commands ###