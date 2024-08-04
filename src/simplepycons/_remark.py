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


class RemarkIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "remark"

    @property
    def original_file_name(self) -> "str":
        return "remark.svg"

    @property
    def title(self) -> "str":
        return "remark"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>remark</title>
     <path d="M4.204 18.089V12.66q0-2.477 1.156-3.947 1.156-1.47
 3.108-1.47.494 0
 1.03.092.54.088.953.245V5.976q-.279-.122-.754-.195-.478-.073-1.007-.073-1.76
 0-2.902.88-1.144.881-1.458
 2.497h-.157V6.01H0v1.186h2.737V18.09Zm-3.959 0H8.04v-1.187H.245ZM19.1
 7.109q1.604 0 2.507 1.095.904 1.091.904
 3.02H15.6q0-1.94.93-3.027.93-1.088 2.569-1.088zm4.846
 7.998h-1.458q-.28.884-1.133 1.378-.854.494-2.087.494-1.68
 0-2.676-1.114-.991-1.118-.991-3.013v-.414H24v-.953q0-1.807-.578-3.074-.574-1.267-1.67-1.933-1.094-.67-2.652-.67-1.493
 0-2.615.658-1.118.655-1.738 1.838-.617 1.183-.617 2.775v1.761q0 2.58
 1.352 4.016 1.351 1.436 3.786 1.436 1.221 0 2.205-.394.98-.39
 1.627-1.11.643-.717.846-1.681z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/remarkjs/remark/blob/26dc5'''

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