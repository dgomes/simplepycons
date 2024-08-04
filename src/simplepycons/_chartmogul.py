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


class ChartmogulIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chartmogul"

    @property
    def original_file_name(self) -> "str":
        return "chartmogul.svg"

    @property
    def title(self) -> "str":
        return "ChartMogul"

    @property
    def primary_color(self) -> "str":
        return "#13324B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ChartMogul</title>
     <path d="M10.621 19.89V8.75L2.867
 19.89H0V4.11h2.758v11.112l7.754-11.113h2.867v11.14L21.16
 4.11H24v15.782h-2.73V8.75l-7.755 11.14Z" />
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