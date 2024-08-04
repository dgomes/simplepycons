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


class NgrxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ngrx"

    @property
    def original_file_name(self) -> "str":
        return "ngrx.svg"

    @property
    def title(self) -> "str":
        return "NgRx"

    @property
    def primary_color(self) -> "str":
        return "#BA2BD2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NgRx</title>
     <path d="M12.024.017V0L12 .008 11.976 0v.017L.812 3.892l1.605
 14.875 9.559 5.207V24l.024-.013.024.013v-.026l9.559-5.207
 1.605-14.875L12.024.017zm6.868 14.244c-1.094 2.632-3.104 4.02-6.031
 4.166-2.829
 0-4.661-1.7-4.66-1.7-1.163-.905-1.963-2.046-2.398-3.417-.695-.76-.702-.841-.774-1.145-.072-.303.045-.388.249-.685.136-.198.168-.483.098-.85-.173-.24-.273-.616-.3-1.128
 0-.247.166-.508.496-.783.33-.275.533-.486.607-.632.056-.079.077-.423.065-1.031-.004-.598.328-.923.995-.975
 1-.08 1.565-.832 1.879-1.174.21-.228.52-.339.91-.341.551-.026
 1.052.185 1.484.62 1.075-.055 2.176.235 3.292.863 1.586.942 2.451
 1.962 2.596 3.055-.17 1.439-2.102 1.4-5.788-.113-1.93.546-2.878
 1.73-2.846 3.552-.001 1.672.808 2.886 2.422
 3.643-.787-.772-1.122-1.422-1.01-1.959 1.637 1.937 3.5 2.662 5.588
 2.173-.92.032-1.65-.264-2.198-.893 1.411-.035 2.743-.69
 3.998-1.972-.724.576-1.482.794-2.284.657 2.173-1.709 2.942-3.702
 2.307-5.98l-.002-.006a3.02 3.02 0 0 1 .788 2.03c.014.783-.249
 1.61-.795 2.477.408-.318.88-1.002 1.413-2.047.23 2.117-.625
 3.724-2.574 4.825.622-.057 1.448-.467
 2.473-1.23zm-5.567-6.63a.319.319 0 1 1 .638 0 .319.319 0 0 1-.638 0z"
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
