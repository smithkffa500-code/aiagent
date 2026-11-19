from functions.run_python_file import run_python_file


def pretty_format(working_directory, file_path, args=None):
    print(run_python_file(working_directory, file_path, args))
    
def main() -> None:
    pretty_format("calculator", "main.py")
    pretty_format("calculator", "main.py", ["3 + 5"])
    pretty_format("calculator", "tests.py")
    pretty_format("calculator", "../main.py")
    pretty_format("calculator", "nonexistent.py")
    pretty_format("calculator", "lorem.txt")

main()