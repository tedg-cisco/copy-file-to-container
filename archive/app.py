import os

def main():
    # Read environment variable
    message = os.getenv("MESSAGE", "Default Message")
    print(f"Environment Variable MESSAGE: {message}")
    
    # Read from file
    file_path = "input.txt"
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print(f"File Content from {file_path}: {content}")
    except FileNotFoundError:
        print(f"File not found at {file_path}")

if __name__ == "__main__":
    main()
