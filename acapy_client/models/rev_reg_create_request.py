from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RevRegCreateRequest")


@attr.s(auto_attribs=True)
class RevRegCreateRequest:
    """ """

    max_cred_num: Union[Unset, int] = UNSET
    credential_definition_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_cred_num = self.max_cred_num
        credential_definition_id = self.credential_definition_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_cred_num is not UNSET:
            field_dict["max_cred_num"] = max_cred_num
        if credential_definition_id is not UNSET:
            field_dict["credential_definition_id"] = credential_definition_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        max_cred_num = d.pop("max_cred_num", UNSET)

        credential_definition_id = d.pop("credential_definition_id", UNSET)

        rev_reg_create_request = cls(
            max_cred_num=max_cred_num,
            credential_definition_id=credential_definition_id,
        )

        rev_reg_create_request.additional_properties = d
        return rev_reg_create_request

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
