from datetime import date

from sqlalchemy import (
    Integer,
    String,
    Date,
    Enum,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base

from app.enums.tipo_exame import TipoExame
from app.enums.resultado_exame import ResultadoExame

class Exame(Base):
    __tablename__ = "exame"

    id_exame: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    tipo: Mapped[TipoExame] = mapped_column(Enum(TipoExame))

    data_solicitacao: Mapped[date] = mapped_column(Date, nullable=False)

    data_resultado: Mapped[date | None] = mapped_column(Date, nullable=True)

    resultado: Mapped[ResultadoExame | None] = mapped_column(
        Enum(ResultadoExame),
        nullable=True
    )

    observacao: Mapped[str] = mapped_column(
        String(500)
    )

    id_paciente: Mapped[int] = mapped_column(
        ForeignKey("paciente.id_paciente")
    )

    pacientes = relationship(
        "Paciente",
        back_populates="exames"
    )