"""{{ cookiecutter.project_name }} entry point."""

import click

from . import __version__, scripts


def _main() -> None:
    """Run main function for entrypoint."""

    @click.group(chain=True)
    @click.version_option(__version__)
    def entry_point() -> None:
        """Package entry point."""

    for command in (scripts.wait_api, scripts.serve):
        entry_point.add_command(command)

    entry_point()


if __name__ == "__main__":
    _main()