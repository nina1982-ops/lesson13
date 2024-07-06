def get_matrix(n, m, value ):                  # Объявили функцию get_matrix c параметрами n, m и value.
    matrix = []                                # Создали пустой список matrix внутри функции get_matrix
    for i in range (n):                        # Первый(внешний) цикл for для кол-ва строк матрицы, n повторов
        matrix.append([])                      # Добавили пустой список в список matrix.
        for j in range(m):                     # Второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов
            matrix[i].append(value)            # Во втором цикле заполняем ранее добавленный пустой список значениями value
    return matrix                              # Вернули значение переменной matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)                                 # Вывjl на экран(консоль) результата работы функции get_matix.
print(result2)
print(result3)

