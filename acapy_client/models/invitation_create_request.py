from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attachment_def import AttachmentDef
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationCreateRequest")


@attr.s(auto_attribs=True)
class InvitationCreateRequest:
    """ """

    use_public_did: Union[Unset, bool] = UNSET
    attachments: Union[Unset, List[AttachmentDef]] = UNSET
    include_handshake: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        use_public_did = self.use_public_did
        attachments: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()

                attachments.append(attachments_item)

        include_handshake = self.include_handshake

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if use_public_did is not UNSET:
            field_dict["use_public_did"] = use_public_did
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if include_handshake is not UNSET:
            field_dict["include_handshake"] = include_handshake

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        use_public_did = d.pop("use_public_did", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = AttachmentDef.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        include_handshake = d.pop("include_handshake", UNSET)

        invitation_create_request = cls(
            use_public_did=use_public_did,
            attachments=attachments,
            include_handshake=include_handshake,
        )

        invitation_create_request.additional_properties = d
        return invitation_create_request

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
