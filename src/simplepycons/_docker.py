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


class DockerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "docker"

    @property
    def original_file_name(self) -> "str":
        return "docker.svg"

    @property
    def title(self) -> "str":
        return "Docker"

    @property
    def primary_color(self) -> "str":
        return "#2496ED"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Docker</title>
     <path d="M13.983 11.078h2.119a.186.186 0
 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.119a.185.185 0
 00-.185.185v1.888c0 .102.083.185.185.185m-2.954-5.43h2.118a.186.186 0
 00.186-.186V3.574a.186.186 0 00-.186-.185h-2.118a.185.185 0
 00-.185.185v1.888c0 .102.082.185.185.185m0 2.716h2.118a.187.187 0
 00.186-.186V6.29a.186.186 0 00-.186-.185h-2.118a.185.185 0
 00-.185.185v1.887c0 .102.082.185.185.186m-2.93 0h2.12a.186.186 0
 00.184-.186V6.29a.185.185 0 00-.185-.185H8.1a.185.185 0
 00-.185.185v1.887c0 .102.083.185.185.186m-2.964 0h2.119a.186.186 0
 00.185-.186V6.29a.185.185 0 00-.185-.185H5.136a.186.186 0
 00-.186.185v1.887c0 .102.084.185.186.186m5.893 2.715h2.118a.186.186 0
 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.118a.185.185 0
 00-.185.185v1.888c0 .102.082.185.185.185m-2.93 0h2.12a.185.185 0
 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0
 00-.184.185v1.888c0 .102.083.185.185.185m-2.964 0h2.119a.185.185 0
 00.185-.185V9.006a.185.185 0 00-.184-.186h-2.12a.186.186 0
 00-.186.186v1.887c0 .102.084.185.186.185m-2.92 0h2.12a.185.185 0
 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0
 00-.184.185v1.888c0 .102.082.185.185.185M23.763
 9.89c-.065-.051-.672-.51-1.954-.51-.338.001-.676.03-1.01.087-.248-1.7-1.653-2.53-1.716-2.566l-.344-.199-.226.327c-.284.438-.49.922-.612
 1.43-.23.97-.09 1.882.403
 2.661-.595.332-1.55.413-1.744.42H.751a.751.751 0 00-.75.748 11.376
 11.376 0 00.692 4.062c.545 1.428 1.355 2.48 2.41 3.124 1.18.723 3.1
 1.137 5.275 1.137.983.003 1.963-.086 2.93-.266a12.248 12.248 0
 003.823-1.389c.98-.567 1.86-1.288 2.61-2.136 1.252-1.418 1.998-2.997
 2.553-4.4h.221c1.372 0 2.215-.549
 2.68-1.009.309-.293.55-.65.707-1.046l.098-.288Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.docker.com/company/newsroom/media'''

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
