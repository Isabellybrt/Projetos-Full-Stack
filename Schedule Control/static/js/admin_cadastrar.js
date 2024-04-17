// Função para substituir um horário
function substituirHorarioModal() {
    var diaSemana = document.getElementById("diaSemanaModal").value;
    var horario = document.getElementById("horarioModal").value;
    var novaMateria = document.getElementById("novaMateriaModal").value;

    // Crie um objeto com os dados a serem enviados para o servidor
    var data = {
        diaSemana: diaSemana,
        horario: horario,
        novaMateria: novaMateria
    };

    // Enviar os dados para o servidor Flask
    fetch('/tabela', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Os dados foram atualizados com sucesso
            alert(data.mensagem);
            $('#substituirModal').modal('hide');
            // Adicione aqui qualquer ação que deseja realizar após a atualização bem-sucedida
        } else {
            alert("Erro ao atualizar o horário: " + data.mensagem);
        }
    })
    .catch(error => {
        alert("Erro ao enviar os dados para o servidor: " + error.message);
    });


    var table = document.querySelector(".table");
    var rows = table.getElementsByTagName("tr");

    var colIndex = -1;
    var ths = rows[0].getElementsByTagName("th");

    for (var i = 0; i < ths.length; i++) {
        if (ths[i].textContent.trim() === diaSemana) {
            colIndex = i;
            break;
        }
    }

    if (colIndex === -1) {
        alert("Dia da semana não encontrado!");
        return;
    }

    var horarioEncontrado = false;

    for (var i = 1; i < rows.length; i++) {
        var row = rows[i];
        var cells = row.getElementsByTagName("td");
        var cellHorario = cells[0].textContent;

        if (cellHorario.includes(horario)) {
            var cellMateria = cells[colIndex];
            cellMateria.textContent = novaMateria;
            horarioEncontrado = true;
            break;
        }
    }

    if (horarioEncontrado) {
        $('#substituirModal').modal('hide');
    } else {
        alert("Horário não encontrado!");
    }
}   

$('#substituirModal').on('hidden.bs.modal', function () {
    // Remova a classe que torna a tela escura
    document.body.classList.remove('modal-open');
});