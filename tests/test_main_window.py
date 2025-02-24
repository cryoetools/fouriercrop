"""Tests for `fouriercrop-gui` module."""

import tkinter as tk
from typing import Generator

import pytest

from fouriercrop.gui import launch_gui
from fouriercrop.gui.main_window import App


def test_launch_gui_import() -> None:
    """Tests that launch_gui is correctly imported from __init__.py."""
    assert launch_gui is not None, "launch_gui should be imported from __init__.py"


@pytest.fixture
def app_instance() -> Generator:
    """Fixture to create and yield an instance of the App class."""
    root = tk.Tk()
    root.withdraw()
    app = App(root)  # type: ignore [arg-type]
    yield app
    app.destroy()
