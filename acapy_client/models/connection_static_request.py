from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionStaticRequest")


@attr.s(auto_attribs=True)
class ConnectionStaticRequest:
    """ """

    their_seed: Union[Unset, str] = UNSET
    their_endpoint: Union[Unset, str] = UNSET
    their_role: Union[Unset, str] = UNSET
    their_label: Union[Unset, str] = UNSET
    their_did: Union[Unset, str] = UNSET
    their_verkey: Union[Unset, str] = UNSET
    my_did: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    my_seed: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        their_seed = self.their_seed
        their_endpoint = self.their_endpoint
        their_role = self.their_role
        their_label = self.their_label
        their_did = self.their_did
        their_verkey = self.their_verkey
        my_did = self.my_did
        alias = self.alias
        my_seed = self.my_seed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if their_seed is not UNSET:
            field_dict["their_seed"] = their_seed
        if their_endpoint is not UNSET:
            field_dict["their_endpoint"] = their_endpoint
        if their_role is not UNSET:
            field_dict["their_role"] = their_role
        if their_label is not UNSET:
            field_dict["their_label"] = their_label
        if their_did is not UNSET:
            field_dict["their_did"] = their_did
        if their_verkey is not UNSET:
            field_dict["their_verkey"] = their_verkey
        if my_did is not UNSET:
            field_dict["my_did"] = my_did
        if alias is not UNSET:
            field_dict["alias"] = alias
        if my_seed is not UNSET:
            field_dict["my_seed"] = my_seed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        their_seed = d.pop("their_seed", UNSET)

        their_endpoint = d.pop("their_endpoint", UNSET)

        their_role = d.pop("their_role", UNSET)

        their_label = d.pop("their_label", UNSET)

        their_did = d.pop("their_did", UNSET)

        their_verkey = d.pop("their_verkey", UNSET)

        my_did = d.pop("my_did", UNSET)

        alias = d.pop("alias", UNSET)

        my_seed = d.pop("my_seed", UNSET)

        connection_static_request = cls(
            their_seed=their_seed,
            their_endpoint=their_endpoint,
            their_role=their_role,
            their_label=their_label,
            their_did=their_did,
            their_verkey=their_verkey,
            my_did=my_did,
            alias=alias,
            my_seed=my_seed,
        )

        connection_static_request.additional_properties = d
        return connection_static_request

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
