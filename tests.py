from functions.get_file_content import *
#from functions.get_files_info import *



if __name__ == "__main__":
    print(get_file_content("calculator", "calculator\main.py"))
    print(get_file_content("calculator", "calculator\pkg\calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))
