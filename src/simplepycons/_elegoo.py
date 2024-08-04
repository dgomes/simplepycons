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


class ElegooIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "elegoo"

    @property
    def original_file_name(self) -> "str":
        return "elegoo.svg"

    @property
    def title(self) -> "str":
        return "Elegoo"

    @property
    def primary_color(self) -> "str":
        return "#2C3A83"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Elegoo</title>
     <path d="M12.686 7.479c.54.829 1.032 1.665 1.476 2.505.64-1.217
 1.849-2.086 3.328-2.086 2.217 0 3.826 1.954 3.826 4.102 0 2.149-1.609
 4.102-3.826 4.102-.656
 0-1.26-.171-1.784-.467l-.001-.001c-.635-.36-1.153-.905-1.509-1.553-.484-.804-.725-1.706-.991-2.657-.598-2.134-1.252-3.773-3.194-4.988-1.001-.626-2.196-.985-3.501-.985C2.815
 5.451 0 8.323 0 12c0 3.727 2.761 6.549 6.51 6.549 1.955 0 3.639-.766
 4.805-2.027-.543-.83-1.034-1.664-1.477-2.505-.641 1.217-1.849
 2.085-3.328 2.085-2.218 0-3.827-1.953-3.827-4.102 0-2.148 1.609-4.102
 3.827-4.102.655 0 1.26.171 1.783.469h.001c.635.36 1.154.904 1.509
 1.553.574.951.807 2.041 1.144 3.188.555 1.89 1.285 3.339 3.002 4.432
 1.008.642 2.217 1.009 3.541 1.009 3.694 0 6.51-2.872 6.51-6.549
 0-3.727-2.76-6.549-6.51-6.549-1.954 0-3.64.766-4.804 2.028Z" />
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
