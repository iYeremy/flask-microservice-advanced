from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

from sqlalchemy import Column, DateTime, Float, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

BASE_DIR = Path(__file__).resolve().parent
RUTA_DB = BASE_DIR / "instance" / "growth.db"

motor = create_engine(f"sqlite:///{RUTA_DB}", future=True, echo=False)
SesionLocal = sessionmaker(bind=motor, autoflush=False, autocommit=False)
Base = declarative_base()


class Simulacion(Base):
    __tablename__ = "simulaciones"

    id = Column(Integer, primary_key=True)
    horas_luz = Column(Float, nullable=False)
    nivel_riego = Column(Float, nullable=False)
    puntaje_crecimiento = Column(Float, nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow, nullable=False)


def inicializar_bd() -> None:
    """Asegura que exista el directorio y crea las tablas necesarias."""
    RUTA_DB.parent.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(bind=motor)


@contextmanager
def sesion_bd():
    session = SesionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
