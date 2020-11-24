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


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1.schema",
    marshal="google.cloud.aiplatform.v1beta1",
    manifest={"ImageDataItem", "VideoDataItem", "TextDataItem",},
)


class ImageDataItem(proto.Message):
    r"""Payload of Image DataItem.

    Attributes:
        gcs_uri (str):
            Required. Google Cloud Storage URI points to
            the original image in user's bucket. The image
            is up to 30MB in size.
        mime_type (str):
            Output only. The mime type of the content of
            the image. Only the images in below listed mime
            types are supported. - image/jpeg
            - image/gif
            - image/png
            - image/webp
            - image/bmp
            - image/tiff
            - image/vnd.microsoft.icon
    """

    gcs_uri = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)


class VideoDataItem(proto.Message):
    r"""Payload of Video DataItem.

    Attributes:
        gcs_uri (str):
            Required. Google Cloud Storage URI points to
            the original video in user's bucket. The video
            is up to 50 GB in size and up to 3 hour in
            duration.
        mime_type (str):
            Output only. The mime type of the content of the video. Only
            the videos in below listed mime types are supported.
            Supported mime_type:

            -  video/mp4
            -  video/avi
            -  video/quicktime
    """

    gcs_uri = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)


class TextDataItem(proto.Message):
    r"""Payload of Text DataItem.

    Attributes:
        gcs_uri (str):
            Output only. Google Cloud Storage URI points
            to the original text in user's bucket. The text
            file is up to 10MB in size.
    """

    gcs_uri = proto.Field(proto.STRING, number=1)


__all__ = tuple(sorted(__protobuf__.manifest))
