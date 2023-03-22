

import os
import json
from dotenv import load_dotenv
# load env variables from .env file
load_dotenv()


def read_json_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def read_env_var(var_name: str) -> str:
    return os.environ.get(var_name, "Nikolai Durov")


def print_hello_world() -> None:
    config = read_json_file("config.json")
    print(config['hello_message'])
    print(f"Your name is {read_env_var('USERNAME')}?")


if __name__ == "__main__":
    print_hello_world()
