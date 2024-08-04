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


class WesternDigitalIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "westerndigital"

    @property
    def original_file_name(self) -> "str":
        return "westerndigital.svg"

    @property
    def title(self) -> "str":
        return "Western Digital"

    @property
    def primary_color(self) -> "str":
        return "#995DFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Western Digital</title>
     <path d="M1.4916 4.6198C.1766 4.6235-.4917 6.2026.4214
 7.149c1.1578 1.1552 2.3139 2.312 3.4705 3.4684 2.4059 2.3815 4.8088
 4.766 7.2025 7.1596l1.0703 1.1152c.9402.9525 2.5611.2658
 2.531-1.0722v-3.4255c-.0105-.8247-.677-1.4905-1.5018-1.4999h-4.156c-1.4481.0095-2.6245-1.1669-2.615-2.615v-4.16c-.0104-.8248-.677-1.4905-1.5018-1.5Zm9.261
 0c-1.316.002-1.9858 1.582-1.0722 2.5292 3.9317 3.927 7.8588 7.8588
 11.7881 11.788.9396.9519 2.5594.267
 2.5311-1.0702v-3.4293c-.0105-.8247-.677-1.4905-1.5019-1.4999-1.4004.0137-2.8005-.0184-4.2007-.043-1.4475.0085-2.6227-1.1676-2.6131-2.615v-4.16c-.0105-.8247-.677-1.4904-1.502-1.4998Zm8.2728
 0c-1.3516-.0072-2.0127 1.645-1.0292 2.5722l3.4313 3.4293c.9472.9137
 2.5273.2439
 2.5291-1.0721V6.1196c-.0104-.8239-.676-1.4893-1.4998-1.4998z" />
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
        yield from [
            "WD",
        ]
