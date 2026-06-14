from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class PlanoSaude(Base):
    __tablename__ = "plano_saude"

    id_plano: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    operadora: Mapped[str] = mapped_column(String(100))

    pacientes = relationship(
        "Paciente",
        back_populates="plano"
    )