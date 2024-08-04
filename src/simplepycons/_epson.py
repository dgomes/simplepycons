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


class EpsonIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "epson"

    @property
    def original_file_name(self) -> "str":
        return "epson.svg"

    @property
    def title(self) -> "str":
        return "Epson"

    @property
    def primary_color(self) -> "str":
        return "#003399"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Epson</title>
     <path d="M16.616 13.915c-1.029 0-1.428-.952-1.428-1.915
 0-.975.398-1.927 1.428-1.927 1.03 0 1.429.952 1.429 1.927 0 .963-.399
 1.915-1.429 1.915m0-4.805c-1.627 0-2.567 1.218-2.567 2.89s.94 2.89
 2.567 2.89c1.628 0 2.568-1.218 2.568-2.89s-.94-2.89-2.568-2.89zM0
 9.266h4.085v.974H1.141v1.207h2.745v.952H1.141v1.351h2.944v.975H0V9.266zM6.73
 12.11H5.701v-1.871H6.73c.709 0 1.185.311 1.185.941 0
 .621-.476.93-1.185.93m-2.168 2.614h1.14v-1.639H6.73c1.384 0
 2.314-.687 2.314-1.904
 0-1.229-.931-1.915-2.314-1.915H4.562v5.458zM20.768
 9.266h-1.162v5.458h1.118v-2.215c0-.598-.022-1.14-.044-1.605.133.267.531
 1.085.708 1.396l1.45 2.425H24V9.266h-1.106v2.158c0 .599.022 1.196.044
 1.672-.133-.276-.531-1.096-.72-1.406l-1.45-2.424zM10.34 12.919c0
 .73.608 1.019 1.251 1.019.421 0 1.118-.122 1.118-.687
 0-.598-.842-.709-1.649-.919-.853-.232-1.672-.543-1.672-1.561 0-1.13
 1.063-1.661 2.059-1.661 1.152 0 2.204.498 2.204
 1.771h-1.13c-.044-.664-.554-.83-1.129-.83-.388 0-.875.154-.875.619 0
 .421.277.487 1.661.842.398.11 1.66.354 1.66 1.595 0 1.018-.797
 1.771-2.292 1.771-1.217 0-2.357-.598-2.347-1.959h1.141z" />
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
