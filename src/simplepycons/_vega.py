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


class VegaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vega"

    @property
    def original_file_name(self) -> "str":
        return "vega.svg"

    @property
    def title(self) -> "str":
        return "Vega"

    @property
    def primary_color(self) -> "str":
        return "#2450B2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vega</title>
     <path d="M19.39 8.693H24l-3.123-6.68ZM6.68 1.987H0L7.098
 22.03h.008l2.86-10.73zm14.197-.016-7.098 20.042h-6.68L14.195 1.97" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/vega/logos/blob/af32bc29f0'''

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