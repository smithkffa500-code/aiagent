import os, subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if os.path.isfile(target_file) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if target_file.endswith('.py') == False:
            return f'Error: "{file_path}" is not a Python file'
        
        # Will be True or False
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if valid_target_file == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        command = ["python", target_file]
        if args != None:
            command.extend(args)
        completed_process = subprocess.run(command, capture_output=True, timeout=30, text=True)
        errorcode = ""
        no_output = ""
        stdout_str = "STDOUT:\n"
        stderr_str = "STDERR:\n"

        if(completed_process.returncode != 0):
            errorcode += f"Process exited with code {completed_process.returncode}"
        if(completed_process.stdout == "" and completed_process.stderr == ""):
            no_output += "No output produced\n"
            return no_output + errorcode
        else:
            return stdout_str + completed_process.stdout + stderr_str + completed_process.stderr + errorcode

    except Exception as e:
        print(f"Error: executing Python file: {e}")

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a python file at a specified file path, relative to the working directory.",
        "parameters": {
            "type": "object",
            "required": {
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path of python file to run, relative to the working directory",
                    },
                },
            },
            "properties": {
                "args": {
                    "type": "array[string]",
                    "description": "Arguments to parse."
                },
            },      
        },
    },
}