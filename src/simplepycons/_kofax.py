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


class KofaxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kofax"

    @property
    def original_file_name(self) -> "str":
        return "kofax.svg"

    @property
    def title(self) -> "str":
        return "Kofax"

    @property
    def primary_color(self) -> "str":
        return "#00558C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kofax</title>
     <path d="M1.38 12.94l.576-.5 1.273 1.698h1.835l-2.001-2.593
 1.85-1.683h-1.82L1.38 11.545V9.862H0v4.276h1.38z M7.353 9.726c-1.455
 0-2.683.5-2.683 2.274s1.228 2.274 2.683 2.274 2.684-.5
 2.684-2.274-1.228-2.274-2.684-2.274zm0 3.593c-.728
 0-1.228-.41-1.228-1.319 0-.894.5-1.319 1.228-1.319.743 0 1.228.425
 1.228 1.32 0 .894-.5 1.318-1.228 1.318zM11.795
 14.138v-1.653h2.365v-.925h-2.365v-.742h2.547v-.956h-3.926v4.276zM22.21
 11.91l1.593-2.063h-1.638L21.407 11l-.758-1.153h-1.637l1.592
 2.062-1.607 2.001-1.668-4.048h-1.683l-1.759
 4.276h1.471l.243-.698h1.804l.242.698h2.896l.88-1.289.879
 1.289H24zm-6.276.651l.576-1.622h.015l.577 1.622z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
