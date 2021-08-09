from typing import Any, Dict

import httpx

from ...client import Client
from ...models.send_message import SendMessage
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    conn_id: str,
    json_body: SendMessage,
) -> Dict[str, Any]:
    url = "{}/connections/{conn_id}/send-message".format(client.base_url, conn_id=conn_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
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
    json_body: SendMessage,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    conn_id: str,
    json_body: SendMessage,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        conn_id=conn_id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)
