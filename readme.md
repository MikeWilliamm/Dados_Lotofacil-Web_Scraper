## Objetivo
Extrair dados históricos da [Lotofácil](https://loterias.caixa.gov.br/Paginas/Lotofacil.aspx), sendo uma modalidade de loteria praticada no Brasil sob o controle da Caixa Econômica Federal. Com os dados extraídos, fazer a:
  - lista com a análise de números mais sorteados.
  - lista com a maior frequência de combinação entre números pares, impares e números primos.
  - Com a quantidade de aparições, mostrar o numero mais frequente e numero menos frequente.
  - A combinação de números pares, impares e primos mais frequente com sua respectiva porcentagem.

## Observação
As análises feitas pelo script não devem ser utilizadas como métricas para escolha de números em apostas reais, os sorteios reais da lotofácil são feitos de forma aleatória, assim tornando essa análise irrelevante para a assertividade em uma aposta. O projeto foi um desafio, com o objetivo pessoal de fixação de conteúdo técnico.

## Solução proposta
<b>Stacks:</b> Python (requests, pandas, collections)

Arquitetura: O Web Scraper obedece etapas hierárquicas, é primeiramente feita a requisição ao link que contem os dados históricos de sorteio em código HTML, em seguida é feito a limpeza dos dados, assim removendo caracteres de código HTML indesejados,  com os dados históricos dos sorteios limpos,  dentro de um laço de repetição com um raspador, foi possível distinguir todos os números históricos sorteados,  com a distinção de números, foi feita a contagem de quantidade de vezes que um número aparece e a quantidade de números pares, impares e primos, nessa etapa a quantidade de vezes que cada número mais aparece já é definida. Com a lista de combinações de números pares, impares e primos, é feito o agrupamento e a contagem de cada combinação, assim sendo possível definir as quantidades de  frequências  de cada combinação, e com as quantidades de frequências,  é possível mostrar numero mais frequente e numero menos frequente, e finalizando a combinação de números pares, impares e primos mais frequentes com seu respectivo percentual.

## Resultados
<b>Problemas resolvidos:</b> O [site oficial](https://loterias.caixa.gov.br/Paginas/Download-Resultados.aspx) da lotofácil apresenta falha de carregamento e muita lentidão, ainda na data de hoje 18/10/2022, dessa forma, através da inspeção da página e análise do código-fonte, foi encontrado o [link de requisição](https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotofácil) para se trazer os dados históricos dos sorteios, com ele foi possível capturar o código-fonte que contem os dados, após fazer a extração dos dados desse código, foi necessário fazer a limpeza dos dados para a remoção de caracteres HTML indesejados antes de seguir para as análises.



<b>Resultado final:</b>

```
----- Lista ordenada de números mais sorteados -----
[[8, 1513], [16, 1526], [6, 1536], [7, 1546], [23, 1558], [15, 1566], [17, 1568], [21, 1569], [2, 1572], [1, 1573], [19, 1576], [18, 1579], [22, 1579], [9, 1580], [12, 1580], [4, 1587], [3, 1598], [5, 1607], [13, 1612], [24, 1612], [14, 1613], [25, 1630], [11, 1635], [10, 1641], [20, 1644]]

```

```
----- Frequência de combinações -----
Combinacao  Frequencia     d_freq
 8p,7i,8np           1   0.037879
 1p,4i,2np           1   0.037879
 9p,6i,1np           1   0.037879
 0p,5i,1np           1   0.037879
 9p,6i,7np           2   0.075758
 0p,5i,6np           2   0.075758
 p,10i,9np           2   0.075758
 6p,9i,9np           2   0.075758
 0p,5i,2np           2   0.075758
 p,11i,9np           2   0.075758
 8p,7i,2np           2   0.075758
 p,12i,8np           3   0.113636
 1p,4i,3np           4   0.151515
 1p,4i,4np           5   0.189394
 9p,6i,2np           6   0.227273
 p,11i,8np           7   0.265152
 p,11i,6np           7   0.265152
 7p,8i,3np           8   0.303030
 p,11i,7np          11   0.416667
 7p,8i,8np          15   0.568182
 p,10i,5np          18   0.681818
 0p,5i,5np          18   0.681818
 0p,5i,4np          22   0.833333
 0p,5i,3np          24   0.909091
 p,10i,8np          24   0.909091
 6p,9i,4np          29   1.098485
 8p,7i,7np          31   1.174242
 6p,9i,8np          35   1.325758
 9p,6i,6np          38   1.439394
 8p,7i,3np          41   1.553030
 9p,6i,3np          47   1.780303
 p,10i,6np          70   2.651515
 p,10i,7np          72   2.727273
 9p,6i,5np         100   3.787879
 9p,6i,4np         106   4.015152
 7p,8i,7np         118   4.469697
 7p,8i,4np         123   4.659091
 6p,9i,5np         132   5.000000
 6p,9i,7np         144   5.454545
 8p,7i,4np         166   6.287879
 8p,7i,6np         167   6.325758
 6p,9i,6np         209   7.916667
 8p,7i,5np         263   9.962121
 7p,8i,5np         275  10.416667
 7p,8i,6np         284  10.757576

```

```
O número mais frequente é o 20 com 1644 Aparições

O número menos frequente é o 8 com 1513 Aparições

A Combinação de números pares, impares e primos mais frequentes é '7p,8i,6np' com a % de frequência igual a 10.76

```