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


class MongodbIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mongodb"

    @property
    def original_file_name(self) -> "str":
        return "mongodb.svg"

    @property
    def title(self) -> "str":
        return "MongoDB"

    @property
    def primary_color(self) -> "str":
        return "#47A248"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MongoDB</title>
     <path d="M17.193
 9.555c-1.264-5.58-4.252-7.414-4.573-8.115-.28-.394-.53-.954-.735-1.44-.036.495-.055.685-.523
 1.184-.723.566-4.438 3.682-4.74 10.02-.282 5.912 4.27 9.435 4.888
 9.884l.07.05A73.49 73.49 0 0111.91
 24h.481c.114-1.032.284-2.056.51-3.07.417-.296.604-.463.85-.693a11.342
 11.342 0 003.639-8.464c.01-.814-.103-1.662-.197-2.218zm-5.336
 8.195s0-8.291.275-8.29c.213 0 .49 10.695.49
 10.695-.381-.045-.765-1.76-.765-2.405z" />
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
