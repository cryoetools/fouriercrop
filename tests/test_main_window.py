"""Tests for `fouriercrop-gui` module."""

from src.fouriercrop.gui import launch_gui


def test_launch_gui_import() -> None:
    """Tests that launch_gui is correctly imported from __init__.py."""
    assert launch_gui is not None, "launch_gui should be imported from __init__.py"
