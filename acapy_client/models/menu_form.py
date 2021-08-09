from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.menu_form_param import MenuFormParam
from ..types import UNSET, Unset

T = TypeVar("T", bound="MenuForm")


@attr.s(auto_attribs=True)
class MenuForm:
    """ """

    title: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    params: Union[Unset, List[MenuFormParam]] = UNSET
    submit_label: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        description = self.description
        params: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.params, Unset):
            params = []
            for params_item_data in self.params:
                params_item = params_item_data.to_dict()

                params.append(params_item)

        submit_label = self.submit_label

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if params is not UNSET:
            field_dict["params"] = params
        if submit_label is not UNSET:
            field_dict["submit-label"] = submit_label

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        params = []
        _params = d.pop("params", UNSET)
        for params_item_data in _params or []:
            params_item = MenuFormParam.from_dict(params_item_data)

            params.append(params_item)

        submit_label = d.pop("submit-label", UNSET)

        menu_form = cls(
            title=title,
            description=description,
            params=params,
            submit_label=submit_label,
        )

        menu_form.additional_properties = d
        return menu_form

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
