"""Tests for the MCP server initialization stub."""

import pytest

from branchmark import server


def test_server_main_exists_and_is_callable():
    """The server module should expose a callable ``main`` function."""
    assert hasattr(server, "main"), "branchmark.server should define a main function"
    assert callable(server.main), "branchmark.server.main should be callable"


def test_server_main_raises_not_implemented():
    """Calling ``main`` should raise ``NotImplementedError`` until the server is wired."""
    with pytest.raises(NotImplementedError):
        server.main()


# End of file
