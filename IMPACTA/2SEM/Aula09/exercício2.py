"""
<-------------->x<-------------->x<------------->x<------------->x<------------->
|Aula 9: técnicas de programação IMPACTA 05 de Setembro de 2024                 |
|Anotações e comentários feitos por Gabriel Muchon Pavanelli (github: gblsunn)  |
|                                                                               |
|    Exercícios:                                                                |
|        Recursividade e Memoização                                             |
<-------------->x<-------------->x<------------->x<------------->x<------------->

2.
Defina a função recursiva div que recebe como parâmetros dois números naturais m e n e retorna o resultado da divisão inteira de m por n. Neste exercício, não se pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.

função recursiva div que recebe como parâmetros dois números naturais m e n 
retorna o resultado da divisão inteira de m por n. 

Neste exercício, não se pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.

"""

# %% --begin
# imports
from functools import lru_cache

# funções
def div(m, n):
    if m < n: 
        return 0
    else:
        return 1+div(m-n,n)
        # contador = 0  <--------------- função não recursiva
        # while valor_restante < n:
        #     valor_restante = m - n 
        #     contador += 1
        # return contador

# programa principal
print(div(10, 3))

# %% --end
