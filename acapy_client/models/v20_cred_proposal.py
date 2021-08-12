from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attach_decorator import AttachDecorator
from ..models.v20_cred_format import V20CredFormat
from ..models.v20_cred_preview import V20CredPreview
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredProposal")


@attr.s(auto_attribs=True)
class V20CredProposal:
    """ """

    filtersattach: List[AttachDecorator]
    formats: List[V20CredFormat]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    credential_preview: Union[Unset, V20CredPreview] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filtersattach = []
        for filtersattach_item_data in self.filtersattach:
            filtersattach_item = filtersattach_item_data.to_dict()

            filtersattach.append(filtersattach_item)

        formats = []
        for formats_item_data in self.formats:
            formats_item = formats_item_data.to_dict()

            formats.append(formats_item)

        id = self.id
        type = self.type
        comment = self.comment
        credential_preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_preview, Unset):
            credential_preview = self.credential_preview.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filters~attach": filtersattach,
                "formats": formats,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if comment is not UNSET:
            field_dict["comment"] = comment
        if credential_preview is not UNSET:
            field_dict["credential_preview"] = credential_preview

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filtersattach = []
        _filtersattach = d.pop("filters~attach")
        for filtersattach_item_data in _filtersattach:
            filtersattach_item = AttachDecorator.from_dict(filtersattach_item_data)

            filtersattach.append(filtersattach_item)

        formats = []
        _formats = d.pop("formats")
        for formats_item_data in _formats:
            formats_item = V20CredFormat.from_dict(formats_item_data)

            formats.append(formats_item)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        comment = d.pop("comment", UNSET)

        _credential_preview = d.pop("credential_preview", UNSET)
        credential_preview: Union[Unset, V20CredPreview]
        if isinstance(_credential_preview, Unset):
            credential_preview = UNSET
        else:
            credential_preview = V20CredPreview.from_dict(_credential_preview)

        v20_cred_proposal = cls(
            filtersattach=filtersattach,
            formats=formats,
            id=id,
            type=type,
            comment=comment,
            credential_preview=credential_preview,
        )

        v20_cred_proposal.additional_properties = d
        return v20_cred_proposal

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
