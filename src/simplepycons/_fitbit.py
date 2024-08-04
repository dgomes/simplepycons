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


class FitbitIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fitbit"

    @property
    def original_file_name(self) -> "str":
        return "fitbit.svg"

    @property
    def title(self) -> "str":
        return "Fitbit"

    @property
    def primary_color(self) -> "str":
        return "#00B0B9"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fitbit</title>
     <path d="M13.298 1.825c0 .976-.81 1.785-1.786 1.785-.972
 0-1.784-.81-1.784-1.785 0-.973.813-1.785 1.784-1.785.976 0 1.786.813
 1.786 1.785zm-1.786 3.243c-1.052 0-1.863.81-1.863 1.866 0 1.053.81
 1.865 1.865 1.865 1.053 0 1.865-.811
 1.865-1.865s-.825-1.866-1.875-1.866h.008zm0 5.029c-1.052
 0-1.945.891-1.945 1.945s.894 1.945 1.947 1.945 1.946-.891
 1.946-1.945-.894-1.945-1.946-1.945h-.002zm0 5.107c-1.052
 0-1.863.81-1.863 1.864s.81 1.866 1.865 1.866c1.053 0 1.865-.811
 1.865-1.866 0-.972-.825-1.864-1.875-1.864h.008zm0 5.191c-.972
 0-1.784.809-1.784 1.784 0 .97.813 1.781 1.784 1.781.977 0 1.786-.809
 1.786-1.784 0-.973-.81-1.781-1.786-1.781zM16.46 4.823c-1.136
 0-2.108.977-2.108 2.111 0 1.134.973 2.107 2.108 2.107 1.135 0
 2.106-.975 2.106-2.107 0-1.135-.972-2.109-2.106-2.109v-.002zm0
 5.03c-1.216 0-2.19.973-2.19 2.19 0 1.216.975 2.187 2.19 2.187 1.215 0
 2.189-.971 2.189-2.189 0-1.216-.974-2.188-2.189-2.188zm0 5.108c-1.136
 0-2.108.976-2.108 2.107 0 1.135.973 2.109 2.108 2.109 1.135 0
 2.106-.976 2.106-2.109s-.971-2.107-2.106-2.107zm5.106-5.353c-1.296
 0-2.43 1.055-2.43 2.434 0 1.297 1.051 2.433 2.43 2.433 1.381 0
 2.434-1.065
 2.434-2.444-.082-1.382-1.135-2.431-2.434-2.431v.008zM6.486
 5.312c-.892 0-1.62.73-1.62 1.623 0 .891.729 1.62 1.62 1.62.893 0
 1.619-.729 1.619-1.62 0-.893-.727-1.62-1.619-1.62v-.003zm0
 5.027c-.973 0-1.703.729-1.703 1.703 0 .975.721 1.703 1.695
 1.703s1.695-.73 1.695-1.703c0-.975-.735-1.703-1.71-1.703h.023zm0
 5.107c-.892 0-1.62.731-1.62 1.62 0 .895.729 1.623 1.62 1.623.893 0
 1.619-.735 1.619-1.635s-.727-1.62-1.619-1.62v.012zm-5.025-4.863c-.813
 0-1.461.646-1.461 1.459 0 .81.648 1.459 1.46 1.459.81 0 1.459-.648
 1.459-1.459s-.648-1.459-1.458-1.459z" />
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
