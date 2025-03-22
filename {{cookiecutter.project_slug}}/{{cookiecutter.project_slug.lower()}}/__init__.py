"""Top level package for {{ cookiecutter.project_name }}."""

import os
from importlib import metadata
from pathlib import Path

__version__ = metadata.version("{{ cookiecutter.package_name }}")

# Dynamic working directory (can be overridden via env)
WORKDIR = Path(os.getenv("WORKDIR", Path.cwd()))

# Base path of the package
BASEPATH = Path(__file__).parent