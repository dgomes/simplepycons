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


class HandlebarsdotjsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "handlebarsdotjs"

    @property
    def original_file_name(self) -> "str":
        return "handlebarsdotjs.svg"

    @property
    def title(self) -> "str":
        return "Handlebars.js"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Handlebars.js</title>
     <path d="M9.1 4.948a3.45 3.45 0 0 0-.398.014C6.32 5.15 5.373
 6.375 4.802 6.9c-.572.525-1.656 1.763-2.376
 1.545-.721-.217-.924-1.107-.67-1.381s.454-.225.613
 0c.097.18.145.383.14.587a1.36 1.36 0 0 0 .438-.665.792.792 0 0
 0-.443-1.017c-1.3-.659-2.139.514-2.26.787-.122.273-.336.707-.2
 1.695.135.989.612 1.902 2.104 2.261a6.31 6.31 0 0 0
 4.238-.495l4.41-1.84a5.408 5.408 0 0 1 .556-.101v9.864c0
 .506.316.913.708.913.391 0 .707-.407.707-.913V8.29a5.408 5.408 0 0 1
 .437.088l4.41 1.84a6.31 6.31 0 0 0 4.238.494c1.492-.36 1.969-1.272
 2.105-2.26.135-.989-.08-1.423-.2-1.696-.122-.273-.962-1.446-2.261-.787a.792.792
 0 0 0-.443 1.017c.076.26.229.492.437.665a1.19 1.19 0 0 1
 .141-.587c.159-.225.359-.274.613 0s.051 1.164-.67
 1.382c-.72.217-1.804-1.02-2.376-1.546-.571-.525-1.518-1.75-3.9-1.938A3.45
 3.45 0 0 0 12 6.653a3.45 3.45 0 0 0-2.9-1.705zm12.39
 2.703v.004l.006.002c-.002-.002-.004-.004-.006-.004zm-18.98
 0c-.002.002-.004.004-.006.004l.006-.001V7.65z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/handlebars-lang/docs/blob/
13a2e2d9e31ebff4295924ea366abf3062e47ede/src/.vuepress/public/icons/ha'''

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
