from os import path

def launch_analysis(data_file):
    # enough path
    #directory = path.dirname(path.dirname(__file__))  # __file__ = current path, la c'est ../current_path
    directory = path.dirname(path_to_file)
    path_to_file = path.join(directory, "data", data_file)
    with open(path_to_file,"r") as f:
        preview = f.readline()


    print("Yeah!, We managed to read the file. Here is a preview: {}".format(preview))


if __name__ == "__main__":
    launch_analysis("SyceronBrut.xml")