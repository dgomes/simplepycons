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


class MicrogeneticsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "microgenetics"

    @property
    def original_file_name(self) -> "str":
        return "microgenetics.svg"

    @property
    def title(self) -> "str":
        return "Microgenetics"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Microgenetics</title>
     <path d="M12.008 6c2.595 0 4.31 1.263 5.583
 2.726l.248.293c.082.101.164.2.242.3.434.569.809 1.146 1.17
 1.674.24.356.465.693.689 1.008l.227.32c.074.105.148.211.24.31.928
 1.171 1.889 1.9 3.283
 1.991.195-.845.301-1.721.301-2.621s-.105-1.776-.301-2.621c-1.395.091-2.355.819-3.301
 1.991-.18-.246-.357-.51-.555-.796-.375-.566-.809-1.208-1.32-1.845
 1.006-1.169 2.25-2.175 3.932-2.557C20.453 2.49 16.523 0 12.008 0c-4.5
 0-8.44 2.49-10.49 6.173 1.681.384 2.923 1.388 3.931
 2.556.086.09.168.18.249.285l.237.3c.479.615.914 1.245 1.305
 1.845l.555.826.24.329c.074.104.165.21.239.315 1.051 1.439 2.115 2.43
 3.75 2.43 1.65 0 2.701-.99 3.765-2.43l.375.555c.451.66.932 1.38 1.455
 2.055-1.273 1.471-3 2.73-5.595 2.73-2.594
 0-4.304-1.275-5.579-2.73l-.24-.3-.24-.3c-.435-.57-.81-1.154-1.17-1.68-.239-.36-.465-.69-.689-1.006l-.226-.33c-.074-.104-.149-.21-.24-.314C2.664
 10.2 1.703 9.465.309 9.375c-.195.849-.3 1.725-.3 2.625s.102 1.776.29
 2.621c1.398-.091 2.355-.819
 3.295-1.991.172.246.354.51.544.796.375.566.806 1.208 1.313
 1.845-1.009 1.169-2.253 2.175-3.93 2.557C3.566 21.51 7.494 24 12.008
 24c4.515 0 8.441-2.49
 10.49-6.173-1.68-.384-2.922-1.388-3.93-2.556-.086-.09-.17-.18-.25-.285l-.236-.3c-.48-.615-.916-1.245-1.305-1.845L16.223
 12c-.074-.111-.154-.225-.23-.33-.078-.111-.154-.219-.232-.325-1.051-1.44-2.1-2.431-3.75-2.431s-2.699.99-3.75
 2.431l-.375-.56c-.436-.669-.916-1.38-1.456-2.059C7.703 7.263 9.383 6
 12.008 6" />
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
