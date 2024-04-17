# Sistema usando Flask, JavaScript, MySQL e HTML/CSS

import json
from flask import Flask, redirect, url_for, request, render_template, session, flash
from flask import jsonify
from models.user import Usuarios
from models.disciplinas import Disciplinas
from models.horarios import Horarios
from models.turmas import Turmas
from models.ofertas import Ofertas
from models.base import Base
from config import password, connection_string, engine, db, app
from functools import wraps
from sqlalchemy import inspect
import subprocess
from datetime import datetime
from dateutil import parser

def criar_tabelas():
    if not inspect(db.engine).has_table('usuario'):
        db.create_all()
        
        db.session.commit()
        
        db.session.close()
        print("Tabelas criadas")
    else:
        print("Tabelas já criados")
        
with app.app_context():
     criar_tabelas()

def bloqueio_de_rota(f):
    @wraps(f)
    def funcao_decorativa(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect('/')
        return f(*args, **kwargs)
    return funcao_decorativa

@app.route('/api/ofertas', methods=["GET"])
def listar_ofertas_api():
   lista_ofertas = pegar_ofertas()

   return jsonify(lista_ofertas)

def pegar_ofertas():
    ofertas = db.session.query(Ofertas).all()
    lista_ofertas = [[] for _ in range(2)]
    for oferta in ofertas:
        disciplinas = oferta.disciplina
        nome_disciplina = disciplinas.nome
        
        turmas = oferta.turma
        curso_turma = turmas.curso

        lista_ofertas[0].append(nome_disciplina)
        lista_ofertas[1].append(curso_turma)

    return(lista_ofertas)


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro(): 
    if request.method == 'POST':
        matricula1 = request.form['matricula']
        senha1 = request.form['password']
        materia1 = request.form.getlist('materias')
        if matricula1 and senha1 and materia1:
            novo_usuario = Usuarios(matricula=matricula1, senha=senha1, materias=materia1, admin=0)
            db.session.add(novo_usuario)
            db.session.commit()
            db.session.close()  
            if (novo_usuario):
                session['logged_in'] = True
                return redirect(url_for('turma')) 
        else:
            print('erro')

    return render_template('cadastro.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if "logged_in" in session:
        return redirect(url_for('turma'))
      
    if request.method == 'POST':
        matricula = request.form['matricula']
        password = request.form['password']

        user = db.session.query(Usuarios).filter_by(matricula = matricula, senha = password).first()
        if (user):
            session['logged_in'] = True
            session['admin'] = user.admin
            if (session['admin']):
                return redirect(url_for('admin'))
            return redirect(url_for('turma'))
        else:
            flash("Matrícula ou senha incorretas")
    return render_template('index.html')

@app.route('/turmas', methods=['GET', 'POST'])
@bloqueio_de_rota
def turma():
    if "logged_in" in session:
        admin = session.get('admin', False)
        turmas = db.session.query(Turmas).all()
        return render_template('turmas.html', admin=admin, turmas=turmas)
    else:
        return redirect(url_for('login'))                                                                                                        
                                                                                                      
@app.route('/turma/<int:id>', methods=['GET', 'POST'])
def tabela(id):
    dados = ""
    logged_in = session.get('logged_in', False)
    admin = session.get('admin', False)
    disciplinas = []
    disciplina = None
    horarios_cancelados = None

    # Use a mesma sessão para a consulta da turma
    with db.session.begin():
        turma = db.session.query(Turmas).get(id)
        if turma is None:
            return "Turma não encontrada"

        ofertas = db.session.query(Ofertas).filter_by(id_turma=id).all()
        
        disciplinas = []
        
        horarios = db.session.query(Horarios).all()
        
        # # Crie uma estrutura de dados intermediária para armazenar as disciplinas
        horarios_disciplinas = {key: [] for key in range(5)}

        # Mapeamento de dia da semana para índice na lista (usando o número do dia da semana)
        dia_semana_para_indice = {
            "Segunda": 0,
            "Terça": 1,
            "Quarta": 2,
            "Quinta": 3,
            "Sexta": 4,
        }

        # Mapeamento de horários
        horarios_para_indice = {
            "07:00 - 08:00": 0,
            "08:00 - 09:00": 1,
            "09:00 - 10:00": 2,
            "10:00 - 10:10": 3,
            "10:10 - 11:10": 4,
            "11:10 - 12:10": 5,
            "12:10 - 13:20": 6,
            "13:20 - 14:20": 7,
            "14:20 - 15:20": 8,
            "15:20 - 15:30": 9,
            "15:30 - 16:30": 10,
            "16:30 - 17:30": 11,
        }

        # Inicialize uma estrutura de dados para armazenar as informações de horários e disciplinas
        horarios_disciplinas = [
            [""] * len(horarios_para_indice) for _ in range(len(dia_semana_para_indice))
        ]
        
        for oferta in ofertas:
            disciplina = oferta.disciplina
            disciplinas.append(disciplina)
            horarios = oferta.horarios
            
            for horario in horarios:
                horarios_cancelados = db.session.query(Horarios).filter(Horarios.cancelado == True).all()
                if horario.dias_semana in dia_semana_para_indice and horario.horas in horarios_para_indice and horario.cancelado == False:
                    dia_semana_indice = dia_semana_para_indice[horario.dias_semana]
                    horario_indice = horarios_para_indice[horario.horas]
                    horarios_disciplinas[dia_semana_indice][horario_indice] = disciplina.nome

                # Verifique o status de cancelamento para o horário específico
                elif horario.dias_semana in dia_semana_para_indice and horario.horas in horarios_para_indice and horario.cancelado == True:
                    dia_semana_indice = dia_semana_para_indice[horario.dias_semana]
                    horario_indice = horarios_para_indice[horario.horas]
                    horarios_disciplinas[dia_semana_indice][horario_indice] = "Horário Vago"

        maior_tamanho = len(horarios_para_indice)

        # Crie dados no formato desejado para a renderização no template
        dados = {
            'cabecalho': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
            'horarios': horarios_disciplinas,
            'maior_tamanho': maior_tamanho,
            'dias_semana': ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
        }
        dias_semana = dados.get('dias_semana', [])  

        # horarios_cancelados = db.session.query(Horarios).filter(Horarios.cancelado == True).all()

            
        if request.method == 'POST':
            tipo = request.form.get('tipo')
            

            # if not dias_semana or not horas or not disciplina_nome or not turma_id:
            #     flash('Todos os campos são obrigatórios', 'error')
            #     return jsonify({"erro": "Campos obrigatórios não preenchidos"})
            
            if tipo == "CadastrarHorario":
                dias_semana = request.form.get('diasSemana')
                horas = request.form.get('horas')
                disciplina_nome = request.form.get('disciplina')
                id_turma = request.form.get('turma_id')
                disciplina = Disciplinas.query.filter_by(nome=disciplina_nome).first()
                if disciplina:
                    disciplina_id = disciplina.id
                else:
                    # Trate o caso em que a disciplina não foi encontrada
                    flash('Disciplina não encontrada', 'error')
                    return jsonify({"erro": "Disciplina não encontrada"})
                
                oferta = Ofertas.query.filter_by(id_turma=id_turma, disciplina=disciplina).first()
                if oferta:
                    oferta_id = oferta.id_oferta
                    oferta_turma = id_turma
                else:
                    flash('Oferta não encontrada', 'error')
                    return jsonify({"erro": "Oferta não encontrada"})
                
                if not disciplina:
                    flash('Disciplina não encontrada', 'error')
                    return jsonify({"erro": "Disciplina não encontrada"})
                
                if not oferta:
                    flash('Oferta não encontrada', 'error')
                    return jsonify({"erro": "Oferta não encontrada"})

                try:
                    # Verifique se o horário já está ocupado para a disciplina e turma selecionadas
                    horario_existente = Horarios.query.join(Ofertas).filter(Horarios.dias_semana == dias_semana, Horarios.horas == horas, Ofertas.id_turma == id_turma).first()
                    
                    if horario_existente:
                        # O horário já está ocupado, substitua-o diretamente
                        flash('Horário já ocupado, deseja substituir?', 'success')
                        db.session.delete(horario_existente)

                    # Crie um novo horário
                    novo_horario = Horarios(dias_semana=dias_semana, horas=horas, id_oferta=oferta_id, disciplina_id=disciplina_id)
                    db.session.add(novo_horario)

                    # Commit para adicionar o novo horário
                    db.session.commit()

                    flash('Horário cadastrado com sucesso', 'success')
                
                except Exception as e:
                    db.session.rollback()
                    flash(f'Erro ao cadastrar horário: {str(e)}', 'error')

                # Recarregue a página após cadastrar o horário
                flash('Horário cadastrado com sucesso', 'success')
                return redirect(url_for('tabela', id=id_turma))
            
            elif tipo == "CancelarAula":
                horas = request.form.get('horas')
                dias_semana = request.form.get('diasSemana')
                disciplina_nome = request.form.get('disciplina')
                data_cancelada = request.form.get('data_cancelada')
                
                 # Verifique se data_cancelada não é vazia antes de tentar converter
                if data_cancelada:
                    try:
                        # Tente converter a string da data cancelada para um objeto de data
                        data_cancelada = datetime.strptime(data_cancelada, '%Y-%m-%d').date()
                        
                        # Consulta para encontrar o horário correspondente com base nas informações fornecidas
                        horario = Horarios.query \
                            .join(Ofertas) \
                            .filter(Horarios.horas == horas, 
                                    Horarios.dias_semana == dias_semana, 
                                    Horarios.disciplina.has(Disciplinas.nome == disciplina_nome)) \
                            .first()
                        
                        if horario:
                            if data_cancelada >= datetime.now().date():
                                horario.cancelado = True
                            else:
                                horario.cancelado = False
                                return 'Não pode cancelar nesse dia'

                            # Faça o commit
                            db.session.commit()
                            # Recarregue a página após cadastrar o horário
                            flash('Aula cancelada com sucesso', 'success')
                    except ValueError:
                        return 'Formato de data inválido'
                else:
                    return 'Data cancelada não foi fornecida'
                                 
                    #             if cancelado_data:
                    # try:
                    #     # Tente converter a string da data cancelada para um objeto de data
                    #     cancelado_data = datetime.strptime(cancelado_data, '%Y-%m-%d').date()

                    #     # Consulta para encontrar o horário correspondente com base nas informações fornecidas
                    #     horario = Horarios.query \
                    #         .join(Ofertas) \
                    #         .filter(Horarios.horas == horas, 
                    #                 Horarios.dias_semana == dias_semana, 
                    #                 Horarios.disciplina.has(Disciplinas.nome == disciplina_nome)) \
                    #         .first()

                    #     if horario:
                    #         # Atualize o status de cancelado apenas para o dia especificado
                    #         horario.cancelado = datetime.now().date() == cancelado_data

                    #         # Faça o commit
                    #         db.session.commit()
                    #         # Recarregue a página após cadastrar o horário
                    #         flash('Aula cancelada com sucesso', 'success')
                    #         return redirect(url_for('tabela', id=id))
                    # except ValueError:
                    #     return 'Formato de data inválido'
                # else:
                #     return 'Data de cancelamento não foi fornecida'

            elif tipo == "AgendarAula": 
                data_aula = request.form.get('data_aula')
                dias_semana = request.form.get('dias_semana')
                horas = request.form.get('horas')
                disciplina_nome = request.form.get('disciplina')

                # Procura a disciplina pelo nome
                disciplina = Disciplinas.query.filter_by(nome=disciplina_nome).first()

                if disciplina:
                    novo_horario = Horarios(
                        dias_semana=dias_semana,
                        horas=horas,
                        data_aula=datetime.strptime(data_aula, '%Y-%m-%d').date(),
                        disciplina_id=disciplina.id,
                        cancelado=False
                    )
        
                    db.session.add(novo_horario)

                    #  Verifica se a data da aula já passou e reverte o estado se necessário
                    # if novo_horario.data_aula and novo_horario.data_aula < datetime.now().date():
                    #     novo_horario.cancelado = True
                    
                    db.session.commit()
                    flash('Aula agendada com sucesso', 'success')

                return redirect(url_for('tabela', id=id))  # Ajuste o nome da rota conforme necessário


    if logged_in:
        return render_template('base_tabela.html', dados=dados, disciplina=disciplina, turma=turma, logged_in=logged_in, admin=admin, dias_semana=dias_semana, disciplinas=disciplinas, id=id, horarios=horarios, horarios_cancelados=horarios_cancelados)
    else:
        return redirect(url_for('login'))
    

def encontrar_disciplina(horario, dia_semana, disciplinas):
    for disciplina in disciplinas:
        if disciplina.horario == horario and disciplina.dia_semana == dia_semana:
            return disciplina
    return None



@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if "logged_in" in session:
        admin = session.get('admin', False)
        turmas = db.session.query(Turmas).all()
        disciplinas = db.session.query(Disciplinas).all()
        
        if request.method == 'POST':
            tipo = request.form['tipo']
            
            if tipo == "turma":
                # Código existente para cadastrar turma
                nome_turma = request.form['nomeTurma']
                ano_turma = request.form['anoTurma']
                turno_turma = request.form['turnoTurma']

                # Verificar se a turma com o mesmo nome e ano já existe
                turma_existente = Turmas.query.filter_by(curso=nome_turma, ano=ano_turma).first()

                if turma_existente:
                    flash('Turma já cadastrada para o ano especificado', 'error')
                else:
                    nova_turma = Turmas(curso=nome_turma, ano=ano_turma, turno=turno_turma)
                    db.session.add(nova_turma)
                    db.session.commit()
                    flash('Turma cadastrada com sucesso', 'success')

            elif tipo == "disciplina":
                # Código existente para cadastrar disciplina
                carga_Horaria = request.form['cargaHoraria']
                nome_Disciplina = request.form['nomeDisciplina']

                # Verificar se a disciplina com o mesmo nome já existe
                disciplina_existente = Disciplinas.query.filter_by(nome=nome_Disciplina).first()

                if disciplina_existente:
                    flash('Disciplina com o mesmo nome já cadastrada', 'error')
                else:
                    nova_disciplina = Disciplinas(carga_horaria=carga_Horaria, nome=nome_Disciplina)
                    db.session.add(nova_disciplina)
                    db.session.commit()
                    flash('Disciplina cadastrada com sucesso', 'success')
                    
            elif tipo == "oferta":
                # Código para cadastrar grade curricular (oferta)
                id_turma = request.form['turma_id']
                id_disciplina = request.form['disciplina_id']

                turma = Turmas.query.get(id_turma)
                disciplina = Disciplinas.query.get(id_disciplina)

                # Verifique se a oferta já existe com os mesmos ids de turma e disciplina
                oferta_existente = Ofertas.query.filter_by(id_turma=id_turma, id_disciplina=id_disciplina).first()

                if oferta_existente:
                    flash('Horário já cadastrado', 'error')
                else:
                    if turma and disciplina:
                        nova_oferta = Ofertas(id_turma=id_turma, id_disciplina=id_disciplina)
                        db.session.add(nova_oferta)
                        db.session.commit()
                        flash('Grade curricular cadastrada com sucesso', 'success')
                    else:
                        flash('Turma ou disciplina não encontrada', 'error')

                # db.session.close()

        return render_template('admin.html', admin=admin, turmas=turmas, disciplinas=disciplinas)

@app.route('/logout')
def logout():
    if "logged_in" in session:
        session.pop('logged_in', None)
        session.pop('admin', None)
        flash("Você encerrou sua sessão")
    return redirect(url_for('login'))

    
@app.route('/disciplinas')
def listar_disciplinas():
    disciplinas = Disciplinas.query.all()
    return render_template('base_tabela.html', disciplinas=disciplinas)



@app.route('/agendar_aula', methods=['POST'])
@bloqueio_de_rota
def agendar_aula():
    # Obtenha os dados do formulário
    data = request.form['data']
    disciplina = request.form['disciplina']
    

@app.route('/bases')
@bloqueio_de_rota
def base():
    return render_template('base.html')

if __name__ == "__main__":
	app.run(debug=True)
