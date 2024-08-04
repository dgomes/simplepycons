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


class HelpdeskIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "helpdesk"

    @property
    def original_file_name(self) -> "str":
        return "helpdesk.svg"

    @property
    def title(self) -> "str":
        return "HelpDesk"

    @property
    def primary_color(self) -> "str":
        return "#2FC774"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>HelpDesk</title>
     <path d="M12 10.71l6.12-5.31H12c-2.16
 0-4.32.06-6.36.21-.84.06-1.5.69-1.56 1.53-.12 1.26-.18 2.85-.18
 4.41v.87c0 1.59.06 3.15.18 4.41.09.81.75 1.47 1.56 1.5a90 90 0
 0012.72 0c.81-.03 1.5-.69 1.56-1.5.09-1.2.15-2.67.18-4.17L24
 9.3V12.66c0 1.59-.06 3.18-.18 4.47a5.57 5.57 0 01-5.19
 5.1c-2.13.18-4.38.27-6.63.27s-4.5-.09-6.63-.24a5.57 5.57 0
 01-5.19-5.1C.06 15.81 0 14.13 0 12.45v-.87C0 9.9.06 8.22.18 6.84a5.57
 5.57 0 015.19-5.1C7.5 1.59 9.75 1.5 12 1.5h12v3.9L12
 15.81l-5.61-4.86L9.33 8.4z" />
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
