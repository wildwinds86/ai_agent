#from functions.get_file_content import *
#from functions.get_files_info import *
#from functions.write_file import write_file
from functions.run_python_file import  run_python_file

if __name__ == "__main__":
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))