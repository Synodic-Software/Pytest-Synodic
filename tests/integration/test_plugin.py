"""Verifies the plugin utilities work as expected"""

from typing import LiteralString

import pytest
from synodic_utilities.plugin import Plugin

from pytest_synodic.plugin import IntegrationTests


class MockPlugin(Plugin):
    """A mock plugin for testing"""


class TestPluginOverride(IntegrationTests[MockPlugin]):
    """Verifies the plugin utilities work as expected"""

    @pytest.fixture(name="plugin_type", scope="session")
    def fixture_plugin_type(self) -> type[MockPlugin]:
        """A required testing hook that allows type generation

        Returns:
            The overridden provider type
        """
        return MockPlugin

    @pytest.fixture(name="plugin_group_name", scope="session")
    def fixture_plugin_group_name(self) -> LiteralString:
        """A required testing hook that allows plugin group name generation

        Returns:
            The plugin group name
        """

        return "plugin"

    @pytest.mark.skip(reason="No entry points for mock class")
    def test_entry_point(self, plugin_type: type[MockPlugin], plugin_group_name: LiteralString) -> None:
        """Verify that the plugin was registered

        Args:
            plugin_type: The type to register
            plugin_group_name: The group name for the plugin type
        """
