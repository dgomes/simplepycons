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


class DiscordIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "discord"

    @property
    def original_file_name(self) -> "str":
        return "discord.svg"

    @property
    def title(self) -> "str":
        return "Discord"

    @property
    def primary_color(self) -> "str":
        return "#5865F2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Discord</title>
     <path d="M20.317 4.3698a19.7913 19.7913 0
 00-4.8851-1.5152.0741.0741 0
 00-.0785.0371c-.211.3753-.4447.8648-.6083
 1.2495-1.8447-.2762-3.68-.2762-5.4868
 0-.1636-.3933-.4058-.8742-.6177-1.2495a.077.077 0 00-.0785-.037
 19.7363 19.7363 0 00-4.8852 1.515.0699.0699 0 00-.0321.0277C.5334
 9.0458-.319 13.5799.0992 18.0578a.0824.0824 0 00.0312.0561c2.0528
 1.5076 4.0413 2.4228 5.9929 3.0294a.0777.0777 0
 00.0842-.0276c.4616-.6304.8731-1.2952 1.226-1.9942a.076.076 0
 00-.0416-.1057c-.6528-.2476-1.2743-.5495-1.8722-.8923a.077.077 0
 01-.0076-.1277c.1258-.0943.2517-.1923.3718-.2914a.0743.0743 0
 01.0776-.0105c3.9278 1.7933 8.18 1.7933 12.0614 0a.0739.0739 0
 01.0785.0095c.1202.099.246.1981.3728.2924a.077.077 0 01-.0066.1276
 12.2986 12.2986 0 01-1.873.8914.0766.0766 0
 00-.0407.1067c.3604.698.7719 1.3628 1.225 1.9932a.076.076 0
 00.0842.0286c1.961-.6067 3.9495-1.5219 6.0023-3.0294a.077.077 0
 00.0313-.0552c.5004-5.177-.8382-9.6739-3.5485-13.6604a.061.061 0
 00-.0312-.0286zM8.02 15.3312c-1.1825 0-2.1569-1.0857-2.1569-2.419
 0-1.3332.9555-2.4189 2.157-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419
 0 1.3332-.9555 2.4189-2.1569 2.4189zm7.9748 0c-1.1825
 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9554-2.4189 2.1569-2.4189
 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332-.946 2.4189-2.1568
 2.4189Z" />
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
