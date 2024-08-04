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


class ProcesswireIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "processwire"

    @property
    def original_file_name(self) -> "str":
        return "processwire.svg"

    @property
    def title(self) -> "str":
        return "ProcessWire"

    @property
    def primary_color(self) -> "str":
        return "#2480E6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ProcessWire</title>
     <path d="M21.939 5.27C21.211 4.183 20 2.941 18.784 2.137
 16.258.407 13.332-.207 10.744.061c-2.699.291-5.01 1.308-6.91
 3.004C2.074 4.637.912 6.559.4 8.392c-.518 1.833-.449 3.53-.264
 4.808.195 1.297.841 2.929.841 2.929.132.313.315.44.41.493.472.258
 1.247.031
 1.842-.637.03-.041.046-.098.03-.146-.166-.639-.226-1.12-.285-1.492-.135-.736-.195-1.969-.105-3.109.045-.617.165-1.277.375-1.969.406-1.367
 1.262-2.794 2.6-3.98 1.441-1.277 3.289-2.066 5.046-2.27.616-.074
 1.788-.145 3.199.203.301.075 1.593.412 2.975 1.348 1.006.684 1.816
 1.528 2.374 2.363.568.797 1.185 2.141 1.366 3.125.256 1.12.256
 2.307.074 3.463-.225 1.158-.631 2.284-1.262 3.275-.435.768-1.337
 1.783-2.403 2.545-.961.676-2.058 1.164-3.184
 1.434-.57.135-1.142.221-1.728.24-.521.016-1.212
 0-1.697-.082-.721-.115-.871-.299-1.036-.549 0
 0-.115-.18-.147-.662.011-4.405.009-3.229.009-5.516
 0-.646-.021-1.232-.015-1.764.03-.873.104-1.473.728-2.123.451-.479
 1.082-.768 1.777-.768.211 0 .938.01 1.577.541.685.572.8 1.354.827
 1.563.156 1.223-.652 2.134-.962
 2.365-.384.288-.729.428-.962.51-.496.166-1.041.214-1.531.182-.075-.005-.143.044-.158.119l-.165.856c-.161.65.2.888.41.972.671.207
 1.266.293 1.971.24 1.081-.076 2.147-.502 3.052-1.346.77-.732
 1.209-1.635
 1.359-2.645.15-1.121-.045-2.328-.556-3.35-.562-1.127-1.532-2.068-2.81-2.583-1.291-.508-2.318-.526-3.642-.188l-.015.005c-.86.296-1.596.661-2.362
 1.452-.525.546-.955 1.207-1.217 1.953-.26.752-.33 1.313-.342
 2.185-.016.646.015 1.246.015 1.808v3.701c0 1.184-.04 1.389 0
 1.998.022.404.078.861.255 1.352.182.541.564 1.096.826
 1.352.367.391.834.705 1.293.9 1.051.467 2.478.541 3.635.496.766-.029
 1.536-.135 2.291-.314 1.51-.359 2.96-1.012 4.235-1.918 1.367-.963
 2.555-2.277 3.211-3.393.841-1.326 1.385-2.814
 1.668-4.343.255-1.532.243-3.103-.099-4.612-.27-1.4-.991-2.936-1.823-4.176l.038.037z"
 />
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
