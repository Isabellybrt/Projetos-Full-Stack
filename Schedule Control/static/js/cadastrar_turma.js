$(document).ready(function () {
    $("#cadastrarTurma").click(function () {
        var nomeTurma = $("#nomeTurma").val();
        var anoTurma = $("#anoTurma").val();

        // Aqui, você pode realizar ações com os dados do formulário, como enviar para o servidor ou atualizar a página.
        // Exemplo de ação: exibindo os dados no console
        console.log("Nome da Turma: " + nomeTurma);
        console.log("Ano: " + anoTurma);

        // Feche o modal após o cadastro (opcional)
        $("#cadastroTurmaModal").modal("hide");
    });
});

function recarregarPagina(){
    location.reload()
}

document.getElementById('recarregarPagina').addEventListener('click', recarregarPagina);



