# Dado o vetor [9, 3, 1, 4, 7], mostre as trocas passo a passo no Bubble, insertion e merge sort.
# Explique a relação entre ordenação e busca binária.

vetor = [9, 3, 1, 4, 7]


# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f'Troca: {arr}')
    return arr
#EXPLICAÇÂO: 
    # No Bubble Sort, o algoritmo percorre o vetor várias vezes, 
    # comparando elementos adjacentes e trocando-os se estiverem na ordem errada. 
    # Isso continua até que o vetor esteja completamente ordenado.


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f'Troca: {arr}')
    return arr
#EXPLICAÇÂO:
    # No Insertion Sort, o algoritmo constrói o vetor ordenado um elemento de cada vez. 
    # Ele pega cada elemento e o insere na posição correta dentro do vetor já ordenado, 
    # deslocando os elementos maiores para a direita conforme necessário.


# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
        print(f'Troca: {arr}')
    return arr
#EXPLICAÇÂO:
    # No Merge Sort, o vetor é dividido repetidamente em metades até que cada sub-vetor contenha um único elemento. 
    # Em seguida, esses sub-vetores são mesclados de volta juntos em ordem crescente, 
    # resultando em um vetor completamente ordenado.



print("Bubble Sort:")
bubble_sort(vetor.copy())

print("\nInsertion Sort:")
insertion_sort(vetor.copy())

print("\nMerge Sort:")
merge_sort(vetor.copy())


# Relação entre ordenação e busca binária:
# A busca binária requer que o vetor esteja ordenado para funcionar corretamente.
# Se o vetor não estiver ordenado, a busca binária pode retornar resultados incorretos ou falhar em encontrar o elemento desejado.
