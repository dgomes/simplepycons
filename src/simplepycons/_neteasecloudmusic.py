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


class NeteaseCloudMusicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "neteasecloudmusic"

    @property
    def original_file_name(self) -> "str":
        return "neteasecloudmusic.svg"

    @property
    def title(self) -> "str":
        return "NetEase Cloud Music"

    @property
    def primary_color(self) -> "str":
        return "#D43C33"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NetEase Cloud Music</title>
     <path d="M13.046 9.388a3.919 3.919 0 0
 0-.66.19c-.809.312-1.447.991-1.666 1.775a2.269 2.269 0 0
 0-.074.81c.048.546.333 1.05.764 1.35a1.483 1.483 0 0 0
 2.01-.286c.406-.531.355-1.183.24-1.636-.098-.387-.22-.816-.345-1.249a64.76
 64.76 0 0 1-.269-.954zm-.82 10.07c-3.984 0-7.224-3.24-7.224-7.223
 0-.98.226-3.02 1.884-4.822A7.188 7.188 0 0 1 9.502 5.6a.792.792 0 1 1
 .587 1.472 5.619 5.619 0 0 0-2.795 2.462 5.538 5.538 0 0 0-.707 2.7
 5.645 5.645 0 0 0 5.638 5.638c1.844 0 3.627-.953 4.542-2.428
 1.042-1.68.772-3.931-.627-5.238a3.299 3.299 0 0
 0-1.437-.777c.172.589.334 1.18.494 1.772.284 1.12.1 2.181-.519
 2.989-.39.51-.956.888-1.592 1.064a3.038 3.038 0 0 1-2.58-.44 3.45
 3.45 0 0 1-1.44-2.514c-.04-.467.002-.93.128-1.376.35-1.256
 1.356-2.339 2.622-2.826a5.5 5.5 0 0 1
 .823-.246l-.134-.505c-.37-1.371.25-2.579 1.547-3.007.329-.109.68-.145
 1.025-.105.792.09 1.476.592 1.709 1.023.258.507-.096 1.153-.706
 1.153a.788.788 0 0 1-.54-.213c-.088-.08-.163-.174-.259-.247a.825.825
 0 0 0-.632-.166.807.807 0 0
 0-.634.551c-.056.191-.031.406.02.595.07.256.159.597.217.82 1.11.098
 2.162.54 2.97 1.296 1.974 1.844 2.35 4.886.892 7.233-1.197 1.93-3.509
 3.177-5.889 3.177zM0 12c0 6.627 5.373 12 12 12s12-5.373 12-12S18.627
 0 12 0 0 5.373 0 12Z" />
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