
var currentDate = new Date();
    var diasDaSemana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado'];
    var diaAtualDaSemana = diasDaSemana[currentDate.getDay()];

    // Formate a data no formato "dd/mm/yyyy"
    var dia = currentDate.getDate();
    var mes = currentDate.getMonth() + 1; // Adicione 1 porque os meses são indexados de 0 a 11
    var ano = currentDate.getFullYear();
 
    // Certifique-se de adicionar um zero à esquerda se o dia ou o mês for menor que 10
    if (dia < 10) {
        dia = '0' + dia;
    }
    if (mes < 10) {
        mes = '0' + mes;
    }

    // Exiba o dia da semana e a data no elemento com o id "currentDay"
    document.getElementById('currentDay').innerText = diaAtualDaSemana + ', ' + dia + '/' + mes + '/' + ano;
    
    document.addEventListener('DOMContentLoaded', function() {
        var modoCancelamento = false;

        // Adicione um ouvinte de evento para o clique no botão "Cancelar Aula"
        document.querySelector('.cancelar-aula-btn').addEventListener('click', function() {
            modoCancelamento = true;

            // Ajuste a interface conforme necessário
            if (modoCancelamento) {
                alert('Clique em uma disciplina para cancelar a aula.');
            } else {
                alert('Modo de cancelamento desativado.');
            }
        });

        // Adicione ouvinte de eventos às células clicáveis quando o modo de cancelamento estiver ativado
        var celulasDisciplina = document.querySelectorAll('.clickable');
        celulasDisciplina.forEach(function(celula) {
            celula.addEventListener('click', disciplinaClicada);
        });

        function disciplinaClicada() {
            var evento = event || window.event; // Obtenha o objeto de evento
            var celula = evento.target || evento.srcElement; // Obtenha o elemento clicado
            var disciplinaNome = celula.getAttribute('data-disciplina-nome');
            var disciplinaHora = celula.getAttribute('data-hora');
            var diaDaSemana = celula.getAttribute('data-dias-semana');
    
            
            // Armazene o disciplinaId na variável local celulaClicadaId
            window.disciplinaNome = disciplinaNome;
            window.disciplinaHora = disciplinaHora;
            window.diaDaSemana = diaDaSemana;
    
                // Defina os atributos de dados diretamente nos botões do modal de Cancelar Aula
            $('#agendarAulaBtn').data('disciplina-nome', disciplinaNome);
            $('#agendarAulaBtn').data('horas', disciplinaHora);
            $('#agendarAulaBtn').data('dias-semana', diaDaSemana);
    
            console.log('Nome da Disciplina:', window.disciplinaNome);
            console.log('Hora da Disciplina:', window.disciplinaHora);
            console.log('Dia da semana:', window.diaDaSemana);
    

    
            // Abra o modal de cancelar aula quando a disciplina for clicada
            $('#cancelarAulaModal').modal('show');
        }
    });
    

    $("#meuFormulario").submit(function(event) {
        event.preventDefault();
    
        var dataCancelada = $('#datacancelada').val();
        console.log(dataCancelada);
    
        if (!dataCancelada) {
            console.log('Data cancelada não foi fornecida.');
            return;
        }
    
        // Restante do código...
        document.getElementById('datacancelada').value = dataCancelada;
        document.getElementById('horas').value = window.disciplinaHora;
        document.getElementById('diasSemana').value = window.diaDaSemana;
        document.getElementById('disciplina').value = window.disciplinaNome;
        document.getElementById('turma_id').value = turma_id;
        tipo = document.getElementById('tipo2').value;
    
        var $form = $(this);
        url = $form.attr("action");
        $('#cancelarAulaModal').modal('hide');
    
        var posting = $.post(url, {
            'horas': document.getElementById('horas').value,
            'diasSemana': document.getElementById('diasSemana').value,
            'disciplina': document.getElementById('disciplina').value,
            'data_cancelada': document.getElementById('datacancelada').value,
            'turma_id': document.getElementById('turma_id').value,
            'tipo': tipo
        });
    
        posting.done(function(response) {
            alert(response);
            location.reload();
        });
    
        posting.fail(function(error) {
            console.error('Error:', error.responseText);
        });
    });

