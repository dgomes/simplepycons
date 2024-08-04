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


class SageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sage"

    @property
    def original_file_name(self) -> "str":
        return "sage.svg"

    @property
    def title(self) -> "str":
        return "Sage"

    @property
    def primary_color(self) -> "str":
        return "#00D639"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sage</title>
     <path d="M2.702 5.316C1.167 5.316 0 6.48 0 7.972c0 1.635 1.167
 2.267 2.46 2.655 1.224.387 1.804.818 1.804 1.666 0 .86-.64
 1.465-1.477 1.465-.84 0-1.566-.604-1.566-1.535
 0-.516.242-.647.242-.934 0-.33-.227-.574-.599-.574-.423
 0-.864.647-.864 1.566 0 1.48 1.266 2.57 2.787 2.57 1.535 0
 2.701-1.163 2.701-2.656
 0-1.623-1.166-2.267-2.472-2.655-1.209-.372-1.792-.818-1.792-1.666
 0-.845.626-1.45 1.463-1.45.867 0 1.565.617 1.577
 1.465.016.388.285.617.599.617a.592.592 0 0 0
 .61-.647c-.027-1.48-1.263-2.543-2.771-2.543zm6.171 9.52c.683 0
 1.21-.23 1.21-.69a.57.57 0 0 0-.557-.574c-.2 0-.341.085-.668.085-.882
 0-1.577-.76-1.577-1.65 0-.962.71-1.725 1.608-1.725 1.009 0 1.65.775
 1.65 1.895v2.054c0 .36.284.604.625.604.327 0
 .61-.244.61-.604v-2.097c0-1.72-1.178-2.984-2.858-2.984-1.566 0-2.86
 1.22-2.86 2.856 0 1.58 1.282 2.83 2.817 2.83zm6.257 3.848c1.535 0
 2.701-1.163 2.701-2.656
 0-1.635-1.166-2.267-2.472-2.655-1.209-.387-1.792-.818-1.792-1.666s.64-1.465
 1.463-1.465c.84 0 1.577.604 1.577 1.535 0 .519-.241.647-.241.934 0
 .33.226.574.583.574.441 0 .882-.647.882-1.566
 0-1.48-1.278-2.57-2.801-2.57-1.535 0-2.687 1.163-2.687 2.656 0 1.623
 1.152 2.267 2.46 2.655 1.224.372 1.804.818 1.804 1.666 0 .86-.64
 1.45-1.462 1.45-.883
 0-1.566-.601-1.578-1.465-.015-.388-.3-.604-.598-.604-.327
 0-.626.216-.61.631.011 1.499 1.247 2.546 2.77 2.546zm6.171-3.849c.795
 0 1.424-.229 1.862-.503.426-.272.595-.504.595-.76
 0-.272-.2-.516-.568-.516-.441 0-.795.66-1.877.66-.952
 0-1.707-.76-1.707-1.722 0-.95.725-1.724 1.635-1.724.982 0 1.508.647
 1.508 1.062 0 .116-.085.174-.2.174h-1.194c-.326 0-.568.216-.568.503 0
 .314.242.546.568.546h1.636c.625 0 1.009-.33 1.009-.89
 0-1.408-1.194-2.512-2.774-2.512-1.566 0-2.83 1.263-2.83 2.84s1.312
 2.842 2.905 2.842z" />
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
