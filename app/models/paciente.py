from sqlalchemy import String, Date, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Paciente(Base):
    __tablename__ = "paciente"

    id_paciente: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(String(100))

    cpf: Mapped[str] = mapped_column(String(11), unique=True)

    telefone: Mapped[str] = mapped_column(String(20))

    email: Mapped[str] = mapped_column(String(100), unique=True)

    endereco: Mapped[str] = mapped_column(String(150))

    data_nascimento: Mapped[Date]

    perfil: Mapped[str] = mapped_column(String(50))

    tipo_usuario : Mapped[str] = mapped_column(String(10)) 
    
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
        back_populates="paciente"
    )

    exames = relationship(
        "Exame",
        back_populates="paciente"
    )