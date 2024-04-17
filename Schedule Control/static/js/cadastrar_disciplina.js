$(document).ready(function () {
    $("#cadastrarDisciplina").click(function () {
        var cargaHoraria = $("#cargaHoraria").val();
        var nomeDisciplina = $("#nomeDisciplina").val();

        // Aqui, você pode realizar ações com os dados do formulário, como enviar para o servidor ou atualizar a página.
        // Exemplo de ação: exibindo os dados no console
        console.log("cargaHoraria: " + cargaHoraria);
        console.log("nome: " + nomeDisciplina);

        // Feche o modal após o cadastro (opcional)
        $("#cadastroDisciplinaModal").modal("hide");
    });
});

function recarregarPagina(){
    location.reload()
}

document.getElementById('recarregarPagina').addEventListener('click', recarregarPagina);



