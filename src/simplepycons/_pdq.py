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


class PdqIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pdq"

    @property
    def original_file_name(self) -> "str":
        return "pdq.svg"

    @property
    def title(self) -> "str":
        return "PDQ"

    @property
    def primary_color(self) -> "str":
        return "#231F20"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PDQ</title>
     <path d="M18.813 7.373a4.655 4.655 0 0 0-3.323 1.354 4.621 4.621
 0 0 0-1.2 2.078 4.213 4.213 0 0 0-.696-1.59 3.725 3.725 0 0
 0-1.084-1.027c-.323-.2-.731-.4-1.184-.5-.479-.104-.994-.14-1.625-.14H6.707v8.891h3.502a4.493
 4.493 0 0 0 1.727-.322c.502-.202.953-.51
 1.324-.904.376-.409.664-.89.847-1.414.07-.191.127-.39.172-.596a4.463
 4.463 0 0 0 1.237 2.09c.442.415.96.742 1.525.965a5 5 0 0 0
 1.89.353c.848.001 1.654-.23
 2.42-.693.206.221.492.394.858.52.397.13.813.192
 1.23.187.188.004.374-.017.561-.025v-1.801c-.082-.001-.11.014-.188.013-.419
 0-.744-.104-.976-.316.25-.365.447-.766.582-1.187.123-.412.185-.839.182-1.268a4.595
 4.595 0 0 0-.368-1.838 4.532 4.532 0 0 0-1.017-1.482 4.888 4.888 0 0
 0-3.402-1.348ZM0 7.549v8.89l2.18-.002v-2.785h.976c.633 0 1.15-.058
 1.551-.173 1.117-.318 1.588-1.234
 1.738-1.612.17-.41.256-.85.254-1.293a3.299 3.299 0 0 0-.267-1.332 2.7
 2.7 0 0 0-1.256-1.34c-.319-.156-.746-.279-1.31-.32a11.989 11.989 0 0
 0-.95-.033Zm18.81 1.824c.346-.003.689.06 1.01.188.653.259 1.098.772
 1.319 1.334.127.322.19.665.187 1.011.003.227 0 .573-.308 1.32a19.46
 19.46 0 0
 1-.32-.372c-.24-.288-.534-.513-.91-.788-1.65-1.15-2.842-.697-3.37-.453.116-.693.389-1.24.816-1.64.428-.4.953-.6
 1.577-.6Zm-16.63.174h.828c.535 0 .922.082
 1.158.248.236.165.354.437.354.812 0 .698-.473 1.047-1.418
 1.047H2.18zm6.8 0h.989c.695 0 1.23.214 1.605.64.375.427.56 1.04.56
 1.84.001.782-.184 1.38-.554
 1.793-.37.413-.912.62-1.625.62H8.98Zm8.467 3.43c.348-.003.692.075
 1.004.226.242.105.467.243.668.412.227.202.432.427.615.668-.453.328-.762.337-.949.332-.455
 0-.899-.142-1.27-.406a2.404 2.404 0 0
 1-.869-1.086c.575-.197.792-.131.801-.146z" />
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