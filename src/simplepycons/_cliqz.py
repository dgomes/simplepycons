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


class CliqzIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cliqz"

    @property
    def original_file_name(self) -> "str":
        return "cliqz.svg"

    @property
    def title(self) -> "str":
        return "Cliqz"

    @property
    def primary_color(self) -> "str":
        return "#00AEF0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Cliqz</title>
     <path d="M19.387 18.146l4.19-1.402L12 12.027l4.716 11.578
 1.403-4.19 3.917 3.917 1.268-1.268zm-7.387 1c.035 0
 .07-.004.105-.004l1.908 4.686c-.654.11-1.326.172-2.013.172-6.617
 0-12-5.383-12-12S5.383 0 12 0s12 5.383 12 12c0 .695-.063 1.376-.177
 2.04l-4.683-1.908c0-.044.006-.087.006-.133A7.153 7.153 0 0 0 12
 4.854a7.155 7.154 0 0 0-7.147 7.145A7.155 7.154 0 0 0 12 19.146z" />
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
