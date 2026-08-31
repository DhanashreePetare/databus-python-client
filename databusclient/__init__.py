"""Top-level package for the databus Python client.

This module exposes a small set of convenience functions and the CLI
entrypoint so the package can be used as a library or via
``python -m databusclient``.
"""

from importlib.metadata import PackageNotFoundError, version
from pathlib import Path
import tomllib

from databusclient import cli
from databusclient.api.deploy import create_dataset, create_distribution, deploy


# Source checkouts do not always have current package metadata installed, so
# prefer pyproject.toml locally and fall back to installed metadata for wheels
def _get_version() -> str:
    pyproject = Path(__file__).resolve().parent.parent / "pyproject.toml"
    if pyproject.exists():
        with pyproject.open("rb") as f:
            return tomllib.load(f)["tool"]["poetry"]["version"]

    try:
        return version("databusclient")
    except PackageNotFoundError:
        return "0.0.0"


__version__ = _get_version()

__all__ = ["create_dataset", "deploy", "create_distribution"]


def run():
    """Start the Click CLI application.

    This function is used by the ``__main__`` module and the package
    entrypoint to invoke the command line interface.
    """

    cli.app()
