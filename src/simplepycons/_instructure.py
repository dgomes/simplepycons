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


class InstructureIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "instructure"

    @property
    def original_file_name(self) -> "str":
        return "instructure.svg"

    @property
    def title(self) -> "str":
        return "Instructure"

    @property
    def primary_color(self) -> "str":
        return "#2A7BA0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Instructure</title>
     <path d="m11.996 0-5.11 2.878L12 5.76l5.115-2.878ZM6.032 3.36.918
 6.237 6.036 9.12l5.115-2.879Zm11.929 0-5.112 2.878 5.115 2.882
 5.118-2.879zM12 11.52.918 17.76 12 24l11.082-6.241Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.instructure.com/canvas/resources/'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.instructure.com/about/brand-guide'''

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