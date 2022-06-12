def bubble_sort(vector: list) -> list:
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(vector) - 1):
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
                sorted = False
    return vector


if __name__ == "__main__":
    lista = [5, 3, 2, 4, 7, 1, 0, 6]
    lista_ordenada = bubble_sort(lista)
    print(lista_ordenada)
