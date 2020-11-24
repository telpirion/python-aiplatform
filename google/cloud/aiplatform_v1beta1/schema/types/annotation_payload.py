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
from google.cloud.aiplatform_v1beta1.schema.types import geometry
from google.protobuf import duration_pb2 as duration  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1.schema",
    marshal="google.cloud.aiplatform.v1beta1",
    manifest={
        "ImageClassificationAnnotation",
        "ImageBoundingBoxAnnotation",
        "ImageSegmentationAnnotation",
        "TextClassificationAnnotation",
        "TextExtractionAnnotation",
        "TextSegment",
        "TextSentimentAnnotation",
        "VideoClassificationAnnotation",
        "TimeSegment",
        "VideoObjectTrackingAnnotation",
        "VideoActionRecognitionAnnotation",
    },
)


class ImageClassificationAnnotation(proto.Message):
    r"""Annotation details specific to image classification.

    Attributes:
        annotation_spec_id (str):
            The resource Id of the AnnotationSpec that
            this Annotation pertains to.
        display_name (str):
            The display name of the AnnotationSpec that
            this Annotation pertains to.
    """

    annotation_spec_id = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)


class ImageBoundingBoxAnnotation(proto.Message):
    r"""Annotation details specific to image object detection.

    Attributes:
        annotation_spec_id (str):
            The resource Id of the AnnotationSpec that
            this Annotation pertains to.
        display_name (str):
            The display name of the AnnotationSpec that
            this Annotation pertains to.
        x_min (float):
            The leftmost coordinate of the bounding box.
        x_max (float):
            The rightmost coordinate of the bounding box.
        y_min (float):
            The topmost coordinate of the bounding box.
        y_max (float):
            The bottommost coordinate of the bounding
            box.
    """

    annotation_spec_id = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)

    x_min = proto.Field(proto.DOUBLE, number=3)

    x_max = proto.Field(proto.DOUBLE, number=4)

    y_min = proto.Field(proto.DOUBLE, number=5)

    y_max = proto.Field(proto.DOUBLE, number=6)


class ImageSegmentationAnnotation(proto.Message):
    r"""Annotation details specific to image segmentation.

    Attributes:
        mask_annotation (~.annotation_payload.ImageSegmentationAnnotation.MaskAnnotation):
            Mask based segmentation annotation. Only one
            mask annotation can exist for one image.
        polygon_annotation (~.annotation_payload.ImageSegmentationAnnotation.PolygonAnnotation):
            Polygon annotation.
        polyline_annotation (~.annotation_payload.ImageSegmentationAnnotation.PolylineAnnotation):
            Polyline annotation.
    """

    class MaskAnnotation(proto.Message):
        r"""The mask based segmentation annotation.

        Attributes:
            mask_gcs_uri (str):
                Google Cloud Storage URI that points to the mask image. The
                image must be in PNG format. It must have the same size as
                the DataItem's image. Each pixel in the image mask
                represents the AnnotationSpec which the pixel in the image
                DataItem belong to. Each color is mapped to one
                AnnotationSpec based on annotation_spec_colors.
            annotation_spec_colors (Sequence[~.annotation_spec_color.AnnotationSpecColor]):
                The mapping between color and AnnotationSpec
                for this Annotation.
        """

        mask_gcs_uri = proto.Field(proto.STRING, number=1)

        annotation_spec_colors = proto.RepeatedField(
            proto.MESSAGE, number=2, message=annotation_spec_color.AnnotationSpecColor,
        )

    class PolygonAnnotation(proto.Message):
        r"""Represents a polygon in image.

        Attributes:
            vertexes (Sequence[~.geometry.Vertex]):
                The vertexes are connected one by one and the
                last vertex is connected to the first one to
                represent a polygon.
            annotation_spec_id (str):
                The resource Id of the AnnotationSpec that
                this Annotation pertains to.
            display_name (str):
                The display name of the AnnotationSpec that
                this Annotation pertains to.
        """

        vertexes = proto.RepeatedField(
            proto.MESSAGE, number=1, message=geometry.Vertex,
        )

        annotation_spec_id = proto.Field(proto.STRING, number=2)

        display_name = proto.Field(proto.STRING, number=3)

    class PolylineAnnotation(proto.Message):
        r"""Represents a polyline in image.

        Attributes:
            vertexes (Sequence[~.geometry.Vertex]):
                The vertexes are connected one by one and the
                last vertex in not connected to the first one.
            annotation_spec_id (str):
                The resource Id of the AnnotationSpec that
                this Annotation pertains to.
            display_name (str):
                The display name of the AnnotationSpec that
                this Annotation pertains to.
        """

        vertexes = proto.RepeatedField(
            proto.MESSAGE, number=1, message=geometry.Vertex,
        )

        annotation_spec_id = proto.Field(proto.STRING, number=2)

        display_name = proto.Field(proto.STRING, number=3)

    mask_annotation = proto.Field(
        proto.MESSAGE, number=3, oneof="annotation", message=MaskAnnotation,
    )

    polygon_annotation = proto.Field(
        proto.MESSAGE, number=4, oneof="annotation", message=PolygonAnnotation,
    )

    polyline_annotation = proto.Field(
        proto.MESSAGE, number=5, oneof="annotation", message=PolylineAnnotation,
    )


class TextClassificationAnnotation(proto.Message):
    r"""Annotation details specific to text classification.

    Attributes:
        annotation_spec_id (str):
            The resource Id of the AnnotationSpec that
            this Annotation pertains to.
        display_name (str):
            The display name of the AnnotationSpec that
            this Annotation pertains to.
    """

    annotation_spec_id = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)


