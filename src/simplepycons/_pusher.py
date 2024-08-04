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


class PusherIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pusher"

    @property
    def original_file_name(self) -> "str":
        return "pusher.svg"

    @property
    def title(self) -> "str":
        return "Pusher"

    @property
    def primary_color(self) -> "str":
        return "#300D4F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Pusher</title>
     <path d="M12 23.966v-6.0166a.0348.0348 0
 01.0182-.031l7.7319-4.4645a.0348.0348 0
 00.0181-.031v-1.711a.0356.0356 0 00-.0537-.031l-7.6608
 4.423a.0356.0356 0 01-.0537-.031v-1.7117a.0356.0356 0
 01.0181-.031l7.732-4.4645a.037.037 0 00.0181-.031v-1.711a.0363.0363 0
 00-.0537-.031l-7.6608 4.4229a.0356.0356 0
 01-.0537-.031v-1.711a.0348.0348 0
 01.0181-.031l7.732-4.4622a.0356.0356 0 00.0181-.031V4.515a.0757.0757
 0 00-.0356-.062L12.0356.0096a.0704.0704 0 00-.0712
 0L10.5002.855a.0356.0356 0 000 .062L18.161 5.34a.0363.0363 0 010
 .062l-1.4642.8452a.0757.0757 0 01-.0719 0L8.9286 1.8038a.0757.0757 0
 00-.0757 0l-1.4597.8445a.0356.0356 0 000 .062l7.6593
 4.4236a.0356.0356 0 010 .0621l-1.4634.8452a.0757.0757 0 01-.0757
 0l-7.6926-4.444a.0757.0757 0 00-.0756
 0l-1.5134.8762v15.0492a.0348.0348 0
 00.0181.031l1.4816.8558a.0356.0356 0 00.0538-.031V5.433a.0356.0356 0
 01.0537-.031l1.4824.8558a.0356.0356 0 01.0174.031v15.028a.0356.0356 0
 00.0181.031l1.4816.8559a.0363.0363 0 00.0545-.0318V7.227a.0356.0356 0
 01.0537-.031l1.4817.855a.0356.0356 0 01.0181.0311v15.0288a.037.037 0
 00.0174.031l1.4862.855A.0356.0356 0 0012 23.966z" />
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