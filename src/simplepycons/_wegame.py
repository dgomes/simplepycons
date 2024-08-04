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


class WegameIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wegame"

    @property
    def original_file_name(self) -> "str":
        return "wegame.svg"

    @property
    def title(self) -> "str":
        return "WeGame"

    @property
    def primary_color(self) -> "str":
        return "#FAAB00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WeGame</title>
     <path d="M21.458 11.005c-.024-.179-.078-.632-.165-1.08a8.082
 8.082 0 0 0-.255-1.006l-.005-.015a1.87 1.87 0 0 0-.151-.315 1.224
 1.224 0 0 0-.317-.354 1.57 1.57 0 0 0-1.412-.138 2.029 2.029 0 0
 0-.861 1.064c-.238.465-.475.93-.742 1.378a2.617 2.617 0 0 1-.572.7
 1.33 1.33 0 0
 1-.367.215c-.534.2-.91-.08-1.321-.403-.438-.342-.824-.744-1.274-1.073a1.851
 1.851 0 0 0-.983-.43c-.637-.003-1.195.619-1.544
 1.078-.195.258-.577.779-.775 1.033a3.403 3.403 0 0 1-.454.458 1.169
 1.169 0 0 1-.196.138 1.101 1.101 0 0 1-.48.136 1.566 1.566 0 0
 1-.869-.263 2.678 2.678 0 0 1-.288-.183l-.035-.027a.469.469 0 0
 0-.734.428.392.392 0 0 0 .024.136c0 .003.003.005.004.008a.395.395 0 0
 0 .093.14c.608.897 1.47 1.55 2.303 1.564a1.507 1.507 0 0 0
 .635-.124c.646-.285 1.13-.903 1.67-1.334a1.314 1.314 0 0 1 .776-.33
 1.038 1.038 0 0 1 .63.215 2.122 2.122 0 0 1 .189.144 8.916 8.916 0 0
 1 .742.753 9.93 9.93 0 0 0 .9.85 2.53 2.53 0 0 0
 1.146.56c.046.007.091.011.136.014a1.522 1.522 0 0 0 1.002-.314 4.176
 4.176 0 0 0 .745-.689 6.13 6.13 0 0 0
 .463-.664c.07-.112.143-.19.2-.308a5.769 5.769 0 0 1-.065.953 10.09
 10.09 0 0 1-.212 1.288q-.062.253-.135.503-.116.397-.262.786a1.906
 1.906 0 0 1-.072.188l-.003.007q-.088.23-.192.453a7.005 7.005 0 0
 1-12.74-.01q-.106-.225-.195-.459l-.004-.009a10.91 10.91 0 0 1
 .426-9.024 13.024 13.024 0 0 1 1.635-2.396 8.352 8.352 0 0 1
 2.132-1.946c.03-.017.057-.037.086-.055a4.168 4.168 0 0 1 4.57
 0l.086.055a11.285 11.285 0 0 1 1.795 1.588l.002.002.052.053a1.183
 1.183 0 0 0 .296.212 1.36 1.36 0 0 0 1.493-.211 1.291 1.291 0 0 0
 .137-1.672c-.041-.05-.083-.1-.121-.15a8.076 8.076 0 0
 0-.722-.763A14.069 14.069 0 0 0 15.375.9a6.85 6.85 0 0
 0-.118-.071A6.126 6.126 0 0 0 12.118 0a5.748 5.748 0 0 0-3.033.841
 3.166 3.166 0 0 0-.117.071A12.178 12.178 0 0 0 6.003 3.39a.455.455 0
 0 1-.024.025 15.477 15.477 0 0 0-3.578 9.8 16.626 16.626 0 0 0 .359
 3.444 9.487 9.487 0 0 0 18.478.017l.028-.13a.097.097 0 0 0
 .002-.012l.02-.103a15.856 15.856 0 0 0
 .286-2.235q.026-.454.026-.91a18.254 18.254 0 0 0-.142-2.28z" />
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
