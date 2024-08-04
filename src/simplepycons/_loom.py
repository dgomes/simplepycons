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


class LoomIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "loom"

    @property
    def original_file_name(self) -> "str":
        return "loom.svg"

    @property
    def title(self) -> "str":
        return "Loom"

    @property
    def primary_color(self) -> "str":
        return "#625DF5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Loom</title>
     <path d="M24 10.665h-7.018l6.078-3.509-1.335-2.312-6.078 3.509
 3.508-6.077L16.843.94l-3.508 6.077V0h-2.67v7.018L7.156.94 4.844
 2.275l3.509 6.077-6.078-3.508L.94 7.156l6.078 3.509H0v2.67h7.017L.94
 16.844l1.335 2.313 6.077-3.508-3.509 6.077 2.312 1.335
 3.509-6.078V24h2.67v-7.017l3.508 6.077 2.312-1.335-3.509-6.078 6.078
 3.509 1.335-2.313-6.077-3.508h7.017v-2.67H24zm-12 4.966a3.645 3.645 0
 1 1 0-7.29 3.645 3.645 0 0 1 0 7.29z" />
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
