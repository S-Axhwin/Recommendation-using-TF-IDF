import numpy as np

def scale_vector(vector, scale_factor):
    vector = np.array(vector)
    vector = vector * scale_factor
    return vector

def rotate_vector(vector):
    vector = np.array(vector)
    vector = np.rot90(vector)

    return vector

def reflect_vector(vector):
    vector = np.array(vector)
    vector = np.flip(vector)

    return vector

print(scale_vector([1,2], 2))