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


class GoogleEarthEngineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googleearthengine"

    @property
    def original_file_name(self) -> "str":
        return "googleearthengine.svg"

    @property
    def title(self) -> "str":
        return "Google Earth Engine"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Earth Engine</title>
     <path d="M7.853.717a1.19 1.19 0 00-.65.17L4.53
 2.49c-.53.317-.732.984-.467 1.543l.93 1.958a9.217 9.217 0 00-1.745
 3.076l-2.124.135A1.198 1.198 0 000 10.399v3.116a1.2 1.2 0 001.084
 1.194l2.171.21a9.207 9.207 0 001.748 3.066l-.941 1.982a1.198 1.198 0
 00.467 1.543l2.673 1.603a1.2 1.2 0 001.605-.347l1.22-1.771a9.22 9.22
 0 001.971.216c.032 0 .064-.004.096-.004a9.245 9.245 0
 001.876-.212l1.22 1.77a1.2 1.2 0
 001.606.348l2.673-1.603c.53-.317.732-.984.467-1.543l-.941-1.982c.022-.025.048-.049.07-.076.066-.077.125-.159.188-.238a9.225
 9.225 0 001.484-2.736l2.138-.137A1.198 1.198 0 0024 13.601v-3.116a1.2
 1.2 0 00-1.084-1.194V9.29l-2.16-.21a9.182 9.182 0
 00-1.501-2.786c-.063-.08-.124-.16-.19-.238-.018-.022-.039-.043-.058-.065l.93-1.958a1.198
 1.198 0 00-.467-1.543L16.797.887a1.2 1.2 0 00-1.605.347L13.99
 2.976a9.169 9.169 0 00-1.896-.219c-.033 0-.064-.004-.096-.004a9.2 9.2
 0 00-1.992.223L8.808 1.234a1.2 1.2 0 00-.955-.517zm4.148 3.882c.574 0
 1.13.072 1.668.197a7.41 7.41 0 015.384 4.993 7.36 7.36 0 01.332
 2.193c0 .764-.116 1.5-.332 2.193a7.407 7.407 0 01-5.384 4.992 7.393
 7.393 0 01-1.668.199c-4.071 0-7.384-3.313-7.384-7.384 0-4.07
 3.313-7.383 7.384-7.383zM11.907 6C9.558 6 8.429 7.207 8.429
 7.207c3.501-1.577 5.23 2.986 6.702 4.386 1.472 1.4 2.887.203
 2.887.203-.012-.787-.252-1.533-.252-1.533-.968.168-1.398-.494-1.97-1.252C15.224
 8.253 13.561 6 11.907 6zm-3.84 3.228c-.705.015-1.3.35-1.653 1-.868
 1.601-.096 3.64-.096 3.64s.3-1.532 1.537-1.309c1.238.224 1.754 1.208
 2.504 1.985.75.776 1.895 2.064 3.978 2.064 2.082 0 3.018-1.516
 3.435-2.937v-.002l-.053.04c-1.265.98-3.335.882-4.548-.275-.89-.846-1.403-1.908-2.135-2.68-.981-1.038-2.065-1.545-2.97-1.526z"
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
        return '''https://github.com/simple-icons/simple-icons/'''

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