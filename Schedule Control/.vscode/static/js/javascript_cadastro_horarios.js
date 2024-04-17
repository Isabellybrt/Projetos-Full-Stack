class Horario{
  constructor(dia, hora, minuto){
    this.dia = dia;
    this.hora = hora;
    this.minuto = minuto;
  }
}

var horarioSelecionado;
//Lista para armazenar os dias da semana selecionados
var diasSelecionados = [];

// Event listener para o botão "Salvar"
document.getElementById("formularioHorarios").addEventListener("submit", function(event) {
  event.preventDefault();

  // Obtém o valor do horário selecionado pelo usuário
  horarioSelecionado = document.getElementById("input_horario").value;

 // Quebra o horarioSelecionado em duas variaveis de hora e minuto
  var partesHoraMinuto = horarioSelecionado.split(":");
  var horaSelecionada = parseInt(partesHoraMinuto[0]);
  var minutoSelecionado = parseInt(partesHoraMinuto[1]);

  // Obtém todos os checkboxes de dias da semana selecionados
  diasSelecionados = document.querySelectorAll('input[type="checkbox"]:checked');


  diasSelecionados.forEach(function(checkbox){
    var nomeDia = checkbox.name;
    var numeroDia = converteDiaNumero(nomeDia);
    var horario = { dia: numeroDia, hora: horaSelecionada, minuto: minutoSelecionado }; // Cria objeto
    var dataToSend = {
      horario : horario
    };
    console.log(horario)

    fetch("/receber_dados",{
      method : 'POST',
      headers :{
        'Content-Type' : 'application/json'
      },
      body: JSON.stringify(dataToSend)
    })
    .then(response => response.json())
    .then(data => {
      console.log(data)
    })
    .catch(error =>{
      console.error('Erro ao enviar dados:', error);
    });
  });
});
  
  function converteDiaNumero(nomeDia){
    switch (nomeDia.toLowerCase()){
      case "domingo":
        return 0;
    case "segunda":
      return 1;
    case "terca":
      return 2;
    case "quarta":
      return 3;
    case "quinta":
      return 4;
    case "sexta":
      return 5;
    case "sabado":
      return 6;
    default:
      return -1;
  }
}



// Cria uma lista para armazenar os dias da semana selecionados
//var diasSelecionadosList = [];

// Função para adcionar um novo horário na tabela
// function adcionarHorario(dia, hora, minuto){
//   var novoHorario
// }

// Itera sobre cada checkbox de dia da semana selecionado
// for (var i = 0; i < diasSelecionados.length; i++) {
//   var diaSelecionado = diasSelecionados[i];

//   // Obtém o texto do label associado ao checkbox (dia da semana selecionado)
//   var diaLabel = diaSelecionado.nextElementSibling.textContent;

//   // Obtém o valor do dia da semana como número
//   var valorDia = valorDiaSemana(diaSelecionado.id);

//   // Adiciona o dia da semana à lista
//   diasSelecionadosList.push({ dia: diaLabel, valor: valorDia });
// }

// // Exibe os valores no console para verificar se estão corretos
// console.log("Horário selecionado:", horarioSelecionado);
// console.log("Dias selecionados:", diasSelecionadosList);

// // Obtém a referência para a tabela onde os horários serão exibidos
// var horariosTable = document.getElementById("horarios-table");

// // Verifica se algum horário foi adicionado
// if (horarioSelecionado && diasSelecionados.length > 0) {
//   // Itera sobre cada dia da semana selecionado
//   for (var j = 0; j < diasSelecionadosList.length; j++) {
//     var diaSelecionado = diasSelecionadosList[j];

//     // Obtém o nome e o valor do dia da semana selecionado
//     var diaLabel = diaSelecionado.dia;
//     var valorDia = diaSelecionado.valor;

//     // Insere uma nova linha na tabela
//     var newRow = horariosTable.insertRow();

//     // Insere uma célula na nova linha para exibir o horário selecionado
//     var horarioCell = newRow.insertCell();
//     horarioCell.textContent = horarioSelecionado;

//     // Insere uma célula na nova linha para exibir o dia da semana selecionado
//     var diaCell = newRow.insertCell();
//     diaCell.textContent = diaLabel;

//     // Insere uma célula na nova linha para o botão de exclusão
//     var deleteCell = newRow.insertCell();
//     var deleteButton = document.createElement("button");
//     deleteButton.innerHTML = '<i class="fas fa-trash fa-sm"></i>'; // Ícone de lixo do Font Awesome com tamanho "sm" (small)
//     deleteButton.classList.add("btn", "btn-danger", "delete-button", "btn-sm"); // Classes do Bootstrap para estilização do botão, incluindo "btn-sm" para tamanho "small"
//       deleteButton.addEventListener("click", function() {
//         confirmarExclusao(this); // Chama a função confirmarExclusao() passando o botão como argumento
//       });
//       deleteCell.appendChild(deleteButton);

//       // Insere uma célula na nova linha para o botão de edição
//       var editCell = newRow.insertCell();
//       var editButton = document.createElement("button");
//       editButton.innerHTML = '<i class="fas fa-pencil-alt fa-sm"></i>'; // Ícone de pincel do Font Awesome com tamanho "sm" (small)
//       editButton.classList.add("btn", "btn-primary", "edit-button", "btn-sm"); // Classes do Bootstrap para estilização do botão, incluindo "btn-sm" para tamanho "small"
//       editButton.addEventListener("click", function() {
//         editarHorario(this); // Chama a função editarHorario() passando o botão como argumento
//       });
//       editCell.appendChild(editButton);

//       exibirMensagem(); // Exibe a mensagem de sucesso para cada iteração do loop
//     }

//     document.getElementById("input_horario").value = ""; // Limpa o valor do input de horário
//   } else {
//     // Caso nenhum horário tenha sido adicionado, exibe uma mensagem de erro
//     var mensagem = document.getElementById("erro");
//     mensagem.classList.add("show");

//     // Oculta a mensagem após 3 segundos
//     setTimeout(function() {
//       mensagem.classList.remove("show");
//     }, 3000);
//   }



// // Função para confirmar a exclusão de um horário
// function confirmarExclusao(button) {
//   if (confirm("Tem certeza que deseja excluir este horário?")) {
//     deleteHorario(button); // Chama a função deleteHorario() passando o botão como argumento
//   }
// }

// // Função para excluir um horário da tabela
// function deleteHorario(button) {
//   var row = button.parentNode.parentNode; // Obtém a linha que contém o botão de exclusão
//   row.remove(); // Remove a linha da tabela
// }


// // Função para editar um horário
// function editarHorario(button) {
//   var row = button.parentNode.parentNode; // Obtém a linha que contém o botão de edição
//   var horarioCell = row.cells[0]; // Obtém a célula que contém o horário
//   var diaCell = row.cells[1]; // Obtém a célula que contém o dia da semana

//   var novoHorario = prompt("Digite o novo horário:");
//   var novoDia = prompt("Digite o novo dia da semana:");

//   if (novoHorario && novoDia) {
//     horarioCell.textContent = novoHorario; // Atualiza o horário na tabela
//     diaCell.textContent = novoDia; // Atualiza o dia da semana na tabela
//   }
// }

// // Função para exibir uma mensagem de sucesso
// function exibirMensagem() {
//   var mensagem = document.getElementById("mensagem");
//   mensagem.classList.add("show");

//   // Oculta a mensagem após 3 segundos
//   setTimeout(function() {
//     mensagem.classList.remove("show");
//   }, 3000);
// }

