from functions.run_python_file import  run_python_file

if __name__ == "__main__":
	print(run_python_file("calculator", "main.py"))
	print(run_python_file("calculator", "tests.py"))
	print(run_python_file("calculator", "../main.py"))
	print(run_python_file("calculator", "nonexistent.py"))