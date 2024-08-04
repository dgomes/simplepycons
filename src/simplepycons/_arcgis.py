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


class ArcgisIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "arcgis"

    @property
    def original_file_name(self) -> "str":
        return "arcgis.svg"

    @property
    def title(self) -> "str":
        return "ArcGIS"

    @property
    def primary_color(self) -> "str":
        return "#2C7AC3"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ArcGIS</title>
     <path d="M12 0a.84923.84923 0 0 0-.33766.07031l-8.5183
 3.69444C2.1458 4.19776 1.4997 5.1816 1.4997 6.2697v13.2521l10.16264
 4.40783c.21517.09333.46015.09407.67532.00073l8.5183-3.6959c.99824-.43301
 1.64434-1.41685 1.64434-2.50495V4.47814L12.33766.06958C12.23007.02291
 12.11516-.00005 12 0Zm0 4.83705c4.16294 0 7.53757 3.3746 7.53757
 7.53757S16.163 19.91218 12 19.91218c-4.163
 0-7.53757-3.37462-7.53757-7.53756S7.837 4.83705 12 4.83705zm-.3501
 1.38871c-.89685-.02267-2.32742.2409-3.74645
 1.6143.34958.55454.64544.97782.49
 1.41801-.23127.65503-.5139.51378-1.07083.99466-.39567.34169.2067
 1.01292-.31275 1.30595-.51945.29306-1.21315.6636-.94925
 1.17557.2639.51196 1.4691.83013 1.95929
 1.07522.49018.2451.92812.70605.6072 1.2371-.31403.51948-.53713
 1.13083-.60134 1.60917 1.0549.94423 2.44706 1.51909 3.97423 1.51909
 3.2928 0 5.81772-2.71048
 5.96208-6.00017.04062-.92531-.93924-.93972-1.53447-.93972 0 0
 .34061.92356.01831 1.43632-.3223.51278-.84968.76166-.83498
 1.37699.01464.61533-.93743 1.5967-1.2598
 1.9483-.32223.35163-.9228.74718-1.12796-.0586-.2051-.80579-.12596-1.47799.1084-2.04938.23442-.57136-.2174-.74707-.92068-.76174-.7032-.01463-1.0798-.10795-1.18656-1.19315-.08787-.89369
 1.2429-1.84356 1.81426-1.84356.33406 0 1.45485.21963
 1.50737-.34058.08056-.8593-.8204-1.04164-1.03934-1.60185C13.2877
 7.58747 14.98596 6.60707 12
 6.24993c-.10475-.01253-.22199-.02093-.3501-.02417z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.esri.com/en-us/arcgis/products/ar'''

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
