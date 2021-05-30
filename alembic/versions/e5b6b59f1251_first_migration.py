"""First migration

Revision ID: e5b6b59f1251
Revises: 
Create Date: 2021-05-23 22:08:46.111167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5b6b59f1251'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('provider',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_provider_id'), 'provider', ['id'], unique=False)
    op.create_index(op.f('ix_provider_name'), 'provider', ['name'], unique=False)

    op.create_table('pair',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('provider_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['provider_id'], ['provider.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pair_id'), 'pair', ['id'], unique=False)
    op.create_index(op.f('ix_pair_name'), 'pair', ['name'], unique=False)

    op.create_table('trade',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('value', sa.Numeric(precision=18, scale=8), nullable=True),
        sa.Column('created', sa.DateTime(), nullable=False),
        sa.Column('updated', sa.DateTime(), nullable=False),
        sa.Column('pair_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['pair_id'], ['pair.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trade_id'), 'trade', ['id'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_trade_id'), table_name='trade')
    op.drop_table('trade')
    op.drop_index(op.f('ix_pair_name'), table_name='pair')
    op.drop_index(op.f('ix_pair_id'), table_name='pair')
    op.drop_table('pair')
    op.drop_index(op.f('ix_provider_name'), table_name='provider')
    op.drop_index(op.f('ix_provider_id'), table_name='provider')
    op.drop_table('provider')
