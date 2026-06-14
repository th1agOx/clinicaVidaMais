from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Medico(Base):
    __tablename__ = "medico"

    id_medico: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    crm: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    especialidade: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    tipo_usuario : Mapped[str] = mapped_column(String(50), nullable=False) 

    consultas = relationship(
        "Consulta",
        back_populates="medico"
    )