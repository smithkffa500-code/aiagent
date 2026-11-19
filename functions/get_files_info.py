import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    if os.path.isdir(target_dir) == False:
        return f'Error: "{directory}" is not a directory'
    
    # Will be True or False
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if valid_target_dir == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    dir_contents = os.listdir(target_dir)
    pretty_contents = list(map(lambda x: f"- {x}: file_size={os.path.getsize(os.path.join(target_dir, x))}, is_dir={os.path.isdir(os.path.join(target_dir, x))}", dir_contents))
    return '\n'.join(pretty_contents)

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "required": {
                "properties": {
                    "directory": {
                        "type": "string",
                        "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                    },
                },
            },
        },
    },
}
