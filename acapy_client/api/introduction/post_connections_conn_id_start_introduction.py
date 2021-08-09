from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    conn_id: str,
    target_connection_id: str,
    message: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/connections/{conn_id}/start-introduction".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "target_connection_id": target_connection_id,
        "message": message,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    target_connection_id: str,
    message: Union[Unset, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        target_connection_id=target_connection_id,
        message=message,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    conn_id: str,
    target_connection_id: str,
    message: Union[Unset, str] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        target_connection_id=target_connection_id,
        message=message,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
