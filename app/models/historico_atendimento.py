from datetime import datetime

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base

class HistoricoAtendimento(Base):
    __tablename__ = "historico_atendimento"

    id_historico: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    data_registro: Mapped[datetime] = mapped_column( DateTime, nullable=False)

    observacao: Mapped[str] = mapped_column(String(500))

    diagnostico: Mapped[str] = mapped_column(String(300), nullable=False)

    id_consulta: Mapped[int] = mapped_column(
        ForeignKey("consulta.id_consulta"),
        unique=True
    )

    consulta = relationship(
        "Consulta",
        back_populates="historico"
    )