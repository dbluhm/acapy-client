from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.didx_request import DIDXRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    their_public_did: str,
    mediation_id: Union[Unset, str] = UNSET,
    my_endpoint: Union[Unset, str] = UNSET,
    my_label: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/didexchange/create-request".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "their_public_did": their_public_did,
        "mediation_id": mediation_id,
        "my_endpoint": my_endpoint,
        "my_label": my_label,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[DIDXRequest]:
    if response.status_code == 200:
        response_200 = DIDXRequest.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[DIDXRequest]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    their_public_did: str,
    mediation_id: Union[Unset, str] = UNSET,
    my_endpoint: Union[Unset, str] = UNSET,
    my_label: Union[Unset, str] = UNSET,
) -> Response[DIDXRequest]:
    kwargs = _get_kwargs(
        client=client,
        their_public_did=their_public_did,
        mediation_id=mediation_id,
        my_endpoint=my_endpoint,
        my_label=my_label,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    their_public_did: str,
    mediation_id: Union[Unset, str] = UNSET,
    my_endpoint: Union[Unset, str] = UNSET,
    my_label: Union[Unset, str] = UNSET,
) -> Optional[DIDXRequest]:
    """ """

    return sync_detailed(
        client=client,
        their_public_did=their_public_did,
        mediation_id=mediation_id,
        my_endpoint=my_endpoint,
        my_label=my_label,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    their_public_did: str,
    mediation_id: Union[Unset, str] = UNSET,
    my_endpoint: Union[Unset, str] = UNSET,
    my_label: Union[Unset, str] = UNSET,
) -> Response[DIDXRequest]:
    kwargs = _get_kwargs(
        client=client,
        their_public_did=their_public_did,
        mediation_id=mediation_id,
        my_endpoint=my_endpoint,
        my_label=my_label,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    their_public_did: str,
    mediation_id: Union[Unset, str] = UNSET,
    my_endpoint: Union[Unset, str] = UNSET,
    my_label: Union[Unset, str] = UNSET,
) -> Optional[DIDXRequest]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            their_public_did=their_public_did,
            mediation_id=mediation_id,
            my_endpoint=my_endpoint,
            my_label=my_label,
        )
    ).parsed
