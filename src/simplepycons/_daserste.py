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


class DasErsteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "daserste"

    @property
    def original_file_name(self) -> "str":
        return "daserste.svg"

    @property
    def title(self) -> "str":
        return "Das Erste"

    @property
    def primary_color(self) -> "str":
        return "#001A4B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Das Erste</title>
     <path d="M11.646.005C5.158.2-.001 5.57 0 12.127.135 18.724 5.468
 24 12 24s11.865-5.276 12-11.873C24.001 5.291 18.41-.195
 11.645.005zm5.138 4.93V16.96L8.78 19.92v-9.08l-3.9
 1.386V9.263l11.903-4.328z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Das_E'''

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
