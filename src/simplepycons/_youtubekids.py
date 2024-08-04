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


class YoutubeKidsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "youtubekids"

    @property
    def original_file_name(self) -> "str":
        return "youtubekids.svg"

    @property
    def title(self) -> "str":
        return "YouTube Kids"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>YouTube Kids</title>
     <path d="m23.99
 13.543-.007-.288c-.015-1.122-.645-6.495-.999-7.457-.41-1.111-.974-1.945-1.675-2.48-1.143-.873-2.115-1.063-3.313-1.087h-.03c-.51
 0-3.848.415-6.642.801-2.797.387-6.303.915-7.14
 1.227-1.153.432-2.07.997-2.796 1.728C.05 7.332-.113 8.731.054
 10.553c.13 1.412.875 6.975 1.302 8.248.574 1.717 1.694 2.75 3.154
 2.909.36.039.704.059 1.045.059 1.28 0 2.295-.278 3.47-.598 1.848-.505
 4.147-1.13 8.893-1.13h.14c1.162 0 4.008-.263
 5.303-2.687.693-1.297.652-2.87.629-3.811zm-7.719-1.67-.105.066c-.274.185-.547.373-.819.563l-4.298
 2.975c-.27.21-.748.521-1.016.521a.236.236 0 0
 1-.107-.024c-.226-.12-.303-.94-.356-1.34l-.011-.087c-.065-.478-.594-5.035-.654-5.535-.017-.142-.105-.663.055-.781.05-.037.12-.05.2-.05.195
 0 .442.083.549.118.845.272 5.083 1.774 6.4
 2.448.038.02.079.04.122.057.188.08.446.192.452.51.004.304-.225.446-.412.56z"
 />
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
