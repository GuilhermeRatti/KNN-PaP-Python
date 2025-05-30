# Trabalho de PaP: Agrupamento de Dados Multi Dimensionais.
Código e estrutura idealizado e implementado por Guilherme Ratti Moraes como trabalho em python para a disciplina de Paradigmas de Programação (PaP).

## Estruturas de Dados usados no trabalho:
* Heap;
* Union-find;  
* Vertex;
* Edge.

### Heap:
  A heap foi usada como fila de prioridade para o algoritmo proposto para a solução do problema. útil tanto para pegar o próximo ponto com menor distância quanto para decidir quais arestas seriam removidas.

### Union-find:
  O union-find foi usado para ter o controle de quais pontos estavam conectados e quais ainda eram "elegíveis". Como remoção de conecção em union-find é algo problemático, essa funcionalidade não foi implementada.

### Vertex:
  Estrutura de dados criada para armazenar os pontos no espaço N dimensional. Representada por uma classe com overload de funções built-in como __lt__() e __gt__().

### Edge:
  Estrutura de dados criada para armazenar a distância entre dois pontos no espaço N dimensional. Representada por uma classe com overload de funções built-in como __lt__() e __gt__().

## Algoritmo Proposto
  Inicialmente, realiza-se a leitura dos arquivos para que os pontos sejam armazenados em uma lista de Vertex. Em um segundo momento, é criada uma lista de Heaps mínimos. Cada índice da lista está diretamente relacionado ao respecivo ponto. Cada Heap mínima armazena todas as distâncias do seu respectivo ponto para todos os outros pontos. Ex.: a heap no índice 0 da lista está relacionada ao ponto 0 e possui a distância do ponto 0 para todos os outros pontos. Cria-se, também, um union-find para controlar o agrupamento de pontos e uma Heap de máximos vazia, para armazenar as arestas usadas para conexões.
  Na primeira iteração do algoritmo, toma-se o ponto 0 como ponto corrente e o ponto com menor distância ao ponto 0 é selecionado pela Heap mínima do índice 0. Verifica-se se o ponto é válido (ainda não foi marcado como conectado pelo union-find) e, se for, conecta-o pelo union find, adiciona a aresta usada para o heap de máximos e torna este ponto o novo ponto corrente; caso o ponto não seja válido, o novo ponto mais próximo é obtido via heap. Essa etapa é repetida N-1 vezes, sendo N o número de pontos;
  Em um último momento, retira-se as K-1 maiores arestas armazenadas no Heap de máximos, sendo K o número de agrupamentos desejados. Com isso, refaz-se a estrutura de union-find usando o restante das ligações no Heap de máximos. Isso vai resultar na marcação dos grupos desejados; a resposta do problema.

## Entrada
  Este programa aceita entradas tanto via argumentos de terminal quanto entrada do console, o que o usuário julgar mais pertinente. Exemplos de uso:
    python3 main.py Caminho/Do/Arquivo-de-entrada.csv Caminho/Do/Arquivo-de-saida.txt Num-Agrupamentos 
    python3 main.py Validacao/base3.csv Resultados/base3k3.txt 3
    python3 main.py
      ... Entradas de K e de arquivo fornecidos posteriormente por console

##  Formatação da Saída
  Os agrupamentos são ordenados internamente em ordem crescente, depois os agrupamentos são ordenados entre si de forma crescente, também, em relação ao menor elemento de cada agrupamento. A saída será redirecionada ao arquivo de saída especificado ou, caso não seja fornecido nenhum arquivo de saída, a saída será representada no console.
