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


class GooglePubsubIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "googlepubsub"

    @property
    def original_file_name(self) -> "str":
        return "googlepubsub.svg"

    @property
    def title(self) -> "str":
        return "Google Pub/Sub"

    @property
    def primary_color(self) -> "str":
        return "#AECBFA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Google Pub/Sub</title>
     <path d="M18.3 7.452a2.064 2.064 0 1 1 4.128 0 2.064 2.064 0 0
 1-4.128 0zM3.636 9.516a2.064 2.064 0 1 0 0-4.128 2.064 2.064 0 0 0 0
 4.128zM12 19.872A2.064 2.064 0 1 0 12 24a2.064 2.064 0 0 0
 0-4.128zm-5.774-3.151a2.591 2.591 0 0 0-.118-.48c0-.002
 0-.004-.002-.006a2.595 2.595 0 0 0-.2-.436l-.004-.008a2.618 2.618 0 0
 0-.276-.39l-.001-.001a2.622 2.622 0 0 0-.346-.336 2.603 2.603 0 0
 0-1.643-.592A2.628 2.628 0 1 0 6.264
 17.1c0-.13-.02-.254-.038-.38zm8.499-2.53c.033-.047.063-.097.094-.147a3.32
 3.32 0 0 0 .201-.37c.026-.055.052-.108.074-.164a3.301 3.301 0 0 0
 .242-1.234c0-1.51-1.01-2.772-2.388-3.183a3.277 3.277 0 0
 0-.42-.1A2.882 2.882 0 0 0 12 8.94c-.183 0-.359.021-.532.054a3.272
 3.272 0 0 0-.428.103 3.325 3.325 0 0 0-2.376 3.179c0 .567.155
 1.093.405
 1.561.028.054.055.108.086.16.062.102.13.198.201.292.039.051.08.099.12.147a3.314
 3.314 0 0 0
 4.885.196c.135-.135.254-.284.364-.44zm-8.987.608c.473.433.818
 1.002.956 1.651l2.575-1.486a3.83 3.83 0 0 1-.946-1.657L5.738
 14.8zm5.302-9.21v2.988A3.79 3.79 0 0 1 12 8.44c.329 0
 .643.055.948.133v-2.98c-.3.097-.615.163-.948.163-.337
 0-.656-.067-.96-.166zm7.317 9.132L15.711 13.2a3.818 3.818 0 0 1-.914
 1.683l2.542 1.46a3.115 3.115 0 0 1 1.018-1.622zm2.007-.249c-.58
 0-1.112.194-1.547.513a2.633 2.633 0 0
 0-.662.701l-.013.024c-.082.13-.155.265-.212.409-.008.02-.012.041-.02.061a2.588
 2.588 0 0 0-.124.421 2.628 2.628 0 1 0 2.578-2.129zm-8.862-9.266a2.52
 2.52 0 0 0 .99 0A2.626 2.626 0 0 0 12 0a2.627 2.627 0 0 0-.498
 5.206z" />
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
