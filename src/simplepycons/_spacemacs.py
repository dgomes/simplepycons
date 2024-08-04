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


class SpacemacsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spacemacs"

    @property
    def original_file_name(self) -> "str":
        return "spacemacs.svg"

    @property
    def title(self) -> "str":
        return "Spacemacs"

    @property
    def primary_color(self) -> "str":
        return "#9266CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Spacemacs</title>
     <path d="M11.997.011c-1.79.015-3.452.397-4.968
 1.093l.005-.002c3.638 2.026 6.955 5.634 8.932 8.241.398.534.753 1.006
 1.078
 1.434l.004-.019c.412-1.738-.313-5.239-1.518-7.331-.117-.203-.201-.379-.187-.392l.006.002.002-.007c.098.024
 1.031.995 1.373 1.433.599.767.832 1.213 1.162 2.23.858 2.645 1.424
 4.801 1.901 7.249.239 1.228.675 3.458.731
 3.884.007.057-.009.128-.01.143a5.164 5.164 0 0
 0-.29-.264c-.645-.568-1.924-1.417-3.183-2.114-1.57-.87-3.118-1.614-6.575-3.162-3.156-1.413-4.61-2.086-5.751-2.661l-1.024-.51c.12.301.249.624.399
 1.005 0 0 1.933 1.08 2.174 1.408 0 0 2.322 4.367 3.353 6.955.767
 1.949 1.634 4.264 2.155
 4.904l.06.069c-1.026-.251-5.745-2.598-5.745-2.598-.518-4.399-1.969-9.61-3.855-14.94a7.259
 7.259 0 0 1-.125-.271c.001-.015.141.121.311.303C4.313 8.13 8.368 9.98
 12.675 10.775a16.48 16.48 0 0 0
 3.533.223c-.307-.392-.64-.821-1.009-1.302-3.418-4.455-6.774-6.326-9.78-7.469-.079-.028-.154-.061-.231-.088A11.902
 11.902 0 0 0 .669 8.071a11.97 11.97 0 0 0-.67 4.016l.003-.088c.033
 5.018 3.129 9.616 8.052 11.33 1.335.465 2.696.68
 4.032.67l-.088-.003c5.018-.033 9.616-3.129
 11.33-8.052.465-1.335.68-2.696.67-4.032l-.003.088c-.033-5.018-3.129-9.616-8.052-11.33A11.966
 11.966 0 0 0 11.911 0l.088.003zm6.133 6.11l-.002.007c-.001 0 0 0 0
 0l.002-.007c.531.511 1.376 1.503 2.336 2.062.789.99 1.216 1.963 1.748
 2.629-.219-.188-1.111-.972-1.111-.972s-1.378-1.305-2.141-2.153c-.293-.326-.32-.38-.478-.628-.062-.097-.275-.825-.354-.935h-.001l.002-.007z"
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
