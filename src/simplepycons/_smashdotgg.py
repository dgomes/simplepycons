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


class SmashdotggIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "smashdotgg"

    @property
    def original_file_name(self) -> "str":
        return "smashdotgg.svg"

    @property
    def title(self) -> "str":
        return "smash.gg"

    @property
    def primary_color(self) -> "str":
        return "#CB333B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>smash.gg</title>
     <path d="M18.01 4.32c-.622.044-1.096.236-1.41.574a1.438 1.438 0
 00-.332.546c-.138.366-.134.288-.142 2.57-.008 2.096-.002 2.328.066
 2.628.142.612.524 1.03 1.124 1.228.342.114.58.14
 1.192.128.586-.01.686-.028.962-.17a1.35 1.35 0
 00.496-.494l.074-.14-.004.6c-.006.686-.01.7-.176.784l-.088.046H16.5v2h1.986c1.976
 0 2.386-.012 2.714-.072.98-.178 1.508-.71
 1.62-1.628.012-.11.02-1.616.02-4.394V4.3h-2.76v.93l-.048-.114c-.17-.412-.48-.664-.932-.756-.226-.046-.736-.066-1.09-.04zm1.844
 2.124a.41.41 0 01.128.15l.048.096v2.94l-.048.096a.392.392 0
 01-.128.15c-.08.052-.088.054-.392.054-.292
 0-.316-.002-.388-.046-.152-.096-.144.004-.15-1.68-.004-1.018.002-1.53.016-1.584.052-.196.16-.242.552-.236.268.006.284.008.362.06zM10.17
 4.32c-.62.044-1.048.214-1.384.55-.16.16-.194.21-.282.392-.112.23-.172.448-.204.738-.016.128-.02.872-.016
 2.29.008 2.048.008 2.104.05
 2.28.096.412.218.648.464.89.294.29.604.434 1.112.51.312.046 1.084.042
 1.33-.01.398-.082.72-.314.886-.64l.076-.15-.006.61c-.006.698-.01.71-.176.794l-.088.046H8.66v2.002l2.176-.008c1.594-.006
 2.22-.014 2.344-.032.6-.09 1.094-.314
 1.372-.628.186-.21.314-.478.394-.824.042-.18.042-.184.048-4.506L15
 4.3h-2.76v.474l-.002.476-.039-.104c-.147-.416-.48-.692-.944-.786-.222-.046-.733-.064-1.086-.04zm1.844
 2.124a.41.41 0 01.128.15l.048.096.006 1.396c.004.91-.002 1.436-.016
 1.51-.026.142-.094.246-.194.296-.064.032-.122.038-.376.038-.34
 0-.402-.02-.48-.15-.04-.068-.04-.098-.04-1.62 0-1.52
 0-1.552.04-1.62a.336.336 0
 01.13-.116c.084-.044.11-.046.382-.04.278.006.294.008.372.06zM2.64
 9.11v9.11H0v1.2h2.64V24h3.84v-4.58H24v-1.2H6.48V0H2.64z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://help.smash.gg/en/articles/1716774-sma'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://help.smash.gg/en/articles/1716774-sma'''

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
