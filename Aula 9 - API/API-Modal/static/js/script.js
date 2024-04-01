// script.js


// Rodar Funções no Roteador

async function executeOption(equipamento, opcao) {
    const bodyRequest = {
        "equipamento": equipamento,
        "opcao": opcao
    };

    try {
        const res = await fetch('http://localhost:5000/executar', {
            body: JSON.stringify(bodyRequest),
            headers: {
                'Content-Type': "application/json"
            },
            method: 'POST'
        });

        let data = await res.json();
        data = data.result;

        console.log(data);
        // Verifica se data e Configurações Atual estão definidos
        if (data && data['Configurações Atual'] && Array.isArray(data['Configurações Atual'])) {
            // Preenche o conteúdo do modal dinamicamente com as configurações atuais
            document.getElementById('modal-content').innerHTML = `<h1>Configurações Atual</h1><pre>${data['Configurações Atual'].join("\n")}</p>`;
            document.body.classList.add('active');
        } else {
            // Caso contrário, exibe a mensagem padrão
            let message = "Dados não disponíveis";
            if (data && data.Mensagem) {
                message = data.Mensagem;
            }
            if (opcao === "1" && data.Resultado) {
                // A mensagem do usuário está no primeiro elemento do array Resultado
                const mensagemUsuario = data.Resultado.Mensagem;
                message = mensagemUsuario; // Inicia a mensagem com a mensagem do usuário
                if (data.Resultado.Resposta) {
                    // Formata cada linha da resposta para exibição em uma nova linha
                    const formattedResposta = data.Resultado.Resposta.map(line => `<p>${line}</p>`).join('');
                    message += `\n\nResposta: ${formattedResposta}`;
                }
            }
            if (opcao === "2" && data.Backup && data.Backup.length > 0) {
                document.getElementById('modal-content').innerHTML = `<h1>Resultado</h1><p>Backup realizado com sucesso</p>`;
            }
            if (opcao === "6" && data.Banner && data.Banner.length > 0) {
                // A mensagem do usuário está no primeiro elemento do array Banner
                const mensagemUsuario = data.Banner[0];
                message += ` ${mensagemUsuario}`;
            }
            document.getElementById('modal-content').innerHTML = `<h1>Resultado</h1><p>${message}</p>`;
            document.body.classList.add('active');
        }
    } catch (error) {
        console.error(error);
        let errorMessage = "Ocorreu um erro: ";
        if (error.Mensagem) {
            errorMessage += error.Mensagem;
        } else {
            errorMessage += "Erro desconhecido";
        }
        openModal(errorMessage);
    }
}

// Rodar Funções no Roteador

document.getElementById('rodarScript').addEventListener('click', function () {
    executeOption("Roteador", "1");
});

document.getElementById('fazerBackup').addEventListener('click', function () {    
    executeOption("Roteador", "2");
});

document.getElementById('criarUsuario').addEventListener('click', function () {
    executeOption("Roteador", "4");
});

document.getElementById('configuracoes').addEventListener('click', function () {
    executeOption("Roteador", "5");
});

document.getElementById('configurarBanner').addEventListener('click', function () {
    executeOption("Roteador", "6");
});


// Rodar Funções no Switch


// Rodar Funções no Switch

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('rodarScriptSwitch').addEventListener('click', function () {
        executeOption("Switch", "1");
    });

    document.getElementById('fazerBackupSwitch').addEventListener('click', function () {
        executeOption("Switch", "2");
    });

    document.getElementById('criarUsuarioSwitch').addEventListener('click', function () {
        executeOption("Switch", "4");
    });

    document.getElementById('configuracoesSwitch').addEventListener('click', function () {
        executeOption("Switch", "5");
    });

    document.getElementById('configurarBannerSwitch').addEventListener('click', function () {
        executeOption("Switch", "6");
    });
});


// MODAL

// Função para abrir o modal
function openModal(message) {
    document.getElementById('modal-message').innerText = message;
    document.getElementById('modal-content').style.display = "block"; // Mostra o modal
    document.body.classList.add('modal-open'); // Adiciona a classe modal-open ao body
}

// Função para fechar o modal
function closeModal() {
    document.getElementById('modal-message').innerText = ''; // Limpa o conteúdo do modal
    document.getElementById('modal-content').style.display = "none"; // Esconde o modal
    document.body.classList.remove('modal-open'); // Remove a classe modal-open do body
}

// Adicionar um ouvinte de evento para fechar o modal quando o usuário clicar fora dele
document.addEventListener('DOMContentLoaded', function() {
    const modalContent = document.getElementById('modal-content');
    const closeModalButton = document.getElementById('close-modal');

    closeModalButton.addEventListener('click', closeModal);

    // Ajuste no ouvinte de evento para fechar o modal quando o usuário clicar fora dele
    window.onclick = function(event) {
        if (event.target == modalContent) { // Certifique-se de que o ID do modal esteja correto
            closeModal();
        }
    }
});

document.addEventListener('click', function(event) {
    if (event.target == modalContent) {
        closeModal();
    }
});