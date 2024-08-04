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


class CitroenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "citroen"

    @property
    def original_file_name(self) -> "str":
        return "citroen.svg"

    @property
    def title(self) -> "str":
        return "Citroën"

    @property
    def primary_color(self) -> "str":
        return "#DA291C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Citroën</title>
     <path d="M12 0C6.684 0 2.292 5.38 2.292 12S6.652 24 12 24c5.347 0
 9.708-5.38 9.708-12S17.316 0 12 0zM4.106
 16.233c-.19-.604-.35-1.241-.414-1.878L12 8.18l8.371 6.175a12.334
 12.334 0 0 1-.413 1.878v.032h-.032L12 10.345zm.923 2.101-.032-.032L12
 13.114l7.003 5.188v.032c-1.655 2.897-4.202 4.616-6.987
 4.616s-5.363-1.751-6.987-4.616zM12 5.347l-8.53
 6.335v-.032c.063-2.674.954-5.284 2.61-7.385C7.67 2.324 9.772 1.21 12
 1.21c2.228 0 4.36 1.114 5.92 3.055 1.56 1.942 2.515 4.616 2.61
 7.417v.032l-.031-.032z" />
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