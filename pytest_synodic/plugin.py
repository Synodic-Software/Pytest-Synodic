"""Implementation of plugin utilities for pytest extensions"""

from abc import ABCMeta
from importlib.metadata import entry_points
from typing import LiteralString

import pytest
from synodic_utilities.plugin import Plugin


class BaseTests[T: Plugin](metaclass=ABCMeta):
    """Shared testing information for all plugin test classes."""

    @pytest.fixture(name="plugin_type", scope="session")
    def fixture_plugin_type(self) -> type[T]:
        """A required testing hook that allows type generation. The user should override this fixture and return their custom plugin type"""

        raise NotImplementedError("Override this fixture in the plugin module")

    @pytest.fixture(name="plugin_group_name", scope="session")
    def fixture_plugin_group_name(self) -> LiteralString:
        """A required testing hook that provides identifying information. The user should override this fixture and return the base group name for their plugin type"""

        raise NotImplementedError("Override this fixture in the base test class")


class IntegrationTests[T: Plugin](BaseTests[T], metaclass=ABCMeta):
    """Integration testing information for all plugin test classes"""

    def test_entry_point(self, plugin_type: type[T], plugin_group_name: LiteralString) -> None:
        """Verify that the plugin was registered

        Args:
            plugin_type: The type to register
            plugin_group_name: The group name for the plugin type
        """
        types = []
        for entry in list(entry_points(group=f"{plugin_group_name}.{plugin_type.group}")):
            types.append(entry.load())

        assert plugin_type in types

    def test_name(self, plugin_type: type[Plugin]) -> None:
        """Verifies the the class name allows name extraction

        Args:
            plugin_type: The type to register
        """

        assert plugin_type.group != ""
        assert plugin_type.name != ""


class UnitTests[T: Plugin](BaseTests[T], metaclass=ABCMeta):
    """Unit testing information for all plugin test classes"""
