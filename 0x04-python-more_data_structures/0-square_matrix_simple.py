def square_matrix_simple(matrix=[]):
  """
  Computes the square value of all integers of a matrix.

  Args:
    matrix: A 2 dimensional array.

  Returns:
    A new matrix with the squares of the elements of the input matrix.
  """

  new_matrix = []
  for row in matrix:
    new_row = []
    for element in row:
      new_row.append(element ** 2)
    new_matrix.append(new_row)
  return new_matrix
