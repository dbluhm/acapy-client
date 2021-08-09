from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.connection_record_accept import ConnectionRecordAccept
from ..models.connection_record_initiator import ConnectionRecordInitiator
from ..models.connection_record_invitation_mode import ConnectionRecordInvitationMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionRecord")


@attr.s(auto_attribs=True)
class ConnectionRecord:
    """ """

    connection_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    invitation_key: Union[Unset, str] = UNSET
    error_msg: Union[Unset, str] = UNSET
    accept: Union[Unset, ConnectionRecordAccept] = UNSET
    inbound_connection_id: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    their_role: Union[Unset, str] = UNSET
    their_label: Union[Unset, str] = UNSET
    their_did: Union[Unset, str] = UNSET
    initiator: Union[Unset, ConnectionRecordInitiator] = UNSET
    routing_state: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    my_did: Union[Unset, str] = UNSET
    alias: Union[Unset, str] = UNSET
    invitation_mode: Union[Unset, ConnectionRecordInvitationMode] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        updated_at = self.updated_at
        invitation_key = self.invitation_key
        error_msg = self.error_msg
        accept: Union[Unset, str] = UNSET
        if not isinstance(self.accept, Unset):
            accept = self.accept.value

        inbound_connection_id = self.inbound_connection_id
        request_id = self.request_id
        their_role = self.their_role
        their_label = self.their_label
        their_did = self.their_did
        initiator: Union[Unset, str] = UNSET
        if not isinstance(self.initiator, Unset):
            initiator = self.initiator.value

        routing_state = self.routing_state
        state = self.state
        created_at = self.created_at
        my_did = self.my_did
        alias = self.alias
        invitation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.invitation_mode, Unset):
            invitation_mode = self.invitation_mode.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if invitation_key is not UNSET:
            field_dict["invitation_key"] = invitation_key
        if error_msg is not UNSET:
            field_dict["error_msg"] = error_msg
        if accept is not UNSET:
            field_dict["accept"] = accept
        if inbound_connection_id is not UNSET:
            field_dict["inbound_connection_id"] = inbound_connection_id
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if their_role is not UNSET:
            field_dict["their_role"] = their_role
        if their_label is not UNSET:
            field_dict["their_label"] = their_label
        if their_did is not UNSET:
            field_dict["their_did"] = their_did
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if routing_state is not UNSET:
            field_dict["routing_state"] = routing_state
        if state is not UNSET:
            field_dict["state"] = state
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if my_did is not UNSET:
            field_dict["my_did"] = my_did
        if alias is not UNSET:
            field_dict["alias"] = alias
        if invitation_mode is not UNSET:
            field_dict["invitation_mode"] = invitation_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connection_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        invitation_key = d.pop("invitation_key", UNSET)

        error_msg = d.pop("error_msg", UNSET)

        _accept = d.pop("accept", UNSET)
        accept: Union[Unset, ConnectionRecordAccept]
        if isinstance(_accept, Unset):
            accept = UNSET
        else:
            accept = ConnectionRecordAccept(_accept)

        inbound_connection_id = d.pop("inbound_connection_id", UNSET)

        request_id = d.pop("request_id", UNSET)

        their_role = d.pop("their_role", UNSET)

        their_label = d.pop("their_label", UNSET)

        their_did = d.pop("their_did", UNSET)

        _initiator = d.pop("initiator", UNSET)
        initiator: Union[Unset, ConnectionRecordInitiator]
        if isinstance(_initiator, Unset):
            initiator = UNSET
        else:
            initiator = ConnectionRecordInitiator(_initiator)

        routing_state = d.pop("routing_state", UNSET)

        state = d.pop("state", UNSET)

        created_at = d.pop("created_at", UNSET)

        my_did = d.pop("my_did", UNSET)

        alias = d.pop("alias", UNSET)

        _invitation_mode = d.pop("invitation_mode", UNSET)
        invitation_mode: Union[Unset, ConnectionRecordInvitationMode]
        if isinstance(_invitation_mode, Unset):
            invitation_mode = UNSET
        else:
            invitation_mode = ConnectionRecordInvitationMode(_invitation_mode)

        connection_record = cls(
            connection_id=connection_id,
            updated_at=updated_at,
            invitation_key=invitation_key,
            error_msg=error_msg,
            accept=accept,
            inbound_connection_id=inbound_connection_id,
            request_id=request_id,
            their_role=their_role,
            their_label=their_label,
            their_did=their_did,
            initiator=initiator,
            routing_state=routing_state,
            state=state,
            created_at=created_at,
            my_did=my_did,
            alias=alias,
            invitation_mode=invitation_mode,
        )

        connection_record.additional_properties = d
        return connection_record

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
