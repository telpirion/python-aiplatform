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


from google.cloud.aiplatform_v1beta1.schema.types import annotation_spec_color


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1.schema",
    marshal="google.cloud.aiplatform.v1beta1",
    manifest={
        "TextSentimentSavedQueryMetadata",
        "VisualInspectionClassificationLabelSavedQueryMetadata",
        "VisualInspectionMaskSavedQueryMetadata",
    },
)


class TextSentimentSavedQueryMetadata(proto.Message):
    r"""The metadata of SavedQuery contains TextSentiment
    Annotations.

    Attributes:
        sentiment_max (int):
            The maximum sentiment of sentiment Anntoation
            in this SavedQuery.
    """

    sentiment_max = proto.Field(proto.INT32, number=1)


class VisualInspectionClassificationLabelSavedQueryMetadata(proto.Message):
    r"""

    Attributes:
        multi_label (bool):
            Whether or not the classification label is multi_label.
    """

    multi_label = proto.Field(proto.BOOL, number=1)


class VisualInspectionMaskSavedQueryMetadata(proto.Message):
    r"""

    Attributes:
        color_map (Sequence[~.annotation_spec_color.AnnotationSpecColor]):
            The mapping between color and AnnotationSpec
            for this SavedQuery.
    """

    color_map = proto.RepeatedField(
        proto.MESSAGE, number=2, message=annotation_spec_color.AnnotationSpecColor,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
