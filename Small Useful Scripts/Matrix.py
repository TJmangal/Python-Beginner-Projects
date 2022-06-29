class Matrix:
    def __init__(self, rows, columns, elements):
        if len(elements) != (rows * columns):
            raise ValueError(f"A {rows}x{columns} matrix cannot be formed using the elements")
        self.rows = rows
        self.columns = columns
        self.elements = elements
        self.matrix = self.__matrix()

    def __matrix(self):
        return [[self.elements[col] for col in range(row * self.columns, (row + 1) * self.columns)] for row in
                range(self.rows)]

    def get_rows_count(self):
        return len(self.matrix)

    def get_column_count(self):
        return len(self.matrix[0])

    def set_element(self, row, col, element):
        self.matrix[row-1][col-1] = element

    def __add__(self, other):
        if self.get_rows_count() != other.get_rows_count() or self.get_column_count() != other.get_column_count():
            return "Matrices cannot be added"
        return [[(self.matrix[row][col] + other.matrix[row][col]) for col in range(self.get_column_count())]
                for row in range(self.get_rows_count())]

    def __mul__(self, other):
        if self.get_rows_count() != other.get_rows_count() or self.get_column_count() != other.get_column_count():
            return "Matrices cannot be added"
        return [[(self.matrix[row][col] * other.matrix[row][col]) for col in range(self.get_column_count())]
                for row in range(self.get_rows_count())]

    def print_matrix(self):
        for row in self.matrix:
            for col in row:
                print(col, end=" ")
            print()


if __name__ == "__main__":
    matrix1 = Matrix(2, 5, [i for i in range(1, 11)])
    matrix2 = Matrix(2, 5, [i for i in range(1, 11)])

    print(matrix1.matrix)
    matrix1.set_element(2, 3, 101)

    print(matrix1.matrix)
    print(matrix2.matrix)

    print(matrix1 + matrix2)
    print(matrix1 * matrix2)

    matrix1.print_matrix()
    matrix2.print_matrix()
