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


class DotaTwoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dota2"

    @property
    def original_file_name(self) -> "str":
        return "dota2.svg"

    @property
    def title(self) -> "str":
        return "Dota 2"

    @property
    def primary_color(self) -> "str":
        return "#BF2E1A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Dota 2</title>
     <path d="M 9.817 23.607 L 9.471 23.313 L 9.003 23.273 C 8.419
 23.225 8.147 23.172 7.817 23.041 L 7.559 22.938 L 7.281 23.048 C
 7.045 23.143 6.467 23.229 6.028 23.236 C 6.004 23.236 5.964 23.18
 5.939 23.111 C 5.911 23.041 5.862 22.974 5.824 22.961 C 5.789 22.949
 5.527 23.007 5.237 23.094 L 4.712 23.252 L 4.523 23.161 C 4.285
 23.045 4.185 23.047 3.787 23.168 C 3.484 23.262 3.446 23.264 3.203
 23.212 C 2.84 23.136 2.537 23.141 1.854 23.238 C 1.11 23.344 1.094
 23.344 0.875 23.194 C 0.728 23.094 0.648 23.069 0.469 23.069 C 0.266
 23.069 0.244 23.06 0.221 22.965 C 0.206 22.906 0.225 22.787 0.264
 22.688 C 0.376 22.41 0.42 21.736 0.432 20.125 L 0.444 18.62 L 0.655
 18.635 L 0.863 18.65 L 0.895 17.78 C 0.911 17.302 0.927 16.611 0.93
 16.246 L 0.935 15.586 L 0.823 15.506 C 0.518 15.283 0.532 15.315
 0.405 14.588 C 0.339 14.211 0.274 13.658 0.259 13.358 C 0.234 12.826
 0.236 12.811 0.334 12.7 L 0.434 12.586 L 0.682 12.799 C 0.82 12.916
 0.937 12.993 0.948 12.969 C 0.984 12.856 0.871 11.508 0.813 11.338 C
 0.775 11.238 0.747 11.101 0.747 11.03 C 0.747 10.962 0.679 10.778
 0.594 10.618 L 0.443 10.329 L 0.494 9.816 C 0.561 9.136 0.475 8.636
 0.19 8.034 L 0.065 7.763 L 0.144 7.09 L 0.228 6.416 L 0.14 6.067 L
 0.049 5.717 L 0.154 5.326 L 0.255 4.933 L 0.14 4.553 L 0.021 4.174 L
 0.164 3.774 C 0.305 3.385 0.308 3.364 0.305 2.73 C 0.303 2.016 0.228
 1.551 0.08 1.365 C -0.047 1.203 -0.026 1.092 0.163 0.919 C 0.253
 0.834 0.328 0.726 0.328 0.681 C 0.328 0.612 0.359 0.599 0.549 0.595 C
 0.669 0.595 1.039 0.563 1.372 0.525 L 1.979 0.452 L 2.773 0.569 C
 3.565 0.684 3.566 0.684 4.652 0.638 L 5.74 0.591 L 5.997 0.746 L
 6.257 0.899 L 7.312 0.884 L 8.368 0.869 L 8.724 0.74 C 8.918 0.669
 9.229 0.545 9.414 0.461 C 9.596 0.377 9.927 0.264 10.144 0.204 L
 10.542 0.099 L 11.056 0.261 L 11.57 0.425 L 12.014 0.276 L 12.456
 0.127 L 12.933 0.285 C 13.196 0.371 13.684 0.583 14.022 0.757 L
 14.633 1.069 L 15.273 1.051 C 15.758 1.036 15.924 1.018 15.95 0.973 C
 15.97 0.942 16.031 0.758 16.083 0.566 L 16.178 0.215 L 16.783 0.235 C
 17.236 0.251 17.642 0.299 18.384 0.429 L 19.379 0.605 L 19.638 0.501
 C 19.778 0.444 20.046 0.375 20.233 0.351 C 20.546 0.309 20.6 0.314
 21.027 0.422 C 21.425 0.522 21.562 0.537 22.109 0.537 C 22.454 0.537
 22.812 0.522 22.907 0.506 C 23.07 0.478 23.097 0.489 23.428 0.728 C
 23.621 0.866 23.792 1.001 23.807 1.03 C 23.824 1.057 23.86 1.203
 23.884 1.354 L 23.93 1.632 L 23.721 2.028 C 23.604 2.246 23.507 2.443
 23.507 2.466 C 23.507 2.489 23.555 2.527 23.611 2.554 C 23.668 2.579
 23.764 2.677 23.826 2.771 L 23.937 2.941 L 23.912 5.226 C 23.897
 6.483 23.872 7.604 23.858 7.715 L 23.831 7.919 L 23.486 7.897 L
 23.142 7.87 L 23.113 8.061 C 23.097 8.164 23.084 8.353 23.084 8.485 C
 23.084 8.677 23.054 8.778 22.924 9.031 L 22.761 9.342 L 22.851 9.471
 C 22.901 9.543 23.072 9.736 23.231 9.901 L 23.523 10.206 L 23.434
 10.529 L 23.344 10.854 L 23.451 11.542 C 23.575 12.369 23.566 12.577
 23.363 13.293 C 23.282 13.58 23.217 13.846 23.217 13.886 C 23.217
 13.961 23.272 13.98 23.644 14.031 C 23.809 14.052 23.844 14.072
 23.844 14.147 C 23.844 14.196 23.87 15.251 23.904 16.492 C 24.011
 20.567 24.021 21.456 23.971 22.38 C 23.944 22.862 23.913 23.262
 23.904 23.271 C 23.894 23.28 23.563 23.147 23.166 22.976 L 22.443
 22.668 L 22.131 22.803 C 21.809 22.942 21.777 22.978 21.735 23.245 C
 21.706 23.422 21.728 23.414 20.935 23.576 L 20.468 23.672 L 20.014
 23.52 C 19.594 23.379 19.537 23.369 19.206 23.391 C 18.959 23.406
 18.789 23.394 18.644 23.351 C 18.436 23.292 18.436 23.292 18.087
 23.453 L 17.735 23.612 L 16.435 23.612 C 15.066 23.61 14.784 23.632
 13.841 23.807 C 13.189 23.927 12.96 23.922 11.819 23.785 L 11.217
 23.711 L 10.796 23.807 C 10.562 23.861 10.326 23.903 10.27 23.901 C
 10.202 23.901 10.046 23.8 9.819 23.607 L 9.817 23.607 Z M 7.284
 19.918 C 8.289 19.539 9.118 19.223 9.123 19.216 C 9.136 19.202 5.206
 15.39 4.684 14.909 C 4.539 14.775 4.409 14.672 4.399 14.682 C 4.39
 14.693 4.07 15.547 3.69 16.577 C 3.27 17.715 3.011 18.476 3.032
 18.508 C 3.057 18.55 5.424 20.599 5.451 20.605 C 5.454 20.605 6.279
 20.296 7.284 19.918 Z M 20.796 17.829 C 21.319 16.564 21.732 15.519
 21.718 15.504 C 21.699 15.483 11.888 8.858 5.02 4.226 L 4.469 3.855 L
 3.569 4.262 C 3.072 4.484 2.673 4.687 2.68 4.709 C 2.69 4.737 6.011
 8.219 10.064 12.449 L 17.432 20.141 L 18.638 20.133 L 19.847 20.125 L
 20.796 17.829 Z M 19.434 6.972 C 19.607 6.01 19.75 5.191 19.75 5.151
 C 19.75 5.108 19.497 4.902 19.074 4.605 C 18.702 4.343 18.373 4.115
 18.344 4.096 C 18.291 4.063 14.442 5.104 14.447 5.149 C 14.451 5.179
 19.091 8.748 19.107 8.731 C 19.115 8.725 19.261 7.932 19.434 6.972 Z"
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
        return '''https://commons.wikimedia.org/wiki/File:Dota_'''

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
