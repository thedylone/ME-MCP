Some useful functions you will likely use.

[A useful guide to conventions in Python](https://peps.python.org/pep-0008/)

<details><summary>Table of Contents</summary>

1. [Variable Manipulation](#Variable-Manipulation)
2. [Lists](#Lists)
3. [File I/O](#File-I/O)
4. [Matrices](#Matrices)
5. [Maths](#Maths)
  
</details>

---
# Variable Manipulation

Swap two variables
```python
a, b = b, a
```
> No need for a temporary variable

Increment a variable
```python
a += value
```

Multiply a variable
```python
a *= value
```

Divide a variable
```python
a /= value
```

Floor divide a variable
```python
a //= value
```

Modulo a variable
```python
a %= value
```

Exponentiate a variable
```python
a **= value
```


# Lists

Concatenating two lists
```python
list_a + list_b
```

Appending an element to a list
```python
list_a.append(6)
```

Inserting an element into a list
```python
list_a.insert(0, 0)
```

Removing an element from a list
```python
list_a.remove(0)
```

Removing an element from a list by index
```python
element = list_a.pop(0)
```

Slice a list
```python
list_a[0:3]
```

Reverse a list
```python
list_a[::-1]
```

List comprehension is a concise way to generate a list.
```python
list_a = []
for i in range(10):
    list_a.append(i)

# is equivalent to:

list_a = [i for i in range(10)]
```

Similarly,
```python
list_a = []
for i in range(10):
    if i % 2 == 0:
        for j in range(20):
            if j % 3 == 0:
                list_a.append((i, j))

# is equivalent to:

list_a = [(i, j) for i in range(10) if i % 2 == 0 for j in range(20) if j % 3 == 0]
```
> However it can get quite confusing to read, so it is best to use it sparingly and only when it makes the code more concise.

```

Generate a list of numbers from 0 to n-1
```python
list(range(n))
```

Generate a list of numbers from a to b-1
```python
list(range(a, b))
```

Generate a list of numbers from a to b-1 with a step size of c
```python
list(range(a, b, c))
```

Generate a list of N zeroes
```python
list_a = [0] * N
```
> Note that this cannot be used to generate a list of N lists of zeroes as the lists are the same object

Generate a list of N lists of zeroes (with list comprehension)
```python
list_a = [[0] * N for _ in range(N)]
```

Generate a list of N lists of M zeroes (with list comprehension)
```python

list_a = [[0] * M for _ in range(N)]
```

Sort a list
```python
list_a.sort() # sorts in place
list_a = sorted(list_a) # returns a new list
list_a.sort(reverse=True) # sorts in descending order
list_a.sort(key=lambda x: x[1]) # sorts by the second element in each tuple
```
> The ```key``` argument is a function which is applied to each element in the list before sorting.



Many operations which involve the elements within the list can be achieved via ```map``` functions, as well as using ```zip```.

Squaring the elements in a list
```python
list(map(lambda x: x * x, list_a))
```

Summing up the elements in two lists into a new list
```python
list(map(sum, zip(self.list_a, self.list_b)))
```
# File I/O

It is good practice to close the file as soon as you are done with it. This is done using the ```with``` statement.

Reading a file
```python
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(lines) # prints a list of lines

with open("input.txt", "r", encoding="utf-8") as f:
    lines = [line for line in f]
```

Reading a file line by line
```python
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line)

with open("input.txt", "r", encoding="utf-8") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line)
```

Cleaning up the lines
```python
with open("input.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
```


Writing to a file
```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello World!")

with open("output.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")

with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```


# Matrices

Reflect a matrix horizontally
```python
def reflect_x(matrix):
    """Returns the matrix reflected horizontally"""
    return [row[::-1} for row in matrix]
```

Reflect a matrix vertically
```python
def reflect_y(matrix):
    """Returns the matrix reflected vertically"""
    return matrix[::-1]
```

Transpose a matrix
```python
def transpose(matrix):
    """Returns the transpose of the matrix"""
    return list(map(list, zip(*matrix)))
````

Rotate a matrix clockwise
```python
def rotate(matrix):
    """Returns the matrix rotated clockwise"""
    return list(map(list, zip(*matrix[::-1])))
```
> Note that it is the tranpose of a vertical flip of the matrix

Rotate a matrix anticlockwise
```python
def antirotate(matrix):
    """Returns the matrix rotated anticlockwise"""
    return list(map(list, zip(*matrix)[::-1]))
```
> Note that it is a vertical flip of the transpose of the matrix

Scalar multiplication
```python
def scalar_mult(scalar, matrix):
    """Multiply a matrix by a scalar."""
    return [[scalar * val for val in row] for row in matrix]
```

Matrix multiplication
```python
def matmult(matrix_a, matrix_b):
    """Multiply two matrices. Return 0 if the sizes are incompatible."""
    if len(matrix_a[0]) != len(matrix_b):
            return [[0]]
    zip_b = list(zip(*matrix_b))
    return [
            [
                sum(val_a * val_b for val_a, val_b in zip(row_a, col_b))
                for col_b in zip_b
            ]
            for row_a in matrix_a
        ]
```

Minor of a matrix
```python
def minor(matrix, i, j):
        """Returns the minor of a matrix, after removing row i and column j."""
        return [
            row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])
        ]
```

Determinant of a matrix
```python
def determinant(matrix):
    """Returns the determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return sum(
        (-1) ** i
        * matrix[0][i]
        * determinant(minor(matrix, 0, i))
        for i in range(len(matrix))
    )
```

Adjoint of a matrix
```python
def adjoint(matrix):
    """Return the adjoint of a matrix."""
    # check square matrix
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix is not square.")
    return transpose(
        [
            [
                ((-1) ** (i + j))
                * determinant(minor(matrix, i, j))
                for j in range(len(matrix))
            ]
            for i in range(len(matrix))
        ]
    )
```

Inverse of a matrix
```python
def inverse(matrix) -> list[list[float | int]]:
    """Return the inverse of a matrix."""
    # check determinant != 0
    det = determinant(matrix)
    if det == 0:
        raise ValueError("Determinant is 0, inverse does not exist.")
    return scalar_mult(1 / det, adjoint(matrix))
```

Matrix class (if numpy not available)
```python
class Matrix:
    """Matrix class"""

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str(self.matrix)

    def __repr__(self):
        return str(self.matrix)

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Matrices must have same number of rows")
        if len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must have same number of columns")
        return Matrix(
            [
                [
                    self.matrix[i][j] + other.matrix[i][j]
                    for j in range(len(self.matrix[i]))
                ]
                for i in range(len(self.matrix))
            ]
        )

    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix):
            raise ValueError("Matrices must have same number of rows")
        if len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices must have same number of columns")
        return Matrix(
            [
                [
                    self.matrix[i][j] - other.matrix[i][j]
                    for j in range(len(self.matrix[i]))
                ]
                for i in range(len(self.matrix))
            ]
        )

    def __matmul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError(
                "Matrices must have same number of rows and columns"
            )
        zip_b = list(zip(*other.matrix))
        return Matrix(
            [
                [
                    sum(val_a * val_b for val_a, val_b in zip(row_a, col_b))
                    for col_b in zip_b
                ]
                for row_a in self.matrix
            ]
        )

    def __mul__(self, other):
        if isinstance(other, int):
            return Matrix(
                [[other * val for val in row] for row in self.matrix]
            )
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError(
                "Matrices must have same number of rows and columns"
            )
        zip_b = list(zip(*other.matrix))
        return Matrix(
            [
                [
                    sum(val_a * val_b for val_a, val_b in zip(row_a, col_b))
                    for col_b in zip_b
                ]
                for row_a in self.matrix
            ]
        )

    def __rmul__(self, other: int | float):
        return Matrix([[other * val for val in row] for row in self.matrix])

    def __truediv__(self, other: int):
        return Matrix(
            [
                [self.matrix[i][j] / other for j in range(len(self.matrix[i]))]
                for i in range(len(self.matrix))
            ]
        )

    def __eq__(self, other) -> bool:
        if len(self.matrix) != len(other.matrix):
            return False
        if len(self.matrix[0]) != len(other.matrix[0]):
            return False
        return all(
            [
                self.matrix[i][j] == other.matrix[i][j]
                for i in range(len(self.matrix))
                for j in range(len(self.matrix[i]))
            ]
        )

    def __ne__(self, other) -> bool:
        return not self == other

    def __getitem__(self, key: tuple[int, int]) -> int:
        return self.matrix[key[0]][key[1]]

    def __setitem__(self, key: tuple[int, int], value: int) -> None:
        self.matrix[key[0]][key[1]] = value

    def __len__(self):
        return len(self.matrix)

    def __iter__(self):
        return iter(self.matrix)

    def __next__(self):
        return next(self.matrix)

    @staticmethod
    def _transpose(matrix):
        """Transpose the matrix"""
        return Matrix(list(map(list, zip(*matrix))))

    @property
    def tranpose(self):
        """Transpose the matrix"""
        return Matrix._transpose(self.matrix)

    @staticmethod
    def _minor(matrix, i, j):
        """Returns the minor of a matrix."""
        return [
            row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])
        ]

    @staticmethod
    def _determinant(matrix):
        """Returns the determinant of a matrix."""
        if len(matrix) == 1:
            return matrix[0][0]
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return sum(
            (-1) ** i
            * matrix[0][i]
            * Matrix._determinant(Matrix._minor(matrix, 0, i))
            for i in range(len(matrix))
        )

    @property
    def determinant(self):
        """Returns the determinant of a matrix."""
        return Matrix._determinant(self.matrix)

    @staticmethod
    def _adjoint(matrix):
        """Return the adjoint of a matrix."""
        # check square matrix
        if len(matrix) != len(matrix[0]):
            raise ValueError("Matrix is not square.")
        return Matrix._transpose(
            [
                [
                    ((-1) ** (i + j))
                    * Matrix._determinant(Matrix._minor(matrix, i, j))
                    for j in range(len(matrix))
                ]
                for i in range(len(matrix))
            ]
        )

    @staticmethod
    def _inverse(matrix):
        """Return the inverse of a matrix."""
        # check determinant != 0
        det = Matrix._determinant(matrix)
        if det == 0:
            raise ValueError("Determinant is 0, inverse does not exist.")
        return 1 / det * Matrix._adjoint(matrix)

    @property
    def inverse(self):
        """Return the inverse of a matrix."""
        return Matrix._inverse(self.matrix)
```

# Maths

Greatest Common Divisor

```python
def gcd(num_a, num_b):
    """Greatest Common Divisor"""
    if num_a == 0:
        return num_b
    return gcd(num_b % num_a, num_a)
```

Lowest Common Multiple

```python
def lcm(num_a, num_b):
    """Least Common Multiple"""
    return (num_a * num_b) // gcd(num_a, num_b)