# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}


### Running the Application

The application can be started by running the command ``python src/main.py``.

To run the application this project offers several options:

1. **Docker Compose**: The application can be run in a containerized environment using Docker Compose:

    ```shell
    make deploy
    ```

2. **Devcontainer**: The application can be run within its own development container, locally or hosted on GitHub Codespaces:

    ```shell
    make run
    ```
3. **Manually**: The application can be run via Python script entrypoint:

    ```shell
    python src/main.py
    ```

## Project Setup and Tooling

### Prerequisites

* [Docker](https://docs.docker.com): For containerized development and services
* [Poetry](https://python-poetry.org/): Dependency and package management
* [Make](https://makefiletutorial.com/): For automation (or use the commands manually)

### Environment setup

1. Clone the repository:

```shell
git clone https://github.com/fcolome14/{{cookiecutter.project_slug}}.git
cd {{ cookiecutter.project_slug }}
```

2. Environment Setup Options:

* Option 1: Use Devcontainer (Recommended):
  * Open the project in VS Code with the Dev [Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
  * Or use GitHub Codespaces to launch the containerized environment online.

* Option 2: Virtual Environment (Manual):
```shell
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
poetry install --all-extras
```

> NOTE: Python version required: {{ cookiecutter.python_version }}

```shell
python -m venv ./venv
```

#### Managing Dependencies with Poetry

To install all project dependencies:

```shell
poetry install --all-extras
```

To add or remove dependencies:

```shell
poetry add <package_name> [--group dev]
poetry remove <package_name>
```

To update the .lock file:

```shell
poetry lock [--no-update]
```

### Notebooks

Launch Jupyter Notebooks in your environment:

```shell
make jupyter
```

### Environment Variables & Secrets

A simple way to handle critical data is saving them as environment variables.

Create a .env file at the root to store secrets and configuration:

```shell
YOUR_USERNAME=your_username
YOUR_PASSWORD=your_password
ANY_OTHER_SECRET=other_secret
```
> .env is automatically excluded from Git via .gitignore.
> Load it in Python with the python-dotenv package.


### Running Tests

Basic (unit + integration):

```shell
make tests-basic
```

Full test suite (including E2E via Docker):

```shell
make tests
```

### Generate documentation

Build HTML docs locally using:

```shell
make docs
```
Output will be generated in the docs/build/ folder.

## Contributors

* {{cookiecutter.author}} ([{{cookiecutter.email}}](mailto:{{cookiecutter.email}}))

## License

This project is licensed under the {{ cookiecutter.license }} license.
