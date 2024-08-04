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


class FreedesktopdotorgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freedesktopdotorg"

    @property
    def original_file_name(self) -> "str":
        return "freedesktopdotorg.svg"

    @property
    def title(self) -> "str":
        return "freedesktop.org"

    @property
    def primary_color(self) -> "str":
        return "#3B80AE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>freedesktop.org</title>
     <path d="M23.855 13.112l-2.054-7.875a4.414 4.414 0 0
 0-5.379-3.153L3.296 5.509a4.413 4.413 0 0 0-3.153 5.378l2.055
 7.875a4.416 4.416 0 0 0 5.379 3.153l13.126-3.425a4.377 4.377 0 0 0
 2.69-2.036 4.377 4.377 0 0 0 .462-3.342zm-1.047 3a3.701 3.701 0 0
 1-2.277 1.723L7.406 21.26a3.735 3.735 0 0 1-4.551-2.668L.8
 10.717a3.734 3.734 0 0 1 2.668-4.552L16.593 2.74a3.727 3.727 0 0 1
 4.551 2.668l2.054 7.875a3.7 3.7 0 0 1-.39
 2.829zm-2.362-9.893c-.482-2.061-2.122-2.941-4.369-2.437l-11.65
 3.04c-2.426.706-3.104 2.014-2.621 4.261l1.748 6.698c.482 2.112 2.281
 3.098 4.369 2.437l11.651-3.04c2.121-.504 3.104-2.095
 2.622-4.261l-1.75-6.698zm-6.277 3.097l.173.663-4.117.475-.173-.663
 4.117-.475zm-9.05 3.861a.639.639 0 0 1-.783-.46l-.777-2.975a.643.643
 0 0 1 .459-.783l4.169-1.087a.644.644 0 0 1 .784.458l.776
 2.975a.643.643 0 0 1-.459.784l-4.169 1.088zm5.618
 1.76l-2.06-1.988.769-.201 2.03 1.959-.519.135a.944.944 0 0
 0-.22.095zm3.397 1.93a.212.212 0 0 1-.128.097l-2.336.609a.21.21 0 0
 1-.257-.151l-.435-1.667a.21.21 0 0 1 .151-.257l2.336-.609a.211.211 0
 0 1 .256.15l.435 1.667a.214.214 0 0 1-.022.161zm.011-2.398a.882.882 0
 0 0-.178-.142.882.882 0 0
 0-.463-.119l1.562-2.351c.183.147.41.235.649.248l-1.57
 2.364zm5.151-3.94l-3.401.887a.462.462 0 0
 1-.563-.33l-.633-2.428a.461.461 0 0 1 .33-.563l3.401-.887a.47.47 0 0
 1 .35.049.457.457 0 0 1 .213.282l.633 2.428a.46.46 0 0 1-.33.562z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Freed'''

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
