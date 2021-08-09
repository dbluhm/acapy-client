from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.get_ledger_did_endpoint_endpoint_type import GetLedgerDidEndpointEndpointType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    did: str,
    endpoint_type: Union[Unset, GetLedgerDidEndpointEndpointType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/ledger/did-endpoint".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_endpoint_type: Union[Unset, str] = UNSET
    if not isinstance(endpoint_type, Unset):
        json_endpoint_type = endpoint_type.value

    params: Dict[str, Any] = {
        "did": did,
        "endpoint_type": json_endpoint_type,
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
    did: str,
    endpoint_type: Union[Unset, GetLedgerDidEndpointEndpointType] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        did=did,
        endpoint_type=endpoint_type,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    did: str,
    endpoint_type: Union[Unset, GetLedgerDidEndpointEndpointType] = UNSET,
) -> Response[Any]:
    kwargs = _get_kwargs(
        client=client,
        did=did,
        endpoint_type=endpoint_type,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)
