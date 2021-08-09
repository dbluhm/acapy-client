from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.connection_record import ConnectionRecord

T = TypeVar("T", bound="ConnectionStaticResult")


@attr.s(auto_attribs=True)
class ConnectionStaticResult:
    """ """

    mv_verkey: str
    my_endpoint: str
    their_did: str
    their_verkey: str
    record: ConnectionRecord
    my_did: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mv_verkey = self.mv_verkey
        my_endpoint = self.my_endpoint
        their_did = self.their_did
        their_verkey = self.their_verkey
        record = self.record.to_dict()

        my_did = self.my_did

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mv_verkey": mv_verkey,
                "my_endpoint": my_endpoint,
                "their_did": their_did,
                "their_verkey": their_verkey,
                "record": record,
                "my_did": my_did,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mv_verkey = d.pop("mv_verkey")

        my_endpoint = d.pop("my_endpoint")

        their_did = d.pop("their_did")

        their_verkey = d.pop("their_verkey")

        record = ConnectionRecord.from_dict(d.pop("record"))

        my_did = d.pop("my_did")

        connection_static_result = cls(
            mv_verkey=mv_verkey,
            my_endpoint=my_endpoint,
            their_did=their_did,
            their_verkey=their_verkey,
            record=record,
            my_did=my_did,
        )

        connection_static_result.additional_properties = d
        return connection_static_result

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
