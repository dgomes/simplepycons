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


class ParamountplusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paramountplus"

    @property
    def original_file_name(self) -> "str":
        return "paramountplus.svg"

    @property
    def title(self) -> "str":
        return "Paramount+"

    @property
    def primary_color(self) -> "str":
        return "#0064FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Paramount+</title>
     <path d="M16.347
 21.373c.057-.084.151-.314-.025-.74l-.53-1.428c-.073-.182.084-.293.19-.173
 0 0 1.004 1.157 1.264 1.64l.495.822c.425.028 1.6.06 2.732.06a3.26
 3.26 0 0
 1-.316-.364c-1.93-2.392-3.154-3.724-3.166-3.737-.391-.426-.572-.508-.87-.643a4.82
 4.82 0 0 1-.138-.065v.364c0 .047-.057.073-.086.022l-2.846-5.001a1.598
 1.598 0 0 0-.508-.587l-.277-.194-1.354 3.123c.212 0
 .354.216.27.409l-1.25 2.893h1.147c.443 0 .883.087
 1.294.255l.302.125s-.913 1.878-.913 2.867c0
 .181.028.362.075.534h2.104l-.096-.595s1.266.294 2.502.413M12
 2.437c-6.627 0-12 5.373-12 12 0 2.669.873 5.133 2.346
 7.126.503-.218.783-.542.983-.791l2.234-2.858a.467.467 0 0 1
 .179-.138l.336-.146 3.674-4.659.534-.417 1.094-1.524a.482.482 0 0 1
 .101-.102l.478-.347a.34.34 0 0 1
 .398-.004l.578.407c.308.216.557.504.726.84l2.322
 4.077c.051.09.09.129.182.174.454.227.732.268 1.33.913.277.304 1.495
 1.666 3.203 3.784.236.318.538.588.963.783A11.948 11.948 0 0 0 24
 14.437c0-6.627-5.373-12-12-12M3.236
 15.1l-.778-.253-.48.662v-.818l-.778-.253.778-.253v-.818l.48.662.778-.253-.48.662Zm-.185
 2.676-.252.778-.253-.778h-.818l.661-.481-.253-.777.663.48.66-.48-.252.777.662.481Zm.156-6.195.253.778-.661-.48-.663.48.253-.778-.66-.48h.817l.253-.778.252.777h.818Zm1.314-1.76L4.04
 9.16l-.778.253.48-.661-.48-.663.778.254.48-.662v.818l.778.253-.777.252Zm2.045-2.862-.253.777-.252-.777h-.818l.662-.48-.253-.778.661.48.661-.48-.252.777.662.48Zm2.577-1.313-.48.661V5.49l-.779-.254.778-.253v-.817l.48.66.78-.253-.481.663.48.66zm3.265-.75.253.778-.661-.48-.662.48.252-.777-.66-.481h.818L12
 3.637l.252.778h.818zm2.93.595v.816l-.481-.661-.777.252.48-.662-.48-.662.777.253.48-.66v.817l.779.252zm5.426
 8.285.778.253.48-.662v.818l.778.253-.778.253v.818l-.48-.662-.778.253.48-.662zm-3.077-6.04-.253-.777h-.818l.662-.48-.253-.778.662.48.662-.48-.254.778.662.48h-.818zm1.792
 2.086v-.818l-.777-.252.777-.253V7.68l.481.662.777-.254-.48.663.48.66-.777-.252zm1.469
 1.278.253-.777.254.777h.816l-.66.481.252.778-.662-.48-.661.48.253-.778-.662-.48zm.506
 6.676-.253.778-.253-.778h-.817l.662-.481-.253-.777.66.48.663-.48-.253.777.661.481zm-12.08-.615.76-1.588c.024-.048-.032-.108-.067-.067l-.664.668c-.313.329-.847
 1.25-.95 1.421l-.808 1.335a.109.109 0 0 1 .1.162l-.739
 1.238c-.18.309.145.523.189.452 1.157-1.868 1.832-1.719
 1.832-1.719l.387-.897c.022-.047-.001-.1-.05-.12-.12-.05-.316-.27.01-.885z"
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
        return '''https://www.paramount.com/brand/paramount-plu'''

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
