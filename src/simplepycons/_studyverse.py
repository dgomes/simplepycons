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


class StudyverseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "studyverse"

    @property
    def original_file_name(self) -> "str":
        return "studyverse.svg"

    @property
    def title(self) -> "str":
        return "Studyverse"

    @property
    def primary_color(self) -> "str":
        return "#1D29E4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Studyverse</title>
     <path d="M12.267 21.4c1.552-.126 3.057-.622 4.325-1.536.55-.404
 1.063-.881 1.427-1.462.186-.297.307-.62.297-.975a2.262 2.262 0 0
 0-.59-1.566c-.385-.437-.852-.777-1.353-1.068a13.116 13.116 0 0
 0-2.397-1.076c-2.426-.842-5.068-1.584-7.366-2.726-.746-.381-1.482-.808-2.089-1.392-.3-.301-.573-.656-.698-1.068-.226-.763-.227-1.605.1-2.34.107-.253.27-.453.421-.68-.063-.088-.094-.192-.217-.204-.206.027-.408.125-.6.202A7.641
 7.641 0 0 0 .915 7.43C.523 7.89.172 8.462.06 9.062c-.174.972.03
 1.99.605 2.797.706 1.02 1.889 1.715 3.015 2.18 2.748 1.094 5.544
 2.072 8.304
 3.134.352.139.695.234.968.512.173.178.296.428.184.673-.137.318-.539.46-.856.502-.742.093-1.476-.175-2.166-.41-2.105-.733-4.17-1.588-6.227-2.444-.116-.047-.167-.05-.268.03-.038.117-.013.208.05.31.411.69.89
 1.342 1.427 1.938 1.107 1.229 2.507 2.307 4.097 2.814 1.01.328
 2.023.348 3.074.302zm7.608-2.708c.233-.033.46-.147.676-.238a7.632
 7.632 0 0 0 2.561-1.917c.51-.608.875-1.307.884-2.119a3.667 3.667 0 0
 0-.81-2.481c-.722-.918-1.834-1.555-2.9-1.992-2.852-1.132-5.752-2.144-8.614-3.251-.295-.116-.58-.27-.754-.545-.105-.167-.136-.371-.035-.548.146-.276.5-.409.79-.455.693-.104
 1.389.122 2.037.343 2.18.748 4.316 1.637 6.444
 2.52.088.038.154.01.226-.045.041-.115.012-.212-.048-.312A12.242
 12.242 0 0 0 18.59
 5.38c-1.053-1.091-2.36-2.03-3.817-2.49-.727-.23-1.512-.316-2.272-.307a8.76
 8.76 0 0 0-3.333.597c-1.012.4-1.992 1.007-2.729
 1.814-.297.335-.6.737-.713 1.177a2.23 2.23 0 0 0 .191
 1.443c.244.48.671.88 1.1 1.196 1.188.845 2.518 1.325 3.89 1.772
 2.102.703 4.331 1.381 6.327 2.348.774.386 1.585.842 2.214
 1.442.302.295.582.649.715 1.054.25.802.244 1.697-.123
 2.463-.102.22-.257.392-.378.6.055.087.089.2.212.203z" />
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
