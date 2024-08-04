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


class SidekiqIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sidekiq"

    @property
    def original_file_name(self) -> "str":
        return "sidekiq.svg"

    @property
    def title(self) -> "str":
        return "Sidekiq"

    @property
    def primary_color(self) -> "str":
        return "#B1003E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sidekiq</title>
     <path d="M9.639 23.767C4.145 22.67 0 17.815 0 12 0 5.377 5.377 0
 12 0c4.47 0 8.373 2.449 10.437
 6.078-.159.124-.425.289-.625.467-.183.162-.566.362-1.149.598-.366-.328-.607-.465-.722-.411-.174.081-1.435.742-2.023.919s-2.621
 1.601-3.156
 1.734c-.534.132-.984.284-1.218.461-.234.176-.526.105-.857.14-.167.018-.435.303-.924.434-.062.06-.114.163-.156.308-.328.957-.564
 1.586-.711 1.887-.146.3-.407.711-.784 1.232.312.356.467.6.467.733 0
 .2-.034 1.332-.143 1.863-.072.353-.145 2.126-.22 5.317 0
 .554-.055.896-.166 1.028-.167.197-.361.727-.361.871 0
 .026-.019.064-.05.108M22.747 6.659C23.549 8.268 24 10.082 24 12c0
 6.623-5.377 12-12 12-.53
 0-1.052-.034-1.564-.101.26-.328.445-.295.597-.434.151-.139.425-.514.288-.677-.092-.109-.137-.347-.137-.713.207-.122.365-.184.472-.184.161
 0
 .03-.574.239-1.178.14-.402.471-2.497.996-6.286.321-.946.539-1.465.653-1.556s.568-.477
 1.363-1.156c1.262-.781 1.966-1.235 2.111-1.361.219-.19 2.354-.798
 2.646-1.185.195-.258.608-.556
 1.241-.895v-.241c.398-.137.66-.205.783-.205.186 0
 .435.113.567-.177.133-.291.046-.615.231-.767.075-.061.169-.141.261-.225M9.253
 13.361c-.02.045-.029.074-.026.081-.047.233-.019.481 0
 .615.104.721-.598.905-.598.905l.37.319c.744-.136.744-1.083.744-1.083-.035-.131-.07-.56-.052-.678.002.001.436-.513.81-1.309.192-.409.374-.921.498-1.258.12-.326.143-.536.125-.595
 0 .02-.219-.072-.428-.129
 0-.004.001-.007.001-.011l-.376-.345c.899-.346 1.41-.598
 1.533-.757.184-.238.516-.958.516-1.231
 0-.181.027-.812.08-1.891-.526.066-.832.066-.92
 0-.132-.099-.256-.493-.256-.826
 0-.221-.068-.52-.205-.896l-.372-.103c-.056-.276-.115-.415-.178-.415q-.093
 0-.198.198c-.079.303-.118.492-.118.566 0
 .11-.08.424.118.65.132.151.288.427.466.826-.111.409-.111.669 0
 .781.167.167 0 .388 0 .516q0
 .1275-.09.594c-1.023.177-1.608.236-1.757.177s-.384.005-.706.193l-.409.392c.07-.302.07-.525
 0-.666-.106-.213-.165-.347-.165-.54 0-.08-.111-.264-.111-.397
 0-.054.015-.144.045-.269l-.291-.276c.068-.003.107-.023.115-.058q.0135-.0525-.189-.141c-.956.048-1.579.237-1.87.568-.291.33-.313.792-.067
 1.387.172.283.32.491.446.623.126.131.319.272.58.422l-.343.195-.237.723-.576
 1.053-.959 2.359-.185.564c.124.733.234 1.142.329
 1.226.094.084.267.118.519.103.253.282.417.382.493.302.03-.032.078-.079.056-.234-.01-.07-.107-.205-.099-.296.007-.087.089-.185.116-.373.011-.081.011-.238
 0-.469l1.519-1.556.874.185 1.154.205z" />
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
