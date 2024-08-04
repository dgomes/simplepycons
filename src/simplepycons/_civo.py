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


class CivoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "civo"

    @property
    def original_file_name(self) -> "str":
        return "civo.svg"

    @property
    def title(self) -> "str":
        return "Civo"

    @property
    def primary_color(self) -> "str":
        return "#239DFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Civo</title>
     <path d="M9.229 7.985h-.993c-.183 0-.303.14-.303.318v7.393c0
 .177.12.318.303.318h.993a.318.318 0 0 0 .323-.318V8.303a.317.317 0 0
 0-.323-.318m-3.1 5.838a.32.32 0 0 0-.507-.104 2.34 2.34 0 0
 1-1.604.635c-1.627 0-2.868-1.65-2.141-3.368a2.128 2.128 0 0 1
 1.13-1.128c.992-.42 1.958-.18 2.599.408a.32.32 0 0 0
 .507-.103l.43-.943a.353.353 0 0 0-.111-.428C5.425 8.03 4.05 7.732
 2.617 8.22a3.838 3.838 0 0 0-2.412 2.478c-.874 2.772 1.172 5.32 3.813
 5.32.92 0 1.764-.31 2.44-.831a.348.348 0 0 0
 .101-.42zm17.666-3.125a3.838 3.838 0 0 0-2.412-2.478 4.176 4.176 0 0
 0-2.329-.13c-1.2.269-2.07.838-2.834 2.479l-1.534
 3.326-2.603-5.722a.32.32 0 0 0-.29-.187l-1.138-.002a.32.32 0 0
 0-.292.453l3.376 7.382a.324.324 0 0 0 .291.19l.056.005h1.276a.236.236
 0 0 0 .076-.013.335.335 0 0 0 .2-.18l1.71-3.893c.515-1.213.827-1.718
 1.643-2.065a2.527 2.527 0 0 1 2.054.026c.492.222.878.629 1.084
 1.128a2.701 2.701 0 0 1 .206.95 2.354 2.354 0 0 1-2.353 2.387 2.34
 2.34 0 0 1-1.604-.635.32.32 0 0 0-.507.104l-.43.944a.348.348 0 0 0
 .1.42c.677.52 1.522.831 2.44.831 2.642 0 4.688-2.548 3.814-5.32" />
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