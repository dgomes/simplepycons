#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class ScilabIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "scilab"

    @property
    def original_file_name(self) -> "str":
        return "scilab.svg"

    @property
    def title(self) -> "str":
        return "Scilab"

    @property
    def primary_color(self) -> "str":
        return "#CD1925"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Scilab</title>
     <path d="M3.813 1.803c-1.103 0-1.99.888-1.99 1.99v16.414c0
 1.102.887 1.99 1.99 1.99h16.375c1.102 0 1.99-.888
 1.99-1.99V3.793c0-1.102-.888-1.99-1.99-1.99zm8.82 1.234a1.802 1.825 0
 0 1 1.803 1.824 1.802 1.825 0 0 1-1.803 1.827A1.802 1.825 0 0 1 10.83
 4.86a1.802 1.825 0 0 1 1.803-1.824Zm2.986 3.496a1.802 1.825 0 0 1
 1.803 1.826 1.802 1.825 0 0 1-1.803 1.825 1.802 1.825 0 0
 1-1.803-1.825 1.802 1.825 0 0 1 1.803-1.826Zm-7.346.26a1.802 1.825 0
 0 1 1.803 1.824 1.802 1.825 0 0 1-1.803 1.826 1.802 1.825 0 0
 1-1.802-1.826 1.802 1.825 0 0 1 1.802-1.824Zm3.98 2.633a1.802 1.825 0
 0 1 1.804 1.826 1.802 1.825 0 0 1-1.803 1.824 1.802 1.825 0 0
 1-1.803-1.824 1.802 1.825 0 0 1 1.803-1.826zm7.044.053a1.802 1.825 0
 0 1 1.803 1.826 1.802 1.825 0 0 1-1.803 1.824 1.802 1.825 0 0
 1-1.8-1.824 1.802 1.825 0 0 1 1.8-1.826zm-3.402 2.535a1.802 1.825 0 0
 1 1.802 1.826 1.802 1.825 0 0 1-1.802 1.824 1.802 1.825 0 0
 1-1.803-1.824 1.802 1.825 0 0 1 1.803-1.826zm-11.614.953a1.802 1.825
 0 0 1 1.803 1.826 1.802 1.825 0 0 1-1.803 1.824 1.802 1.825 0 0
 1-1.802-1.824 1.802 1.825 0 0 1 1.802-1.826Zm15.518.93a1.802 1.825 0
 0 1 1.803 1.824 1.802 1.825 0 0 1-1.803 1.826 1.802 1.825 0 0
 1-1.803-1.826 1.802 1.825 0 0 1 1.803-1.825zM7.81 15.665a1.802 1.825
 0 0 1 1.802 1.824 1.802 1.825 0 0 1-1.802 1.826 1.802 1.825 0 0
 1-1.803-1.826 1.802 1.825 0 0 1 1.803-1.824ZM3.564 0A3.556 3.556 0 0
 0 0 3.564v16.872A3.556 3.556 0 0 0 3.564 24h16.872A3.556 3.556 0 0 0
 24 20.436V3.564A3.556 3.556 0 0 0 20.436 0Zm-.002 1.021h16.875a2.536
 2.536 0 0 1 2.542 2.542v16.875a2.536 2.536 0 0 1-2.542
 2.54H3.563a2.536 2.536 0 0 1-2.54-2.54V3.563a2.536 2.536 0 0 1
 2.54-2.542z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://gitlab.com/scilab/scilab/-/blob/599df
2b32347029f4806a7c5fa2fe9d5f1293f0d/scilab/modules/gui/images/icons/sc'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
