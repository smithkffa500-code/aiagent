import os
from config import *


def get_file_content(working_directory: str, file_path: str) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    if os.path.isfile(target_file) == False:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # Will be True or False
    valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

    if valid_target_file == False:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    with open(target_file, "r") as f:
        content = f.read(MAX_CHARS)
        # After reading the first MAX_CHARS...
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return content

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Gets the content of a specified file path, relative to the working directory.",
        "parameters": {
            "type": "object",
            "required": {
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path of file to retreive content from, relative to the working directory",
                    },
                },
            },
        },
    },
}