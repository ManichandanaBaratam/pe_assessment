import random
import string
import os
from datetime import datetime
import os
import time

def generate_random_text():
    # letters = string.ascii_letters + string.digits
    letters=datetime.now().strftime("%H-%M-%S %d-%m-%Y") 
    return ''.join(letters)


def create_new_file():
    path='/app/files'
    file_name=len(os.listdir(path))+1
    random_name = generate_random_text()
    file_name = os.path.join( "files", f"{file_name}.txt")
    with open(file_name, "w") as file:
        random_text = random_name
        file.write(random_text)

    print(f"New file created: {file_name}")
if __name__ =="__main__":
    create_new_file()