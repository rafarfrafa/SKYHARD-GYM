// Máscara de data de nascimento (dd/mm/aaaa)
document.getElementById('data_nascimento').addEventListener('input', function(e) {
    let value = e.target.value.replace(/\D/g, ''); // Remove qualquer coisa que não seja número
    if (value.length <= 2) {
        e.target.value = value.replace(/(\d{2})/, '$1');
    } else if (value.length <= 4) {
        e.target.value = value.replace(/(\d{2})(\d{2})/, '$1/$2');
    } else {
        e.target.value = value.replace(/(\d{2})(\d{2})(\d{4})/, '$1/$2/$3');
    }
});

// Máscara de telefone (DDD) 00000-0000
document.getElementById('telefone').addEventListener('input', function(e) {
    let value = e.target.value.replace(/\D/g, ''); // Remove qualquer coisa que não seja número
    if (value.length <= 2) {
        e.target.value = '(' + value;
    } else if (value.length <= 6) {
        e.target.value = '(' + value.substring(0, 2) + ') ' + value.substring(2);
    } else {
        e.target.value = '(' + value.substring(0, 2) + ') ' + value.substring(2, 7) + '-' + value.substring(7, 11);
    }
});
