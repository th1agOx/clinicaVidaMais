from app.database.connector import engine, SessionLocal

from app.database.base import Base

from app.models.plano_saude import PlanoSaude  
from app.models.consulta import Consulta        
from app.models.exame import Exame
from app.models.historico_atendimento import HistoricoAtendimento
from app.models.pagamento import Pagamento
from app.models.medico import Medico
from app.models.paciente import Paciente 