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


class TuiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tui"

    @property
    def original_file_name(self) -> "str":
        return "tui.svg"

    @property
    def title(self) -> "str":
        return "TUI"

    @property
    def primary_color(self) -> "str":
        return "#D40E14"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TUI</title>
     <path d="M24 4.5167a2.117 2.117 0 01-2.117 2.117 2.117 2.117 0
 01-2.117-2.117 2.117 2.117 0 012.117-2.117A2.117 2.117 0 0124
 4.5168zM1.1397 7.7475h5.7055c.5642 0 .9806.1772
 1.1465.9716.185.8836.1129 1.4986-.8858 1.5686l-1.7909.132c1.318
 8.3303 9.0277 11.0453 13.2221 2.073.6952-1.485.922-1.7548
 1.6826-1.5663 1.0314.2561 1.1724.7899.677 2.2828-3.6234
 11.0566-15.8186 12.166-18.211-2.6044l-1.4546.105C.0463 10.7942 0
 9.7956 0 9.2404c0-1.0992.4074-1.493 1.1397-1.493z" />
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
