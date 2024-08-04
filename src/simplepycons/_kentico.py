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


class KenticoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kentico"

    @property
    def original_file_name(self) -> "str":
        return "kentico.svg"

    @property
    def title(self) -> "str":
        return "Kentico"

    @property
    def primary_color(self) -> "str":
        return "#F05A22"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kentico</title>
     <path d="M0 0v24h24V0zm11.65 3.417c.698 0 1.566.216 1.566
 1.279v2.72c0 1.5-2.433 1.533-2.433.018V3.63a.146.146 0 0 1
 .118-.142c.15-.028.432-.072.75-.071zm5.508 1.76a.146.146 0 0 1
 .079.026c.408.277 1.875 1.397.782 2.49L16.091 9.62c-1.06
 1.06-2.803-.64-1.733-1.707l2.695-2.695a.146.146 0 0 1
 .105-.041zm-10.27.4c.263.01.538.123.811.396l1.928 1.93c1.061
 1.059-.64 2.803-1.707 1.73L5.226 6.94a.142.142 0 0
 1-.018-.182c.209-.307.891-1.208 1.68-1.18zm5.104 4.65a1.773 1.773 0 0
 1 .008 0A1.773 1.773 0 1 1 10.227 12a1.773 1.773 0 0 1
 1.765-1.773zm-7.291.55h2.728c1.499 0 1.532 2.433.017
 2.433h-3.81a.144.144 0 0 1-.142-.117c-.092-.48-.337-2.315
 1.207-2.315zm11.859 0h3.802a.142.142 0 0 1 .142.117c.093.48.338
 2.316-1.206 2.316h-2.72c-1.5 0-1.533-2.433-.018-2.433zm-1.238
 3.24c.259.002.523.102.756.337l2.695 2.692a.146.146 0 0 1
 .017.184c-.278.41-1.398
 1.876-2.49.784l-1.929-1.93c-.829-.827.028-2.072.951-2.066zm-6.657.013c.93-.011
 1.811 1.209.975 2.044l-2.694 2.692a.144.144 0 0
 1-.184.018c-.408-.278-1.876-1.398-.783-2.49l1.928-1.93a1.08 1.08 0 0
 1 .758-.334zm3.334 1.403c.608-.007 1.217.364 1.217
 1.122v3.802a.144.144 0 0
 1-.118.14c-.48.093-2.316.338-2.316-1.206v-2.72c0-.749.609-1.132
 1.217-1.138z" />
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