class TextExtractionAnnotation(proto.Message):
    r"""Annotation details specific to text extraction.

    Attributes:
        text_segment (~.annotation_payload.TextSegment):
            The segment of the text content.
        annotation_spec_id (str):
            The resource Id of the AnnotationSpec that
            this Annotation pertains to.
        display_name (str):
            The display name of the AnnotationSpec that
            this Annotation pertains to.
    """

    text_segment = proto.Field(proto.MESSAGE, number=1, message="TextSegment",)

    annotation_spec_id = proto.Field(proto.STRING, number=2)

    display_name = proto.Field(proto.STRING, number=3)


class TextSegment(proto.Message):
    r"""The text segment inside of DataItem.

    Attributes:
        start_offset (int):
            Zero-based character index of the first
            character of the text segment (counting
            characters from the beginning of the text).
        end_offset (int):
            Zero-based character index of the first character past the
            end of the text segment (counting character from the
            beginning of the text). The character at the end_offset is
            NOT included in the text segment.
        content (str):
            The text content in the segment for output
            only.
    """

    start_offset = proto.Field(proto.UINT64, number=1)

    end_offset = proto.Field(proto.UINT64, number=2)

    content = proto.Field(proto.STRING, number=3)


class TextSentimentAnnotation(proto.Message):
    r"""Annotation details specific to text sentiment.

    Attributes:
        sentiment (int):
            The sentiment score for text.
        sentiment_max (int):
            The sentiment max score for text.
        annotation_spec_id (str):
            The resource Id of the AnnotationSpec that
            this Annotation pertains to.
        display_name (str):
            The display name of the AnnotationSpec that
            this Annotation pertains to.
    """

    sentiment = proto.Field(proto.INT32, number=1)

    sentiment_max = proto.Field(proto.INT32, number=2)

    annotation_spec_id = proto.Field(proto.STRING, number=3)

    display_name = proto.Field(proto.STRING, number=4)


class VideoClassificationAnnotation(proto.Message):
    r"""Annotation details specific to video classification.

    Attributes:
        time_segment (~.annotation_payload.TimeSegment):
            This Annotation applies to the time period
            represented by the TimeSegment. If it's not set,
            the Annotation applies to the whole video.
        annotation_spec_id (str):
            The resource Id of the AnnotationSpec that
            this Annotation pertains to.
        display_name (str):
            The display name of the AnnotationSpec that
            this Annotation pertains to.
    """

    time_segment = proto.Field(proto.MESSAGE, number=1, message="TimeSegment",)

    annotation_spec_id = proto.Field(proto.STRING, number=2)

    display_name = proto.Field(proto.STRING, number=3)


class TimeSegment(proto.Message):
    r"""A time period inside of a DataItem that has a time dimension
    (e.g. video).

    Attributes:
        start_time_offset (~.duration.Duration):
            Start of the time segment (inclusive),
            represented as the duration since the start of
            the DataItem.
        end_time_offset (~.duration.Duration):
            End of the time segment (exclusive),
            represented as the duration since the start of
            the DataItem.
    """

    start_time_offset = proto.Field(proto.MESSAGE, number=1, message=duration.Duration,)

    end_time_offset = proto.Field(proto.MESSAGE, number=2, message=duration.Duration,)


class VideoObjectTrackingAnnotation(proto.Message):
    r"""Annotation details specific to video object tracking.

    Attributes:
        time_offset (~.duration.Duration):
            A time (frame) of a video to which this
            annotation pertains. Represented as the duration
            since the video's start.
        x_min (float):
            The leftmost coordinate of the bounding box.
        x_max (float):
            The rightmost coordinate of the bounding box.
        y_min (float):
            The topmost coordinate of the bounding box.
        y_max (float):
            The bottommost coordinate of the bounding
            box.
        instance_id (int):
            The instance of the object, expressed as a
            positive integer. Used to track the same object
            across different frames.
        annotation_spec_id (str):
            The resource Id of the AnnotationSpec that
            this Annotation pertains to.
        display_name (str):
            The display name of the AnnotationSpec that
            this Annotation pertains to.
    """

    time_offset = proto.Field(proto.MESSAGE, number=1, message=duration.Duration,)

    x_min = proto.Field(proto.DOUBLE, number=2)

    x_max = proto.Field(proto.DOUBLE, number=3)

    y_min = proto.Field(proto.DOUBLE, number=4)

    y_max = proto.Field(proto.DOUBLE, number=5)

    instance_id = proto.Field(proto.INT64, number=6)

    annotation_spec_id = proto.Field(proto.STRING, number=7)

    display_name = proto.Field(proto.STRING, number=8)


class VideoActionRecognitionAnnotation(proto.Message):
    r"""Annotation details specific to video action recognition.

    Attributes:
        time_segment (~.annotation_payload.TimeSegment):
            This Annotation applies to the time period
            represented by the TimeSegment. If it's not set,
            the Annotation applies to the whole video.
        annotation_spec_id (str):
            The resource Id of the AnnotationSpec that
            this Annotation pertains to.
        display_name (str):
            The display name of the AnnotationSpec that
            this Annotation pertains to.
    """

    time_segment = proto.Field(proto.MESSAGE, number=1, message="TimeSegment",)

    annotation_spec_id = proto.Field(proto.STRING, number=2)

    display_name = proto.Field(proto.STRING, number=3)


__all__ = tuple(sorted(__protobuf__.manifest))
