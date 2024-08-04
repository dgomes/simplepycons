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


class NetteIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nette"

    @property
    def original_file_name(self) -> "str":
        return "nette.svg"

    @property
    def title(self) -> "str":
        return "Nette"

    @property
    def primary_color(self) -> "str":
        return "#3484D2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nette</title>
     <path d="M6.244
 14.334c-.341.243-.558.39-.65.443-.488.29-.934.437-1.338.437-.226
 0-.446-.053-.663-.155a1.17 1.17 0 0 1-.486-.403.988.988 0 0
 1-.162-.556c0-.292.099-.663.296-1.113.282-.658.433-1.01.452-1.057a.497.497
 0 0 1-.015-.127 2.511 2.511 0 0 0-.268.127 7.1 7.1 0 0 0-.774.578
 13.77 13.77 0 0 0-.691.676 6.005 6.005 0 0 0-.085 1.001c0
 .253.015.507.043.761l-1.705.268A6.198 6.198 0 0 1 0
 13.706c0-.292.028-.588.085-.889.056-.3.16-.638.309-1.014.104-.263.249-.592.437-.987l1.959-.324c-.122.301-.211.526-.267.677a9.26
 9.26 0 0 0-.254.691c.47-.433.94-.767 1.409-1.001.376-.188.714-.282
 1.015-.282.17 0
 .343.032.522.098.178.066.307.17.387.311.08.141.12.309.12.507 0
 .282-.08.629-.24 1.043-.188.47-.371.939-.549 1.409 0
 .066.024.106.07.12a.49.49 0 0 0 .141.02c.189 0
 .469-.098.841-.294a1.74 1.74 0 0
 1-.052-.424c0-.226.032-.441.098-.648.066-.207.166-.423.297-.648.234-.386.564-.714.986-.987a3.45
 3.45 0 0 1 1.339-.521c.17-.019.3-.029.395-.029.31 0
 .587.052.831.156.244.103.446.272.606.507.094.15.141.301.141.45 0
 .236-.117.466-.352.691-.169.16-.397.311-.684.451a6.777 6.777 0 0
 1-.853.352c-.206.066-.498.147-.873.24.122.254.296.459.522.614.225.154.464.232.718.232.386
 0 .771-.099 1.156-.296.018-.01.312-.195.883-.557a4.035 4.035 0 0 1
 .096-.641l.047-.214 2.035-.121-.151.525a1.982 1.982 0 0 0-.092.529c0
 .226.045.383.135.471.089.09.217.135.387.135.244 0
 .563-.103.958-.31l.454-.274c.003-.075.009-.156.018-.241.014-.135.043-.303.084-.5l.048-.213
 2.034-.122c-.048.17-.098.345-.151.525-.06.211-.092.388-.092.529 0
 .226.045.383.135.471.089.09.218.135.387.135.245 0
 .565-.103.959-.31l.294-.178a1.505 1.505 0 0
 1-.013-.203c0-.226.034-.441.099-.648.066-.207.165-.423.296-.648.234-.386.564-.714.986-.987.424-.272.87-.447
 1.339-.521.17-.019.302-.029.396-.029.309 0
 .586.052.831.156.243.103.446.272.605.507.094.15.141.301.141.45 0
 .236-.117.466-.352.691-.168.16-.396.311-.683.451a6.902 6.902 0 0
 1-.853.352c-.207.066-.498.147-.874.24.122.254.296.459.522.614.226.154.465.232.718.232.386
 0 .771-.099
 1.156-.296.019-.01.338-.211.958-.606v.634c-.056.038-.281.198-.675.479a4.575
 4.575 0 0 1-.72.437c-.47.207-.987.31-1.55.31-.375
 0-.709-.045-1.001-.133a2.078 2.078 0 0 1-.803-.473 1.58 1.58 0 0
 1-.357-.456c-.414.3-.732.513-.954.64-.497.281-.949.422-1.352.422-.227
 0-.41-.014-.62-.113-.358-.15-.607-.345-.748-.584a1.504 1.504 0 0
 1-.158-.397c-.435.316-.768.54-.997.672-.498.281-.949.422-1.353.422-.227
 0-.41-.014-.62-.113-.358-.15-.606-.345-.748-.584a1.505 1.505 0 0
 1-.177-.493c-.099.067-.307.216-.625.443a4.667 4.667 0 0
 1-.719.437c-.47.207-.987.31-1.55.31-.377 0-.71-.045-1.001-.133a2.089
 2.089 0 0 1-.804-.473 1.66 1.66 0 0 1-.224-.245zm2.832-2.574a.786.786
 0 0 0 .013-.169c0-.244-.102-.366-.309-.366a.757.757 0 0
 0-.155.028c-.282.066-.503.245-.663.536a1.885 1.885 0 0
 0-.239.915c.395-.102.681-.206.859-.309.292-.16.456-.371.494-.635zm12.782
 0a.715.715 0 0 0 .014-.169c0-.244-.103-.366-.31-.366a.768.768 0 0
 0-.155.028c-.281.066-.503.245-.662.536-.16.291-.24.597-.24.915.395-.102.682-.206.86-.309.291-.16.455-.371.493-.635zm-10.838.043l.283-1.113.578-.028.549-1.509
 2.085-.366-.591 1.776.944-.043-.253
 1.057c-1.198.082-2.395.155-3.595.226zm3.877
 0l.281-1.113.578-.028.549-1.509 2.086-.366-.592 1.776.944-.043-.253
 1.057c-1.201.082-2.408.156-3.593.226z" />
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