# migrations/env.py - For project root structure
import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from dotenv import load_dotenv
from alembic import context

# Add backend/app to Python path since we run from project root
current_dir = os.path.dirname(os.path.abspath(__file__))  # /migrations
project_root = os.path.dirname(current_dir)              # /project-root
backend_app_path = os.path.join(project_root, 'backend', 'app')

# Add backend/app to Python path
sys.path.insert(0, backend_app_path)
print(f"Added to Python path: {backend_app_path}")

# Load environment variables from project root
dotenv_path = os.path.join(project_root, '.env')
load_dotenv(dotenv_path)
print(f"Loading .env from: {dotenv_path}")

# Now import your models from backend/app/database/models
try:
    from database.models import Base
    print("✅ Successfully imported Base from database.models")
    print(f"Found tables: {list(Base.metadata.tables.keys())}")
except ImportError as e:
    print(f"❌ Failed to import from database.models: {e}")
    print(f"Python path: {sys.path}")
    raise ImportError("Could not import Base from database.models")

# Alembic Config object
config = context.config

# Set the SQLAlchemy URL from environment variable  
database_url = os.getenv("DATABASE_URL")
if database_url:
    config.set_main_option("sqlalchemy.url", database_url)
    print(f"Database URL set: {database_url}")
else:
    raise ValueError("DATABASE_URL environment variable not found")

# Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Target metadata for autogenerate
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Remove +asyncpg for Alembic (sync only)
    url = config.get_main_option("sqlalchemy.url")
    if "+asyncpg" in url:
        url = url.replace("+asyncpg", "")
        print(f"Modified URL for Alembic (removed +asyncpg): {url}")
    
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = url
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()