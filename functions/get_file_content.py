import os
from google.genai import types

def get_file_content(working_directory, file_path):
	max_chars = 10000
	abs_working_dir = os.path.abspath(working_directory)
	abs_file_path = os.path.abspath(str(os.path.join(working_directory, file_path)))

	if not abs_file_path.startswith(abs_working_dir, 0, len(abs_working_dir)):
		return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

	if not os.path.isfile(abs_file_path):
		return f'Error: File not found or is not a regular file: "{file_path}"'

	try:
		truncate = True if os.path.getsize(abs_file_path) > 20000 else False

		with open(abs_file_path, 'r') as f:
			if truncate:
				file_contents = f.read(max_chars)
				file_contents += f'\n[...File "{file_path}" truncated at 10000 characters]'
			else:
				file_contents = f.read()

	except Exception as e:
		return f"Error: reading file - {e}"


	return file_contents

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Returns the content of a file, constrained to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to get the contents of, relative to the working directory",
            ),
        },
    ),
)