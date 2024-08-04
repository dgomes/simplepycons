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


class QuantcastIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "quantcast"

    @property
    def original_file_name(self) -> "str":
        return "quantcast.svg"

    @property
    def title(self) -> "str":
        return "Quantcast"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Quantcast</title>
     <path d="M11.548 10.96c-.306
 0-.579.102-.806.43h-.011v-.353H10v2.724h.763v-1.548c0-.37.191-.634.497-.634.24
 0
 .408.132.408.525v1.66h.763v-1.851c0-.528-.227-.952-.884-.952zm-1.952
 2.8v-1.917c0-.627-.562-.88-1.236-.88-.954
 0-1.25.537-1.277.956h.73c.017-.245.202-.402.514-.402.334 0
 .536.16.536.483v.126l-.705.043c-1.064.064-1.16.544-1.16.836 0
 .621.526.832.955.832.318 0 .68-.096.933-.43h.01v.354zm-.73-.937c0
 .328-.388.46-.626.46-.256 0-.478-.073-.478-.317
 0-.197.118-.303.466-.334l.635-.06Zm11.831-1.065c0-.165.203-.244.402-.244.292
 0 .455.138.466.365l.764-.017c-.042-.592-.503-.901-1.202-.901-.806
 0-1.129.455-1.129.873 0 1.124 1.632.71 1.632 1.166 0
 .222-.256.28-.45.28-.227 0-.46-.106-.471-.37h-.764c.064.806.825.921
 1.207.921 1.124 0 1.242-.7 1.242-.913
 0-1.098-1.697-.674-1.697-1.16zm-.983
 2.003v-1.918c0-.627-.561-.88-1.235-.88-.955
 0-1.25.537-1.278.956h.73c.017-.245.202-.402.514-.402.334 0
 .537.16.537.483v.126l-.705.042c-1.065.065-1.16.545-1.16.837 0
 .621.525.832.955.832.317 0 .68-.096.932-.43h.011v.354zm-.73-.938c0
 .328-.387.46-.626.46-.255 0-.477-.073-.477-.317
 0-.197.118-.303.466-.334l.635-.06v.25zm-2.769-.02c-.047.25-.196.416-.477.416-.399
 0-.525-.402-.525-.764 0-.351.059-.848.53-.848.197 0
 .413.084.439.44h.744l.05-.002c-.036-.579-.424-1.087-1.235-1.087-.826
 0-1.326.59-1.326 1.463 0 .837.45 1.41 1.343 1.41.73 0 1.092-.432
 1.207-1.03zm-3.201-1.755v-.795h.772v.795h.407v.59h-.407v1.393c0
 .123.053.182.253.182a.617.617 0 0 0
 .154-.017v.607c-.123.017-.247.03-.37.03-.503
 0-.81-.123-.81-.718v-1.48h-.353v-.587zm9.807
 0v-.795h.772v.795H24v.59h-.407v1.393c0 .123.053.182.253.182a.617.617
 0 0 0 .154-.017v.607a2.75 2.75 0 0 1-.37.03c-.503
 0-.81-.123-.81-.718v-1.48h-.353v-.587ZM5.94 12.584c0
 .37-.191.635-.497.635-.24 0-.408-.132-.408-.525v-1.66h-.764v1.85c0
 .526.298.95.955.95.306 0
 .509-.101.736-.43h.011v.354h.73v-2.724H5.94Zm-3.27
 1.163.25.43h.89l-.47-.815c.426-.388.648-.958.648-1.525
 0-1-.685-2.013-1.994-2.013S0 10.837 0 11.837s.685 2.014 1.994
 2.014c.244 0 .472-.037.677-.104zm-1.808-1.91c0-.649.348-1.303
 1.126-1.303.778 0 1.126.654 1.126 1.303 0
 .28-.064.565-.202.792h-.89l.272.472a1.17 1.17 0 0 1-.306.04c-.778
 0-1.126-.655-1.126-1.304z" />
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
