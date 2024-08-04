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


class IconfinderIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "iconfinder"

    @property
    def original_file_name(self) -> "str":
        return "iconfinder.svg"

    @property
    def title(self) -> "str":
        return "Iconfinder"

    @property
    def primary_color(self) -> "str":
        return "#1A1B1F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Iconfinder</title>
     <path d="M12 0C4.492 2.746-.885 11.312.502 19.963.502 19.963
 4.989 24 12 24c7.01 0 11.496-4.037 11.496-4.037C24.882 11.312 19.508
 2.746 12 0zm0 1.846s2.032.726 3.945
 2.488c.073.067.13.163.129.277-.001.168-.128.287-.301.287a.496.496 0
 01-.137-.027 6.537 6.537 0 00-2.316-.4 6.625 6.625 0 00-3.914
 1.273l-.002.002a7.978 7.978 0 016.808.768C20.48 9.11 22.597 14.179
 21.902 19c0 0-1.646 1.396-4.129 2.172a.369.369 0
 01-.303-.026c-.144-.084-.185-.255-.1-.404a.492.492 0 01.094-.103
 6.562 6.562 0 001.504-1.809 6.632 6.632 0
 00.856-4.027l-.002-.002a7.949 7.949 0 01-3.838 5.383c-4.42 2.552-9.99
 1.882-13.885-1.184 0 0-.388-2.124.182-4.662a.373.373 0
 01.176-.25c.145-.084.31-.033.396.117a.448.448 0
 01.045.13c.126.762.405 1.5.814 2.208a6.637 6.637 0 003.059 2.756 7.96
 7.96 0 01-1.672-2.033 7.928 7.928 0 01-1.066-4.205C4.128 8.047 7.464
 3.659 12 1.846zm0 7.623c-2.726 0-5.117.93-6.483
 2.332-.064.32-.1.65-.1.984 0 3.146 2.947 5.695 6.583 5.695 3.635 0
 6.584-2.549 6.584-5.695 0-.334-.038-.664-.102-.984C17.116 10.4 14.724
 9.469 12 9.469zm0 .693a3.12 3.12 0 010 6.238 3.118 3.118 0
 01-2.872-4.336 1.3 1.3 0 101.657-1.656A3.108 3.108 0 0112 10.162z" />
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
