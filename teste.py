from app.database.connector import engine, SessionLocal

from app.database.base import Base

from app.models.plano_saude import PlanoSaude  
from app.models.consulta import Consulta        
from app.models.exame import Exame
from app.models.historico_atendimento import HistoricoAtendimento
from app.models.pagamento import Pagamento
from app.models.medico import Medico
from app.models.paciente import Paciente 

from datetime import date

def testar_aplicacao_completa():
    print("Criando tabelas no SQLite via SQLAlchemy...")
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        print("Testando inserção do ORM...")
        novo_paciente = Paciente( 
            nome = "Thiago",
            cpf = "123.123.321-09",
            telefone = "21900204916",
            email = "thiago@gmail.com",
            endereco = "rua teste, bairro alto do python, cidade alambic",
            data_nascimento = date(1999, 9, 9),
            tipo_usuario = "paciente",
            id_paciente = None
        )
        db.add(novo_paciente)
        db.commit()
        db.refresh(novo_paciente)
        print(f"✅ Sucesso! Paciente gravado no SQLite com ID: {novo_paciente.id_paciente}")
        print(f"✅ Iniciandi metodo de busca de paciente por cpf: {paciente_buscado.cpf}")

        paciente_buscado = db.query(Paciente).filter_by(cpf="123.123.321-09").first()

        assert paciente_buscado is not None
        assert paciente_buscado.nome == "Thiago"
        print("✅ Teste de SELECT funcionou perfeitamente com inserção prévia!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Erro no teste: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    testar_aplicacao_completa()
