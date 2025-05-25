# KNN-PaP-Python: Estrategia inicial

## Estrutura Geral do Projeto:
- Usar o logger para verificar o passo a passo da execução do codigo
- Leitura dos argumentos de entrada feita via terminal (args)
- Um arquivo main que deve executar:
    - Leitura e armazenamento dos pontos
    - Execução de uma classe de KNN, que vai realizar o agrupamento (classe de grupos)
    - Apresentar resultados

## Leitura dos Pontos:
- A leitura vai ser feita e inicialmente armazenada em uma lista
- Essa lista é "as is", não vai alterar nada, só vai fazer a leitura sequencial dos pontos
- Essa lista de pontos vai ser fornecida para a classe de KNN

## Classe de KNN:
- Vai ser feito por uma classe que recebe em seu método construtor a lista de pontos
- Essa classe vai montar uma lista com a distância de todos os pontos para todos os pontos
- Essa classe vai montar um min heap com a lista de distâncias.
- Essa classe vai ser responsável por montar os grupos e garantir uma série de exigências para o bom funcionamento do algoritmo:
    - Dois pontos de um mesmo grupo não podem ser conectados.

# Classe de heap:
- Uma classe que recebe em seu metodo construtor uma lista de tuplas (chave, valor)
- Deve dar overload nos métodos built ins de __iter__ e __next__
- Vai ser um min heap
- A chave pode ser um dicionário com os dois ids de pontos
