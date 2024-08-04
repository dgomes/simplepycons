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


class YamahaMotorCorporationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "yamahamotorcorporation"

    @property
    def original_file_name(self) -> "str":
        return "yamahamotorcorporation.svg"

    @property
    def title(self) -> "str":
        return "Yamaha Motor Corporation"

    @property
    def primary_color(self) -> "str":
        return "#E60012"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Yamaha Motor Corporation</title>
     <path d="M12 0A12 12 0 000 12a12 12 0 0012 12 12 12 0 0012-12A12
 12 0 0012 0zm0 .57C18.315.57 23.43 5.685 23.43 12c0 6.31-5.115
 11.43-11.43 11.43C5.69 23.43.57 18.314.57 12 .57 5.69 5.69.57 12
 .57zm0 .234c-.1 0-.183.06-.218.147l-.492 1.551A9.523 9.523 0 002.475
 12c0 1.48.337 2.885.94 4.136l-1.1 1.206a.241.241 0
 00-.015.262.246.246 0 00.238.115l1.592-.353a9.52 9.52 0 007.87
 4.16c3.27 0 6.16-1.652 7.874-4.16l1.592.353a.236.236 0
 00.23-.123.234.234 0 00-.016-.262l-1.1-1.198A9.431 9.431 0 0021.526
 12a9.523 9.523 0 00-8.815-9.498L12.218.947A.237.237 0 0012
 .804zm-.003.25c.024 0 .048.02.056.043l1.02 3.354a1.2 1.2 0
 00-.48.957c0 .389.19.734.48.952h-.004c.436.326.718.846.718
 1.429v1.12l4.326-2.497.476.825-4.802 2.77v.965l.834.48
 4.802-2.774.476.825-4.326 2.5.972.56c.508.294.818.798.882
 1.338v-.004a1.193 1.193 0 001.655.953l2.393
 2.56c.02.02.02.047.008.07-.016.025-.04.033-.068.029l-3.413-.794a1.193
 1.193 0
 00-1.65-.957l.003-.004c-.5.215-1.091.199-1.6-.095l-.968-.56v4.994h-.952v-5.545l-.834-.48-.833.48v5.545h-.953V15.1l-.972.555c-.508.294-1.1.31-1.6.096l.004.004a1.193
 1.193 0 00-1.651.957l-3.413.793a.054.054 0
 01-.063-.028c-.016-.02-.012-.047.008-.067l2.397-2.56c.333.143.73.135
 1.067-.064.338-.194.544-.528.588-.889v.004c.063-.54.373-1.044.88-1.337l.97-.56-4.327-2.496.477-.826
 4.802 2.774.833-.484v-.964l-4.802-2.77.476-.826 4.326
 2.496V7.79c0-.583.282-1.103.719-1.429h-.004c.29-.214.476-.56.476-.952
 0-.393-.19-.738-.48-.957l1.02-3.353c.008-.028.031-.044.051-.044zm.004
 5.902a.833.833 0 00-.833.833v1.67L12 9.94l.833-.48V7.789a.833.833 0
 00-.833-.833zm0 4.084l-.833.48v.964l.833.476.833-.48v-.96zm-2.62
 1.516l-1.444.833a.833.833 0 00-.306 1.14.822.822 0 00.723.412.83.83 0
 00.416-.111l1.445-.834v-.96zm5.243 0l-.833.48V14l1.445.834a.834.834 0
 00.833-1.445z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Yamah'''

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
