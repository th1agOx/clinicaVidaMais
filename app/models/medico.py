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

    crm: Mapped[str] = mapped_column(
        String(20),
        unique=True
    )

    nome: Mapped[str] = mapped_column(String(100))

    especialidade: Mapped[str] = mapped_column(
        String(100)
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    
    tipo_usuario : Mapped[str] = mapped_column(String(10)) 

    consultas = relationship(
        "Consulta",
        back_populates="medico"
    )