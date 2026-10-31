"""Tests for GitHubClient initialization.

Ensures that the client sets up authentication headers correctly and uses the
default base URL when none is provided, trimming any trailing slash.
"""

from branchmark.github import GitHubClient


def test_default_base_url_and_headers() -> None:
    token = "my-secret-token"
    client = GitHubClient(token)
    # Default base URL should be the public API without trailing slash
    assert client.base_url == "https://api.github.com"
    # Authorization header should include the token
    assert client.headers["Authorization"] == f"token {token}"
    # Other expected headers are present
    assert client.headers["Accept"] == "application/vnd.github.v3+json"
    assert client.headers["User-Agent"] == "branchmark-client"


def test_custom_base_url_stripped() -> None:
    token = "another-token"
    # Provide a base URL with a trailing slash to ensure it is stripped
    custom_url = "https://custom.github.com/"
    client = GitHubClient(token, base_url=custom_url)
    assert client.base_url == "https://custom.github.com"
    # Header should still contain the token
    assert client.headers["Authorization"] == f"token {token}"
