from typing import Any, Callable

from typing_extensions import Self

from ...binding import BindableProperty, bind, bind_from, bind_to
from ...element import Element


class DisableableElement(Element):
    enabled = BindableProperty(on_change=lambda sender, value: sender.on_enabled_change(value))

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.enabled = True

    def enable(self) -> None:
        """Enable the element."""
        self.enabled = True

    def disable(self) -> None:
        """Disable the element."""
        self.enabled = False

    def bind_enabled_to(self,
                        target_object: Any,
                        target_name: str = 'enabled',
                        forward: Callable[..., Any] = lambda x: x,
                        ) -> Self:
        """Bind the enabled state of this element to the target object's target_name property.

        The binding works one way only, from this element to the target.

        :param target_object: The object to bind to.
        :param target_name: The name of the property to bind to.
        :param forward: A function to apply to the value before applying it to the target.
        """
        bind_to(self, 'enabled', target_object, target_name, forward)
        return self

    def bind_enabled_from(self,
                          target_object: Any,
                          target_name: str = 'enabled',
                          backward: Callable[..., Any] = lambda x: x,
                          ) -> Self:
        """Bind the enabled state of this element from the target object's target_name property.

        The binding works one way only, from the target to this element.

        :param target_object: The object to bind from.
        :param target_name: The name of the property to bind from.
        :param backward: A function to apply to the value before applying it to this element.
        """
        bind_from(self, 'enabled', target_object, target_name, backward)
        return self

    def bind_enabled(self,
                     target_object: Any,
                     target_name: str = 'enabled', *,
                     forward: Callable[..., Any] = lambda x: x,
                     backward: Callable[..., Any] = lambda x: x,
                     ) -> Self:
        """Bind the enabled state of this element to the target object's target_name property.

        The binding works both ways, from this element to the target and from the target to this element.

        :param target_object: The object to bind to.
        :param target_name: The name of the property to bind to.
        :param forward: A function to apply to the value before applying it to the target.
        :param backward: A function to apply to the value before applying it to this element.
        """
        bind(self, 'enabled', target_object, target_name, forward=forward, backward=backward)
        return self

    def set_enabled(self, value: bool) -> None:
        """Set the enabled state of the element."""
        self.enabled = value

    def on_enabled_change(self, enabled: bool) -> None:
        """Called when the element is enabled or disabled.

        :param enabled: The new state.
        """
        self._props['disable'] = not enabled
        self.update()
