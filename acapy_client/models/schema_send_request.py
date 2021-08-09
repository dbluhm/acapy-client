from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="SchemaSendRequest")


@attr.s(auto_attribs=True)
class SchemaSendRequest:
    """ """

    schema_version: str
    schema_name: str
    attributes: List[str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schema_version = self.schema_version
        schema_name = self.schema_name
        attributes = self.attributes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema_version": schema_version,
                "schema_name": schema_name,
                "attributes": attributes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schema_version = d.pop("schema_version")

        schema_name = d.pop("schema_name")

        attributes = cast(List[str], d.pop("attributes"))

        schema_send_request = cls(
            schema_version=schema_version,
            schema_name=schema_name,
            attributes=attributes,
        )

        schema_send_request.additional_properties = d
        return schema_send_request

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
