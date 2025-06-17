import os

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