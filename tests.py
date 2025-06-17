#from functions.get_file_content import *
#from functions.get_files_info import *
from functions.write_file import write_file


if __name__ == "__main__":
    write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
