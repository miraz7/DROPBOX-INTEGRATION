"""user model update 

Revision ID: a59f3066d46d
Revises: 44f3872123bf
Create Date: 2024-01-20 20:47:28.457085

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a59f3066d46d'
down_revision: Union[str, None] = '44f3872123bf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('expires_at', sa.String(), nullable=True))
    op.add_column('user', sa.Column('uid', sa.String(), nullable=True))
    op.add_column('user', sa.Column('account_id', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'account_id')
    op.drop_column('user', 'uid')
    op.drop_column('user', 'expires_at')
    # ### end Alembic commands ###
