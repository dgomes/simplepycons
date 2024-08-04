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


class OpentextIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opentext"

    @property
    def original_file_name(self) -> "str":
        return "opentext.svg"

    @property
    def title(self) -> "str":
        return "OpenText"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenText</title>
     <path d="M3.412 11.809c0 .786-.468 1.637-1.7 1.637-.894
 0-1.712-.49-1.712-1.637 0-.946.616-1.68 1.828-1.616 1.297.074 1.584
 1.052 1.584 1.616zm-2.307-.596c-.117.17-.159.383-.159.596 0
 .478.244.914.765.914.51 0 .755-.404.755-.872
 0-.34-.085-.595-.266-.754a.727.727 0 0
 0-.553-.17c-.255.01-.414.095-.542.286zm10.63-.67c.095-.095.148-.17.318-.244.149-.063.35-.106.585-.106.191
 0
 .404.032.563.117.33.17.425.446.425.935v2.126h-.946v-1.754c0-.276-.01-.382-.042-.467-.075-.17-.234-.234-.425-.234-.49
 0-.49.382-.49.776v1.68h-.935v-3.105h.946v.277zm-1.393
 2.02c-.085.181-.361.883-1.584.883-.946 0-1.605-.564-1.605-1.584
 0-.744.383-1.669 1.637-1.669.191 0 .733-.021 1.148.404.415.436.436
 1.042.446 1.392H8.1c0
 .383.223.776.734.776s.69-.33.807-.542l.702.34zm-.935-1.148c-.022-.127-.043-.308-.181-.435a.66.66
 0 0 0-.457-.17.67.67 0 0
 0-.478.202c-.128.138-.16.276-.192.414l1.308-.01zm13.977-.5H24v-.637h-.616V9.62h-.936v.648H22.3l-.425.638h.574v1.478c0
 .297.01.52.138.701.202.287.553.308.883.308.17 0
 .297-.02.488-.053v-.712l-.329.01c-.255
 0-.255-.159-.244-.35v-1.371zM14.073
 9.62h.935v.648h.967l-.425.638h-.553v1.382c-.01.191-.01.35.245.35l.33-.01v.712c-.203.032-.32.053-.49.053-.318
 0-.68-.02-.882-.308-.127-.18-.138-.404-.138-.701V9.619h.01zm4.836
 2.944-.18.266c-.171.234-.48.606-1.383.606-.946
 0-1.573-.563-1.573-1.584 0-.744.383-1.669 1.637-1.669.191 0 .733-.02
 1.148.404.415.436.436 1.042.446
 1.393H16.73c-.01.382.191.776.69.776.51 0
 .66-.33.777-.542l.712.35zm-.872-1.148c-.021-.127-.042-.308-.18-.435a.66.66
 0 0 0-.458-.17.67.67 0 0
 0-.478.202c-.127.138-.16.276-.191.414l1.307-.01zm4.071
 1.956-1.17-1.626.968-1.467h-1.063l-.457.691-.5-.69h-1.062l1.052
 1.466-1.084
 1.626h1.063l.563-.86.617.86h1.073zm-17.41-2.827c.085-.138.372-.35.829-.35.776
 0 1.329.573 1.329 1.604 0 .638-.234 1.637-1.372 1.637-.403
 0-.722-.223-.797-.35v1.296h-.935v-4.114h.946v.277zm.638.361c-.17
 0-.351.064-.479.234-.138.16-.19.404-.19.68 0
 .362.105.585.222.712a.588.588 0 0 0 .425.192c.457 0 .66-.468.66-.925
 0-.383-.117-.786-.5-.872-.053-.01-.096-.02-.138-.02z" />
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
        yield from [
            "Micro Focus",
        ]
