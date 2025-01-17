from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.doc import Doc

T = TypeVar("T", bound="SignRequest")


@attr.s(auto_attribs=True)
class SignRequest:
    """ """

    doc: Doc
    verkey: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc = self.doc.to_dict()

        verkey = self.verkey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "doc": doc,
                "verkey": verkey,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doc = Doc.from_dict(d.pop("doc"))

        verkey = d.pop("verkey")

        sign_request = cls(
            doc=doc,
            verkey=verkey,
        )

        sign_request.additional_properties = d
        return sign_request

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
