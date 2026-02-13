

#10.	Considere a função recursiva abaixo:

def exemplo3(n):
	if n <= 1:
		return 1
	else:
		return exemplo3(n-1) + exemplo3(n-1)

#Determine sua complexidade assintótica.
'''
    Resposta:
    A complexidade assintótica da função exemplo3 é O(2^n).
    Justificativa: A função faz duas chamadas recursivas para cada valor de n maior que 1, o que resulta em uma árvore de chamadas binária. 
    O número total de chamadas cresce exponencialmente com n, levando a uma complexidade de tempo O(2^n).
'''


#11.	Analise o seguinte algoritmo e determine sua complexidade:

def exemplo2(n):
    for i in range(n):
        j = i**2
        while j < n:
            j += 1

#Qual a complexidade de tempo total do algoritmo?
'''
    Resposta:
    A complexidade de tempo total do algoritmo é O(n^1.5).
    Justificativa: O loop externo itera n vezes. O loop interno começa em i^2 e vai até n, o que significa que o número de iterações do loop interno depende do valor de i. 
    Para i variando de 0 a n-1, o número total de iterações do loop interno pode ser aproximado pela soma dos termos (n - i^2) para i de 0 a √n, resultando em uma complexidade total de O(n^1.5).
'''
