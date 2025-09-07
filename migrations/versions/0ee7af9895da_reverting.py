"""Reverting

Revision ID: 0ee7af9895da
Revises: 87fcf325a4c7
Create Date: 2025-09-01 13:41:15.556091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ee7af9895da'
down_revision: Union[str, Sequence[str], None] = '87fcf325a4c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint(
        constraint_name="uq_tool_name", 
        table_name="tools", 
        columns=["name"]
    )
    op.create_check_constraint(
        constraint_name="check_tool_name_length", 
        table_name="tools", 
        # For a CHECK constraint on a single column, use `columns` with the SQL.
        # Alternatively, for PostgreSQL, you can use `sqltext`.
        sqltext="char_length(name) > 2"
    )
    # ### end commands ###

def downgrade() -> None:
    # ### commands to manually add ###
    op.drop_constraint("uq_tool_name", "tools", type="unique")
    op.drop_constraint("check_tool_name_length", "tools", type="check")
    # ### end commands ###
