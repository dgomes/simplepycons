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


class FoundryVirtualTabletopIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "foundryvirtualtabletop"

    @property
    def original_file_name(self) -> "str":
        return "foundryvirtualtabletop.svg"

    @property
    def title(self) -> "str":
        return "Foundry Virtual Tabletop"

    @property
    def primary_color(self) -> "str":
        return "#FE6A1F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Foundry Virtual Tabletop</title>
     <path d="m11.391
 23.879-9.386-5.5c-.269-.158-.492-.546-.492-.86V6.48c0-.314.223-.7.494-.857L11.506.116c.274-.157.717-.154.988.003l9.499
 5.561c.271.16.494.546.494.86v10.979c0 .314-.223.7-.494.857l-9.613
 5.509c-.271.154-.717.154-.989-.006m1.221-.934
 6.929-3.958c.274-.157.471-.354.443-.443-.029-.088-.309-.125-.62-.085l-6.684.877c-.311.04-.566.331-.566.646v2.674c0
 .315.226.446.498.289M9.714 1.951l-6.766 3.92c-.272.158-.272.418 0
 .575l2.208
 1.288c.272.158.652.086.846-.162l4.075-5.204c.194-.248.306-.508.243-.577s-.335.003-.606.16m2.429
 16.222 5.212-9.064c.157-.272.028-.494-.286-.494H6.725c-.314
 0-.443.222-.289.497l5.141
 9.058c.154.274.409.274.566.003m1.489-7.247s-.949.28-.952.958c0 .674
 1.129 1.025 1.129
 1.025v.669h-1.12c-.232-.151-.483-.237-.752-.237-.268
 0-.523.086-.751.237H10.12v-.669c.36 0 1.086-.591 1.086-1.02
 0-.428-.683-.517-.683-.517h-.54c-1.258
 0-1.749-1.186-1.749-1.186h2.08v-.228h4.824v.731c-.646
 0-1.506.237-1.506.237m-3.052-.58h4.303c.026 0
 .049-.02.049-.048v-.029c0-.026-.02-.048-.049-.048H10.58c-.026
 0-.049.02-.049.048v.029c0
 .025.02.048.049.048m-.297.2v-.097c0-.014-.012-.023-.023-.023H8.868c-.02
 0-.028.032-.008.043.211.112.351.1.351.1h1.049c.014 0
 .023-.011.023-.023M2.17 7.166v7.972c0
 .315.075.589.166.606s.266-.203.386-.494l2.617-6.252a.655.655 0 0
 0-.28-.803L2.67
 6.872c-.274-.152-.5-.02-.5.294m11.459-5.375c-.06.071.048.329.243.577l4.072
 5.204c.194.248.574.32.845.162l2.209-1.288c.272-.157.272-.417
 0-.575l-6.763-3.92c-.272-.157-.546-.229-.606-.16m8.172
 13.347V7.166c0-.314-.226-.446-.5-.294l-2.389 1.323a.652.652 0 0
 0-.28.803l2.618
 6.252c.123.291.294.511.385.494.092-.02.166-.291.166-.606m-8.895 3.652
 8.218-1.083c.311-.04.466-.311.346-.6l-3.201-7.644c-.123-.288-.348-.303-.505-.031l-5.141
 8.938c-.154.271-.029.46.283.42m4.317-11.144-4.88-6.444c-.189-.251-.503-.254-.697-.005L6.594
 7.649c-.195.248-.095.451.22.451h10.184c.314 0
 .414-.203.225-.454M2.759 17.71l8.055
 1.077c.314.043.44-.146.286-.42L6.036
 9.44c-.157-.274-.38-.26-.5.032L2.41
 17.104c-.12.292.037.563.349.606m8.841
 4.946h-.003v-2.669c0-.314-.254-.605-.566-.648l-6.54-.878c-.312-.042-.592-.002-.621.083-.028.086.169.289.441.446l6.795
 3.949c.271.16.494.032.494-.283" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/simple-icons/simple-icons/'''

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