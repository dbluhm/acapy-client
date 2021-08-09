from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    conn_id: str,
) -> Dict[str, Any]:
    url = "{}/connections/{conn_id}/remove".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    conn_id: str,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    conn_id: str,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
