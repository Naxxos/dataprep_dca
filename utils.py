import os
import tarfile
from pathlib import Path, PurePath

PATH = Path.cwd()
PATH_SRC = Path.joinpath(PATH, 'src')
PATH_DATA = Path.joinpath(PATH, 'data')

def create_repositories(data_path=PATH_DATA, src_path=PATH_SRC):
    print("Creating repositories")
    try:
        os.mkdir(data_path)  
    except FileExistsError :
        print("Directory \"data\" already exist")
        
    for i in os.listdir(src_path):
        try:
            os.mkdir(Path.joinpath(data_path, i))
        except FileExistsError :
            print("Directory \""+i+"\" already exist")


def extract_tar_gz(data_path=PATH_DATA, src_path=PATH_SRC):
    print("Extracting tar.gz files")
    list_error = []
    for i in os.listdir(src_path):
        directory = Path.joinpath(src_path, i)
        os.chdir(Path.joinpath(data_path,i))
        for file in os.listdir(directory):
            try:
                tf = tarfile.open(Path.joinpath(directory, file))
                tf.extractall()
            except :
                list_error += file
                              
def clean_empty_files(data_path=PATH_DATA):
    print("Cleaning empty files")
    count = 0
    for i in os.listdir(data_path):
        for file in os.listdir(Path.joinpath(data_path,i)):
            path_file = Path.joinpath(data_path,i,file)
            if os.path.getsize(path_file) <= 3000:
                os.remove(path_file)
                count += 1
    print(count, " files deleted")


