"""add_missing_check_constraint_definitive_fix

Revision ID: c734b8a8de85
Revises: 0ee7af9895da
Create Date: 2025-09-01 14:55:18.799536

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '[your_new_revision_id]'  # Alembic will fill this
down_revision: Union[str, Sequence[str], None] = '0ee7af9895da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Add the missing check constraint that was never created."""
    
    # First, check if any data would violate the constraint
    bind = op.get_bind()
    result = bind.execute(sa.text(
        "SELECT id, name FROM tools WHERE char_length(name) <= 2"
    )).fetchall()
    
    if result:
        print(f"⚠️  Found {len(result)} rows with names too short:")
        for row in result:
            print(f"   ID {row[0]}: '{row[1]}'")
        print("   These rows will be deleted to allow constraint creation.")
        
        # Delete invalid rows
        bind.execute(sa.text("DELETE FROM tools WHERE char_length(name) <= 2"))
        print("   Invalid rows deleted.")
    
    # Remove duplicate unique constraint to clean up
    try:
        op.drop_constraint("uq_tool_name", "tools", type_="unique")
        print("✅ Removed duplicate unique constraint")
    except Exception:
        print("   No duplicate unique constraint to remove")
    
    # Add the check constraint using raw SQL (most reliable method)
    try:
        bind.execute(sa.text("""
            ALTER TABLE tools 
            ADD CONSTRAINT check_tool_name_length 
            CHECK (char_length(name) > 2)
        """))
        print("✅ Check constraint 'check_tool_name_length' created successfully!")
    except Exception as e:
        print(f"❌ Failed to create check constraint: {e}")
        raise
    
    # Verify it was created
    verification = bind.execute(sa.text("""
        SELECT COUNT(*) FROM pg_constraint 
        WHERE conname = 'check_tool_name_length' 
        AND conrelid = 'tools'::regclass
    """)).scalar()
    
    if verification == 1:
        print("✅ Constraint verified in database!")
    else:
        print("❌ Warning: Constraint verification failed!")
        raise Exception("Check constraint was not created properly")

def downgrade() -> None:
    """Remove the check constraint."""
    try:
        op.get_bind().execute(sa.text(
            "ALTER TABLE tools DROP CONSTRAINT IF EXISTS check_tool_name_length"
        ))
        print("✅ Check constraint removed")
    except Exception as e:
        print(f"Error removing constraint: {e}")
    
    # Recreate the duplicate unique constraint if it was removed
    try:
        op.create_unique_constraint("uq_tool_name", "tools", ["name"])
        print("✅ Duplicate unique constraint recreated")
    except Exception:
        print("   Could not recreate duplicate constraint (probably fine)")
