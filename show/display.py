import os
import time
path='/app/files'
file_name=str(len(os.listdir(path)))
file_name=file_name+".txt"
filepath = os.path.join(path, file_name)
def display():
    with open(filepath,"r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
if __name__ == "__main__":  
    display()
