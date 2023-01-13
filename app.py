import sqlalchemy
from sqlalchemy import String, Integer, Float
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.schema import Column
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask, render_template, redirect, request

engine = sqlalchemy.create_engine('sqlite:///Nico.db',echo=True,connect_args={'check_same_thread': False})
Base = declarative_base()
class Pessoa(Base):
    __tablename__ = 'contato' # campo obrigatório
    id = Column(Integer, primary_key=True) # campo obrigatório
    nome = Column(String(100))
    email = Column(String(100))
    celular= Column(String(100))
    tags = Column(String(100))

Base.metadata.create_all(engine)

app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)
link_tags = {
    "Trabalho":'https://cdn-icons-png.flaticon.com/512/8347/8347468.png',
    "Familia":'https://cdn-icons-png.flaticon.com/512/3636/3636519.png',
    "Compras":'https://cdn-icons-png.flaticon.com/512/3144/3144456.png'
}
#------------- FUNÇÕES -------------
#criar contato
def criar_contato_sql(contato: Pessoa):
  Session = sessionmaker(bind=engine)
  session = Session()
#criando a sessão 
  session.add(contato)
  session.commit()
  return 'sucess'
#deletar contato
@app.route('/deletar_contato',methods=['POST',])
def deletar_contato_sql(id):
  Session = sessionmaker(bind=engine)
  session = Session()
  contato_del = session.query(Pessoa).filter_by(id=id).first()
  session.delete(contato_del)
  session.commit()
  return 'sucess'
@app.route('/buscar_contato',methods=['POST',])
def buscar_contato_sql():
    Session = sessionmaker(bind=engine)
    session = Session()
    contatos = session.query(Pessoa).all()
    return contatos

#salvar contato
#@app.route('/salvar_contato',methods=['POST',])
def salvar_contato():
  cont = Pessoa(nome=request.form['nome'],
                email=request.form['email'],
                celular=request.form['celular'],
                tags=request.form['tags'],
                links='familia')
  criar_contato_sql(cont)
  return redirect('/')


#commit de info com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

#----------- ADD CONTATOS DIRETO NO BANCO ---------
contato1= Pessoa( nome='Ronaldo', email='ronaldo@gmail.com', celular='2390-1231', tags='familia')
contato2= Pessoa( nome='joao', email='joao@gmail.com', celular='2312-1290', tags='familia')
contato3= Pessoa( nome='cleber', email='cleber@gmail.com', celular='2312-1091', tags='familia')
contato4= Pessoa( nome='richard', email='richard@gmail.com', celular='2009-1209', tags='familia')
contato5= Pessoa( nome='patricia', email='patricia@gmail.com', celular='2002-1231', tags='familia')
contato6= Pessoa( nome='kingo', email='kingo@gmail.com', celular='2312-1224', tags='familia')
contato7= Pessoa( nome='xandao', email='xandao@gmail.com', celular='2312-1212', tags='familia')
contato8= Pessoa( nome='maiara', email='maiara@gmail.com', celular='2312-1581', tags='familia')
contato9= Pessoa( nome='maraisa', email='maraisa@gmail.com', celular='2312-1241', tags='familia')
contato10= Pessoa(nome='americanas', email='americanas@gmail.com', celular='2323-1211', tags='familia')
contato11= Pessoa(nome='teresinha', email='teresinha@gmail.com', celular='2363-1541', tags='familia')
contato12= Pessoa( nome='rodney', email='rodney@gmail.com', celular='2326-1341', tags='familia')
contato13= Pessoa(nome='Rubens', email='Rubens@gmail.com', celular='2982-1231', tags='familia')
contato14= Pessoa( nome='Rodolfo', email='Rodolfo@gmail.com', celular='2542-1231', tags='familia')
contato15= Pessoa( nome='Rinaldo', email='Rinaldo@gmail.com', celular='2312-1231', tags='familia')
contato16= Pessoa( nome='Richardson', email='Richardson@gmail.com', celular='2534-1241', tags='familia')
contato17= Pessoa( nome='Rosvaldo', email='Rosvaldo@gmail.com', celular='2123-1231', tags='familia')




#adicionar o objeto criado
session.add(contato1)
session.add(contato2)
session.add(contato3)
session.add(contato4)
session.add(contato5)
session.add(contato6)
session.add(contato7)
session.add(contato8)
session.add(contato9)
session.add(contato10)
session.add(contato11)
session.add(contato12)
session.add(contato13)
session.add(contato14)
session.add(contato15)
session.add(contato16)
session.add(contato17)


#commit no final
session.commit()


app.run(host = '0.0.0.0', debug=False, Port = 81)