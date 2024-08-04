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


class ShortcutIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shortcut"

    @property
    def original_file_name(self) -> "str":
        return "shortcut.svg"

    @property
    def title(self) -> "str":
        return "Shortcut"

    @property
    def primary_color(self) -> "str":
        return "#58B1E4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shortcut</title>
     <path d="M24 6a6 6 0 0 0-6-6H6a5.975 5.975 0 0 0-4.242 1.758
 5.998 5.998 0 0 0 0 8.484l2.137 2.137A6.007 6.007 0 0 0 0 18a6 6 0 0
 0 6 6h12a5.975 5.975 0 0 0 4.242-1.758 5.998 5.998 0 0 0
 0-8.484l-2.137-2.137A6.002 6.002 0 0 0 24 6zM3.404
 20.598c-.694-.694-1.075-1.615-1.075-2.596s.38-1.903 1.075-2.595a3.65
 3.65 0 0 1 2.443-1.074l7.34 7.34H6a3.664 3.664 0 0
 1-2.596-1.075zm17.192-5.194C21.29 16.1 21.67 17.02 21.67 18s-.38
 1.904-1.075 2.596A3.644 3.644 0 0 1 18 21.67a3.64 3.64 0 0
 1-2.596-1.075l-12-11.998C2.71 7.904 2.33 6.983 2.33 6.002s.38-1.903
 1.075-2.595C4.1 2.712 5.02 2.33 6 2.33s1.904.381 2.596 1.076l12
 11.997zm0-6.806a3.65 3.65 0 0 1-2.443 1.073l-7.34-7.342H18a3.64 3.64
 0 0 1 2.596 1.075C21.29 4.1 21.67 5.02 21.67 6s-.38 1.904-1.075
 2.598z" />
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
