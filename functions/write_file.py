import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    if os.path.isdir(target_file) == True:
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    # Will be True or False
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if valid_target_file == False:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    parent_dir = os.path.dirname(target_file)
    if os.path.isfile(target_file) == False:
            os.makedirs(parent_dir, exist_ok=True)

    with open(target_file, "w") as f:
        f.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content to a specified file path, relative to the working directory. This will overwrite anything that was previously in the file.",
        "parameters": {
            "type": "object",
            "required": {
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path of file to write to, relative to the working directory",
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to write to file. This will overwrite anything that was previously in the file."
                    },
                },
            },
        },
    },
}