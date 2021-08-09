from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.did_posture import DIDPosture
from ..types import UNSET, Unset

T = TypeVar("T", bound="DID")


@attr.s(auto_attribs=True)
class DID:
    """ """

    did: Union[Unset, str] = UNSET
    posture: Union[Unset, DIDPosture] = UNSET
    verkey: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        did = self.did
        posture: Union[Unset, str] = UNSET
        if not isinstance(self.posture, Unset):
            posture = self.posture.value

        verkey = self.verkey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if did is not UNSET:
            field_dict["did"] = did
        if posture is not UNSET:
            field_dict["posture"] = posture
        if verkey is not UNSET:
            field_dict["verkey"] = verkey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        did = d.pop("did", UNSET)

        _posture = d.pop("posture", UNSET)
        posture: Union[Unset, DIDPosture]
        if isinstance(_posture, Unset):
            posture = UNSET
        else:
            posture = DIDPosture(_posture)

        verkey = d.pop("verkey", UNSET)

        did = cls(
            did=did,
            posture=posture,
            verkey=verkey,
        )

        did.additional_properties = d
        return did

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
