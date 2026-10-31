"""GitHub API client.

Provides a minimal client for interacting with the GitHub REST API.
The client is intentionally lightweight and uses only the standard library.
"""

from __future__ import annotations

import json
import urllib.request
from urllib.parse import urlencode

__all__ = ["GitHubClient"]


class GitHubClient:
    """Simple GitHub REST API client.

    Parameters
    ----------
    token:
        Personal access token used for authentication.
    base_url:
        Base URL for the GitHub API. Defaults to the public API.
    """

    def __init__(self, token: str, base_url: str = "https://api.github.com") -> None:
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "branchmark-client",
        }

    def _request(self, method: str, path: str, *, data: dict | None = None) -> dict:
        url = f"{self.base_url}{path}"
        req = urllib.request.Request(url, headers=self.headers, method=method)
        if data is not None:
            req.data = json.dumps(data).encode("utf-8")
            req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req) as resp:
            return json.load(resp)

    def get(self, path: str, params: dict | None = None) -> dict:
        if params:
            path = f"{path}?{urlencode(params)}"
        return self._request("GET", path)

    def post(self, path: str, data: dict | None = None) -> dict:
        return self._request("POST", path, data=data)

    def put(self, path: str, data: dict | None = None) -> dict:
        return self._request("PUT", path, data=data)

    def delete(self, path: str) -> dict:
        return self._request("DELETE", path)

# End of file
