document.addEventListener('DOMContentLoaded', function() {
    // Encontre o formulário e adicione um evento de envio
    var form = document.querySelector('form');
    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Impede o envio padrão do formulário
        
        // Obtenha os valores dos campos de formulário
        var nomeTurma = document.getElementById('nomeTurma').value;
        var anoTurma = document.getElementById('anoTurma').value;
        
        // Crie um novo card com os valores inseridos
        var cardHtml = `
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">${nomeTurma}</h5>
                    <p class="card-text">Ano: ${anoTurma}</p>
                </div>
            </div>
        `;
        
        // Adicione o card ao elemento de container
        var cardContainer = document.getElementById('turmaCardContainer');
        cardContainer.innerHTML += cardHtml;
        
        // Feche o modal
        $('#cadastroTurmaModal').modal('hide');
    });
});

