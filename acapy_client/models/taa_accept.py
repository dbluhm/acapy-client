from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TAAAccept")


@attr.s(auto_attribs=True)
class TAAAccept:
    """ """

    version: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    mechanism: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        text = self.text
        mechanism = self.mechanism

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if version is not UNSET:
            field_dict["version"] = version
        if text is not UNSET:
            field_dict["text"] = text
        if mechanism is not UNSET:
            field_dict["mechanism"] = mechanism

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version", UNSET)

        text = d.pop("text", UNSET)

        mechanism = d.pop("mechanism", UNSET)

        taa_accept = cls(
            version=version,
            text=text,
            mechanism=mechanism,
        )

        taa_accept.additional_properties = d
        return taa_accept

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
