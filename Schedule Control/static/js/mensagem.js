var currentDate = new Date();
    var diasDaSemana = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado'];
    var diaAtualDaSemana = diasDaSemana[currentDate.getDay()];

    // Formate a data no formato "dd/mm/yyyy"
    var dia = currentDate.getDate();
    var mes = currentDate.getMonth() + 1; // Adicione 1 porque os meses são indexados de 0 a 11
    var ano = currentDate.getFullYear();
 
    // Certifique-se de adicionar um zero à esquerda se o dia ou o mês for menor que 10
    if (dia < 10) {
        dia = '0' + dia;
    }
    if (mes < 10) {
        mes = '0' + mes;
    }

    // Exiba o dia da semana e a data no elemento com o id "currentDay"
    document.getElementById('currentDay').innerText = 'Hoje: ' + diaAtualDaSemana + ', ' + dia + '/' + mes + '/' + ano;