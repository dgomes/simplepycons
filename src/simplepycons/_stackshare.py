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


class StackshareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stackshare"

    @property
    def original_file_name(self) -> "str":
        return "stackshare.svg"

    @property
    def title(self) -> "str":
        return "StackShare"

    @property
    def primary_color(self) -> "str":
        return "#0690FA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>StackShare</title>
     <path d="M17.209 6.697c-.035-.274 0-.594
 0-.594v-.01c.141-.714.771-1.254 1.525-1.254.005 0
 .009.001.014.001h.002c.859 0 1.557.698 1.557 1.556s-.697 1.556-1.557
 1.556c-.003
 0-.006-.001-.009-.001h-.007c-.742-.001-1.38-.526-1.525-1.254zM24
 1.54v20.92c0 .851-.646 1.54-1.443 1.54H1.444C.647 24 0 23.311 0
 22.46V1.54C0 .69.647 0 1.444 0h21.113C23.354 0 24 .69 24 1.54zm-2.303
 16.007c0-1.636-1.326-2.962-2.961-2.962-1.317 0-2.477.87-2.844
 2.134h-1.758l-2.74-4.717-.002-.004.002-.004 2.736-4.709h1.748c.457
 1.571 2.102 2.474 3.673 2.017 1.571-.457 2.475-2.102
 2.017-3.673-.457-1.571-2.102-2.474-3.672-2.017a2.9638 2.9638 0 0
 0-2.018 2.017h-2.665l-.026-.016-3.227
 5.552-.025.042H8.018c-.457-1.571-2.102-2.474-3.673-2.016-1.571.458-2.474
 2.102-2.017 3.673.458 1.571 2.103 2.474 3.673 2.017.973-.283
 1.733-1.045 2.017-2.017h1.961l3.208 5.52.015-.009h2.69a2.9592 2.9592
 0 0 0 2.842 2.134h.002c1.636 0 2.961-1.326
 2.961-2.962zm-2.933-1.619c-.743.002-1.381.526-1.527
 1.254-.004.029-.004.057-.007.085-.004.017-.015.029-.018.046-.041.301
 0 .602 0 .602.173.842.995 1.383 1.837 1.209.573-.118 1.005-.548
 1.164-1.088.065-.172.105-.356.105-.551
 0-.859-.697-1.557-1.554-1.557zM5.2 10.417c-.858 0-1.556.698-1.556
 1.557 0 .006.002.012.002.018 0 .003-.001.005-.001.008.001.854.693
 1.547 1.548 1.548.541-.001 1.015-.278
 1.292-.698.171-.249.272-.551.272-.875 0-.86-.698-1.558-1.557-1.558z"
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
