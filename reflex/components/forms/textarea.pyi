"""Stub file for textarea.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Dict, Optional, Union, overload
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class TextArea(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, value: Optional[Union[Var[str], str]] = None, default_value: Optional[Union[Var[str], str]] = None, placeholder: Optional[Union[Var[str], str]] = None, error_border_color: Optional[Union[Var[str], str]] = None, focus_border_color: Optional[Union[Var[str], str]] = None, is_disabled: Optional[Union[Var[bool], bool]] = None, is_invalid: Optional[Union[Var[bool], bool]] = None, is_read_only: Optional[Union[Var[bool], bool]] = None, is_required: Optional[Union[Var[bool], bool]] = None, variant: Optional[Union[Var[str], str]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_change: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_key_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_key_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "TextArea":  # type: ignore
        """Create an Input component.

        Args:
            *children: The children of the component.
            value: State var to bind the input.
            default_value: The default value of the textarea.
            placeholder: The placeholder text.
            error_border_color: The border color when the input is invalid.
            focus_border_color: The border color when the input is focused.
            is_disabled: If true, the form control will be disabled.
            is_invalid: If true, the form control will be invalid.
            is_read_only: If true, the form control will be read-only.
            is_required: If true, the form control will be required.
            variant: "outline" | "filled" | "flushed" | "unstyled"
            **props: The properties of the component.

        Returns:
            The component.
        """
        ...
