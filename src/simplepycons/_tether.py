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


class TetherIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tether"

    @property
    def original_file_name(self) -> "str":
        return "tether.svg"

    @property
    def title(self) -> "str":
        return "Tether"

    @property
    def primary_color(self) -> "str":
        return "#50AF95"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tether</title>
     <path d="M18.7538 10.5176c0 .6251-2.2379 1.1483-5.2381
 1.2812l.0028.0007c-.0848.0064-.5233.0325-1.5012.0325-.7778
 0-1.33-.0233-1.5237-.0325-3.0059-.1322-5.2495-.6555-5.2495-1.2819s2.2436-1.149
 5.2495-1.2834v2.0442c.1965.0142.7594.0474 1.5372.0474.9334 0
 1.4008-.0389 1.4849-.0466V9.2356c2.9994.1337 5.2381.657 5.2381
 1.282zm5.19.5466L12.1248 22.389a.1803.1803 0 0 1-.2496 0L.0562
 11.0635a.1781.1781 0 0 1-.0382-.2079l4.3762-9.1921a.1767.1767 0 0 1
 .1626-.1026h14.8878a.1768.1768 0 0 1 .1612.1032l4.3762
 9.1922a.1782.1782 0 0
 1-.0382.2079zm-4.478-.4038c0-.8068-2.5515-1.4799-5.9473-1.6369V7.195h4.186V4.4055H6.3076V7.195h4.1852v1.8286c-3.4018.1562-5.9601.83-5.9601
 1.6376 0 .8075 2.5583 1.4806 5.9601
 1.6376v5.8618h3.025v-5.8639c3.394-.1563 5.948-.8295 5.948-1.6363z" />
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
        yield from [
            "USDt",
        ]
