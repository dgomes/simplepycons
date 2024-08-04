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


class SatdotOneIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sat1"

    @property
    def original_file_name(self) -> "str":
        return "sat1.svg"

    @property
    def title(self) -> "str":
        return "Sat.1"

    @property
    def primary_color(self) -> "str":
        return "#047DA3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sat.1</title>
     <path d="M11.3437.0066c-.292.01-.586.028-.881.06-10.092
 1.088-6.4994 16.6226-5.9704
 18.1375-3.9647-8.4243-1.6329-13.7038.118-15.4917.049-.05-.004-.136-.05-.095C.6046
 5.8241.2506 9.4498.2506 9.4498c-.684 3.9517 3.1578 7.8334 4.2457
 8.7653C1.5295 16.2152.6556 14.7794.1146
 12.7985c-.016-.06-.118-.08-.113 0 .081 1.064.185 2.4898 1.005
 4.1737.7519.9729 2.8147 1.2469 3.4897 1.2459h.003l-.003-.006C5.3792
 14.9634 7.17 9.2928 9.9908 5.473 12.7185 1.9356 14.8204.8237
 15.3933.5687c.048-.023.025-.077-.03-.114-.128-.082-1.9788-.513-4.0196-.448zM4.4983
 18.2191c.7149 1.2099 2.9297 4.5456 6.9754 5.6995 1.3818.277
 5.6175-.02 8.6012-3.0108.054-.053.007-.175-.106-.099-1.9698
 1.344-8.1393
 2.6818-15.4706-2.5897zl-.003.002c-1.053.447-2.2199.28-2.7298.044-.065-.031-.125-.02-.09.044.748
 1.2639 1.1659 1.6998 2.1098
 2.5448.051.053.104.04.08-.064-.01-.046-.189-1.342.63-2.5648-.105.822-.206
 3.1047.6919 3.7107 1.0579.7219 2.1468 1.4138 4.0836
 1.8288.076.018.145-.071.071-.11-3.1657-1.5458-3.9116-3.4737-4.8445-5.4325zM17.612
 1.3985c-.226.026-.462.215-1.0159.552C9.9728 6.36 5.0582 17.0342
 4.4982 18.215c0 0 11.0691-2.3898 17.8545-9.2892 1.06-1.085
 1.138-.85.64-2.0538-.239-.597-.866-1.8129-1.9499-3.0358-.8539-.9549-1.9698-1.7028-2.4658-2.0098-.52-.316-.7379-.454-.9649-.428zM4.4983
 18.2151c1.3628.78 16.1146 7.0634
 18.9573-2.7248.665-2.2838.576-4.6746.468-4.9636-.022-.062-.073-.034-.076-.014-.35.516-1.8279
 2.4198-5.7795 4.4947C13.8265 17.1182 7.84 17.913 4.4993 18.215z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.prosiebensat1.com/presse/download'''

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
