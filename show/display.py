import os
path='/app/files'
file_name=os.listdir(path)[0]
filepath = os.path.join(path, file_name)
def display():
    with open(filepath,"r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())
if __name__ == "__main__":
    display()   
