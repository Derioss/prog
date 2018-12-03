
class Rename :

    def __init__(self,dir,pattern, add):
        self.dir = dir
        self.pattern = pattern
        self.add = add

    def rename(self):
        for f in os.listdir(self.dir):
            if re.search(self.pattern,f):
                os.rename(self.dir + "/" + f, self.dir + "/" + self.add + f )
                print(self.dir + f + " are rename in " + self.dir + self.add + f)

    def zip(self):
        for f in os.listdir(self.dir):
            if re.search(self.pattern,f):
                # faire un if en with .zip
                path = self.dir + "/" + f
                print(path)
                if not os.path.exists(path):
                    os.mkdir(path[:-4])
                else:
                    print(path + " exist ")
                z = ZipFile(path)
                z.extractall(path=path[:-4])

    def purge(dir, pattern):
        for f in os.listdir(dir):
            if re.search(pattern, f):
                os.remove(os.path.join(dir, f))



class Path:

    def __init__(self,dir,data_file):

        self.dir = dir
        self.data_file = data_file

    def parent_path_to_file(self):
        path_to_file = os.path.join(os.pardir, self.dir, self.data_file)
        return path_to_file
