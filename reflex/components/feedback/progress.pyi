"""Stub file for progress.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Optional, Union, overload
from reflex.components.libs.chakra import ChakraComponent
from reflex.components.component import Component
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventHandler, EventChain, EventSpec

class Progress(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, has_stripe: Optional[Union[Var[bool], bool]] = None, is_animated: Optional[Union[Var[bool], bool]] = None, is_indeterminate: Optional[Union[Var[bool], bool]] = None, max_: Optional[Union[Var[int], int]] = None, min_: Optional[Union[Var[int], int]] = None, value: Optional[Union[Var[Union[int, float]], Union[int, float]]] = None, color_scheme: Optional[Union[Var[str], str]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Progress":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            has_stripe: If true, the progress bar will show stripe
            is_animated: If true, and hasStripe is true, the stripes will be animated
            is_indeterminate: If true, the progress will be indeterminate and the value prop will be ignored
            max_: The maximum value of the progress
            min_: The minimum value of the progress
            value: The value of the progress indicator. If undefined the progress bar will be in indeterminate state
            color_scheme: The color scheme of the progress bar.
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
