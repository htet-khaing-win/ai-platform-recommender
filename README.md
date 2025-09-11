# AI Platform Recommender

A FastAPI-based project that recommends workflows and tools for user goals.

## Features
- PostgreSQL database with Alembic migrations
- Async SQLAlchemy support
- CRUD API with FastAPI
- Pre-commit hooks for code quality
- Git Flow branching strategy

## Setup

- git clone https://github.com/yourusername/ai-platform-recommender.git
- cd ai-platform-recommender
- pip install -r requirements.txt
- uvicorn backend.app.main:app --reload


## Progress A – PostgreSQL Migration
- Installed and configured PostgreSQL
- Connected FastAPI to PostgreSQL using SQLAlchemy
- Migrated schema with indexes and foreign keys
- Wrote seeding and reset scripts
- Practiced raw SQL queries (SELECT, INSERT, JOIN, GROUP BY)
- Verified CRUD endpoints against PostgreSQL
- Used Git feature branching workflow for safe migration

## Progress B – Advanced Database Features
- Added async DB engine with SQLAlchemy + asyncpg
- Set up Alembic for schema migrations
- Learned PostgreSQL backup & restore (pg_dump / psql)
- Enhanced models with metadata, tags, timestamps
- Added constraints
- Set up pytest with DB fixtures for automated CRUD testing
