from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.v20_pres_problem_report_request import V20PresProblemReportRequest
from ...models.v20_present_proof_module_response import V20PresentProofModuleResponse
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    pres_ex_id: str,
    json_body: V20PresProblemReportRequest,
) -> Dict[str, Any]:
    url = "{}/present-proof-2.0/records/{pres_ex_id}/problem-report".format(client.base_url, pres_ex_id=pres_ex_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[V20PresentProofModuleResponse]:
    if response.status_code == 200:
        response_200 = V20PresentProofModuleResponse.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[V20PresentProofModuleResponse]:
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
    json_body: V20PresProblemReportRequest,
) -> Response[V20PresentProofModuleResponse]:
    kwargs = _get_kwargs(
        client=client,
        pres_ex_id=pres_ex_id,
        json_body=json_body,
    )

    response = httpx.post(
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    pres_ex_id: str,
    json_body: V20PresProblemReportRequest,
) -> Optional[V20PresentProofModuleResponse]:
    """ """

    return sync_detailed(
        client=client,
        pres_ex_id=pres_ex_id,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pres_ex_id: str,
    json_body: V20PresProblemReportRequest,
) -> Response[V20PresentProofModuleResponse]:
    kwargs = _get_kwargs(
        client=client,
        pres_ex_id=pres_ex_id,
        json_body=json_body,
    )

    async with httpx.AsyncClient() as _client:
        response = await _client.post(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    pres_ex_id: str,
    json_body: V20PresProblemReportRequest,
) -> Optional[V20PresentProofModuleResponse]:
    """ """

    return (
        await asyncio_detailed(
            client=client,
            pres_ex_id=pres_ex_id,
            json_body=json_body,
        )
    ).parsed
