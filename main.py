import meshlib.mrmeshpy as mr


datapath = "D:\SHREC2021\datasetCulture\train_fix\115_fix\fractured_0"
try:
    mesh0 = mr.loadMesh("piece_0.obj")
except ValueError as e:
    print(e)

try:
    #mesh1 = mr.loadMesh("115_meshinspector.obj")
    mesh1 = mr.loadMesh("115.obj")
except ValueError as e:
    print(e)


# find the difference mesh between two spheres:
diff = mr.boolean( mesh0, mesh1, mr.BooleanOperation.Intersection )
#print(diff)
# save the result in file:
mr.saveMesh(diff.mesh, mr.Path("intersec.obj"))