import os

class Path:

    def __init__(self,dir,data_file):

        self.dir = dir
        self.data_file = data_file

    def parent_path_to_file(self):
        path_to_file = os.path.join(os.pardir, self.dir, self.data_file)
        return path_to_file


