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


class MailboxdotorgIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "mailboxdotorg"

    @property
    def original_file_name(self) -> "str":
        return "mailboxdotorg.svg"

    @property
    def title(self) -> "str":
        return "mailbox.org"

    @property
    def primary_color(self) -> "str":
        return "#76BB21"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>mailbox.org</title>
     <path d="M2.229 22.844H24V10.501l-8.628
 5.882c-.613.419-1.226-.003-1.226-.003L0 6.646v13.969s0 2.229 2.229
 2.229m12.558-9.273L24 7.261V1.156H2.229S0 1.156 0 3.384v.06l14.787
 10.127Z" />
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
