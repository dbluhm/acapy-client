from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.conn_record import ConnRecord
from ...models.invitation_message import InvitationMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: InvitationMessage,
    alias: Union[Unset, str] = UNSET,
    auto_accept: Union[Unset, bool] = UNSET,
    mediation_id: Union[Unset, str] = UNSET,
    use_existing_connection: Union[Unset, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/out-of-band/receive-invitation".format(client.base_url)

    headers: Dict[str, Any] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {
        "alias": alias,
        "auto_accept": auto_accept,
        "mediation_id": mediation_id,
        "use_existing_connection": use_existing_connection,
    }
    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[ConnRecord]:
    if response.status_code == 200:
        response_200 = ConnRecord.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[ConnRecord]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: InvitationMessage,
    alias: Union[Unset, str] = UNSET,
    auto_accept: Union[Unset, bool] = UNSET,
    mediation_id: Union[Unset, str] = UNSET,
    use_existing_connection: Union[Unset, bool] = UNSET,
) -> Response[ConnRecord]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        alias=alias,
        auto_accept=auto_accept,
        mediation_id=mediation_id,
        use_existing_connection=use_existing_connection,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: InvitationMessage,
    alias: Union[Unset, str] = UNSET,
    auto_accept: Union[Unset, bool] = UNSET,
    mediation_id: Union[Unset, str] = UNSET,
    use_existing_connection: Union[Unset, bool] = UNSET,
) -> Optional[ConnRecord]:
    """ """

    return sync_detailed(
        client=client,
        json_body=json_body,
        alias=alias,
        auto_accept=auto_accept,
        mediation_id=mediation_id,
        use_existing_connection=use_existing_connection,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: InvitationMessage,
    alias: Union[Unset, str] = UNSET,
    auto_accept: Union[Unset, bool] = UNSET,
    mediation_id: Union[Unset, str] = UNSET,
    use_existing_connection: Union[Unset, bool] = UNSET,
) -> Response[ConnRecord]:
    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        alias=alias,
        auto_accept=auto_accept,
        mediation_id=mediation_id,
        use_existing_connection=use_existing_connection,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: InvitationMessage,
    alias: Union[Unset, str] = UNSET,
    auto_accept: Union[Unset, bool] = UNSET,
    mediation_id: Union[Unset, str] = UNSET,
    use_existing_connection: Union[Unset, bool] = UNSET,
) -> Optional[ConnRecord]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            alias=alias,
            auto_accept=auto_accept,
            mediation_id=mediation_id,
            use_existing_connection=use_existing_connection,
        )
    ).parsed