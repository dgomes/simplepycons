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


class FathomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fathom"

    @property
    def original_file_name(self) -> "str":
        return "fathom.svg"

    @property
    def title(self) -> "str":
        return "Fathom"

    @property
    def primary_color(self) -> "str":
        return "#9187FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fathom</title>
     <path d="M14.185 0c-1.702.008-3.693.467-6.068 1.331C.115
 4.244-1.581 7.881 1.33 15.883c2.912 8.002 6.55 9.698 14.552 6.786
 8.002-2.913 9.699-6.55 6.786-14.552C20.62 2.491 18.214-.018 14.185
 0zm2.77 6.57h1.253a.25.25 0 01.199.098.25.25 0 01.043.217L15.672
 17.22a.25.25 0 01-.241.186h-1.254a.25.25 0
 01-.242-.315l.169-.628.123-.457 2.486-9.252a.25.25 0
 01.241-.185zm-9.184.808h.504a.25.25 0 01.25.25v.844a.25.25 0
 01-.25.25h-.428a1.7 1.7 0 00-.258.012.221.221 0 00-.12.048.197.197 0
 00-.049.078.886.886 0 00-.043.315v.641h.898a.25.25 0
 01.25.25v.844a.25.25 0 01-.25.25h-.898v5.094a.25.25 0
 01-.25.25h-.985a.25.25 0 01-.25-.25v-7.23a1.723 1.723 0 01.169-.78
 1.395 1.395 0 01.453-.523c.37-.257.826-.341 1.257-.343zm3.85
 2.344c.767 0 1.419.218 1.883.622.465.404.725.994.723
 1.668v1.683l-.755 2.809h-.48a.25.25 0 01-.25-.25v-.187a1.84 1.84 0
 01-.223.167c-.335.213-.79.352-1.39.352a2.936 2.936 0 01-1.337-.29
 1.898 1.898 0 01-.883-.907 2.193 2.193 0 01-.187-.916 1.907 1.907 0
 01.245-.99 1.724 1.724 0 01.646-.618c.52-.293 1.16-.396
 1.788-.48H11.4c.342-.046.616-.075.827-.103a1.968 1.968 0
 00.431-.088.147.147 0 00.065-.04l.01-.021a.319.319 0
 00.009-.086v-.035a.809.809 0
 00-.274-.638c-.178-.155-.458-.26-.847-.261-.385
 0-.686.106-.89.262a.821.821 0 00-.338.588.25.25 0
 01-.249.228H9.101a.25.25 0 01-.25-.261 2.139 2.139 0
 01.825-1.593c.491-.391 1.165-.615 1.945-.615zm1.121
 3.783c-.09.024-.187.047-.296.068-.303.06-.67.113-1.025.163a2.855
 2.855 0 00-.692.171c-.196.082-.333.186-.407.308a.569.569 0
 00-.08.307v.007a.604.604 0 00.062.275.554.554 0
 00.176.198c.16.115.428.194.79.194.56-.002.915-.164
 1.14-.39.223-.228.33-.542.332-.896v-.404z" />
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
