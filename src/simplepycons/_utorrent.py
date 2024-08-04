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


class UtorrentIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "utorrent"

    @property
    def original_file_name(self) -> "str":
        return "utorrent.svg"

    @property
    def title(self) -> "str":
        return "uTorrent"

    @property
    def primary_color(self) -> "str":
        return "#76B83F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>uTorrent</title>
     <path d="M13.684 23.94a12.013 12.013 0 0 0
 9.599-7.79c-.118.044-.26.096-.432.147-2
 .59-3.404-.466-3.687-.649-.283-.18-.587-.48-.643-.464-.183
 1.132-1.218 2.706-3.58
 3.42-1.295.391-2.687.4-3.681-.157l.328.822c.13.328.351.866.488 1.192
 0 0 .858 2.044 1.608 3.48M2.723
 7.153l3.54-.66c.323-.059.68.124.794.407l2.432
 6.07c.332.633.399.773.615 1.043 0 0 1.68 2.398 4.24 1.812 1.726-.394
 2.532-1.69 2.587-2.612.057-.296-.032-.669-.185-1.016L13.832
 5.61c-.117-.266.022-.527.306-.581l2.953-.55a.69.69 0 0 1
 .706.376l3.227 6.91c.13.276.394.712.588.966 0 0 .671.964 1.747.78.266
 0 .569-.143.569-.143.047-.43.072-.866.072-1.31
 0-6.627-5.373-12-12.002-12C5.372.06 0 5.433 0 12.06c0 5.319 3.46
 9.827 8.252 11.402a24.768 24.768 0 0 1-.919-2.121L2.298
 7.808c-.111-.297.083-.59.425-.654" />
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