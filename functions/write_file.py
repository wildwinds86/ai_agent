import os

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