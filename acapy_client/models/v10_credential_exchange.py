from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v10_credential_exchange_credential import V10CredentialExchangeCredential
from ..models.v10_credential_exchange_credential_offer import V10CredentialExchangeCredentialOffer
from ..models.v10_credential_exchange_credential_offer_dict import V10CredentialExchangeCredentialOfferDict
from ..models.v10_credential_exchange_credential_proposal_dict import V10CredentialExchangeCredentialProposalDict
from ..models.v10_credential_exchange_credential_request import V10CredentialExchangeCredentialRequest
from ..models.v10_credential_exchange_credential_request_metadata import V10CredentialExchangeCredentialRequestMetadata
from ..models.v10_credential_exchange_initiator import V10CredentialExchangeInitiator
from ..models.v10_credential_exchange_raw_credential import V10CredentialExchangeRawCredential
from ..models.v10_credential_exchange_role import V10CredentialExchangeRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="V10CredentialExchange")


@attr.s(auto_attribs=True)
class V10CredentialExchange:
    """ """

    updated_at: Union[Unset, str] = UNSET
    credential_request_metadata: Union[Unset, V10CredentialExchangeCredentialRequestMetadata] = UNSET
    role: Union[Unset, V10CredentialExchangeRole] = UNSET
    error_msg: Union[Unset, str] = UNSET
    revoc_reg_id: Union[Unset, str] = UNSET
    credential: Union[Unset, V10CredentialExchangeCredential] = UNSET
    credential_definition_id: Union[Unset, str] = UNSET
    auto_issue: Union[Unset, bool] = UNSET
    initiator: Union[Unset, V10CredentialExchangeInitiator] = UNSET
    schema_id: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    auto_remove: Union[Unset, bool] = UNSET
    parent_thread_id: Union[Unset, str] = UNSET
    credential_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    revocation_id: Union[Unset, str] = UNSET
    credential_request: Union[Unset, V10CredentialExchangeCredentialRequest] = UNSET
    auto_offer: Union[Unset, bool] = UNSET
    credential_exchange_id: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    credential_offer_dict: Union[Unset, V10CredentialExchangeCredentialOfferDict] = UNSET
    credential_offer: Union[Unset, V10CredentialExchangeCredentialOffer] = UNSET
    credential_proposal_dict: Union[Unset, V10CredentialExchangeCredentialProposalDict] = UNSET
    raw_credential: Union[Unset, V10CredentialExchangeRawCredential] = UNSET
    created_at: Union[Unset, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        updated_at = self.updated_at
        credential_request_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_request_metadata, Unset):
            credential_request_metadata = self.credential_request_metadata.to_dict()

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        error_msg = self.error_msg
        revoc_reg_id = self.revoc_reg_id
        credential: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential.to_dict()

        credential_definition_id = self.credential_definition_id
        auto_issue = self.auto_issue
        initiator: Union[Unset, str] = UNSET
        if not isinstance(self.initiator, Unset):
            initiator = self.initiator.value

        schema_id = self.schema_id
        connection_id = self.connection_id
        auto_remove = self.auto_remove
        parent_thread_id = self.parent_thread_id
        credential_id = self.credential_id
        state = self.state
        revocation_id = self.revocation_id
        credential_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_request, Unset):
            credential_request = self.credential_request.to_dict()

        auto_offer = self.auto_offer
        credential_exchange_id = self.credential_exchange_id
        thread_id = self.thread_id
        credential_offer_dict: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_offer_dict, Unset):
            credential_offer_dict = self.credential_offer_dict.to_dict()

        credential_offer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_offer, Unset):
            credential_offer = self.credential_offer.to_dict()

        credential_proposal_dict: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_proposal_dict, Unset):
            credential_proposal_dict = self.credential_proposal_dict.to_dict()

        raw_credential: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.raw_credential, Unset):
            raw_credential = self.raw_credential.to_dict()

        created_at = self.created_at
        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if credential_request_metadata is not UNSET:
            field_dict["credential_request_metadata"] = credential_request_metadata
        if role is not UNSET:
            field_dict["role"] = role
        if error_msg is not UNSET:
            field_dict["error_msg"] = error_msg
        if revoc_reg_id is not UNSET:
            field_dict["revoc_reg_id"] = revoc_reg_id
        if credential is not UNSET:
            field_dict["credential"] = credential
        if credential_definition_id is not UNSET:
            field_dict["credential_definition_id"] = credential_definition_id
        if auto_issue is not UNSET:
            field_dict["auto_issue"] = auto_issue
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if schema_id is not UNSET:
            field_dict["schema_id"] = schema_id
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if auto_remove is not UNSET:
            field_dict["auto_remove"] = auto_remove
        if parent_thread_id is not UNSET:
            field_dict["parent_thread_id"] = parent_thread_id
        if credential_id is not UNSET:
            field_dict["credential_id"] = credential_id
        if state is not UNSET:
            field_dict["state"] = state
        if revocation_id is not UNSET:
            field_dict["revocation_id"] = revocation_id
        if credential_request is not UNSET:
            field_dict["credential_request"] = credential_request
        if auto_offer is not UNSET:
            field_dict["auto_offer"] = auto_offer
        if credential_exchange_id is not UNSET:
            field_dict["credential_exchange_id"] = credential_exchange_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if credential_offer_dict is not UNSET:
            field_dict["credential_offer_dict"] = credential_offer_dict
        if credential_offer is not UNSET:
            field_dict["credential_offer"] = credential_offer
        if credential_proposal_dict is not UNSET:
            field_dict["credential_proposal_dict"] = credential_proposal_dict
        if raw_credential is not UNSET:
            field_dict["raw_credential"] = raw_credential
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        updated_at = d.pop("updated_at", UNSET)

        _credential_request_metadata = d.pop("credential_request_metadata", UNSET)
        credential_request_metadata: Union[Unset, V10CredentialExchangeCredentialRequestMetadata]
        if isinstance(_credential_request_metadata, Unset):
            credential_request_metadata = UNSET
        else:
            credential_request_metadata = V10CredentialExchangeCredentialRequestMetadata.from_dict(
                _credential_request_metadata
            )

        _role = d.pop("role", UNSET)
        role: Union[Unset, V10CredentialExchangeRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = V10CredentialExchangeRole(_role)

        error_msg = d.pop("error_msg", UNSET)

        revoc_reg_id = d.pop("revoc_reg_id", UNSET)

        _credential = d.pop("credential", UNSET)
        credential: Union[Unset, V10CredentialExchangeCredential]
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = V10CredentialExchangeCredential.from_dict(_credential)

        credential_definition_id = d.pop("credential_definition_id", UNSET)

        auto_issue = d.pop("auto_issue", UNSET)

        _initiator = d.pop("initiator", UNSET)
        initiator: Union[Unset, V10CredentialExchangeInitiator]
        if isinstance(_initiator, Unset):
            initiator = UNSET
        else:
            initiator = V10CredentialExchangeInitiator(_initiator)

        schema_id = d.pop("schema_id", UNSET)

        connection_id = d.pop("connection_id", UNSET)

        auto_remove = d.pop("auto_remove", UNSET)

        parent_thread_id = d.pop("parent_thread_id", UNSET)

        credential_id = d.pop("credential_id", UNSET)

        state = d.pop("state", UNSET)

        revocation_id = d.pop("revocation_id", UNSET)

        _credential_request = d.pop("credential_request", UNSET)
        credential_request: Union[Unset, V10CredentialExchangeCredentialRequest]
        if isinstance(_credential_request, Unset):
            credential_request = UNSET
        else:
            credential_request = V10CredentialExchangeCredentialRequest.from_dict(_credential_request)

        auto_offer = d.pop("auto_offer", UNSET)

        credential_exchange_id = d.pop("credential_exchange_id", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        _credential_offer_dict = d.pop("credential_offer_dict", UNSET)
        credential_offer_dict: Union[Unset, V10CredentialExchangeCredentialOfferDict]
        if isinstance(_credential_offer_dict, Unset):
            credential_offer_dict = UNSET
        else:
            credential_offer_dict = V10CredentialExchangeCredentialOfferDict.from_dict(_credential_offer_dict)

        _credential_offer = d.pop("credential_offer", UNSET)
        credential_offer: Union[Unset, V10CredentialExchangeCredentialOffer]
        if isinstance(_credential_offer, Unset):
            credential_offer = UNSET
        else:
            credential_offer = V10CredentialExchangeCredentialOffer.from_dict(_credential_offer)

        _credential_proposal_dict = d.pop("credential_proposal_dict", UNSET)
        credential_proposal_dict: Union[Unset, V10CredentialExchangeCredentialProposalDict]
        if isinstance(_credential_proposal_dict, Unset):
            credential_proposal_dict = UNSET
        else:
            credential_proposal_dict = V10CredentialExchangeCredentialProposalDict.from_dict(_credential_proposal_dict)

        _raw_credential = d.pop("raw_credential", UNSET)
        raw_credential: Union[Unset, V10CredentialExchangeRawCredential]
        if isinstance(_raw_credential, Unset):
            raw_credential = UNSET
        else:
            raw_credential = V10CredentialExchangeRawCredential.from_dict(_raw_credential)

        created_at = d.pop("created_at", UNSET)

        trace = d.pop("trace", UNSET)

        v10_credential_exchange = cls(
            updated_at=updated_at,
            credential_request_metadata=credential_request_metadata,
            role=role,
            error_msg=error_msg,
            revoc_reg_id=revoc_reg_id,
            credential=credential,
            credential_definition_id=credential_definition_id,
            auto_issue=auto_issue,
            initiator=initiator,
            schema_id=schema_id,
            connection_id=connection_id,
            auto_remove=auto_remove,
            parent_thread_id=parent_thread_id,
            credential_id=credential_id,
            state=state,
            revocation_id=revocation_id,
            credential_request=credential_request,
            auto_offer=auto_offer,
            credential_exchange_id=credential_exchange_id,
            thread_id=thread_id,
            credential_offer_dict=credential_offer_dict,
            credential_offer=credential_offer,
            credential_proposal_dict=credential_proposal_dict,
            raw_credential=raw_credential,
            created_at=created_at,
            trace=trace,
        )

        v10_credential_exchange.additional_properties = d
        return v10_credential_exchange

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
