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


class OpenSourceHardwareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opensourcehardware"

    @property
    def original_file_name(self) -> "str":
        return "opensourcehardware.svg"

    @property
    def title(self) -> "str":
        return "Open Source Hardware"

    @property
    def primary_color(self) -> "str":
        return "#0099B0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Open Source Hardware</title>
     <path d="M23.87 11.525c.071.013.13.084.13.157v3.033a.166.166 0 0
 1-.13.157l-2.875.535a.243.243 0 0 0-.17.151l-.898 2.242a.252.252 0 0
 0 .017.229l1.633 2.379a.167.167 0 0 1-.02.204l-2.144 2.144a.167.167 0
 0 1-.203.019l-2.338-1.604a.23.23 0 0 0-.224-.008l-1.03.55a.121.121 0
 0 1-.17-.062l-2.125-5.135a.161.161 0 0 1
 .062-.192l.258-.158c.048-.03.113-.08.163-.125a3.354 3.354 0 1 0-3.612
 0c.05.046.115.096.163.125l.258.158a.16.16 0 0 1 .062.192L8.552
 21.65a.121.121 0 0 1-.17.063l-1.03-.55a.23.23 0 0 0-.224.007L4.79
 22.775a.168.168 0 0 1-.204-.019l-2.145-2.144a.167.167 0 0
 1-.019-.204l1.633-2.38a.251.251 0 0 0 .017-.228l-.897-2.242a.244.244
 0 0 0-.17-.15L.13 14.871a.166.166 0 0
 1-.13-.157v-3.032c0-.073.059-.144.13-.157l2.947-.548a.253.253 0 0 0
 .175-.15l.903-2.108a.246.246 0 0 0-.014-.227L2.424 5.989a.167.167 0 0
 1 .019-.203L4.587 3.64a.166.166 0 0 1 .204-.019L7.337
 5.37c.06.041.163.048.229.016l2.043-.836c.07-.023.137-.1.15-.173l.567-3.047a.167.167
 0 0 1 .157-.131h3.034c.073 0 .143.059.157.13l.567 3.048a.25.25 0 0 0
 .15.173l2.043.836a.252.252 0 0 0 .23-.016l2.546-1.748a.166.166 0 0 1
 .203.02l2.144 2.144c.052.051.06.143.02.203l-1.718 2.503a.245.245 0 0
 0-.014.227l.903 2.108a.256.256 0 0 0 .175.15l2.946.548" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.oshwa.org/open-source-hardware-lo'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.oshwa.org/open-source-hardware-lo'''

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
            "OSHWA",
        ]
