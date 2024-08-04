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


class AdobeXdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adobexd"

    @property
    def original_file_name(self) -> "str":
        return "adobexd.svg"

    @property
    def title(self) -> "str":
        return "Adobe XD"

    @property
    def primary_color(self) -> "str":
        return "#FF61F6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Adobe XD</title>
     <path d="M4.25.3C1.9.3 0 2.2 0 4.55v14.9c0 2.35 1.9 4.25 4.25
 4.25h15.5c2.35 0 4.25-1.9 4.25-4.25V4.55C24 2.2 22.1.3 19.75.3Zm14.07
 5.13h2.03c.05-.01.09.03.1.07v9.54c0 .18.01.38.02.6.02.21.03.41.04.58
 0
 .07-.03.13-.1.16-.52.22-1.07.38-1.63.48-.51.09-1.02.14-1.54.14-.74.01-1.48-.14-2.15-.45-.63-.29-1.15-.77-1.51-1.36-.37-.61-.55-1.37-.55-2.28a4.107
 4.107 0 0 1 2.14-3.66c.7-.39 1.54-.58 2.53-.58.05 0 .12 0
 .21.01s.19.01.31.02V5.54c0-.07.03-.11.1-.11zM3.68 6.3h2.27c.05 0
 .1.01.14.02.04.02.07.05.1.09.19.43.41.86.64 1.29.24.43.47.85.72
 1.27.24.42.46.84.67
 1.27h.02c.21-.44.43-.87.65-1.29.22-.42.45-.84.68-1.26.23-.42.45-.85.67-1.26.01-.04.03-.08.06-.1a.19.19
 0 0 1 .13-.02h2.11c.05-.01.1.02.11.07.01.01-.01.05-.03.07l-3 4.95 3.2
 5.25c.02.04.03.08.02.12-.01.04-.05.01-.11.02h-2.29c-.16
 0-.27-.01-.34-.11-.21-.42-.43-.83-.64-1.25-.21-.41-.44-.83-.68-1.26-.24-.43-.48-.86-.72-1.3h-.02c-.21.43-.44.86-.67
 1.29-.23.43-.46.86-.68 1.28-.23.42-.46.85-.69
 1.26-.04.1-.12.11-.23.11h-2.2c-.04 0-.07.02-.07-.03a.14.14 0 0 1
 .02-.11l3.11-5.1L3.6
 6.44c-.03-.04-.04-.08-.02-.1.02-.03.06-.04.1-.04zm13.94 4.23c-.39
 0-.78.08-1.13.26-.34.17-.63.42-.85.74-.22.32-.33.75-.33
 1.27-.01.35.05.7.17
 1.03.1.27.25.51.45.71.19.18.42.32.68.4.27.09.55.13.83.13.15 0
 .29-.01.42-.02.13.01.24-.01.36-.05v-4.4c-.09-.02-.18-.04-.27-.05-.11-.01-.22-.02-.33-.02Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://developer.adobe.com/developer-distrib'''
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
