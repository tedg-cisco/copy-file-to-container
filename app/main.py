import os
import requests

def main():
    # Read environment variable
    env_var = os.getenv("MY_ENV_VAR", "default_value")
    print(f"Environment Variable: {env_var}")
    
    # Read contents of the file
    try:
        with open("/app/input.txt", "r") as f:
            content = f.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    main()
