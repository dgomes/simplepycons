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


class CyberdefendersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "cyberdefenders"

    @property
    def original_file_name(self) -> "str":
        return "cyberdefenders.svg"

    @property
    def title(self) -> "str":
        return "CyberDefenders"

    @property
    def primary_color(self) -> "str":
        return "#335EEA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CyberDefenders</title>
     <path d="M18.918 17.48c-.126 2.727-2.384 4.696-5.364
 4.696H7.34v-6.123l-2.185-.957V24h8.381c4.334 0 7.549-2.962
 7.549-6.881v-.163c-.65.235-1.372.415-2.167.524Zm1.355-9.501C18.611
 4.313 17.726.989
 15.432.213c-1.336-.452-2.005-.091-2.637.217-.199.09-.235.361-.072.505.361.307.813.687
 1.336 1.174-1.95-1.138-7.333-2.835-7.874-.776-.488 1.86-1.319
 4.587-1.319 4.587S.603 5.487.116 7.293c-.488 1.806 3.323 5.274 9.627
 7.134 6.303 1.861 11.198 1.373 13.311-.921
 2.113-2.294.072-5.473-2.781-5.527Zm-1.247.036c-.487.47-2.077
 1.68-5.563
 1.427-3.738-.271-6.809-2.474-7.604-3.088-.126-.091-.18-.235-.126-.398.054-.18.126-.469.253-.849.072-.234.343-.343.542-.216
 1.571.903 4.1 2.221 6.791 2.402 2.402.163 3.847-.542
 4.786-1.066.199-.108.452-.018.542.199l.47
 1.156c.036.162.018.325-.091.433Z" />
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
