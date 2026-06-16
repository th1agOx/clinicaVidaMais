from app.database.connector import engine, SessionLocal

from app.database.base import Base

from app.models.plano_saude import PlanoSaude  
from app.models.consulta import Consulta        
from app.models.exame import Exame
from app.models.historico_atendimento import HistoricoAtendimento
from app.models.pagamento import Pagamento
from app.models.medico import Medico
from app.models.paciente import Paciente 

def populando_tabela_medico():
    print("Criando tabelas no SQLite via SQLAlchemy...")
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        print("Adicionando inserção")
        novo_medico = Medico(
            crm = "7163894",
            nome = "DRA. Flávia Hook",
            especialidade = "Pneumologia",
            email = "flaviahok@gmail.com",
            tipo_usuario = "medico"
        )
        db.add(novo_medico)
        db.commit()
        db.refresh(novo_medico)
        print(f"✅ Sucesso! Paciente gravado no SQLite com ID: {novo_medico.id_medico}")

    except Exception as e :
        db.rollback()

        print(f"Não foi possível popular a tabela medico, erro => {e}")
    finally :
        db.close()

if __name__ == "__main__":
    populando_tabela_medico()