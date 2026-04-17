const btnNao = document.getElementById('btn-nao');

if (btnNao) {
    btnNao.addEventListener('mouseenter', () => {
        btnNao.innerText = 'Sim';
        btnNao.className = 'btn-sim'; 
        btnNao.onclick = () => {
            window.location.href = '/aceitou';
        };
    });
}