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


class NexusModsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nexusmods"

    @property
    def original_file_name(self) -> "str":
        return "nexusmods.svg"

    @property
    def title(self) -> "str":
        return "Nexus Mods"

    @property
    def primary_color(self) -> "str":
        return "#E6832B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nexus Mods</title>
     <path d="M17.376 0c-.993 0-2.18.686-2.907
 1.182-1.676-.36-4.036-.545-6.787.635-1.365-.513-2.425-.562-3.32-.488a2.16
 2.16 0 0 0-1.27.429c-.33.22-2.788 2.69-3.069 4.652C-.15 7.508.68
 8.932 1.218 9.718c-.44 1.76-.2 4.572.517 6.188-.353 1.041-.713
 2.089-.664 3.205.01.584.061 1.188.398 1.684C1.72 21.19 4.528 24 6.545
 24c.957 0 1.93-.428 3.07-1.24 2.16.383 4.402.348 6.448-.532 2.573
 1.001 4.224.625 4.84.162.587-.457 2.826-2.915
 3.07-4.622.1-.672-.023-1.638-1.226-3.397a10.983 10.983 0 0
 0-.501-6.455c.396-1.069.673-2.188.59-3.337-.015-.68-.221-1.167-.487-1.507-.209-.335-2.415-2.39-4.028-2.91A3.105
 3.105 0 0 0 17.376 0m-.03 2.082c.65.015 2.155 1.093 3.01
 1.906l.355.34c-.959-.163-2.125.428-3.26 1.55a10.28 10.28 0 0 0-1.358
 1.595c-.28.384-.517.768-.753 1.285l1.18.635-3.895 1.477-1.122-4.18
 1.033.547c1.358-3.102 2.524-3.973 3.232-4.416h.015a5.12 5.12 0 0 1
 1.49-.724zM12 3.065a8.932 8.932 0 0 1 2.22.279 7.67 7.67 0 0
 0-.42.488 8.403 8.403 0 0 0-1.8-.196 8.336 8.336 0 0 0-5.897 2.432
 7.86 7.86 0 0 1-.37-.433A8.905 8.905 0 0 1 12
 3.065m-7.076.305c.71-.002 1.309.127 2.2.466a9.526 9.526 0 0 0-1.713
 1.337c-.327-.542-.624-1.156-.488-1.803m-.606.042c-.162.96.428 2.126
 1.55 3.264.457.487 1.003.945 1.594 1.358.383.281.767.517
 1.283.754l.62-1.182 1.49 3.914-4.176
 1.122.546-1.033c-3.099-1.36-3.969-2.526-4.412-3.235v-.015a5.144 5.144
 0 0 1-.723-1.491l-.015-.074c.015-.65 1.092-2.156 1.904-3.013Zm16.035
 1.483a1.259 1.259 0 0 1 .26.015l.14.023a5.05 5.05 0 0 1-.13
 1.137v.015c-.1.383-.228.765-.377 1.148a9.526 9.526 0 0
 0-1.346-1.776c.547-.357 1.051-.546 1.453-.562M18.43 5.8a8.903 8.903 0
 0 1 2.506 6.2 8.937 8.937 0 0 1-.27 2.183 7.658 7.658 0 0
 0-.488-.425A8.407 8.407 0 0 0 20.364 12 8.334 8.334 0 0 0 18
 6.173a7.904 7.904 0 0 1 .429-.373M3.315
 9.905c.157.148.319.29.488.425A8.417 8.417 0 0 0 3.636 12c0 2.248.887
 4.286 2.327 5.788a8.11 8.11 0 0 1-.426.376A8.902 8.902 0 0 1 3.065
 12a8.937 8.937 0 0 1 .25-2.095m13.988 1.541-.546 1.034c3.098 1.359
 3.969 2.526 4.412 3.235v.014c.34.488.575.99.723
 1.492l.014.074c-.014.65-1.092 2.156-1.903
 3.013l-.34.354c.163-.96-.427-2.127-1.549-3.264a10.298 10.298 0 0
 0-1.594-1.359 7.008 7.008 0 0 0-1.283-.753l-.605
 1.152-1.505-3.87zm-6.006 1.684 1.121 4.18-1.033-.547c-1.357
 3.102-2.523 3.973-3.231
 4.416h-.015c-.487.34-.989.576-1.49.724l-.074.015c-.65-.015-2.154-1.093-3.01-1.906l-.354-.34c.959.163
 2.124-.428 3.26-1.55.488-.458.945-1.004
 1.358-1.595.28-.384.517-.768.753-1.285l-1.166-.635ZM3.72 16.663A9.526
 9.526 0 0 0 5.086
 18.5c-.697.47-1.33.665-1.777.59l-.138-.024c0-.367.038-.748.128-1.137v-.015c.11-.417.254-.835.42-1.252m14.131
 1.314c.129.14.253.283.372.43A8.904 8.904 0 0 1 12 20.936a8.932 8.932
 0 0 1-2.282-.296 7.757 7.757 0 0 0 .417-.487 8.335 8.335 0 0 0
 7.716-2.175m.696.889c.43.666.607 1.267.534 1.698l-.023.138a5.034
 5.034 0 0 1-1.136-.128h-.014a10.718 10.718 0 0 1-1.114-.366 9.526
 9.526 0 0 0 1.753-1.342" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://wiki.nexusmods.com/skins/Metrolook/im'''

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
