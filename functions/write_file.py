import os
from google.genai import types

def write_file(working_directory, file_path, content):
	abs_working_dir = os.path.abspath(working_directory)
	abs_file_path = os.path.abspath(str(os.path.join(working_directory, file_path)))

	if not abs_file_path.startswith(abs_working_dir, 0, len(abs_working_dir)):
		return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

	try:
		if not os.path.exists(os.path.split(abs_file_path)[0]):
			os.makedirs(os.path.split(abs_file_path)[0])

		with open(abs_file_path, 'w') as f:
			f.write(content)

	except Exception as e:
		return f"Error: writing file - {e}"

	return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to be written, relative to the working directory"),
	        "content": types.Schema(
		        type=types.Type.STRING,
		        description="The contents to be written to the file"
            ),
        },
    ),
)