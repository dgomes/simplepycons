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


class ShopwareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shopware"

    @property
    def original_file_name(self) -> "str":
        return "shopware.svg"

    @property
    def title(self) -> "str":
        return "Shopware"

    @property
    def primary_color(self) -> "str":
        return "#189EFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shopware</title>
     <path d="M23.9477 10.8913a.1735.1735 0
 00-.061-.1178c-2.5032-2.078-4.5288-2.9261-6.9905-2.9261-1.3127
 0-2.32.2638-2.9916.7827-.5822.4492-.8896 1.0772-.8896 1.812 0 2.0605
 2.5184 3.0003 5.4358 4.0883 1.5023.5604 3.057 1.1404 4.483
 1.9319a.1626.1626 0 00.0828.0218.187.187 0
 00.0589-.011c.0458-.0174.085-.0523.1025-.1002.545-1.3955.822-2.8673.822-4.374a13.082
 13.082 0 00-.0523-1.1076zm-4.81
 10.4791c-1.0423-.785-2.5795-1.3824-4.2061-2.0125-1.9362-.7501-4.132-1.6027-5.7803-2.913-1.8665-1.4871-2.7757-3.3623-2.7757-5.7324
 0-2.1281.883-3.9466 2.5533-5.2614 1.873-1.474 4.7119-2.2546
 8.2071-2.2546.966 0 1.8883.0589 2.743.1766a.1696.1696 0
 00.1788-.098.17.17 0 00-.0414-.2007C17.814 1.0924 14.9664.0022
 12.001.0022c-3.2052 0-6.2186 1.2472-8.4862 3.5148C1.2494 5.7825 0
 8.796 0 11.999c0 3.2051 1.2472 6.2185 3.5149 8.484 2.2654 2.2654
 5.2788 3.5148 8.4862 3.5148 2.5903 0 5.0564-.8133
 7.1344-2.3505a.1714.1714 0 00.0697-.1374.1735.1735 0 00-.0676-.1395Z"
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
        return '''https://www.shopware.com/en/press/press-mater'''

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
