//Calculadora dinâmica.
            
var numeroInicial = prompt('Informe o número incial');

var sinal = prompt('Informe o sinal da operação');

while(sinal != '-' && sinal != '+' && sinal != '/' && sinal != '*'){
   alert('Informe um sinal válido');
   sinal = prompt('Informe o sinal da operação');
}

var numeroFinal = prompt('Informe o número final');

//Funções para converter string em número
numeroInicial = parseInt(numeroInicial);
numeroFinal = parseInt(numeroFinal);

var resultadoFinal = 0;

if(sinal == '+'){
    resultadoFinal = numeroInicial + numeroFinal;
}else if(sinal == '-'){
    resultadoFinal = numeroInicial - numeroFinal;
}else if(sinal == '*'){
    resultadoFinal = numeroInicial * numeroFinal;
}else if(sinal == '/'){
    resultadoFinal = numeroInicial / numeroFinal;
}

alert('O resultado final é: '+resultadoFinal);
