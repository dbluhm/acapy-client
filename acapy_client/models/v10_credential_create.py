from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credential_preview import CredentialPreview
from ..types import UNSET, Unset

T = TypeVar("T", bound="V10CredentialCreate")


@attr.s(auto_attribs=True)
class V10CredentialCreate:
    """ """

    credential_proposal: CredentialPreview
    auto_remove: Union[Unset, bool] = UNSET
    schema_name: Union[Unset, str] = UNSET
    cred_def_id: Union[Unset, str] = UNSET
    issuer_did: Union[Unset, str] = UNSET
    schema_issuer_did: Union[Unset, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    schema_version: Union[Unset, str] = UNSET
    schema_id: Union[Unset, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credential_proposal = self.credential_proposal.to_dict()

        auto_remove = self.auto_remove
        schema_name = self.schema_name
        cred_def_id = self.cred_def_id
        issuer_did = self.issuer_did
        schema_issuer_did = self.schema_issuer_did
        comment = self.comment
        schema_version = self.schema_version
        schema_id = self.schema_id
        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credential_proposal": credential_proposal,
            }
        )
        if auto_remove is not UNSET:
            field_dict["auto_remove"] = auto_remove
        if schema_name is not UNSET:
            field_dict["schema_name"] = schema_name
        if cred_def_id is not UNSET:
            field_dict["cred_def_id"] = cred_def_id
        if issuer_did is not UNSET:
            field_dict["issuer_did"] = issuer_did
        if schema_issuer_did is not UNSET:
            field_dict["schema_issuer_did"] = schema_issuer_did
        if comment is not UNSET:
            field_dict["comment"] = comment
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version
        if schema_id is not UNSET:
            field_dict["schema_id"] = schema_id
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credential_proposal = CredentialPreview.from_dict(d.pop("credential_proposal"))

        auto_remove = d.pop("auto_remove", UNSET)

        schema_name = d.pop("schema_name", UNSET)

        cred_def_id = d.pop("cred_def_id", UNSET)

        issuer_did = d.pop("issuer_did", UNSET)

        schema_issuer_did = d.pop("schema_issuer_did", UNSET)

        comment = d.pop("comment", UNSET)

        schema_version = d.pop("schema_version", UNSET)

        schema_id = d.pop("schema_id", UNSET)

        trace = d.pop("trace", UNSET)

        v10_credential_create = cls(
            credential_proposal=credential_proposal,
            auto_remove=auto_remove,
            schema_name=schema_name,
            cred_def_id=cred_def_id,
            issuer_did=issuer_did,
            schema_issuer_did=schema_issuer_did,
            comment=comment,
            schema_version=schema_version,
            schema_id=schema_id,
            trace=trace,
        )

        v10_credential_create.additional_properties = d
        return v10_credential_create

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
