from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.attach_decorator import AttachDecorator
from ..models.invitation_receive_request_service import InvitationReceiveRequestService
from ..models.service import Service
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationReceiveRequest")


@attr.s(auto_attribs=True)
class InvitationReceiveRequest:
    """ """

    requestattach: List[AttachDecorator]
    type: Union[Unset, str] = UNSET
    service_dids: Union[Unset, List[str]] = UNSET
    service: Union[Unset, InvitationReceiveRequestService] = UNSET
    label: Union[Unset, str] = UNSET
    handshake_protocols: Union[Unset, List[str]] = UNSET
    id: Union[Unset, str] = UNSET
    service_blocks: Union[Unset, List[Service]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requestattach = []
        for requestattach_item_data in self.requestattach:
            requestattach_item = requestattach_item_data.to_dict()

            requestattach.append(requestattach_item)

        type = self.type
        service_dids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.service_dids, Unset):
            service_dids = self.service_dids

        service: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        label = self.label
        handshake_protocols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.handshake_protocols, Unset):
            handshake_protocols = self.handshake_protocols

        id = self.id
        service_blocks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.service_blocks, Unset):
            service_blocks = []
            for service_blocks_item_data in self.service_blocks:
                service_blocks_item = service_blocks_item_data.to_dict()

                service_blocks.append(service_blocks_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request~attach": requestattach,
            }
        )
        if type is not UNSET:
            field_dict["@type"] = type
        if service_dids is not UNSET:
            field_dict["service_dids"] = service_dids
        if service is not UNSET:
            field_dict["service"] = service
        if label is not UNSET:
            field_dict["label"] = label
        if handshake_protocols is not UNSET:
            field_dict["handshake_protocols"] = handshake_protocols
        if id is not UNSET:
            field_dict["@id"] = id
        if service_blocks is not UNSET:
            field_dict["service_blocks"] = service_blocks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        requestattach = []
        _requestattach = d.pop("request~attach")
        for requestattach_item_data in _requestattach:
            requestattach_item = AttachDecorator.from_dict(requestattach_item_data)

            requestattach.append(requestattach_item)

        type = d.pop("@type", UNSET)

        service_dids = cast(List[str], d.pop("service_dids", UNSET))

        _service = d.pop("service", UNSET)
        service: Union[Unset, InvitationReceiveRequestService]
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = InvitationReceiveRequestService.from_dict(_service)

        label = d.pop("label", UNSET)

        handshake_protocols = cast(List[str], d.pop("handshake_protocols", UNSET))

        id = d.pop("@id", UNSET)

        service_blocks = []
        _service_blocks = d.pop("service_blocks", UNSET)
        for service_blocks_item_data in _service_blocks or []:
            service_blocks_item = Service.from_dict(service_blocks_item_data)

            service_blocks.append(service_blocks_item)

        invitation_receive_request = cls(
            requestattach=requestattach,
            type=type,
            service_dids=service_dids,
            service=service,
            label=label,
            handshake_protocols=handshake_protocols,
            id=id,
            service_blocks=service_blocks,
        )

        invitation_receive_request.additional_properties = d
        return invitation_receive_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
