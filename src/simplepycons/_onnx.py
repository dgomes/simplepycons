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


class OnnxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "onnx"

    @property
    def original_file_name(self) -> "str":
        return "onnx.svg"

    @property
    def title(self) -> "str":
        return "ONNX"

    @property
    def primary_color(self) -> "str":
        return "#005CED"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ONNX</title>
     <path d="M23.0325 11.2963c-.0503 0-.1006
 0-.1508.0126l-4.021-7.4387c.0754-.1383.1131-.289.1131-.4524
 0-.5403-.4398-.9675-.9675-.9675-.2765 0-.5278.113-.7037.3015L9.286
 1.156C9.2357.6785 8.821.3016 8.3184.3016c-.5277
 0-.9675.4398-.9675.9675 0 .1634.0377.3141.113.4524l-6.245
 8.9591c-.0753-.0251-.1633-.0377-.2513-.0377-.5403
 0-.9675.4398-.9675.9676 0 .5403.4398.9675.9675.9675h.0377l3.3676
 8.3309c-.0503.1257-.088.2639-.088.402 0
 .5404.4398.9676.9676.9676.2764 0
 .5277-.113.7036-.3015l10.1152.9926c.1005.4273.49.7288.9424.7288.5403
 0 .9676-.4398.9676-.9675
 0-.2388-.088-.465-.2262-.6283l5.1141-8.8712c.0503.0126.1005.0126.1634.0126.5403
 0 .9675-.4398.9675-.9676 0-.5403-.4272-.98-.9675-.98zM17.2272
 4.021c.1131.1508.2765.264.4524.3267l-1.533
 11.5728c-.1005.0252-.1885.0503-.2764.1005L7.4513
 8.708c.0251-.0754.0377-.1634.0377-.2514
 0-.0628-.0126-.1256-.0126-.1884zm4.8754 8.5068l-5.177 3.556a1.105
 1.105 0 0 0-.1256-.0753L18.3455 4.335h.0126l3.9456
 7.288c-.1508.1759-.2388.3895-.2388.6408 0
 .1005.0126.1885.0377.2638zM6.3832
 7.5016c-.4649.0754-.8293.4775-.8293.955v.0628l-3.4555 2.0481
 5.378-7.7026zm.3519 1.91c.1256-.0252.2513-.088.3518-.1634l8.356
 7.2628c-.0377.113-.0628.2262-.0628.3518v.0503l-9.311
 3.845c-.1382-.201-.3518-.3518-.6031-.402zm8.8963
 8.1172c.1257.1382.3016.2513.5026.289l.465
 4.046c-.201.1006-.3519.264-.4524.4524l-9.8136-.955zm1.1435.2136c.3267-.1633.5403-.49.5403-.867
 0-.088-.0126-.1634-.0377-.2513l4.7372-3.2545-4.8
 8.331zm.2513-14.3497l-9.889 4.31-.1131-.0755
 1.2565-5.3906h.0377c.3393 0 .6409-.1759.8168-.4397l7.891
 1.5706zM1.935
 11.6105c0-.0629-.0126-.1257-.0126-.1885l3.9079-2.2995c.0754.0754.1633.1508.2638.201L4.8252
 20.243l-3.2043-7.9036c.1885-.176.3142-.4398.3142-.7288Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/onnx/onnx.github.io/blob/3'''

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