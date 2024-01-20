"""your_migration_message

Revision ID: 2169f8782227
Revises: ef2b451e9d90
Create Date: 2024-01-19 19:46:19.332158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2169f8782227'
down_revision: Union[str, None] = 'ef2b451e9d90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
