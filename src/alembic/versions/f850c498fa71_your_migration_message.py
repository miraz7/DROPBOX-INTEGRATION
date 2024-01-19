"""your_migration_message

Revision ID: f850c498fa71
Revises: 2169f8782227
Create Date: 2024-01-19 19:47:28.034716

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f850c498fa71'
down_revision: Union[str, None] = '2169f8782227'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
