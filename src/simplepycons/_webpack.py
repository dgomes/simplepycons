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


class WebpackIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "webpack"

    @property
    def original_file_name(self) -> "str":
        return "webpack.svg"

    @property
    def title(self) -> "str":
        return "Webpack"

    @property
    def primary_color(self) -> "str":
        return "#8DD6F9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Webpack</title>
     <path d="M22.1987 18.498l-9.7699 5.5022v-4.2855l6.0872-3.3338
 3.6826 2.117zm.6683-.6026V6.3884l-3.5752
 2.0544v7.396zm-21.0657.6026l9.7699 5.5022v-4.2855L5.484
 16.3809l-3.6826 2.117zm-.6683-.6026V6.3884l3.5751
 2.0544v7.396zm.4183-12.2515l10.0199-5.644v4.1434L5.152
 7.6586l-.0489.028zm20.8975 0l-10.02-5.644v4.1434l6.4192
 3.5154.0489.028 3.5518-2.0427zm-10.8775
 13.096l-6.0056-3.2873V8.9384l6.0054 3.4525v6.349zm.8575
 0l6.0053-3.2873V8.9384l-6.0053 3.4525zM5.9724
 8.1845l6.0287-3.3015L18.03 8.1845l-6.0288 3.4665z" />
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
