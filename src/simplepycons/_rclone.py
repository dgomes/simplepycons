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


class RcloneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rclone"

    @property
    def original_file_name(self) -> "str":
        return "rclone.svg"

    @property
    def title(self) -> "str":
        return "Rclone"

    @property
    def primary_color(self) -> "str":
        return "#3F79AD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rclone</title>
     <path d="M11.842.6258C9.3647.6813 6.9754 1.9906 5.646
 4.2933c-.7593 1.3144-1.0647 2.7662-.966 4.1745a7.99 7.99 0 0 1
 2.6568-.4541l1.4705-.0013c-.0093-.5594.1245-1.1284.4245-1.6482.8827-1.5284
 2.837-2.0522 4.3654-1.1695 1.5284.8824 2.0519 2.8366 1.1695
 4.365l-1.4782 2.5647 1.1955 2.0714 2.3914-.0004
 1.4775-2.5655c2.0262-3.5088.8239-7.9959-2.6853-10.0217C14.4614.9118
 13.1396.5967 11.842.6258m-1.5451 8.073-2.9605.0029C3.2844 8.7017 0
 11.9867 0 16.0383c0 4.052 3.2844 7.3367 7.3364 7.3367 1.5174 0
 2.9267-.4609 4.0967-1.2497a8 8 0 0
 1-1.72-2.0748l-.7368-1.273c-.4799.288-1.0392.4565-1.6395.4565-1.765
 0-3.1958-1.4307-3.1958-3.1958 0-1.7647 1.4307-3.1954
 3.1958-3.1954l2.96-.0022 1.1962-2.0708zm9.587.7475a7.99 7.99 0 0
 1-.935 2.5278l-.7344 1.2745c.4892.2717.915.6719 1.2153 1.192.8823
 1.528.3585 3.4826-1.1699
 4.365-1.528.8823-3.4828.3588-4.3651-1.1696l-1.482-2.5628h-2.3915L8.8256
 17.144l1.483 2.5626c2.0262 3.5091 6.513 4.7112 10.022 2.685
 3.5089-2.0257 4.7112-6.5125
 2.6853-10.0216-.7588-1.3144-1.863-2.3052-3.132-2.9237" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/rclone/rclone/blob/8f1c309
c8149a734ccc3a0d2ce185b936dbe783a/graphics/logo/svg/logo_symbol_color.'''

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