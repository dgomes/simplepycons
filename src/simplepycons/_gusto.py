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


class GustoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gusto"

    @property
    def original_file_name(self) -> "str":
        return "gusto.svg"

    @property
    def title(self) -> "str":
        return "Gusto"

    @property
    def primary_color(self) -> "str":
        return "#F45D48"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Gusto</title>
     <path d="M21.311 8.768c-1.482 0-2.69 1.212-2.69 2.702s1.208 2.701
 2.69 2.701c1.483 0 2.689-1.212
 2.689-2.701s-1.206-2.702-2.689-2.702Zm0 4.123a1.42 1.42 0 0
 1-1.415-1.421 1.42 1.42 0 0 1 1.415-1.422c.78 0 1.415.638 1.415
 1.422s-.635 1.42-1.415
 1.42Zm-7.919-1.969-.47-.235c-.204-.102-.332-.18-.384-.239a.283.283 0
 0 1-.078-.19c0-.091.04-.168.122-.228.08-.063.193-.091.338-.091.264 0
 .556.16.878.48l.794-.797a2.09 2.09 0 0 0-.744-.63 2.06 2.06 0 0
 0-.937-.22c-.484 0-.884.143-1.196.431a1.367 1.367 0 0 0-.468 1.04c0
 .63.412 1.154 1.24 1.57l.433.218c.373.189.559.381.559.58 0
 .108-.052.201-.155.284a.63.63 0 0 1-.409.122c-.156
 0-.336-.054-.538-.163a1.81 1.81 0 0 1-.528-.427l-.79.864c.446.584
 1.04.878 1.786.878.561 0 1.009-.153
 1.34-.458.335-.304.502-.685.502-1.141
 0-.342-.093-.642-.277-.897-.185-.255-.525-.504-1.018-.75Zm-7.985
 2.66V8.876H4.131v.316a2.662 2.662 0 0 0-1.442-.423C1.206 8.768 0 9.98
 0 11.47s1.206 2.701 2.689 2.701c.505 0 1-.142
 1.427-.412l-.002.104a1.42 1.42 0 0 1-1.415 1.42c-.265
 0-.524-.075-.748-.217l-.631 1.11c.416.255.894.39 1.382.39a2.713 2.713
 0 0 0 2.705-2.702c0-.057.004-.227 0-.281ZM2.69 12.89a1.42 1.42 0 0
 1-1.415-1.42c0-.784.636-1.422 1.415-1.422s1.415.638 1.415 1.422a1.42
 1.42 0 0 1-1.415 1.42Zm7.803-4.016H9.21v2.568c.002.365.002.995-.265
 1.264-.128.128-.269.245-.563.245a.707.707 0 0
 1-.565-.245c-.269-.27-.266-.901-.265-1.264V8.874H6.27v2.56c-.004.528-.01
 1.509.633 2.16.377.38.827.575 1.476.575.65 0 1.1-.193
 1.477-.576.643-.65.637-1.633.633-2.159l.004-2.56Zm7.27
 3.787c-.104.078-.353.253-.636.213-.23-.03-.418-.2-.447-.768v-2.13h1.507V8.87H16.68V7.434H15.4v.281h-.002v4.223c0
 .671.17 2.231 1.726 2.231.788-.012 1.266-.441
 1.467-.609l.026-.02-.767-.95a4.174 4.174 0 0 1-.089.07Z" />
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
