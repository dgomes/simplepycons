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


class NormalizedotcssIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "normalizedotcss"

    @property
    def original_file_name(self) -> "str":
        return "normalizedotcss.svg"

    @property
    def title(self) -> "str":
        return "Normalize.css"

    @property
    def primary_color(self) -> "str":
        return "#E3695F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Normalize.css</title>
     <path d="M8.427 6.361v5.064l-5.381.705 7.058.924v-1.915l5.469
 6.5v-5.064l5.382-.705-7.059-.924v1.914zM12 0l12 12-12 12L0 12Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/necolas/normalize.css/blob'''

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