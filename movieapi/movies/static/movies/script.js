document.addEventListener("DOMContentLoaded", function () {
    const botaoBusca = document.getElementById("botao-busca");
    const inputBusca = document.getElementById("input-busca");
    const resultadoBusca = document.getElementById("resultado-busca");  

    botaoBusca.addEventListener("click", function() {  
        const valor = inputBusca.value;
        if (valor) {
            fetchMovies(valor);
        }
    });
});

function fetchMovies(valor) {
    fetch(`/api/movies/?search=${valor}`)
        .then(resposta => resposta.json())
        .then(dado => {
            exibirFilmes(dado);
        })
        .catch(error => console.error("Erro ao buscar filmes:", error));
}

function exibirFilmes(filmes) {
    const resultadoBusca = document.getElementById("resultado-busca");  
    resultadoBusca.innerHTML = "";
    
    if (filmes.length === 0) {
        resultadoBusca.innerHTML = "<p>Nenhum filme encontrado.</p>";
        return;
    }

    filmes.forEach(filme => {
        const elementoFilme = document.createElement("div");
        elementoFilme.classList.add("filme");

        elementoFilme.innerHTML = `
            <img src="${filme.imagem}" alt="${filme.titulo}">
            <h3>${filme.titulo}</h3>
            <p>Ano: ${filme.ano}</p>
        `;

        resultadoBusca.appendChild(elementoFilme);
    });
}
