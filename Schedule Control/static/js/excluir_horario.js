function confirmarExclusao(horarioId) {
    if (confirm('Deseja realmente excluir este horário?')) {
        // Se o usuário confirmar, envie o formulário de exclusão
        document.querySelector('form[action="{{ url_for("excluir_horario") }}"] input[name="horario_id"]').value = horarioId;
        document.querySelector('form[action="{{ url_for("excluir_horario") }}"]').submit();
    }
}