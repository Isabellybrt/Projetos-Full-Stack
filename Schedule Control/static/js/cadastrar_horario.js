function cadastrarHorario() {
    // Obtenha os valores dos campos
    var diasSemana = document.getElementById('diasSemanaSelect').value;
    var horas = document.getElementById('horasSelect').value;
    var disciplina = document.getElementById('disciplinaSelect').value;
    var turmaId = document.getElementById('turma_id').value;

    // Defina os valores dos campos ocultos
    document.getElementById('diasSemana').value = diasSemana;
    document.getElementById('horas').value = horas;
    document.getElementById('disciplina').value = disciplina;
    document.getElementById('turmaId').value = turmaId;
    
    // Envie o formulário
    document.getElementById('horarioForm').submit();
}

var recarregarElement = document.getElementById('recarregarPagina');
if (recarregarElement) {
    recarregarElement.addEventListener('click', recarregarPagina);
}










// function cadastrarHorario() {
//     console.log('Antes de obter os valores');
//     const diasSemana = document.getElementById('diasSemanaSelect').value;
//     const horas = document.getElementById('horasSelect').value;
//     const disciplina = document.getElementById('disciplinaSelect').value;
//     const turmaId = document.getElementById('turma_id').value;
//     const ofertaId = document.getElementById('oferta_id').value;

//     console.log('Valores obtidos:', diasSemana, horas, disciplina, turmaId, ofertaId);

//     const formData = new FormData();
//     formData.append('diasSemana', diasSemana);
//     formData.append('horas', horas);
//     formData.append('disciplina', disciplina);
//     formData.append('turma_id', turmaId);
//     formData.append('oferta_id', ofertaId);
//     console.log('Objeto formData:', formData);

//     // Realize uma requisição Ajax para verificar se o horário está ocupado
//     $.ajax({
//         url: '/cadastrar_horario',
//         method: 'POST',
//         data: { diasSemana: diasSemana, horas: horas, disciplina: disciplina, turma_id: turmaId },  // Inclua o ID da turma na requisição
//         success: function(response) {
//             if (response.ocupado) {
//                 // Horário ocupado, mostrar modal de substituição
//                 $('#substituirHorarioModal').modal('show');
//             } else {
//                 // Horário não está ocupado, prosseguir com o cadastro
//                 $.ajax({
//                     url: '/cadastrar_horario',
//                     method: 'POST',
//                     data: { diasSemana: diasSemana, horas: horas, disciplina: disciplina, turma_id: turmaId },  // Inclua o ID da turma na requisição
//                     success: function() {
//                         alert('Horário cadastrado com sucesso!');
//                         $('#horarioModal').modal('hide');
//                         location.reload(true);
//                     },
//                     error: function() {
//                         alert('Erro ao cadastrar horário.');
//                     }
//                 });
//             }
//         },
//         error: function() {
//             console.log("deu errado");
//             alert('Erro ao verificar o horário.');
//         }
//     });
// }
