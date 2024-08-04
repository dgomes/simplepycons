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


class LimesurveyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "limesurvey"

    @property
    def original_file_name(self) -> "str":
        return "limesurvey.svg"

    @property
    def title(self) -> "str":
        return "LimeSurvey"

    @property
    def primary_color(self) -> "str":
        return "#14AE5C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>LimeSurvey</title>
     <path d="M3.9339 2.3012c.7181 0 1.4363.1657 2.1544.3867.6629.221
 1.3258.5524 1.9887.8839.6077.3314 1.2153.7181 1.823
 1.16l.8286.663c.1657.1104.2762.221.3867.3314.0553.0552.1105.1105.221.1657l.1105.1658.1105.1104H9.5685l.1658-.221.1657-.1656.3314-.3315c.221-.2762.442-.4972.663-.7181.221-.221.4971-.442.718-.6077.1106-.1105.2763-.221.3868-.2762l.1657-.1657.1657-.1658c.4972-.3867
 1.0496-.7181 1.602-1.0496.5525-.3314 1.1049-.6076 1.7126-.8838
 1.16-.5525 2.3754-.9392 3.5907-1.2154.6076-.1104 1.2706-.221
 1.8782-.2762.663-.1105 1.3258-.1105
 1.9335-.0552l-.8286.4972c-.1105.0552-.2763.1657-.3867.221-.0553.0552-.1105.0552-.221.1104l-.221.1105c-.4972.3315-1.0496.6077-1.5468.9391-.939.663-1.8782
 1.2706-2.8725 1.9335-.9944.6629-1.8783 1.3258-2.8174
 1.9887l-.6629.4972c-.221.1657-.442.3314-.6629.5524-.221.221-.442.3867-.6629.5524-.1105.1105-.221.1657-.3314.2762l-.2762.2762-1.2154
 1.0496-.7734-1.0496-.0552-.0552-.0552-.1105-.221-.1657-.3315-.3867c-.221-.2762-.4419-.4972-.6629-.7182L6.917
 5.0633c-.442-.4972-.8838-.9944-1.381-1.4363-.4972-.4972-1.0496-.9391-1.602-1.3258Zm16.4068
 11.9925c0-1.2153-.221-2.4307-.6629-3.5355l-3.4802 1.4915c.9943
 2.7621-.1657 5.8557-2.7621 7.2367l1.4915 3.4803c3.3145-1.602
 5.4137-4.9718 5.4137-8.673zm-3.867-7.7339-3.3144 2.4307c1.1048.5524
 2.044 1.4362 2.5963
 2.4858l3.4803-1.4915c-.6077-1.3258-1.5468-2.4859-2.7621-3.425ZM4.7626
 14.2937c0-2.044 1.1048-3.9774 2.8173-5.027L5.1492 6.3388c-3.646
 2.486-5.1375 7.1815-3.5907
 11.3246l3.5354-1.4915c-.221-.6077-.3314-1.2706-.3314-1.8782Zm5.8556
 5.9109c-2.2096 0-4.2536-1.2706-5.248-3.2593L1.89 18.4368c2.1544
 4.5851 7.513 6.7395 12.2637
 4.9166l-1.4915-3.4803c-.663.221-1.3258.3315-2.044.3315z" />
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