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


class WwiseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wwise"

    @property
    def original_file_name(self) -> "str":
        return "wwise.svg"

    @property
    def title(self) -> "str":
        return "Wwise"

    @property
    def primary_color(self) -> "str":
        return "#00549F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wwise</title>
     <path d="M6 12c0 .7644-.6193 1.3846-1.3846 1.3846-.7645
 0-1.3847-.6202-1.3847-1.3846 0-.765.6202-1.3846 1.3847-1.3846C5.3807
 10.6154 6 11.2351 6 12m7.8462-5.5384c0 1.0191-.826 1.8461-1.8463
 1.8461-1.0188 0-1.8461-.827-1.8461-1.8461 0-1.0197.8273-1.8462
 1.8461-1.8462 1.0203 0 1.8463.8265 1.8463 1.8462M1.8462 12a.923.923 0
 0 1-.9231.923C.4143 12.923 0 12.5096 0
 12c0-.5102.4142-.923.923-.923.51 0 .923.4128.923.923M24 12c0
 .5095-.4133.923-.923.923-.5089 0-.9231-.4135-.9231-.923
 0-.5102.4142-.923.923-.923.5098 0 .923.4128.923.923m-3.2306 0c0
 .7644-.6195 1.3846-1.3847 1.3846C18.6203 13.3846 18 12.7644 18
 12c0-.765.6203-1.3846 1.3846-1.3846.7652 0 1.3847.6197 1.3847
 1.3846m-8.2252 2.8356c.0034.535.2557 1.0139.6581
 1.3139.4006.3332.6584.8409.6584 1.4048 0 1.0139-.8192 1.8303-1.8295
 1.8303H12c-1.0116 0-1.8317-.8164-1.8317-1.8303
 0-.564.2596-1.0716.6606-1.4048.3999-.3.6615-.7788.6577-1.314v-.1283c-.004-.5395-.2578-1.0183-.6577-1.3154-.401-.336-.6606-.8423-.6606-1.4077
 0-1.0125.8201-1.8302 1.8317-1.8302h.0312c1.0103 0 1.8295.8177 1.8295
 1.8302 0 .5654-.2578 1.0717-.6584 1.4077a1.6166 1.6166 0 0 0-.658
 1.3154v.1284m3.6922-2.7692c.0033.535.2557 1.0139.658
 1.3139.4007.3332.6585.8409.6585 1.4048 0 1.0139-.8192 1.8302-1.8295
 1.8302h-.031c-1.0118 0-1.8318-.8163-1.8318-1.8302
 0-.564.2597-1.0716.6606-1.4048.3999-.3.6614-.7788.6577-1.314v-.1283c-.004-.5395-.2578-1.0183-.6577-1.3154-.401-.336-.6606-.8423-.6606-1.4077
 0-1.0125.82-1.8302 1.8318-1.8302h.031c1.0103 0 1.8295.8177 1.8295
 1.8302 0 .5654-.2578 1.0717-.6584 1.4077a1.6166 1.6166 0 0 0-.658
 1.3154v.1284m-7.3848 0c.0035.535.2559 1.0139.6582 1.3139a1.828 1.828
 0 0 1 .6583 1.4048c0 1.0139-.8193 1.8302-1.8294 1.8302h-.0312c-1.0116
 0-1.8317-.8163-1.8317-1.8302
 0-.564.2596-1.0716.6606-1.4048.3999-.3.6615-.7788.6577-1.314v-.1283c-.004-.5395-.2578-1.0183-.6577-1.3154-.401-.336-.6606-.8423-.6606-1.4077
 0-1.0125.8201-1.8302 1.8317-1.8302h.0312c1.0101 0 1.8294.8177 1.8294
 1.8302 0 .5654-.2578 1.0717-.6583 1.4077a1.617 1.617 0 0 0-.6582
 1.3154v.1284" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.audiokinetic.com/resources/credit'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.audiokinetic.com/resources/credit'''

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
