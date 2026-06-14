from datetime import date  
from decimal import Decimal

from sqlalchemy.orm import (
    Mapped, 
    mapped_column
)

from sqlalchemy import (
    Date, 
    Integer, 
    ForeignKey, 
    Numeric, 
    Enum
)

from app.database.base import Base
from app.enums.status_pagamento import StatusPagamento
from app.enums.tipo_pagamento import TipoPagamento

class Pagamento(Base):
    __tablename__ = "pagamento"

    id_pagamento: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    valor: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    data_emissao: Mapped[date] = mapped_column(Date, nullable=False)
    
    data_vencimento: Mapped[date] = mapped_column(Date, nullable=False)

    data_pagamento: Mapped[date] = mapped_column(Date, nullable=False)

    status: Mapped[StatusPagamento] = mapped_column(
        Enum(StatusPagamento),
        nullable=False
    )

    tipo: Mapped[TipoPagamento] = mapped_column(
        Enum(TipoPagamento),
        nullable=False
    )

    id_paciente: Mapped[int] = mapped_column(
        ForeignKey("paciente.id_paciente")
    )

    id_consulta: Mapped[int] = mapped_column(
        ForeignKey("consulta.id_consulta"),
        unique=True
    )