from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import Client
from ...models.indy_cred_precis import IndyCredPrecis
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    pres_ex_id: str,
    count: Union[Unset, str] = UNSET,
    extra_query: Union[Unset, str] = UNSET,
    referent: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/present-proof-2.0/records/{pres_ex_id}/credentials".format(client.base_url, pres_ex_id=pres_ex_id)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "count": count,
        "extra_query": extra_query,
        "referent": referent,
        "start": start,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[IndyCredPrecis]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IndyCredPrecis.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[IndyCredPrecis]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    pres_ex_id: str,
    count: Union[Unset, str] = UNSET,
    extra_query: Union[Unset, str] = UNSET,
    referent: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
) -> Response[List[IndyCredPrecis]]:
    kwargs = _get_kwargs(
        client=client,
        pres_ex_id=pres_ex_id,
        count=count,
        extra_query=extra_query,
        referent=referent,
        start=start,
    )

    response = httpx.get(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    pres_ex_id: str,
    count: Union[Unset, str] = UNSET,
    extra_query: Union[Unset, str] = UNSET,
    referent: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
) -> Optional[List[IndyCredPrecis]]:
    """ """

    return sync_detailed(
        client=client,
        pres_ex_id=pres_ex_id,
        count=count,
        extra_query=extra_query,
        referent=referent,
        start=start,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pres_ex_id: str,
    count: Union[Unset, str] = UNSET,
    extra_query: Union[Unset, str] = UNSET,
    referent: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
) -> Response[List[IndyCredPrecis]]:
    kwargs = _get_kwargs(
        client=client,
        pres_ex_id=pres_ex_id,
        count=count,
        extra_query=extra_query,
        referent=referent,
        start=start,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.get(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    pres_ex_id: str,
    count: Union[Unset, str] = UNSET,
    extra_query: Union[Unset, str] = UNSET,
    referent: Union[Unset, str] = UNSET,
    start: Union[Unset, str] = UNSET,
) -> Optional[List[IndyCredPrecis]]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            pres_ex_id=pres_ex_id,
            count=count,
            extra_query=extra_query,
            referent=referent,
            start=start,
        )
    ).parsed
