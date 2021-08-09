from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credential_signature import CredentialSignature
from ..models.credential_signature_correctness_proof import CredentialSignatureCorrectnessProof
from ..models.credential_values import CredentialValues
from ..models.rev_reg import RevReg
from ..models.witness import Witness
from ..types import UNSET, Unset

T = TypeVar("T", bound="Credential")


@attr.s(auto_attribs=True)
class Credential:
    """ """

    rev_reg_id: Union[Unset, str] = UNSET
    signature_correctness_proof: Union[Unset, CredentialSignatureCorrectnessProof] = UNSET
    cred_def_id: Union[Unset, str] = UNSET
    rev_reg: Union[Unset, RevReg] = UNSET
    witness: Union[Unset, Witness] = UNSET
    signature: Union[Unset, CredentialSignature] = UNSET
    schema_id: Union[Unset, str] = UNSET
    values: Union[Unset, CredentialValues] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        rev_reg_id = self.rev_reg_id
        signature_correctness_proof: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signature_correctness_proof, Unset):
            signature_correctness_proof = self.signature_correctness_proof.to_dict()

        cred_def_id = self.cred_def_id
        rev_reg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rev_reg, Unset):
            rev_reg = self.rev_reg.to_dict()

        witness: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.witness, Unset):
            witness = self.witness.to_dict()

        signature: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signature, Unset):
            signature = self.signature.to_dict()

        schema_id = self.schema_id
        values: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if rev_reg_id is not UNSET:
            field_dict["rev_reg_id"] = rev_reg_id
        if signature_correctness_proof is not UNSET:
            field_dict["signature_correctness_proof"] = signature_correctness_proof
        if cred_def_id is not UNSET:
            field_dict["cred_def_id"] = cred_def_id
        if rev_reg is not UNSET:
            field_dict["rev_reg"] = rev_reg
        if witness is not UNSET:
            field_dict["witness"] = witness
        if signature is not UNSET:
            field_dict["signature"] = signature
        if schema_id is not UNSET:
            field_dict["schema_id"] = schema_id
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rev_reg_id = d.pop("rev_reg_id", UNSET)

        _signature_correctness_proof = d.pop("signature_correctness_proof", UNSET)
        signature_correctness_proof: Union[Unset, CredentialSignatureCorrectnessProof]
        if isinstance(_signature_correctness_proof, Unset):
            signature_correctness_proof = UNSET
        else:
            signature_correctness_proof = CredentialSignatureCorrectnessProof.from_dict(_signature_correctness_proof)

        cred_def_id = d.pop("cred_def_id", UNSET)

        _rev_reg = d.pop("rev_reg", UNSET)
        rev_reg: Union[Unset, RevReg]
        if isinstance(_rev_reg, Unset):
            rev_reg = UNSET
        else:
            rev_reg = RevReg.from_dict(_rev_reg)

        _witness = d.pop("witness", UNSET)
        witness: Union[Unset, Witness]
        if isinstance(_witness, Unset):
            witness = UNSET
        else:
            witness = Witness.from_dict(_witness)

        _signature = d.pop("signature", UNSET)
        signature: Union[Unset, CredentialSignature]
        if isinstance(_signature, Unset):
            signature = UNSET
        else:
            signature = CredentialSignature.from_dict(_signature)

        schema_id = d.pop("schema_id", UNSET)

        _values = d.pop("values", UNSET)
        values: Union[Unset, CredentialValues]
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = CredentialValues.from_dict(_values)

        credential = cls(
            rev_reg_id=rev_reg_id,
            signature_correctness_proof=signature_correctness_proof,
            cred_def_id=cred_def_id,
            rev_reg=rev_reg,
            witness=witness,
            signature=signature,
            schema_id=schema_id,
            values=values,
        )

        credential.additional_properties = d
        return credential

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
