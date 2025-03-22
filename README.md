# cookiecutter-api

cookiecutter-api is a Cookiecutter template for quickly setting up a new project following best development practices.

## 📦 Features

- Automatically generates a structured project API layout.
- Customizable settings via `cookiecutter.json`.
- Pre-configured for easy deployment and version control.

## 🛠️ Installation

First, install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/):

```sh
pip install cookiecutter
```

## 🚀 Usage

To create a new project based on this template:

```sh
cookiecutter gh:fcolome14/cookiecutter-api
```

You will be prompted to enter:

- `project_name`
- `project_slug`
- `package_name`
- `description`
- `author`
- `email`
- `license`

## 📝 Customization

Modify `cookiecutter.json` to change default values according to your needs:

```json
{
  "project_name": "Cookiecutter API Template",
  "project_slug": "{{ cookiecutter.project_name.lower().replace(' ', '_') }}",
  "package_name": "{{ cookiecutter.project_slug }}",
  "version": "0.1.0",
  "description": "Your description",
  "author": "Lastname, Name",
  "email": "your_email@gmail.com",
  "license": "MIT",
  "python_version": "3.10.7",
  "cli_command": "{{ cookiecutter.project_slug.replace('_', '-') }}",
  "use_jupyter": "y",
  "use_dvc": "n",
  "use_docker": "y"
}

```

This is a sample output of each project variable:


| Variable          | Value                                               |
|-------------------|-----------------------------------------------------|
| `project_name`    | Data Science Project Template                       |
| `project_slug`    | data_science_project_template                       |
| `package_name`    | data_science_project_template                       |
| `version`         | 0.1.0                                               |
| `description`     | A reusable data science project template            |
| `author`          | Colomé Sanz, Ferran                                 |
| `email`           | ferrancolomsanz@gmail.com                           |
| `license`         | MIT                                                 |
| `python_version`  | 3.10.7                                              |
| `cli_command`     | data-science-project-template                       |
| `use_jupyter`     | Yes                                                 |
| `use_dvc`         | No                                                  |
| `use_docker`      | Yes                                                 |


## 📂 Project Structure

After generation, your project will have the following structure:

```
Cookiecutter API Template/
│
├── .devcontainer/                       # Configuration for VS Code Dev Containers (Docker-based)
│   ├── devcontainer.json                # VS Code settings for running inside a container
│   ├── docker-compose.yml               # Docker Compose services for development environment
│   ├── Dockerfile                       # Dockerfile for the main development container
│
├── .github/
│   ├── workflows/                       # GitHub Actions CI/CD workflows
│   └── dependabot.yml                   # Automates dependency updates
│
├── .vscode/
│   ├── extensions.json                  # Recommended extensions for VS Code
│   ├── settings.json                    # Project-specific VS Code settings
│
├── cookiecutter_api_template/           # Main application package (use {{ cookiecutter.package_name }} in Cookiecutter)
│   ├── api/                             # FastAPI route definitions and API logic
│   ├── core/                            # Core business logic and shared functionality
│   ├── database/                        # Database models, sessions, and migrations
│   ├── locales/                         # Translations and internationalization files (i18n)
│   ├── schemas/                         # Pydantic models (input/output validation schemas)
│   ├── templates/                       # Jinja2 templates (e.g., for HTML responses or email)
│   ├── utils/                           # Utility/helper functions
│
├── deployment/                          # Production deployment configuration
│   ├── docker-compose.yml               # Docker Compose for production deployment
│   ├── Dockerfile                       # Production Dockerfile
│
├── docs/                                # Project documentation
│   └── Makefile                         # Build Sphinx docs locally using `make html`
│
├── logs/                                # Runtime logs (should be gitignored or rotated)
│
├── notebooks/                           # Jupyter notebooks for experiments, prototyping, or EDA
│
├── tests/                               # All test code
│   ├── __init__.py
│   ├── compose/                         # Docker Compose tests or integration with external services
│   ├── e2e/                             # End-to-end tests (simulate real user behavior)
│   ├── integration/                     # Tests between integrated components (e.g., API ↔ DB)
│   ├── unit/                            # Unit tests (test individual functions/classes)
│   ├── conftest.py                      # Pytest fixtures and test configuration
│
├── data/                                # Local data storage (typically ignored in version control)
│   ├── raw/                             # Original, unmodified datasets
│   ├── processed/                       # Finalized, cleaned datasets for modeling or use
│   ├── interim/                         # Intermediate datasets (e.g., partially cleaned)
│   ├── external/                        # Data obtained from third-party APIs or services
│
├── README.md                            # Project overview and usage instructions
├── .gitignore                           # Ignore files/folders in Git version control
├── Makefile                             # Common development commands (e.g., test, lint, run)
├── .coveragerc                          # Coverage.py config for measuring test coverage
├── .dockerignore                        # Files to exclude from Docker image build context
├── .editorconfig                        # Code formatting consistency across editors
├── LICENSE                              # Software license (e.g., MIT)
├── babel.cfg                            # Babel translation config for i18n/l10n (used with Flask/FastAPI + Jinja)

```

## 🔄 Updating the Template

If you want to update the template, modify the files inside `cookiecutter-your_project_slug` and push changes to your repository.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Author: Colomé Sanz, Ferran