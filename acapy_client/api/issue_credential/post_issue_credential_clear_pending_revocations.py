from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v10_clear_pending_revocations_request import V10ClearPendingRevocationsRequest
from ...models.v10_publish_revocations import V10PublishRevocations
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: V10ClearPendingRevocationsRequest,
) -> Dict[str, Any]:
    url = "{}/issue-credential/clear-pending-revocations".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[V10PublishRevocations]:
    if response.status_code == 200:
        response_200 = V10PublishRevocations.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V10PublishRevocations]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: V10ClearPendingRevocationsRequest,
) -> Response[V10PublishRevocations]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: V10ClearPendingRevocationsRequest,
) -> Optional[V10PublishRevocations]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: V10ClearPendingRevocationsRequest,
) -> Response[V10PublishRevocations]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: V10ClearPendingRevocationsRequest,
) -> Optional[V10PublishRevocations]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
