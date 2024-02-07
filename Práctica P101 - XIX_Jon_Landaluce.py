from statistics import mean

def process_matrix(matrix):

    result_matrix = []

    # Verificar si la matriz tiene longitud menor o igual a 1
    if len(matrix) <= 1:
        return result_matrix

    # Bucle externo para iterar matrix y asignar valores a las filas
    for i, row in enumerate(matrix):
        
        temporalList = []

        # Bucle interno para iterar y dar valores a los elementos de las filas
        for j, value in enumerate(row):

            # Promedio Esquina Superior Izquierda
            if i == 0 and j == 0:
                temporalList.append(mean([matrix[0][0], matrix[0][1], matrix[1][0]]))

            # Promedio Esquina Superior Derecha
            elif i == 0 and j == len(matrix[i]) - 1:
                temporalList.append(mean([matrix[0][-2], matrix[0][-1], matrix[1][-1]]))

            # Promedio Esquina Inferior Izquierda
            elif i == len(matrix) - 1 and j == 0:
                temporalList.append(mean([matrix[-1][0], matrix[-1][1], matrix[-2][0]]))

            # Promedio Esquina Inferior Derecha
            elif i == len(matrix) - 1 and j == len(matrix[i]) - 1 :
                temporalList.append(mean([matrix[-1][-1], matrix[-1][-2], matrix[-2][-1]]))



            # Promedio Elementos Borde Superior
            elif i == 0 and (j != 0 and j != len(matrix[i])):
                temporalList.append(mean([matrix[i][j], matrix[i][j - 1], matrix[i][j + 1], matrix[1][j]]))

            # Promedio Elementos Borde Inferior
            elif i == len(matrix) - 1 and (j != 0 and j != len(matrix[i])):
                temporalList.append(mean([matrix[i][j], matrix[i][j - 1], matrix[i][j + 1], matrix[i - 1][j]]))

            # Promedio Elementos Borde Izquierdo
            elif (i != 0 and i != len(matrix) - 1) and j == 0:
                temporalList.append(mean([matrix[i][0], matrix[i - 1][0], matrix[i + 1][0], matrix[i][1]]))

            # Promedio Elementos Borde Derecho
            elif (i != 0 and i != len(matrix) - 1) and j == len(matrix[i]) - 1:
                temporalList.append(mean([matrix[i][len(matrix[i]) - 1 ], matrix[i - 1][len(matrix[i]) - 1 ], matrix[i + 1][len(matrix[i]) - 1 ], matrix[i][len(matrix[i]) - 2 ]]))



            # Promedio Elementos Internos
            else:
                temporalList.append(mean([matrix[i][j], matrix[i + 1][j], matrix[i - 1][j], matrix[i][j + 1], matrix[i][j - 1]]))


        result_matrix.append(temporalList)


    return result_matrix



result = process_matrix([

    [2, 5, 8, 3, 1, 7, 4, 9, 6, 2],
    [6, 1, 7, 8, 4, 2, 9, 3, 5, 8],
    [4, 9, 3, 5, 1, 6, 7, 8, 2, 4],
    [8, 2, 6, 7, 3, 9, 1, 4, 5, 6],
    [1, 7, 4, 9, 5, 8, 3, 6, 2, 1],
    [5, 8, 2, 1, 6, 4, 9, 2, 7, 5],
    [7, 3, 9, 2, 8, 5, 6, 1, 4, 7],
    [9, 6, 1, 4, 2, 3, 8, 5, 3, 9],
    [3, 4, 5, 6, 7, 1, 2, 7, 9, 3],
    [2, 1, 8, 3, 9, 7, 5, 4, 1, 8]

])

print(result)