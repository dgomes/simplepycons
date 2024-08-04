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


class DropboxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dropbox"

    @property
    def original_file_name(self) -> "str":
        return "dropbox.svg"

    @property
    def title(self) -> "str":
        return "Dropbox"

    @property
    def primary_color(self) -> "str":
        return "#0061FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dropbox</title>
     <path d="M6 1.807L0 5.629l6 3.822 6.001-3.822L6 1.807zM18
 1.807l-6 3.822 6 3.822 6-3.822-6-3.822zM0 13.274l6 3.822
 6.001-3.822L6 9.452l-6 3.822zM18 9.452l-6 3.822 6 3.822
 6-3.822-6-3.822zM6 18.371l6.001 3.822 6-3.822-6-3.822L6 18.371z" />
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