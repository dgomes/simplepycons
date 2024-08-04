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


class LutrisIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lutris"

    @property
    def original_file_name(self) -> "str":
        return "lutris.svg"

    @property
    def title(self) -> "str":
        return "Lutris"

    @property
    def primary_color(self) -> "str":
        return "#FF9900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lutris</title>
     <path d="m21.231 18.89.001-.002c-1.293 3.243-5.218 5.232-9.447
 5.105C5.3 23.993 0 18.48 0 11.906S5.276.001 11.785.001c1.793 0
 3.493.406 5.015
 1.13.081-.177.271-.544.451-.557.238-.017.374.137.526.309.154.172.46.429.46.429s1.393-.481
 2.955.377c1.563.858 1.783 1.116 2.09 1.716.152.301.195.829.2
 1.282a.796.796 0 0 0-.07-.003c-.496 0-.96.455-.96 1.08 0
 .263.082.496.215.678l-.01.007a1.505 1.505 0 0 0-.132.01 18.704 18.704
 0 0 0-.389-.142 2.53 2.53 0 0 1-.82-.472 1.402 1.402 0 0
 0-1.196-2.112c-.383
 0-.73.156-.982.41-.472-.271-1.174-.482-2.527-.565l-.407-.011c-2.282.012-3.611.279-5.979
 1.301-.603.283-1.206.615-1.785 1.001-.423.3-.639.67-.709 1.137a1.326
 1.326 0 0 0 1.23 1.373h.042c1.27.06 2.039 1.99 2.063
 2.497.004.05.004.023.003.08-.032.727-.37 1.267-1.088 1.246a1.231
 1.231 0 0
 1-.976-.494c-.063-.077-.103-.172-.159-.254-.666-1.081-1.732-1.36-2.771-1.523-.438-.068-1.073-.122-1.31.25a8.28
 8.28 0 0 0-.577 3.063c-.02 5.036 4.041 9.118 9.026 9.118 2.575 0
 5.349-.952 6.993-2.7l-.035.03c-1.772 1.473-4.66 1.941-6.027
 1.941-4.302 0-7.818-3.232-7.818-7.578
 0-1.276.288-2.396.814-3.36.495.183.947.483 1.28 1.022a.24.24 0 0 0
 .013.021c.064.092.111.197.182.284.424.524.881.658
 1.342.68h.01c.43.013.768-.12
 1.024-.342.347-.3.55-.79.577-1.382v-.014c.002-.085
 0-.053-.004-.112-.024-.376-.333-1.318-.906-2.027-.266-.331-.587-.607-.95-.774l.12-.074c.756-.457
 2.364-.977 4.592-.638 1.13.173 2.055.419 3.483.879 1.657.534 2.579
 1.279 3.854 1.427.15.017.301.018.45.003.41 1.129.634 2.35.634 3.621 0
 2.068-.59 3.995-1.611
 5.62zm1.947-12.274s-.115.201-.364.322c-.103.05-.282-.075-.45.1-.359.726.516
 1.332.923
 1.315.408-.017.73-.432.712-.793-.017-.558-.82-.944-.82-.944zm.234-1.432c.255
 0 .462.26.462.58 0 .32-.207.58-.462.58-.254 0-.46-.26-.46-.58
 0-.32.206-.58.46-.58zm-3.292-.951c.492 0 .89.403.89.9a.895.895 0 0
 1-.89.898.895.895 0 0 1-.89-.899c0-.496.399-.899.89-.899z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/lutris/lutris/blob/f62feae
f063868cb39afddefbb9ba7a5928bd978/share/icons/hicolor/scalable/apps/lu'''

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