from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawEncCredAttr")


@attr.s(auto_attribs=True)
class RawEncCredAttr:
    """ """

    raw: Union[Unset, str] = UNSET
    encoded: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        raw = self.raw
        encoded = self.encoded

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if raw is not UNSET:
            field_dict["raw"] = raw
        if encoded is not UNSET:
            field_dict["encoded"] = encoded

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        raw = d.pop("raw", UNSET)

        encoded = d.pop("encoded", UNSET)

        raw_enc_cred_attr = cls(
            raw=raw,
            encoded=encoded,
        )

        raw_enc_cred_attr.additional_properties = d
        return raw_enc_cred_attr

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
