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


class PlexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "plex"

    @property
    def original_file_name(self) -> "str":
        return "plex.svg"

    @property
    def title(self) -> "str":
        return "Plex"

    @property
    def primary_color(self) -> "str":
        return "#EBAF00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Plex</title>
     <path d="M3.987 8.409c-.96
 0-1.587.28-2.12.933v-.72H0v8.88s.038.018.127.037c.138.03.821.187
 1.331-.249.441-.377.542-.814.542-1.318v-1.283c.533.573 1.147.813 2
 .813 1.84 0 3.253-1.493 3.253-3.48
 0-2.12-1.36-3.613-3.266-3.613Zm16.748 5.595.406.591c.391.614.894.906
 1.492.908.621-.012 1.064-.562 1.226-.755 0
 0-.307-.27-.686-.72-.517-.614-1.214-1.755-1.24-1.803l-1.198
 1.779Zm-3.205-1.955c0-2.08-1.52-3.64-3.52-3.64s-3.467 1.587-3.467
 3.573a3.48 3.48 0 0 0 3.507 3.52c1.413 0 2.626-.84
 3.253-2.293h-2.04l-.093.093c-.427.4-.72.533-1.227.533-.787
 0-1.373-.506-1.453-1.266h4.986c.04-.214.054-.307.054-.52Zm-7.671-.219c0
 .769.11 1.701.868 2.722l.056.069c-.306.526-.742.88-1.248.88-.399
 0-.814-.211-1.138-.579a2.177 2.177 0 0 1-.538-1.441V6.409H9.86l-.001
 5.421Zm9.283 3.46h-2.39l2.247-3.332-2.247-3.335h2.39l2.248
 3.335-2.248 3.332Zm1.593-1.286Zm-17.162-.342c-.933
 0-1.68-.773-1.68-1.72s.76-1.666 1.68-1.666c.92 0 1.68.733 1.68 1.68 0
 .946-.733 1.706-1.68 1.706Zm18.361-1.974L24 8.622h-2.391l-.87 1.293
 1.195 1.773Zm-9.404-.466c.16-.706.72-1.133 1.493-1.133.773 0
 1.373.467 1.507 1.133h-3Z" />
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