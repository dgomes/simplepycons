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


class SimpleloginIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "simplelogin"

    @property
    def original_file_name(self) -> "str":
        return "simplelogin.svg"

    @property
    def title(self) -> "str":
        return "SimpleLogin"

    @property
    def primary_color(self) -> "str":
        return "#EA319F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SimpleLogin</title>
     <path d="M23.451
 3.672c.106.105.199.222.277.348.178.293.272.628.272.97v9.604c0
 .342-.095.679-.274.971a1.899 1.899 0 0
 1-.383.444c-.335.286-.76.443-1.201.443H11.727a9.773 9.773 0 0 1-5.2
 4.365l-.136.049-.135-.052a9.741 9.741 0 0 1-4.499-3.526A9.702 9.702 0
 0 1 0 11.701a9.794 9.794 0 0 1
 .227-2.1l.052-.237.236-.058c.055-.013.109-.028.162-.042a11.979 11.979
 0 0 0
 5.568-3.262l.04-.043.232-.239v-.73c0-.343.095-.68.274-.972.078-.126.171-.242.278-.346a1.835
 1.835 0 0 1 1.193-.537h13.994a1.84 1.84 0 0 1
 1.195.537Zm-15.075.346c-.033 0-.066.001-.098.004h-.142l.023.021 6.815
 6.029a.435.435 0 0 0 .576 0l6.815-6.029.023-.021h-.146a1.042 1.042 0
 0 0-.098-.004H8.376Zm-.898.605a.945.945 0 0 0-.072.367v1.586a11.997
 11.997 0 0 0 4.938 2.681l.114.029.057.015.237.058.051.239a8.49 8.49 0
 0 1 .1.565l.417-.369-5.842-5.171ZM2.329 16.719a9.049 9.049 0 0 0
 4.074 3.312 8.997 8.997 0 0 0 5.68-10.036 12.736 12.736 0 0
 1-5.555-3.169 12.751 12.751 0 0 1-5.583 3.177 9.044 9.044 0 0 0-.161
 1.698 9.038 9.038 0 0 0 1.545 5.018Zm10.684-5.098a9.709 9.709 0 0
 1-.837 3.944h10.212l-.028-.025-5.826-5.153-.985.87a.43.43 0 0 1-.575
 0l-.985-.87-.984.87c.005.122.008.242.008.364Zm10.029 3.339a.94.94 0 0
 0 .072-.366l.001-9.603a.967.967 0 0 0-.071-.364l-5.84 5.168 5.838
 5.165ZM6.609 8.206a10.24 10.24 0 0 0 4.379 2.464c.074.404.113.813.118
 1.223v.082a7.233 7.233 0 0 1-1.705 4.655l-.007.008a7.234 7.234 0 0
 1-2.97 2.095 7.259 7.259 0 0
 1-4.515-6.692c0-.458.043-.915.129-1.365a10.252 10.252 0 0 0
 4.486-2.551l.084.081h.001Zm-3.177 5.053 2.752
 2.752h.001l3.831-3.831-.847-.846-2.983 2.984-1.908-1.907-.846.848Z"
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
