$(document).ready(function () {
    $("#adicionarGrade").click(function () {
        var turmaId = $("#turma").val();
        var disciplinaId = $("#disciplina").val();

        // Aqui, você pode realizar ações com os dados do formulário, como enviar para o servidor ou atualizar a página.
        // Exemplo de ação: exibindo os dados no console
        console.log("Turma ID: " + turmaId);
        console.log("Disciplina ID: " + disciplinaId);

        // Feche o modal após adicionar a grade curricular (opcional)
        $("#adicionarGradeModal").modal("hide");
    });
});

function recarregarPagina(){
    location.reload()
}

document.getElementById('recarregarPagina').addEventListener('click', recarregarPagina);



