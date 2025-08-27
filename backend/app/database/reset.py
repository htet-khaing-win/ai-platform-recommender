import SessionLocal, engine
from models import Base

def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    reset_db()
    print(" Database reset complete")
