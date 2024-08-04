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


class AdobePhotoshopIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "adobephotoshop"

    @property
    def original_file_name(self) -> "str":
        return "adobephotoshop.svg"

    @property
    def title(self) -> "str":
        return "Adobe Photoshop"

    @property
    def primary_color(self) -> "str":
        return "#31A8FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Adobe Photoshop</title>
     <path d="M9.85 8.42c-.37-.15-.77-.21-1.18-.2-.26 0-.49
 0-.68.01-.2-.01-.34 0-.41.01v3.36c.14.01.27.02.39.02h.53c.39 0
 .78-.06
 1.15-.18.32-.09.6-.28.82-.53.21-.25.31-.59.31-1.03.01-.31-.07-.62-.23-.89-.17-.26-.41-.46-.7-.57zM19.75.3H4.25C1.9.3
 0 2.2 0 4.55v14.899c0 2.35 1.9 4.25 4.25 4.25h15.5c2.35 0 4.25-1.9
 4.25-4.25V4.55C24 2.2 22.1.3 19.75.3zm-7.391
 11.65c-.399.56-.959.98-1.609 1.22-.68.25-1.43.34-2.25.34-.24 0-.4
 0-.5-.01s-.24-.01-.43-.01v3.209c.01.07-.04.131-.11.141H5.52c-.08
 0-.12-.041-.12-.131V6.42c0-.07.03-.11.1-.11.17 0 .33 0
 .56-.01.24-.01.49-.01.76-.02s.56-.01.87-.02c.31-.01.61-.01.91-.01.82
 0 1.5.1 2.06.31.5.17.96.45 1.34.82.32.32.57.71.73
 1.14.149.42.229.85.229 1.3.001.86-.199 1.57-.6 2.13zm7.091
 3.89c-.28.4-.671.709-1.12.891-.49.209-1.09.318-1.811.318-.459
 0-.91-.039-1.359-.129-.35-.061-.7-.17-1.02-.32-.07-.039-.121-.109-.111-.189v-1.74c0-.029.011-.07.041-.09.029-.02.06-.01.09.01.39.23.8.391
 1.24.49.379.1.779.15 1.18.15.38 0
 .65-.051.83-.141.16-.07.27-.24.27-.42
 0-.141-.08-.27-.24-.4-.16-.129-.489-.279-.979-.471-.51-.18-.979-.42-1.42-.719-.31-.221-.569-.51-.761-.85-.159-.32-.239-.67-.229-1.021
 0-.43.12-.84.341-1.21.25-.4.619-.72 1.049-.92.469-.239 1.059-.349
 1.769-.349.41 0 .83.03
 1.24.09.3.04.59.12.86.23.039.01.08.05.1.09.01.04.02.08.02.12v1.63c0
 .04-.02.08-.05.1-.09.02-.14.02-.18
 0-.3-.16-.62-.27-.96-.34-.37-.08-.74-.13-1.12-.13-.2-.01-.41.02-.601.07-.129.03-.24.1-.31.2-.05.08-.08.18-.08.27s.04.18.101.26c.09.11.209.2.34.27.229.12.47.23.709.33.541.18
 1.061.43 1.541.73.33.209.6.49.789.83.16.318.24.67.23
 1.029.011.471-.129.94-.389 1.331z" />
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
