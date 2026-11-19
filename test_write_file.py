from functions.write_file import write_file


def pretty_format(working_directory, file_path, content):
    print(write_file(working_directory, file_path, content))

def main() -> None:
    pretty_format("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    pretty_format("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    pretty_format("calculator", "/tmp/temp.txt", "this should not be allowed")

main()