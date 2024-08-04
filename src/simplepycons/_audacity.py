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


class AudacityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "audacity"

    @property
    def original_file_name(self) -> "str":
        return "audacity.svg"

    @property
    def title(self) -> "str":
        return "Audacity"

    @property
    def primary_color(self) -> "str":
        return "#0000CC"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Audacity</title>
     <path d="M12 2.145c-2.487 0-4.755.776-6.428 2.08-1.673 1.303-2.76
 3.169-2.76 5.244v.75C1.153 11.06 0 13.268 0 15.856c0 3.312 1.884 6
 4.312 6V9.468c0-1.554.805-2.984 2.186-4.06C7.879 4.331 9.829 3.643 12
 3.643c2.17 0 4.12.688 5.502 1.764 1.38 1.077 2.186 2.507 2.186
 4.06v12.387c2.428 0 4.312-2.687 4.312-6
 0-2.587-1.152-4.795-2.813-5.636v-.75c0-2.075-1.086-3.94-2.76-5.244-1.672-1.304-3.94-2.08-6.427-2.08zm0
 6.153l-1.125 8.683L9.75 9.105l-.562 6.75-.376-.75-.375-4.5-.187
 4.5-.563 1.313-.374-4.5-.376
 3.562-.562-.937v2.625l-.563-2.11v-4.64a1.432 1.432 0 0
 0-.937-.375v11.812c.375 0 .75-.187.937-.562v-3.375l.188.187.563
 1.875.187-2.25.563 2.813v-3.562l.374.937.563
 2.625v-3.562l.375.374.563 3.188.562-4.313 1.24
 4.86.072-2.985.375-1.124.376 4.687 1.124-4.687.375
 3.937.938-4.125.938 4.5.187-3.375.562-1.125.188 4.313.938-4.125.562
 1.875.188-1.688.374.75v3.375c.188.375.563.562.938.562V10.043c-.375
 0-.75.188-.938.375v4.813l-.374 1-.188-3.188-.375
 2.437-.375-.75-.188-2.625-.937 3.563-.188-.75L15 9.293l-.562
 4.875-.376 1.5-.75-5.062-.75 4.312-.375 1.125Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/audacity/audacity/blob/c81'''

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
