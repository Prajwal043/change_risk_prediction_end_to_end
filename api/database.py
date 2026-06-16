from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql://postgres:postgres@localhost:5432/change_risk_db"
)

engine = create_engine(
    DATABASE_URL
)