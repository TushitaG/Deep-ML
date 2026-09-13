import numpy as np
def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	new_matrix = np.array(matrix)
	new_matrix = new_matrix*scalar
	return new_matrix