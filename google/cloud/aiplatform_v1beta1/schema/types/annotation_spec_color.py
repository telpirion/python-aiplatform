# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import proto  # type: ignore


from google.type import color_pb2 as gt_color  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1.schema",
    marshal="google.cloud.aiplatform.v1beta1",
    manifest={"AnnotationSpecColor",},
)


class AnnotationSpecColor(proto.Message):
    r"""An entry of mapping between color and AnnotationSpec. The
    mapping is used in segmentation mask.

    Attributes:
        color (~.gt_color.Color):
            The color of the AnnotationSpec in a
            segmentation mask.
        display_name (str):
            The display name of the AnnotationSpec
            represented by the color in the segmentation
            mask.
        id (str):
            The ID of the AnnotationSpec represented by
            the color in the segmentation mask.
    """

    color = proto.Field(proto.MESSAGE, number=1, message=gt_color.Color,)

    display_name = proto.Field(proto.STRING, number=2)

    id = proto.Field(proto.STRING, number=3)


__all__ = tuple(sorted(__protobuf__.manifest))
