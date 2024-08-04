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


class BrandfolderIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "brandfolder"

    @property
    def original_file_name(self) -> "str":
        return "brandfolder.svg"

    @property
    def title(self) -> "str":
        return "Brandfolder"

    @property
    def primary_color(self) -> "str":
        return "#40D1F5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Brandfolder</title>
     <path
 d="M0,23.291h19.601v-2.978H2.98V3.689h16.626v10.911h-1.422l2.908,2.909L24,14.599
 h-1.417V0.709H0V23.291z
 M16.148,13.356c-0.191-0.406-0.432-0.739-0.72-0.997c-0.287-0.258-0.599-0.454-0.933-0.583
 c-0.337-0.132-0.641-0.217-0.916-0.254c0.251-0.034,0.496-0.134,0.735-0.296c0.241-0.161,0.455-0.364,0.647-0.609
 c0.192-0.247,0.345-0.535,0.458-0.863c0.115-0.33,0.171-0.686,0.171-1.069c0-0.648-0.126-1.186-0.377-1.617
 c-0.252-0.432-0.597-0.775-1.033-1.033c-0.436-0.258-0.948-0.44-1.536-0.547c-0.586-0.108-1.21-0.162-1.868-0.162
 c-0.754,0-1.382,0.018-1.887,0.054C8.387,5.417,7.944,5.463,7.56,5.525v12.933c0.684,0.083,1.293,0.141,1.834,0.171
 c0.539,0.03,1.082,0.044,1.634,0.044c0.718,0,1.404-0.054,2.057-0.162c0.652-0.107,1.227-0.304,1.723-0.592
 c0.499-0.288,0.893-0.68,1.187-1.177c0.294-0.498,0.441-1.135,0.441-1.914C16.436,14.253,16.34,13.763,16.148,13.356z
 M10.165,7.321c0.91-0.111,1.873-0.054,2.301,0.304c0.38,0.317,0.607,0.599,0.607,1.42c0,0.751-0.357,1.195-0.608,1.356
 c-0.251,0.161-0.59,0.368-1.403,0.368s-0.897,0-0.897,0V7.321z
 M13.194,16.001c-0.449,0.39-1.114,0.552-1.816,0.552
 c-0.79,0-1.213-0.072-1.213-0.072v-3.737h1.132c0.711,0,1.438,0.126,1.832,0.464c0.509,0.437,0.611,0.895,0.611,1.505
 C13.741,15.322,13.528,15.711,13.194,16.001z" />
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
