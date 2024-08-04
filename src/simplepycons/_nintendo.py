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


class NintendoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nintendo"

    @property
    def original_file_name(self) -> "str":
        return "nintendo.svg"

    @property
    def title(self) -> "str":
        return "Nintendo"

    @property
    def primary_color(self) -> "str":
        return "#E60012"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nintendo</title>
     <path d="m4.447 12.546-1.202-1.942h-.864v2.793h.864v-1.942l1.202
 1.942h.856v-2.793H4.44l.007
 1.942Zm6.828-1.001v-.279h-.451v-.376h-.841v.376h-.458v.279h.458v1.852h.841v-1.852h.451Zm-5.491
 1.844h.834v-1.852h-.834v1.852Zm0-2.213h.841v-.572h-.841v.572Zm14.663.233c-.676
 0-1.224.467-1.224 1.039 0 .572.548 1.039 1.224 1.039.676 0 1.225-.467
 1.225-1.039 0-.572-.549-1.039-1.225-1.039Zm.338 1.431c0
 .293-.173.414-.338.414-.165
 0-.346-.121-.346-.414v-.783c0-.294.173-.414.346-.414.165 0
 .338.12.338.414v.783Zm-2.659-1.212a1.093 1.093 0 0
 0-.473-.166c-.601-.053-1.067.482-1.067.971 0
 .648.496.881.571.919.285.128.646.135.961-.068v.105h.827v-2.785h-.827c.008
 0 .008.595.008 1.024Zm.008.828v.331c0
 .286-.196.361-.331.361s-.331-.075-.331-.361v-.662c0-.287.196-.362.331-.362.128
 0 .33.075.33.362v.331h.001Zm-9.556-1.001a1.02 1.02 0 0
 0-.668.278v-.196h-.834v1.852h.834V12.17c0-.158.172-.339.398-.339.225
 0
 .383.181.383.339v1.219h.834v-1.008c0-.731-.631-.942-.947-.926Zm6.798
 0a1.01 1.01 0 0
 0-.668.278v-.196h-.834v1.852h.834V12.17c0-.158.173-.339.398-.339.225
 0
 .383.181.383.339v1.219h.834v-1.008c0-.731-.631-.942-.947-.926Zm-1.75
 1.016c0-.572-.556-1.054-1.232-1.054-.683 0-1.232.467-1.232 1.039 0
 .572.549 1.039 1.232 1.039.564 0 1.044-.324 1.187-.76h-.834v.112c0
 .339-.225.414-.345.414-.128
 0-.353-.075-.353-.413v-.385l1.577.008Zm-1.517-.655a.346.346 0 0 1
 .293-.166c.112 0
 .225.053.293.166.052.09.052.203.052.361h-.698c0-.158.007-.263.06-.361Zm9.893-.866c0-.09-.068-.135-.203-.135h-.188v.474h.113v-.196h.06l.09.196h.128l-.105-.211c.067-.022.105-.068.105-.128Zm-.218.068h-.06v-.136h.052c.068
 0 .105.023.105.068 0 .053-.029.068-.097.068Zm.007-.392a.433.433 0 0
 0-.428.43c0 .233.196.429.429.429a.429.429 0 0 0 0-.859h-.001Zm0
 .776a.35.35 0 0 1-.345-.346.35.35 0 0 1 .346-.347.35.35 0 0 1
 .345.347.35.35 0 0 1-.345.346h-.001Zm-.938-2.364H3.132C1.254 9.03 0
 10.386 0 12.004s1.254 2.959 3.14 2.959h17.72c1.886 0 3.14-1.34
 3.14-2.959-.007-1.618-1.269-2.966-3.147-2.966Zm-.008
 5.202H3.14c-1.495.008-2.404-1.001-2.404-2.236 0-1.235.917-2.228
 2.404-2.236h17.705c1.487 0 2.404 1.001 2.404 2.236 0 1.235-.909
 2.236-2.404 2.236Z" />
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
