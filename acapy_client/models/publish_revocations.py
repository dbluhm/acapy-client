from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.publish_revocations_rrid_2_crid import PublishRevocationsRrid2Crid

T = TypeVar("T", bound="PublishRevocations")


@attr.s(auto_attribs=True)
class PublishRevocations:
    """ """

    rrid2crid: PublishRevocationsRrid2Crid
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rrid2crid = self.rrid2crid.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rrid2crid": rrid2crid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rrid2crid = PublishRevocationsRrid2Crid.from_dict(d.pop("rrid2crid"))

        publish_revocations = cls(
            rrid2crid=rrid2crid,
        )

        publish_revocations.additional_properties = d
        return publish_revocations

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
