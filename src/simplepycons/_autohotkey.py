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


class AutohotkeyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "autohotkey"

    @property
    def original_file_name(self) -> "str":
        return "autohotkey.svg"

    @property
    def title(self) -> "str":
        return "AutoHotkey"

    @property
    def primary_color(self) -> "str":
        return "#334455"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AutoHotkey</title>
     <path d="M20.514.508V.51H1.803C1.053.51.079 1.135 0
 2.27v17.133h.002v2.325c.08 1.136 1.05 1.763 1.8
 1.763h1.505l.002-.002h18.869c1.256-.053 1.766-1.066
 1.822-1.699v-3.023h-.002V2.209c-.056-.633-.567-1.648-1.824-1.701h-1.66zM3.412
 1.623h17.154c.898 0 1.618.72 1.618 1.617v16.64c0 .898-.72 1.62-1.618
 1.62H3.412a1.616 1.616 0 01-1.619-1.62V3.24c0-.897.722-1.617
 1.62-1.617zm3.315 12.412l-1.895 5.037h.703l.526-1.467h2.02l.497
 1.467h.744l-1.824-5.037h-.771zm8.43.008v5.037h.679v-1.767l.793-.758
 1.76 2.525h.884l-2.154-3.002 2.098-2.035h-.94l-2.441
 2.441v-2.441h-.68zm-5.153.027v5.037h.682v-2.351h2.628v2.351h.682V14.07h-.682v2.084h-2.628V14.07h-.682zm-2.926.717h.014l.742
 2.217H6.271l.807-2.217z" />
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
