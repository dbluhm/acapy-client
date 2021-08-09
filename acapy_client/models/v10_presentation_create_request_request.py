from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_proof_request import IndyProofRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="V10PresentationCreateRequestRequest")


@attr.s(auto_attribs=True)
class V10PresentationCreateRequestRequest:
    """ """

    proof_request: IndyProofRequest
    trace: Union[Unset, bool] = UNSET
    comment: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proof_request = self.proof_request.to_dict()

        trace = self.trace
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proof_request": proof_request,
            }
        )
        if trace is not UNSET:
            field_dict["trace"] = trace
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        proof_request = IndyProofRequest.from_dict(d.pop("proof_request"))

        trace = d.pop("trace", UNSET)

        comment = d.pop("comment", UNSET)

        v10_presentation_create_request_request = cls(
            proof_request=proof_request,
            trace=trace,
            comment=comment,
        )

        v10_presentation_create_request_request.additional_properties = d
        return v10_presentation_create_request_request

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
