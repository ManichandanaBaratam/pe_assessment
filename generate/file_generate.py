import random
import string
import os

def generate_random_text(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def create_new_file():
    random_name = generate_random_text(10)
    file_name = os.path.join( "files", f"{random_name}.txt")
    with open(file_name, "w") as file:
        random_text = random_name
        file.write(random_text)

    print(f"New file created: {file_name}")

create_new_file()