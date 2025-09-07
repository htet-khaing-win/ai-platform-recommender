"""Added missing constraints to tools table

Revision ID: 87fcf325a4c7
Revises: 1e855c4e5880
Create Date: 2025-09-01 13:37:50.307392

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87fcf325a4c7'
down_revision: Union[str, Sequence[str], None] = '1e855c4e5880'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
