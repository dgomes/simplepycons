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


class LootCrateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lootcrate"

    @property
    def original_file_name(self) -> "str":
        return "lootcrate.svg"

    @property
    def title(self) -> "str":
        return "Loot Crate"

    @property
    def primary_color(self) -> "str":
        return "#1E1E1E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Loot Crate</title>
     <path d="M19.895 11.048a.116.116 0 0 0 .031.201c1.621.579
 2.393.66 2.393 2.081v4.011c0 .716-.051.88-.531 1.254-.877.683-6.185
 4.747-6.392 4.913-.774.62-1.169.556-2.054.339a515.44 515.44 0 0
 1-9.945-2.577c-1.746-.47-1.701-2.064-1.701-3.203
 0-3.945-.015-7.468-.015-11.202 0-1.186.049-1.222.95-1.881.83-.607
 4.296-3.135 6.153-4.499.553-.406.828-.607 1.618-.406 1.616.41 6.664
 1.649 9.382 2.339 2.083.529 2.535.893 2.535 2.326V8.38c0
 .465-.007.638-.408.981-.202.173-1.348 1.14-2.016
 1.687Zm1.624-2.556a.113.113 0 0 0
 .141-.112c.001-1.414.011-2.495.011-3.666
 0-.622-.35-1.137-1.121-1.343C16.501 2.29 10.486.866
 10.191.778c-.197-.059-.322.108-.322.199-.001 4.294.029 7.832.029
 11.854 0 .741.408 1.525 1.292 1.765 3.582.973 6.578 1.655 10.331
 2.667a.115.115 0 0 0 .143-.112c.001-.848.014-1.405.014-1.95
 0-2.27.279-2.679-1.57-3.194-2.198-.612-5.306-1.378-5.554-1.441-.485-.124-.548-.266-.548-.591
 0-.122-.011-2.346-.003-2.869.002-.157.006-.31.157-.397.134-.077.264-.046.664.053.448.111
 4.598 1.186 6.695 1.73Zm-7.65 14.735a.114.114 0 0 0
 .142-.111c.001-1.185.017-2.484.017-3.352
 0-1.475.182-1.334-1.064-1.639-1.474-.36-4.433-1.146-5.967-1.552-.355-.094-.459-.424-.459-.998
 0-1.726-.006-4.575-.006-6.577
 0-1.834.193-1.599-.703-1.832-.565-.146-2.468-.637-3.313-.828-.144-.032-.225.085-.225.224-.003
 3.939.053 8.211.053 11.994 0 1.228.439 1.815 1.321 2.051 3.589.963
 6.446 1.652 10.204 2.62Z" />
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
