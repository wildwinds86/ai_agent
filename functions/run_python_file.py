import os
import sys
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(str(os.path.join(working_directory, file_path)))

    if not abs_file_path.startswith(abs_working_dir, 0, len(abs_working_dir)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if os.path.splitext(abs_file_path)[1] != ".py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        os.chdir(abs_working_dir)
        code_run = subprocess.run([sys.executable, abs_file_path], timeout=30, capture_output=True)
        output = [f"Ran {file_path}",f"STDOUT: {str(code_run.stdout).lstrip('b')}", f"STDERR: {str(code_run.stderr).lstrip('b')}"]
        return_code = code_run.returncode

        if return_code != 0:
            return f"Process exited with code {return_code}"

        if code_run.stdout == "b''\n":
            return "No output produced"
        else:
            return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"