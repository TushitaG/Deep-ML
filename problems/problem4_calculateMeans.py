import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	new_matrix = np.array(matrix)
	means = []
	if(mode == "row"):
		means=new_matrix.mean(axis=1)

	elif (mode=="column"):
		means=new_matrix.mean(axis=0)
	means = means.tolist()
	return means