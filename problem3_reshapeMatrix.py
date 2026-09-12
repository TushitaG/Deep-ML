import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	a_length = len(a) * len(a[0])
	new_length = new_shape[0] * new_shape[1]
	reshaped_matrix = []
	if(a_length == new_length):
		matrix = np.array(a)
		reshaped_matrix = matrix.reshape(new_shape)
		reshaped_matrix = reshaped_matrix.tolist()
	return reshaped_matrix