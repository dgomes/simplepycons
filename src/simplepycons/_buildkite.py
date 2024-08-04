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


class BuildkiteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "buildkite"

    @property
    def original_file_name(self) -> "str":
        return "buildkite.svg"

    @property
    def title(self) -> "str":
        return "Buildkite"

    @property
    def primary_color(self) -> "str":
        return "#14CC80"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Buildkite</title>
     <path d="M23.613 8.143l-7.668-3.856v7.712l7.668-3.855zM8.166
 15.857V8.143L.387 4.287V12l7.78 3.857zM.183 3.958a.382.382 0
 01.377-.017l7.606 3.771 7.607-3.771a.386.386 0 01.346 0l7.668
 3.857a.386.386 0 01.213.345v7.71a.388.388 0 01-.213.346l-7.668
 3.86a.389.389 0 01-.562-.345v-7.09l-7.219 3.58a.392.392 0 01-.344
 0L.215 12.346A.387.387 0 010 12V4.287a.385.385 0 01.183-.329z" />
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