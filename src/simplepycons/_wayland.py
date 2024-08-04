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


class WaylandIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wayland"

    @property
    def original_file_name(self) -> "str":
        return "wayland.svg"

    @property
    def title(self) -> "str":
        return "Wayland"

    @property
    def primary_color(self) -> "str":
        return "#FFBC00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wayland</title>
     <path d="M23.982 12c0 9.224-9.985 14.989-17.973 10.377A11.982
 11.982 0 0 1 .018 12c0-3.386 1.346-6.306 3.444-8.418v.675l.553
 3.413v1.07l.077 1.365c-.23
 0-.344.053-.344.159v.09l.344-.09h.076v2.366c.178 1.578.509 2.981.992
 4.21.05.864.146 1.297.286 1.297.229.864.394 1.297.496 1.297a5.494
 5.494 0 0 0 2.422 1.865c.344 0
 .63-.432.859-1.296.292-1.866.528-3.004.706-3.414.165.167.451.281.858.342v-.091c0-.152-.26-.311-.782-.478.14-.728.33-1.35.572-1.866.038-.88.49-2.1
 1.354-3.663l.344.09c.05.714.146 1.305.286 1.776.521 1.061.782
 2.063.782 3.003 0 .364.407 1.585 1.22 3.663.204 1.366.465 2.17.783
 2.412h.152c.42 0 .916-.538 1.488-1.615.56-1.214 1.011-1.889
 1.354-2.025 0-.106-.12-.16-.362-.16v-.09c.19 0
 .286-.054.286-.16v-.068l-.076-.091.801-.319c0-.273-.095-.41-.286-.41v-.09h.572v-.16c-.292
 0-.483-.159-.572-.477h.133v-.319l-.076-.091c.432 0
 .649-.083.649-.25v-.069h-.134v-.09c.153 0
 .267-.16.343-.478-.42-.137-.629-.273-.629-.41l.553-1.615c0-.82.146-1.715.439-2.685.33-.94.566-1.965.706-3.072.304-1.064.617-1.787.938-2.17A11.979
 11.979 0 0 1 23.982 12Zm-5.99-10.377c.587.34 1.138.724 1.65
 1.148a33.45 33.45 0 0 0-.157 1.736c-.458 1.077-.96 2.594-1.507
 4.55h-1.411l-.725.07v.181h.362l.286-.09 1.202.158v.092c-.343
 1.183-.553 1.774-.63 1.774-.445 2.215-.8 3.322-1.068
 3.322h-.229c-.318-.288-.674-.88-1.068-1.774a.861.861 0 0
 0-.21-.57L13.42
 9.855c-.216-1-.502-1.752-.858-2.252-.115-.334-.305-.5-.572-.5h-.134c-.42
 0-.826.295-1.22.887l.076.25c-.178.607-.465 1.312-.859 2.116-.61
 1.775-1.01 2.662-1.201
 2.662h-.153l-.286-.227c-.483-1.305-.814-3.224-.992-5.757h-.134v-.16h.058a1.33
 1.33 0 0 1
 .515-.75v-.069l-.077-.09-.076.09-.076-.09-.344.09h-.152c-.09
 0-.23-.348-.42-1.046v-.183h.496v-.16h-.648c-.139-.698-.545-1.53-1.218-2.494.296-.206.601-.398.915-.577h.016l.077.068.438-.068h.783c.228
 0 .464.083.705.25.115-.152.33-.235.649-.25v-.16h-2.38c3.11-1.667
 6.947-1.99 10.51-.392l-.443.142v.16c.24 0
 .4-.095.482-.284.368.166.734.354 1.095.562Zm3.477
 3.203h-.134l.035-.295.179.23-.08.065ZM9.719
 1.595h.572l.133.159.363-.16.42.069.438-.068v-.16H9.72v.16Zm3.7
 1.297v.159l.21.09v-.09l.076-.091c.14 0
 .21-.053.21-.16v-.068h-.21l-.286.16Zm-1.144.887h-.058l-.076-.068-.42.227v.16c.61-.137.916-.266.916-.387V3.62l-.362.159Zm-2.842.978c0
 .167-.051.25-.153.25v.16c.598-.197 1.03-.417
 1.297-.66V4.44l-1.144.318Zm4.482.57v.068l.153.182h.076l.134-.182v-.069l-.077-.09-.286.09Zm2.785.159v.09h.076l.134-.181v-.069h-.076l-.134.16Zm-1.354
 1.206.152.25c.23 0
 .37-.084.42-.25l-.286-.228c-.19.076-.286.152-.286.228Zm1.85.978v.091h.153l.057-.091v-.068l-.057-.091-.153.159Zm-3.128.978v.091h.21l.362-.34v-.07c-.382.077-.572.183-.572.32ZM2.24
 12.13v.341h.153c.14-.106.305-.41.496-.91v-.068h-.076l-.573.637Zm9.328
 3.413v.159l.076.091.572-.341v-.16h-.076l-.572.25Zm-7.267.887.21.82h.152l-.229-.888h-.133v.068Zm7.63
 1.07.133.227h.076l.076-.068-.228-.25h-.058v.09Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://gitlab.freedesktop.org/wayland/weston'''

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
