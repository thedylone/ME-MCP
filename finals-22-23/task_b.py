"""Task B"""

import os
import numpy as np

CID: str = os.environ.get("CID", "02131550")
# CID = "02131550"


def import_matrix() -> np.ndarray:
    """The file Matrix.txt contains 49 numerical values. Read in the content
    and organise the values into a mathematical matrix A, with
    dimensions 7 x 7, composing it row by row."""
    mat_a: np.ndarray = np.loadtxt("Matrix.txt", dtype=float).reshape(7, 7)
    return mat_a


def create_matrix_c(matrix_a) -> np.ndarray:
    """Write a script to form a matrix C, obtained by augmenting matrix A
    with an extra row and an extra column, positioned as first row and
    first column, respectively, as depicted in Figure 1.
    Each element C0j of the new first row will contain the largest value of
    the respective column in A.
    Each element Ci0  of the new first column will contain the smallest value
    of the respective row in A
    """
    mat_c: np.ndarray = np.zeros((8, 8))
    mat_c[0, 1:] = matrix_a.max(axis=0)
    mat_c[1:, 0] = matrix_a.min(axis=1)
    mat_c[1:, 1:] = matrix_a
    return mat_c


def diagonals(matrix) -> tuple[float, float]:
    """Write a function, Diagonals(), to calculate the sum of all the elements
    in the diagonal of C and the sum of all the elements in the anti-diagonal
    of C. The function receives a matrix as input argument and returns a tuple
    with two values as output argument, namely the values of the two sums."""
    diagonal: float = matrix.diagonal().sum()
    anti_diagonal: float = np.fliplr(matrix).diagonal().sum()
    return diagonal, anti_diagonal


def minor(matrix, i, j) -> np.ndarray:
    """Returns the minor of a matrix, after removing row i and column j."""
    return np.delete(np.delete(matrix, i, 0), j, 1)


def sum_det_minor(matrix) -> float:
    """Write a script to compute the sum S of the determinants of all the
    minor matrices that can be obtained from matrix C"""
    return sum(
        (
            np.linalg.det(minor(matrix, i, j))
            for i in range(len(matrix))
            for j in range(len(matrix))
        )
    )


def subdivide_and_transpose(matrix) -> np.ndarray:
    """Subdivide matrix C in four sub-quadrants. Compose a new matrix D, of
    same size as C, where each sub-quadrant is obtained by transposing the
    homologous sub-quadrant of C"""
    mat_d: np.ndarray = np.zeros((8, 8))
    mat_d[:4, :4] = np.transpose(matrix[:4, :4])
    mat_d[:4, 4:] = np.transpose(matrix[:4, 4:])
    mat_d[4:, :4] = np.transpose(matrix[4:, :4])
    mat_d[4:, 4:] = np.transpose(matrix[4:, 4:])
    return mat_d


def main() -> None:
    """Implement the following operations:
    1. Read the matrix A from the file Matrix.txt
    2. Create the matrix C
    3. Compute the sum of the diagonal and anti-diagonal elements of C
    4. Compute the sum of the determinants of all the minor matrices that can
    be obtained from C
    5. Subdivide C in four sub-quadrants. Compose a new matrix D, of same size
    as C, where each sub-quadrant is obtained by transposing the homologous
    sub-quadrant of C"""
    mat_a: np.ndarray = import_matrix()
    print(mat_a)
    mat_c: np.ndarray = create_matrix_c(mat_a)
    print(mat_c)
    print(diagonals(mat_c))
    print(sum_det_minor(mat_c))
    mat_d: np.ndarray = subdivide_and_transpose(mat_c)
    print(mat_d)


if __name__ == "__main__":
    main()
