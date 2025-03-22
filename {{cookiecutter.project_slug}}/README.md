# {{ cookiecutter.project_name }}

Brief description of the application

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

## Project Setup and Tools

### Dependencies

* [Docker](https://docs.docker.com): Used to develop insider Docker development container and run several services in Docker Compose.

### Environment setup

First step is to clone the repository.

```shell
git clone https://github.com/fcolome14/{{cookiecutter.project_slug}}.git
```

After having cloned the repo, there are 2 ways to manage the development environment:

* Use a devcontainer (preferred):
  * Open the project in a development container with VSCode locally.
  * Open the project in a development container with VSCode hosted on GitHub Codespaces.
* Create a virtual environment and install Python packages:

> NOTE: The Python version used in this project is {{ cookiecutter.python_version }}

```shell
python -m venv ./venv
```

#### Poetry

To include a new package to the project it should be added to ``pyproject.toml`` under the correct group:

* Packages needed to run the applications should be under the ``tool.poetry.dependencies`` section.
* Packages used as development tools such as ``pytest``, ``ruff`` or ``black`` belong to the ``tool.poetry.group.dev.dependencies`` section.

To add a package you can use ``poetry add``. You can indicate the group to add the dependency to with the option ``--group=GROUP``.

To remove a package use ``poetry remove``.

##### poetry.lock

The ``poetry.lock`` file contains a snapshot of the resolved dependencies from ``pyproject.toml``.

To manually force the update of `poetry.lock` file, run ``poetry lock``. The ``--no-update`` flag can be used to avoid updating those dependencies which do not need to.

### Notebooks

You can start a local notebook or jupyter lab server with:

```shell
make jupyter
```

### Passwords

Some applications connect to any third-party service (for example a SQL server) requiring
a user name and a password.

This kind of information shall be never be hardcoded in the code or saved in any configuration
file that may be uploaded to the repository.

A simple way to handle critical data is saving them as environment variables.

Simply create a `.env` file at the root of the repository. Then and save user names and passwords
like:

```shell
YOUR_USERNAME=your_username
YOUR_PASSWORD=your_password
```

You can then read `.env` files for Python code with the `dotenv` package.

`.env` files are excluded from the Git repository in the `.gitignore` file.

### Testing

To verify correct installation, execute the {{cookiecutter.project_name}} tests by running the following command in your Python environment:

```shell
make tests-basic
```

If you want to run all tests, that will require using Docker Compose:


### Generate documentation

Run the following command to generate project documentation:

```shell
make docs
```

## Contributors

* {{cookiecutter.author}} ([{{cookiecutter.email}}](mailto:{{cookiecutter.email}}))

