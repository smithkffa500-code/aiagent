from functions.get_file_content import get_file_content


def pretty_format(working_directory, file_path):
    result = get_file_content(working_directory, file_path)
    if 'truncated' in result:
        print(f"{file_path} length: {len(result)}")
        print(f"{file_path} truncated: {'truncated' in result}")
    else:
        print(result)

def main() -> None:
    pretty_format("calculator", "lorem.txt")
    pretty_format("calculator", "main.py")
    pretty_format("calculator", "pkg/calculator.py")
    pretty_format("calculator", "/bin/cat")
    pretty_format("calculator", "pkg/does_not_exist.py")

main()