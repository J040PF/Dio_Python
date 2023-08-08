from sqlalchemy.orm import declarative_base, Session, relationship
from sqlalchemy import Column, create_engine, select, func, inspect
from sqlalchemy import Integer, String, ForeignKey, DECIMAL

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    name = Column(String)  
    cpf = Column(String) 
    endereco = Column(String)
    contas = relationship("Conta", back_populates="cliente", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Cliente(id = {self.id}, name = {self.name}, cpf = {self.cpf}, endereco = {self.endereco})"  


class Conta(Base):
    __tablename__ = "conta"

    id = Column(Integer, primary_key=True, autoincrement=True)  
    tipo = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)  
    saldo = Column(Integer)
    
    cliente = relationship("Cliente", back_populates="contas")  

    def __repr__(self):
        return f"Conta(id = {self.id}, agencia = {self.agencia}, num = {self.num}, id_cliente = {self.id_cliente}, saldo = {self.saldo})"  


# conexao com banco de dados
engine = create_engine("sqlite:///")

# criando classes como tabela banco de dados
Base.metadata.create_all(engine)


with Session(engine) as session:
    juliana = Cliente(
        name = 'juliana',
        cpf ='123456789',
        endereco = 'rua bla bla bla',
        contas = [Conta(tipo='corrente', agencia= '001', saldo = 10)]
    )

    sandy = Cliente(
        name= 'sandy',
        cpf='987654321',
        endereco = 'rua tal tal',
        contas=[Conta(tipo='corrente', agencia= '001', saldo = 100)]
    )

    session.add_all([juliana, sandy])
    session.commit()


# todas os clientes
order = select(Cliente).order_by(Cliente.name)
print("Todos os clientes\n")
for result in session.scalars(order):
    print(f"{result.id} = {result.name}\n")

respond = input('Deseja recuperar dados de algum cliente ?\n')

# recupera cliente
stmt = select(Cliente).where(Cliente.id.in_([respond]))
for user in session.scalars(stmt):
    print(user)

# recupera dados da conta
stmt_contas = select(Conta).where(Conta.id_cliente.in_([respond]))
for conta in session.scalars(stmt_contas):
    print(conta)
