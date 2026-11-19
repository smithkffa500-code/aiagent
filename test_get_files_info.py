from functions.get_files_info import get_files_info

def pretty_format(working_directory, directory):
    if directory == ".":
        print("Result for current directory:")
    else:
        print(f"Result for {directory} directory:")
    print(get_files_info(working_directory, directory))

def main():
    pretty_format("calculator", ".")
    pretty_format("calculator", "pkg")
    pretty_format("calculator", "/bin")
    pretty_format("calculator", "../")

main()