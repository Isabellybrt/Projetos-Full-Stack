// Adicione isso ao seu script JavaScript existente
$('#substituirAulaModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var horas = button.data('hora');
    var diasSemana = button.data('dias-semana');
    var disciplina = button.data('disciplina-nome');

    // Atualize os valores dos campos do modal
    $('#substituirHoras').val(horas);
    $('#substituirDiasSemana').val(diasSemana);
    $('#substituirDisciplina').val(disciplina);
});
