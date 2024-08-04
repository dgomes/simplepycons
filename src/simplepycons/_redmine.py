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


class RedmineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "redmine"

    @property
    def original_file_name(self) -> "str":
        return "redmine.svg"

    @property
    def title(self) -> "str":
        return "Redmine"

    @property
    def primary_color(self) -> "str":
        return "#B32024"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Redmine</title>
     <path d="m1.092 15.088c.789.243 4.098 1.005 4.098
 1.005.198.061.139.21.139.21-.228 1.798-.178 3.17-.178 3.644 0
 .21-.153.18-.153.18h-4.83c-.209
 0-.164-.19-.164-.19.04-.599.212-2.303.878-4.746 0 0
 .033-.157.21-.103zm21.816 0c-.789.243-4.098 1.005-4.098
 1.005-.198.061-.139.21-.139.21.228 1.798.178 3.17.178 3.644 0
 .21.153.18.153.18h4.83c.21 0
 .164-.19.164-.19-.04-.599-.212-2.303-.878-4.746 0
 0-.034-.157-.21-.103zm-1.929-5.354-3.448
 1.667c-.164.063-.082.212-.082.212.476 1.134.766 2.091.99
 3.251.038.194.169.132.169.132l3.879-1.684s.116-.044.068-.193c-.172-.531-1.05-2.649-1.402-3.341
 0 0-.062-.105-.174-.044zm-17.958 0 3.448
 1.667c.164.063.082.212.082.212-.476 1.134-.766 2.091-.991
 3.251-.037.194-.169.132-.169.132l-3.878-1.684s-.116-.044-.068-.193c.172-.531
 1.05-2.649 1.402-3.341 0 0 .062-.105.174-.044zm4.085-4.368 2.302
 2.681c.099.128-.032.222-.032.222-.923.498-1.59 1.25-2.161
 2.111-.114.17-.236.046-.236.046l-2.917-2.184s-.126-.074-.016-.22c.854-1.134
 1.63-1.934 2.871-2.689 0 0 .094-.089.189.033zm9.788 0-2.302
 2.681c-.099.128.032.222.032.222.923.498 1.59 1.25 2.161
 2.111.114.17.236.046.236.046l2.917-2.184s.126-.074.016-.22c-.854-1.134-1.63-1.934-2.871-2.689
 0 0-.094-.089-.189.033zm-4.894 2.295c.388 0 1.105.037
 1.444.093.177.03.221-.088.221-.088l1.449-3.028s.097-.114-.106-.188c-1.082-.396-1.657-.578-3.008-.578-1.335
 0-1.926.182-3.008.578-.203.074-.106.188-.106.188l1.449
 3.028s.044.118.221.088c.339-.056 1.056-.093 1.444-.093z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.redmine.org/projects/redmine/wiki'''

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
