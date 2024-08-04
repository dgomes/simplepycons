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


class AdrollIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adroll"

    @property
    def original_file_name(self) -> "str":
        return "adroll.svg"

    @property
    def title(self) -> "str":
        return "Adroll"

    @property
    def primary_color(self) -> "str":
        return "#0DBDFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Adroll</title>
     <path d="M24 12c0-6.01-4.727-10.886-10.886-10.886a10.863 10.863 0
 0 0-9.508 5.578L8.914 12c0-2.323 1.958-4.2 4.2-4.2 2.377 0 4.2 1.877
 4.2 4.2s-1.836 4.2-4.2 4.2H4.065A4.07 4.07 0 0 0 0
 20.266v2.62h13.114C19.232 22.886 24 18.01 24 12" />
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
