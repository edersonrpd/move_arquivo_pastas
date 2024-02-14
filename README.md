# Descrição

Este script Python organiza arquivos de uma pasta de origem para uma pasta de destino, criando subpastas com base em regras predefinidas nos nomes dos arquivos.

## Funcionalidades

- Seleciona a pasta de origem e a pasta de destino através de interfaces gráficas.
- Define regras para identificar o destino dos arquivos, mapeando strings nos nomes dos arquivos para subpastas.
- Move os arquivos para as subpastas de acordo com as regras.
- Cria as subpastas caso não existam.

## Exemplo de Uso

1. Execute o script Python.
2. Selecione a pasta que contém os arquivos a serem organizados como pasta de origem.
3. Selecione a pasta onde os arquivos serão organizados como pasta de destino.
4. O script moverá os arquivos para as subpastas de acordo com as regras definidas.

# Documentação das Funções

1. **ask_pasta_origem():** Solicita ao usuário a pasta de origem e retorna o caminho selecionado.
2. **ask_pasta_destino():** Solicita ao usuário a pasta de destino e retorna o caminho selecionado.
3. **listar_arquivos(pasta_origem):** Retorna uma lista com os nomes dos arquivos na pasta de origem.
4. **mover_arquivo(nome_arquivo, pasta_origem, pasta_destino, nova_pasta):** Move um arquivo para a nova pasta especificada.
5. **organizar_arquivos():** Função principal que organiza os arquivos de acordo com as regras definidas.
