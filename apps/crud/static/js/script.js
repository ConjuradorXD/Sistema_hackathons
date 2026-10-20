const maskCpf = document.querySelector('#cpf');
const maskTel = document.querySelector('#telefone');

if (maskCpf) {
    maskCpf.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d)/, '$1.$2')
        .replace(/(\d{3})(\d{1,2})$/, '$1-$2');
    });
}

if (maskTel) {
    maskTel.addEventListener('input', function() {
        this.value = this.value.replace(/\D/g, '')
        .replace(/(\d{2})(\d)/, '($1) $2')
        .replace(/(\d{4,5})(\d)/, '$1-$2')
        .replace(/(\d{4})\d+?$/, '$1');
    });
}
