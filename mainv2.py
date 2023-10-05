import tripy
import numpy as np

def get_vf_from_file(file_path):
    # Initialize lists to store vertices and faces
    vertices = []
    faces = []

    # Open and read the file
    with open(file_path, 'r') as file:
        for line in file:
            # Strip leading and trailing whitespace
            line = line.strip()
            
            # Check if the line starts with 'v' (vertex) or 'f' (face)
            if line.startswith('v '):
                # Remove the 'v ' prefix and split the line into coordinates
                vertex_data = line[2:].split()
                # Convert coordinates to floats and append to the vertices list
                vertex = [float(coord) for coord in vertex_data]
                vertices.append(vertex)
            elif line.startswith('f '):
                # Remove the 'f ' prefix and split the line into face indices
                face_data = line[2:].split()
                # Convert face indices to integers and append to the faces list
                face = [int(index) for index in face_data]
                faces.append(face)

    # Now, 'vertices' contains a list of vertex coordinates, and 'faces' contains a list of face indices
    return (vertices, faces)

file1 = "piece_0.obj"
res1 = get_vf_from_file(file1)

print(file1)
print('Vertices:', len(res1[0]))
print('Faces:', len(res1[1]))

file2 = "115_meshinspector.obj"
res2 = get_vf_from_file(file2)

print(file2)
print('Vertices:', len(res2[0]))
print('Faces:', len(res2[1]))

vertices_model1 = np.array(res1[0])  # Vertices of model 1
faces_model1 = np.array(res1[1])     # Faces (triangles) of model 1
vertices_model2 = np.array(res2[0])  # Vertices of model 2
faces_model2 = np.array(res2[1])     # Faces (triangles) of model 2

intersection_triangles = []

for triangle1 in faces_model1:
    for triangle2 in faces_model2:
        intersection = np.intersect(triangle1, triangle2)
        if intersection:
            intersection_triangles.append(intersection)

# Extract intersection vertices
intersection_vertices = np.unique(np.vstack(intersection_triangles), axis=0)

print(len(intersection_vertices))