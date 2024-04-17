function substituirHorario() {
    const disciplina = document.getElementById('disciplinaSelect').value;

    // Realize uma requisição Ajax para substituir o horário ocupado
    const diasSemana = document.getElementById('diasSemanaSelect').value;
    const horas = document.getElementById('horasSelect').value;

    $.ajax({
        url: '/substituir_horario',
        method: 'POST',
        data: { diasSemana: diasSemana, horas: horas, disciplina: disciplina },
        success: function(response) {
            if (response.success) {
                alert('Horário substituído com sucesso!');
                $('#substituirHorarioModal').modal('hide');
                location.reload(true);
            } else {
                alert('Erro ao substituir o horário.');
            }
        },
        error: function() {
            console.log("deu errado");
            alert('Erro ao substituir o horário.');
        }
    });
}