from config import *
from .models.base import Base
from .models.horarios import Horarios
from .models.usuarios import Usuarios
from .models.ativacoes import Ativacoes
from .models.diasdasemana import DiasDaSemana
from .models.usuarios import Usuarios
    
def create_tables():
   if not inspect(db.engine).has_table('Usuarios'):
      db.create_all()
      Base.metadata.create_all(engine)
      print("tabelas criadas com sucesso")

      senha = "123456"
      email = "joao.exemplo@gmail.com"

      admin = Usuarios(matricula = "admin", senha = senha, email = email)
      db.session.add(admin)
      db.session.commit()
      db.session.close()

with app.app_context():
      create_tables()
      
@app.route("/", methods= ["GET","POST"])
def login():
   if "logged_in" in session:
         return redirect(url_for('tela_principal'))
   
   if request.method == "POST":
      matriculaUsuario = request.form['matricula']
      senhaUsuario = request.form['senha']
      usuario = db.session.query(Usuarios).filter_by(matricula=matriculaUsuario, senha = senhaUsuario).first()
      if usuario:
         session['logged_in'] = True
         return redirect(url_for('tela_principal'))
   return render_template ('login.html')

@app.route("/tela_principal")
def tela_principal():
   if 'logged_in' in session:
      # exibe = exibir_horarios()

      return render_template('tela_principal.html')
   else:
      return redirect(url_for('login'))

@app.route("/cadastro_horarios")
def  cadastra_horarios():
   return render_template('cadastro_horarios.html')

@app.route("/logout")
def logout():
   if 'logged_in' in session:
      session.pop('logged_in', None)
   return redirect(url_for('login'))

@app.route("/horarios")
def horarios():
   return render_template('horarios.html')

@app.route("/horario_semana")
def horario_semana():
   return render_template('horario_semana.html')

@app.route("/cadastro", methods = ["GET","POST"])
def cadastro():
   if 'logged_in' in session:
      if request.method == "POST":
         matriculaUsuario = request.form["matricula"]
         senhaUsuario = request.form["senha"]
         usuario = Usuarios(matricula = matriculaUsuario,senha = senhaUsuario)
         db.session.add(usuario)
         db.session.commit()
         checar = db.session.query(Usuarios).filter_by(matricula = matriculaUsuario).all()
         for usuario in checar:
            # mensagem de confirmação de cadastro
            print(f"ID: {usuario.chave}, Matricula: {usuario.matricula}")
         db.session.close()
      return render_template('cadastro.html')
   else:
      return redirect(url_for('login'))

      
@app.route("/receber_dados", methods=["POST"])
def receber_dados():
   dados_recebidos = request.json
   horario = dados_recebidos['horario']
   
   print(dados_recebidos)

   dia = horario['dia']
   hora = horario['hora']
   minuto = horario['minuto']
   
   horario_enviar = Horarios(diaSemana = dia, hora = hora, minuto = minuto)
   db.session.add(horario_enviar)
   db.session.commit()
   db.session.close()

   return jsonify({'mensagem': 'Dados recebidos com sucesso!'})

@app.route('/exibir')
def exibir_horarios():
   

   i = 1
   pegar_horario = db.session.query(Horarios).filter_by(id = i).first()
   domingo=[]
   segunda=[]
   terca=[]
   quarta=[]
   quinta=[]
   sexta=[]
   sabado=[]

   while pegar_horario is not None:
      i+=1
      if pegar_horario.diaSemana== 0 :
         domingo.append({pegar_horario.hora,pegar_horario.minuto})
      elif pegar_horario.diaSemana== 1 :
         segunda.append({pegar_horario.hora,pegar_horario.minuto})
      elif pegar_horario.diaSemana== 2 :
         terca.append({pegar_horario.hora,pegar_horario.minuto})
      elif pegar_horario.diaSemana== 3:
         quarta.append({pegar_horario.hora,pegar_horario.minuto})
      elif pegar_horario.diaSemana== 4 :
         quinta.append({pegar_horario.hora,pegar_horario.minuto})
      elif pegar_horario.diaSemana== 5 :
         sexta.append({pegar_horario.hora,pegar_horario.minuto})
      elif pegar_horario.diaSemana== 6 :
         sabado.append({pegar_horario.hora,pegar_horario.minuto})
      else:
         return print("horário inválido")

      pegar_horario = db.session.query(Horarios).filter_by(id = i).first()
   

   dado = {'cabecalho':['Domingo','Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'],
           'horarios':[domingo, segunda, terca, quarta, quinta, sexta, sabado]}
   print(dado)
   return render_template('teste.html', dados = dado)

# def cadastro_horarios():
#    horarios=[]

#    i = 1
#    pegar_horario = db.session.query(Horarios).filter_by(id = i).first()

#    while pegar_horario is not None:
#       horarios.append({'dia': pegar_horario.diaSemana, 'hora': pegar_horario.hora, 'minuto': pegar_horario.minuto})
#       i+=1
#       pegar_horario = db.session.query(Horarios).filter_by(id = i).first()
   
#    print("horarios", horarios)




if __name__ == "__main__":
   app.run(debug=True)
