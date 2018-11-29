import sys

sys.path.insert(0, "D:\programmation\prog\python")



from fonction.path_to_file import Path

dir = "log"
data_file = "test.log"
path = Path(dir,data_file)


print(path.parent_path_to_file())
