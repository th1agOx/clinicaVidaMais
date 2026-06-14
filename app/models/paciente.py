from datetime import date

from sqlalchemy import (
    String, 
    Date, 
    Integer, 
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base

class Paciente(Base):
    __tablename__ = "paciente"

    id_paciente: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    cpf: Mapped[str] = mapped_column(String(15), unique=True, nullable=False)

    telefone: Mapped[str] = mapped_column(String(20), nullable=False)

    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    endereco: Mapped[str] = mapped_column(String(150), nullable=False)

    data_nascimento: Mapped[date] = mapped_column(Date, nullable=False)

    tipo_usuario: Mapped[str] = mapped_column(String(50), nullable=False)
    
    id_plano: Mapped[int | None] = mapped_column(
        ForeignKey("plano_saude.id_plano"),
        nullable=True
    )

    plano = relationship(
        "PlanoSaude",
        back_populates="pacientes"
    )

    consultas = relationship(
        "Consulta",
        back_populates="pacientes"
    )

    exames = relationship(
        "Exame",
        back_populates="pacientes"
    )