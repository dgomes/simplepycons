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


class VectorLogoZoneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vectorlogozone"

    @property
    def original_file_name(self) -> "str":
        return "vectorlogozone.svg"

    @property
    def title(self) -> "str":
        return "Vector Logo Zone"

    @property
    def primary_color(self) -> "str":
        return "#184D66"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vector Logo Zone</title>
     <path d="M19.458 0l-5.311 2.024 1.989.534-4.847
 16.085-4.867-16.25H1.48L8.974 24h4.645l7.043-20.226 1.858.499Z" />
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