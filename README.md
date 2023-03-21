# Python Project Template

This Python project template provides a basic structure for starting a Python project.

## Project Structure

- `config.json`: A JSON file to store project configuration data, such as the hello_message used in the `main.py` script.
- `README.md`: This file, which provides an overview of the project and instructions for getting started.
- `.env`: A file that stores environment variables, such as the `USERNAME` variable used in the`main.py` script.
- `requirements.txt`: A file that lists the project dependencies. Users should install these dependencies before running the project.
- `.gitignore`: A file that specifies files and directories to be ignored by Git. This template includes standard ignore patterns for macOS and Python.
- `src`: A folder containing the main Python script.
- `main.py`: The main script that reads the `config.json` file and prints a `hello_message`. It also reads the `USERNAME` environment variable from the `.env` file.

## main.py

The `main.py` script consists of the following functions:

- `read_json_file(file_path)`: A function that reads a JSON file and returns the data as a Python object.
- `read_env_var(var_name)`: A function that reads an environment variable and returns its value. If the variable is not set, it returns the default value "Nikolai Durov".
- `print_hello_world()`: A function that reads the `hello_message` from the `config.json` file, reads the `USERNAME` environment variable, and prints both values.

When the script is run, the `print_hello_world()` function is called, and the `hello_message` from the `config.json` file and the `USERNAME` from the `.env` file are printed.

## Getting Started

- Clone or download this repository to your local machine.
- Navigate to the project directory and locate the `config.json` file. You can customize the `hello_message` value as needed.
- Create a `.env` file in the project directory and set the `USERNAME` environment variable to your desired value.
- Install the project dependencies by running the following command:

```bash
pip install -r requirements.txt
```

- Open a terminal or command prompt and navigate to the src folder.
- Run the main.py script using the following command:

```bash
python src/main.py
```

This will print the `hello_message` from the `config.json` file and the `USERNAME` from the `.env` file.
