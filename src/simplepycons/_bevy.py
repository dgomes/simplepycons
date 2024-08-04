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


class BevyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bevy"

    @property
    def original_file_name(self) -> "str":
        return "bevy.svg"

    @property
    def title(self) -> "str":
        return "Bevy"

    @property
    def primary_color(self) -> "str":
        return "#232326"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bevy</title>
     <path d="M18.8 6.271a3.149 3.149 0 0
 0-.765.081c-.018.004-.033.01-.05.013-.29.288-.616.576-.963.859.115.536.308
 1.053.572 1.534.51.913.93 1.402 1.175 2.036.247.633.29 1.38.06
 2.737-.283 1.685-1.307 3.469-2.933 4.785 1.262-.368 2.337-1.047
 3.049-1.87.769-.887 1.025-1.39
 1.115-1.895.09-.506.006-1.061.04-2.003.024-.547.131-1.088.318-1.603l.04-.112.117-.015c1.052-.137
 2.003-.406
 2.494-.722-.158-.71-.828-1.26-1.717-1.68l-.084-.04-.021-.09c-.282-1.209-1.226-1.989-2.448-2.015Zm.61
 1.494c.064 0 .126.01.185.028a.622.622 0 0 1 .396.786.622.622 0 0
 1-.778.412.622.622 0 0 1-.396-.787.627.627 0 0 1
 .594-.439zm-5.69-4.61c-.764-.006-1.547.3-2.22.952-.884.858-1.158
 1.63-1.003
 2.594l.042.265-.263-.043c-1.942-.315-4.345-.156-7.078.95.804.344
 2.278.919 3.915 1.704l.52.25-.565.115C4.907 10.38 2.342 11.645 0
 14.407c1.048-.082 3.189-.334 5.423-.33 1.241.002 2.465.088
 3.462.346.996.258 1.903.85 2.03 1.283.128.433.055.662-.07
 1-.126.34-.512.854-1.048
 1.194-.534.341-1.213.638-1.92.89-1.41.505-2.91.828-3.573.89-.14.013-.197.063-.25.162a.972.972
 0 0 0-.09.416c-.006.215.028.329.09.414.06.086.156.12.254.127
 4.165.281 7.278-.766 9.54-1.663 2.6-1.193 4.244-3.548
 4.601-5.668.224-1.329.176-1.98-.04-2.534-.216-.555-.629-1.047-1.153-1.988a6.15
 6.15 0 0 1-.642-1.75l-.024-.116.092-.074c.964-.772 1.75-1.615
 2.034-2.23-.585-.622-1.594-.753-2.726-.632l-.092.01-.066-.067c-.602-.614-1.35-.929-2.113-.933Zm.337
 1.434a.717.717 0 0 1 .704.553.712.712 0 0 1-.517.865.713.713 0 0
 1-.856-.533.713.713 0 0 1 .669-.885Zm6.677
 6.669h-.006c-.14.421-.221.86-.241 1.303-.034.911.058 1.465-.047
 2.056-.105.59-.414 1.17-1.204 2.08-.937 1.085-2.424 1.924-4.143
 2.207a8.908 8.908 0 0 1-1.012.559c1.337.503 2.736.531 3.844.166
 1.953-.64 1.802-1.101 2.677-2.442.276-.422.594-.745.913-1.01.911.398
 1.808.652
 2.366.59.301-.697-.006-1.505-.517-2.27.419-1.303-.218-2.606-1.628-3.068a3.043
 3.043 0 0 0-1.002-.171zM22.2 13.35c.194.22.169.56-.057.758a.538.538 0
 0 1-.759-.042.538.538 0 0 1 .055-.759.56.56 0 0 1 .366-.136.523.523 0
 0 1 .395.179z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/bevyengine/bevy/blob/371c9
0f6faecf318ff66e3c6efa6f9f48781f63f/assets/branding/bevy_bird_simpleic'''

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