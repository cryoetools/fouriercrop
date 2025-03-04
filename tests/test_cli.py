"""Tests for `fouriercrop`.cli module."""

from typing import List

import pytest
from typer.testing import CliRunner

import fouriercrop
from fouriercrop import cli

runner = CliRunner()


@pytest.mark.parametrize(
    "options,expected",
    [
        ([], "fouriercrop.cli.main"),
        (["--help"], "Usage: "),
        (
            ["--version"],
            f"fouriercrop, version { fouriercrop.__version__ }\n",
        ),
    ],
)
def test_command_line_interface(options: List[str], expected: str) -> None:
    """Test the CLI."""
    result = runner.invoke(cli.app, options)
    assert result.exit_code == 0
    assert expected in result.stdout
