import os

# ideas: file-inator, replace in rename, 

# print(directory_path)
def rmCharInator(directory_path, extension):
    # get the length of the extension to prevent that from being overwritten
    ext_len = len(extension) * -1
    prefix_del = int(input("[?] If you want to delete the first _ characters, type any number above 0:\n[~] "))
    suffix_del = int(input("[?] If you want to delete the last _ characters, type any number above 0:\n[~] "))
    print("[!] Affected Files:")

    for file in os.listdir(directory_path):

        if file[ext_len:] == extension:
            # remove the file extension so that it doesn't get removed in the process
            rename = f"{file[:ext_len]}"
            # if the prefix deletion was set, delete the requested amount of characters
            rename = f"{rename[prefix_del:]}" if prefix_del > 0 else rename
            # if suffix deletion was set, delete requested amount of characters from the end
            rename = f"{rename[:(suffix_del * -1)]}" if suffix_del > 0 else rename
            # put the extension back in the filename, or so help me!
            rename += extension
            # show user what has been affected
            print(f"[!] {rename}")
            
            ### make filepath for the renamed file and for the old file, and then officially rename the file!
            new_path = os.path.join(directory_path, rename)
            old_path = os.path.join(directory_path, file)
            os.rename(old_path, new_path)

def replacerInator(directory_path, extension):
    question = "[?] Please type the character"
    ext_len = len(extension) * -1
    # the character to be replaced
    victim_char = input(f"{question} you want replaced: ")
    replace_char = input(f"{question} to replace the previous: ")
    
    certainty = input(f"[?] Are you sure you want to replace {victim_char} with {replace_char}? (y/n): ")
    if certainty == "y":
        print("[!] Affected files:")

        for file in os.listdir(directory_path):
            # see if the file in question is the optimal filetype
            if file[ext_len:] == extension:
                rename = f"{file[:ext_len]}"
                rename = rename.replace(victim_char, replace_char)
                rename += extension
                print(f"[!] {rename}")

                new_path = os.path.join(directory_path, rename)
                old_path = os.path.join(directory_path, file)
                os.rename(old_path, new_path)




def main():

    directory_path = os.path.dirname(os.path.abspath(__file__))

    print("[#] Welcome to the File-Renamer-Inator!\n[#] Before we begin, make sure this program is in the folder with the files you want to edit!")
    confirmation = input("[?] Type y if so, anything else to exit:\n[~] ")
    
    if confirmation == "y":
        extension = input("[?] For the files you want to manipulate, what is the file extension? (ex: .png, .mp3)\n[~] ")
        rmchar = input("[?] Now then, do you want to remove characters from your filenames? (Type y to proceed)\n[~] ")
        replacer = input("[?] Do you want to replace characters that are in the filename?\n[~] ")


        
        if rmchar == "y":
            rmCharInator(directory_path, extension)
        if replacer == "y":
            replacerInator(directory_path, extension)

main()
