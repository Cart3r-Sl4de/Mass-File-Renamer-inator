import os

directory_path = os.path.dirname(os.path.abspath(__file__))
# print(directory_path)
for file in os.listdir(directory_path):
    #print(file[-4:])
    if file[-4:] == ".gba":
        rename = f"{file[7:]}"
        new_path = os.path.join(directory_path, rename)
        old_path = os.path.join(directory_path, file)
        os.rename(old_path, new_path)


def main():

    print("soup")

main()
