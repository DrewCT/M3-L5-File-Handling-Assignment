import os

def list_directory_contents(path):
    try:
        print(f"Contents of '{path}':")
        for item in os.listdir(path):
            print(item)
    except FileNotFoundError:
        print(f"Error: The path '{path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)