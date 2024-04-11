# Caixeiro-Viajante Múltiplo (mTSP)

## Introdução
O problema do Caixeiro-Viajante (PCV) é um desafio clássico que visa encontrar a rota mais curta para visitar um conjunto de cidades uma única vez e retornar à cidade de origem. Apesar da existência de algoritmos de aproximação eficazes para o PCV, novos métodos continuam a ser explorados, como os algoritmos evolutivos, devido à sua aplicabilidade em problemas do mundo real. Este projeto se concentra em uma variação do PCV, conhecida como o problema dos múltiplos caixeiros-viajantes (mTSP), onde mais de um caixeiro viajante é envolvido, cada um com um conjunto específico de cidades para visitar.

## Heurística Construtiva
A heurística utilizada para resolver o mTSP é a Heurística do Centroide. Este método busca encontrar um ponto médio, denominado centroide, que representa uma posição central em relação às cidades a serem visitadas. Inicia-se com a escolha aleatória de uma cidade como ponto de partida, seguido pelo cálculo do centroide das cidades restantes. O processo continua selecionando a cidade mais próxima do centroide para visitar, repetindo-se até que todas as cidades tenham sido visitadas. Embora ofereça uma solução aproximada para o problema, a heurística do Centroide é eficaz e relativamente simples de implementar, sendo adequada para situações práticas onde a complexidade computacional é um problema.

## Experimentos Computacionais
Os experimentos foram conduzidos em um computador macOS Sonoma com um chip Apple M1 e 16GB de memória RAM. O projeto foi implementado em Python 3.12.4 e desenvolvido no Visual Studio Code 2024. O conjunto de testes consiste em 9 instâncias, variando o número de cidades e o número de caixeiros. Os resultados obtidos para cada instância são resumidos na Tabela 1 abaixo. Observa-se uma disparidade em relação às soluções ótimas disponibilizadas, o que era esperado devido à natureza aproximada da heurística utilizada. No entanto, os resultados demonstram a eficácia da heurística do Centroide na resolução prática do mTSP.

### Instâncias de Testes
- **Número de cidades (n)**: 13, 17, 19, 31, 47, 59, 71, 83, 91
- **Número de caixeiros (m)**: 1, 3, 5

### Resultados
| Instância      | n   | m   | k  | f(x) | r    |
|----------------|-----|-----|----|------|------|
| mTSP-n13-m1    | 13  | 1   | 13 | 3071 | 4148 |
| mTSP-n17-m1    | 17  | 1   | 17 | 3948 | 5766 |
| mTSP-n19-m1    | 19  | 1   | 19 | 4218 | 7614 |
| mTSP-n31-m3    | 31  | 3   | 11 | 5841 | 8319 |
| mTSP-n47-m3    | 47  | 3   | 16 | 6477 | 12346|
| mTSP-n59-m3    | 59  | 3   | 20 | 6786 | 12078|
| mTSP-n71-m5    | 71  | 5   | 15 | 8618 | 16762|
| mTSP-n83-m5    | 83  | 5   | 17 | 9246 | 16911|
| mTSP-n91-m5    | 91  | 5   | 19 | 9586 | 19082|

**Tabela 1:** Resultados das Instâncias

## Conclusão
Os resultados dos experimentos demonstram a eficácia da heurística do Centroide na solução prática do problema dos múltiplos caixeiros-viajantes. Apesar das soluções aproximadas apresentarem disparidades em relação às soluções ótimas, a simplicidade e eficácia desta abordagem a tornam uma escolha viável para problemas do mundo real onde a complexidade computacional é uma preocupação.

# Authors

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/114159027?v=4" width=115><br><sub>Eduarda Paiva</sub>](https://github.com/PaivaEduarda) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/114162946?v=4" width=115><br><sub>Eloisa Paixão</sub>](https://github.com/eloisapaixao) | 
| :---: | :---: |

