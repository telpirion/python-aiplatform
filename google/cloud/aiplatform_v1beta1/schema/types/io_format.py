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


from google.protobuf import duration_pb2 as duration  # type: ignore
from google.protobuf import struct_pb2 as struct  # type: ignore
from google.protobuf import wrappers_pb2 as wrappers  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.aiplatform.v1beta1.schema",
    marshal="google.cloud.aiplatform.v1beta1",
    manifest={
        "ImageClassificationPredictionInstance",
        "ImageObjectDetectionPredictionInstance",
        "ImageSegmentationPredictionInstance",
        "VideoClassificationPredictionInstance",
        "VideoObjectTrackingPredictionInstance",
        "VideoActionRecognitionPredictionInstance",
        "TextClassificationPredictionInstance",
        "TextSentimentPredictionInstance",
        "TextExtractionPredictionInstance",
        "ImageClassificationPredictionParams",
        "ImageObjectDetectionPredictionParams",
        "ImageSegmentationPredictionParams",
        "VideoClassificationPredictionParams",
        "VideoObjectTrackingPredictionParams",
        "VideoActionRecognitionPredictionParams",
        "PredictionResult",
        "TextSentimentPredictionResult",
        "ClassificationPredictionResult",
        "ImageObjectDetectionPredictionResult",
        "VideoClassificationPredictionResult",
        "VideoObjectTrackingPredictionResult",
        "TextExtractionPredictionResult",
    },
)


class ImageClassificationPredictionInstance(proto.Message):
    r"""Prediction input format for Image Classification.

    Attributes:
        content (str):
            The image bytes or GCS URI to make the
            prediction on.
        mime_type (str):
            The MIME type of the content of the image.
            Only the images in below listed MIME types are
            supported. - image/jpeg
            - image/gif
            - image/png
            - image/webp
            - image/bmp
            - image/tiff
            - image/vnd.microsoft.icon
    """

    content = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)


class ImageObjectDetectionPredictionInstance(proto.Message):
    r"""Prediction input format for Image Object Detection.

    Attributes:
        content (str):
            The image bytes or GCS URI to make the
            prediction on.
        mime_type (str):
            The MIME type of the content of the image.
            Only the images in below listed MIME types are
            supported. - image/jpeg
            - image/gif
            - image/png
            - image/webp
            - image/bmp
            - image/tiff
            - image/vnd.microsoft.icon
    """

    content = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)


class ImageSegmentationPredictionInstance(proto.Message):
    r"""Prediction input format for Image Segmentation.

    Attributes:
        content (str):
            The image bytes to make the predictions on.
        mime_type (str):
            The MIME type of the content of the image.
            Only the images in below listed MIME types are
            supported. - image/jpeg
            - image/png
    """

    content = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)


class VideoClassificationPredictionInstance(proto.Message):
    r"""Prediction input format for Video Classification.

    Attributes:
        content (str):
            The Google Cloud Storage location of the
            video on which to perform the prediction.
        mime_type (str):
            The MIME type of the content of the video.
            Only the following are supported: video/mp4
            video/avi video/quicktime
        time_segment_start (str):
            The beginning, inclusive, of the video's time
            segment on which to perform the prediction.
            Expressed as a number of seconds as measured
            from the start of the video, with "s" appended
            at the end. Fractions are allowed, up to a
            microsecond precision.
        time_segment_end (str):
            The end, exclusive, of the video's time
            segment on which to perform the prediction.
            Expressed as a number of seconds as measured
            from the start of the video, with "s" appended
            at the end. Fractions are allowed, up to a
            microsecond precision, and "Infinity" is
            allowed, which means the end of the video.
    """

    content = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)

    time_segment_start = proto.Field(proto.STRING, number=3)

    time_segment_end = proto.Field(proto.STRING, number=4)


class VideoObjectTrackingPredictionInstance(proto.Message):
    r"""Prediction input format for Video Classification.

    Attributes:
        content (str):
            The Google Cloud Storage location of the
            video on which to perform the prediction.
        mime_type (str):
            The MIME type of the content of the video.
            Only the following are supported: video/mp4
            video/avi video/quicktime
        time_segment_start (str):
            The beginning, inclusive, of the video's time
            segment on which to perform the prediction.
            Expressed as a number of seconds as measured
            from the start of the video, with "s" appended
            at the end. Fractions are allowed, up to a
            microsecond precision.
        time_segment_end (str):
            The end, exclusive, of the video's time
            segment on which to perform the prediction.
            Expressed as a number of seconds as measured
            from the start of the video, with "s" appended
            at the end. Fractions are allowed, up to a
            microsecond precision, and "Infinity" is
            allowed, which means the end of the video.
    """

    content = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)

    time_segment_start = proto.Field(proto.STRING, number=3)

    time_segment_end = proto.Field(proto.STRING, number=4)


class VideoActionRecognitionPredictionInstance(proto.Message):
    r"""Prediction input format for Video Action Recognition.

    Attributes:
        content (str):
            The Google Cloud Storage location of the
            video on which to perform the prediction.
        mime_type (str):
            The MIME type of the content of the video.
            Only the following are supported: video/mp4
            video/avi video/quicktime
        time_segment_start (str):
            The beginning, inclusive, of the video's time
            segment on which to perform the prediction.
            Expressed as a number of seconds as measured
            from the start of the video, with "s" appended
            at the end. Fractions are allowed, up to a
            microsecond precision.
        time_segment_end (str):
            The end, exclusive, of the video's time
            segment on which to perform the prediction.
            Expressed as a number of seconds as measured
            from the start of the video, with "s" appended
            at the end. Fractions are allowed, up to a
            microsecond precision, and "Infinity" is
            allowed, which means the end of the video.
    """

    content = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)

    time_segment_start = proto.Field(proto.STRING, number=3)

    time_segment_end = proto.Field(proto.STRING, number=4)


class TextClassificationPredictionInstance(proto.Message):
    r"""Prediction input format for Text Classification.

    Attributes:
        content (str):
            The text snippet to make the predictions on.
        mime_type (str):
            The MIME type of the text snippet. The
            supported MIME types are listed below.
            - text/plain
    """

    content = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)


class TextSentimentPredictionInstance(proto.Message):
    r"""Prediction input format for Text Sentiment.

    Attributes:
        content (str):
            The text snippet to make the predictions on.
        mime_type (str):
            The MIME type of the text snippet. The
            supported MIME types are listed below.
            - text/plain
    """

    content = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)


class TextExtractionPredictionInstance(proto.Message):
    r"""Prediction input format for Text Extraction.

    Attributes:
        content (str):
            The text snippet to make the predictions on.
        mime_type (str):
            The MIME type of the text snippet. The
            supported MIME types are listed below.
            - text/plain
        key (str):
            This field is only used for batch prediction.
            If a key is provided, the batch prediction
            result will by mapped to this key. If omitted,
            then the batch prediction result will contain
            the entire input instance. AI Platform will not
            check if keys in the request are duplicates, so
            it is up to the caller to ensure the keys are
            unique.
    """

    content = proto.Field(proto.STRING, number=1)

    mime_type = proto.Field(proto.STRING, number=2)

    key = proto.Field(proto.STRING, number=3)


class ImageClassificationPredictionParams(proto.Message):
    r"""Prediction model parameters for Image Classification.

    Attributes:
        confidence_threshold (float):
            The Model only returns predictions with at
            least this confidence score. Default value is
            0.0
        max_predictions (int):
            The Model only returns up to that many top,
            by confidence score, predictions per instance.
            If this number is very high, the Model may
            return fewer predictions. Default value is 10.
    """

    confidence_threshold = proto.Field(proto.FLOAT, number=1)

    max_predictions = proto.Field(proto.INT32, number=2)


class ImageObjectDetectionPredictionParams(proto.Message):
    r"""Prediction model parameters for Image Object Detection.

    Attributes:
        confidence_threshold (float):
            The Model only returns predictions with at
            least this confidence score. Default value is
            0.0
        max_predictions (int):
            The Model only returns up to that many top,
            by confidence score, predictions per instance.
            Note that number of returned predictions is also
            limited by metadata's predictionsLimit. Default
            value is 10.
    """

    confidence_threshold = proto.Field(proto.FLOAT, number=1)

    max_predictions = proto.Field(proto.INT32, number=2)


class ImageSegmentationPredictionParams(proto.Message):
    r"""Prediction model parameters for Image Segmentation.

    Attributes:
        confidence_threshold (float):
            When the model predicts category of pixels of
            the image, it will only provide predictions for
            pixels that it is at least this much confident
            about. All other pixels will be classified as
            background. Default value is 0.5.
    """

    confidence_threshold = proto.Field(proto.FLOAT, number=1)


class VideoClassificationPredictionParams(proto.Message):
    r"""Prediction model parameters for Video Classification.

    Attributes:
        confidence_threshold (float):
            The Model only returns predictions with at
            least this confidence score. Default value is
            0.0
        max_predictions (int):
            The Model only returns up to that many top,
            by confidence score, predictions per instance.
            If this number is very high, the Model may
            return fewer predictions. Default value is
            10,000.
        segment_classification (bool):
            Set to true to request segment-level
            classification. AI Platform returns labels and
            their confidence scores for the entire time
            segment of the video that user specified in the
            input instance. Default value is true
        shot_classification (bool):
            Set to true to request shot-level
            classification. AI Platform determines the
            boundaries for each camera shot in the entire
            time segment of the video that user specified in
            the input instance. AI Platform then returns
            labels and their confidence scores for each
            detected shot, along with the start and end time
            of the shot.
            WARNING: Model evaluation is not done for this
            classification type, the quality of it depends
            on the training data, but there are no metrics
            provided to describe that quality.
            Default value is false
        one_sec_interval_classification (bool):
            Set to true to request classification for a
            video at one-second intervals. AI Platform
            returns labels and their confidence scores for
            each second of the entire time segment of the
            video that user specified in the input WARNING:
            Model evaluation is not done for this
            classification type, the quality of it depends
            on the training data, but there are no metrics
            provided to describe that quality. Default value
            is false
    """

    confidence_threshold = proto.Field(proto.FLOAT, number=1)

    max_predictions = proto.Field(proto.INT32, number=2)

    segment_classification = proto.Field(proto.BOOL, number=3)

    shot_classification = proto.Field(proto.BOOL, number=4)

    one_sec_interval_classification = proto.Field(proto.BOOL, number=5)


class VideoObjectTrackingPredictionParams(proto.Message):
    r"""Prediction model parameters for Video Object Tracking.

    Attributes:
        confidence_threshold (float):
            The Model only returns predictions with at
            least this confidence score. Default value is
            0.0
        max_predictions (int):
            The model only returns up to that many top,
            by confidence score, predictions per frame of
            the video. If this number is very high, the
            Model may return fewer predictions per frame.
            Default value is 50.
        min_bounding_box_size (float):
            Only bounding boxes with shortest edge at
            least that long as a relative value of video
            frame size are returned. Default value is 0.0.
    """

    confidence_threshold = proto.Field(proto.FLOAT, number=1)

    max_predictions = proto.Field(proto.INT32, number=2)

    min_bounding_box_size = proto.Field(proto.FLOAT, number=3)


class VideoActionRecognitionPredictionParams(proto.Message):
    r"""Prediction model parameters for Video Action Recognition.

    Attributes:
        confidence_threshold (float):
            The Model only returns predictions with at
            least this confidence score. Default value is
            0.0
        max_predictions (int):
            The model only returns up to that many top,
            by confidence score, predictions per frame of
            the video. If this number is very high, the
            Model may return fewer predictions per frame.
            Default value is 50.
    """

    confidence_threshold = proto.Field(proto.FLOAT, number=1)

    max_predictions = proto.Field(proto.INT32, number=2)


class PredictionResult(proto.Message):
    r"""Represents a line of JSONL in the batch prediction output
    file.

    Attributes:
        instance (~.struct.Struct):
            User's input instance.
            Struct is used here instead of Any so that
            JsonFormat does not append an extra "@type"
            field when we convert the proto to JSON.
        key (str):
            Optional user-provided key from the input
            instance.
        prediction (~.struct.Value):
            The prediction result.
            Value is used here instead of Any so that
            JsonFormat does not append an extra "@type"
            field when we convert the proto to JSON and so
            we can represent array of objects.
    """

    instance = proto.Field(
        proto.MESSAGE, number=1, oneof="input", message=struct.Struct,
    )

    key = proto.Field(proto.STRING, number=2, oneof="input")

    prediction = proto.Field(proto.MESSAGE, number=3, message=struct.Value,)


class TextSentimentPredictionResult(proto.Message):
    r"""Represents a line of JSONL in the text sentiment batch
    prediction output file. This is a hack to allow printing of
    integer values.

    Attributes:
        instance (~.io_format.TextSentimentPredictionInstance):
            User's input instance.
        prediction (~.io_format.TextSentimentPredictionResult.Prediction):
            The prediction result.
    """

    class Prediction(proto.Message):
        r"""Prediction output format for Text Sentiment.

        Attributes:
            sentiment (int):
                The integer sentiment labels between 0
                (inclusive) and sentimentMax label (inclusive),
                while 0 maps to the least positive sentiment and
                sentimentMax maps to the most positive one. The
                higher the score is, the more positive the
                sentiment in the text snippet is. Note:
                sentimentMax is an integer value between 1
                (inclusive) and 10 (inclusive).
        """

        sentiment = proto.Field(proto.INT32, number=1)

    instance = proto.Field(
        proto.MESSAGE, number=1, message="TextSentimentPredictionInstance",
    )

    prediction = proto.Field(proto.MESSAGE, number=2, message=Prediction,)


class ClassificationPredictionResult(proto.Message):
    r"""Prediction output format for Image Classification.

    Attributes:
        ids (Sequence[int]):
            The resource IDs of the AnnotationSpecs that
            had been identified, ordered by the confidence
            score descendingly.
        display_names (Sequence[str]):
            The display names of the AnnotationSpecs that
            had been identified, order matches the IDs.
        confidences (Sequence[float]):
            The Model's confidences in correctness of the
            predicted IDs, higher value means higher
            confidence. Order matches the Ids.
    """

    ids = proto.RepeatedField(proto.INT64, number=1)

    display_names = proto.RepeatedField(proto.STRING, number=2)

    confidences = proto.RepeatedField(proto.FLOAT, number=3)


class ImageObjectDetectionPredictionResult(proto.Message):
    r"""Prediction output format for Image Object Detection.

    Attributes:
        ids (Sequence[int]):
            The resource IDs of the AnnotationSpecs that
            had been identified, ordered by the confidence
            score descendingly.
        display_names (Sequence[str]):
            The display names of the AnnotationSpecs that
            had been identified, order matches the IDs.
        confidences (Sequence[float]):
            The Model's confidences in correctness of the
            predicted IDs, higher value means higher
            confidence. Order matches the Ids.
        bboxes (Sequence[~.struct.ListValue]):
            Bounding boxes, i.e. the rectangles over the image, that
            pinpoint the found AnnotationSpecs. Given in order that
            matches the IDs. Each bounding box is an array of 4 numbers
            ``xMin``, ``xMax``, ``yMin``, and ``yMax``, which represent
            the extremal coordinates of the box. They are relative to
            the image size, and the point 0,0 is in the top left of the
            image.
    """

    ids = proto.RepeatedField(proto.INT64, number=1)

    display_names = proto.RepeatedField(proto.STRING, number=2)

    confidences = proto.RepeatedField(proto.FLOAT, number=3)

    bboxes = proto.RepeatedField(proto.MESSAGE, number=4, message=struct.ListValue,)


class VideoClassificationPredictionResult(proto.Message):
    r"""Prediction output format for Video Classification.

    Attributes:
        id (str):
            The resource ID of the AnnotationSpec that
            had been identified.
        display_name (str):
            The display name of the AnnotationSpec that
            had been identified.
        type_ (str):
            The type of the prediction. The requested
            types can be configured via parameters. This
            will be one of - segment-classification
            - shot-classification
            - one-sec-interval-classification
        time_segment_start (~.duration.Duration):
            The beginning, inclusive, of the video's time
            segment in which the AnnotationSpec has been
            identified. Expressed as a number of seconds as
            measured from the start of the video, with
            fractions up to a microsecond precision, and
            with "s" appended at the end. Note that for
            'segment-classification' prediction type, this
            equals the original 'timeSegmentStart' from the
            input instance, for other types it is the start
            of a shot or a 1 second interval respectively.
        time_segment_end (~.duration.Duration):
            The end, exclusive, of the video's time
            segment in which the AnnotationSpec has been
            identified. Expressed as a number of seconds as
            measured from the start of the video, with
            fractions up to a microsecond precision, and
            with "s" appended at the end. Note that for
            'segment-classification' prediction type, this
            equals the original 'timeSegmentEnd' from the
            input instance, for other types it is the end of
            a shot or a 1 second interval respectively.
        confidence (~.wrappers.FloatValue):
            The Model's confidence in correction of this
            prediction, higher value means higher
            confidence.
    """

    id = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)

    type_ = proto.Field(proto.STRING, number=3)

    time_segment_start = proto.Field(
        proto.MESSAGE, number=4, message=duration.Duration,
    )

    time_segment_end = proto.Field(proto.MESSAGE, number=5, message=duration.Duration,)

    confidence = proto.Field(proto.MESSAGE, number=6, message=wrappers.FloatValue,)


class VideoObjectTrackingPredictionResult(proto.Message):
    r"""Prediction output format for Video Object Tracking.

    Attributes:
        id (str):
            The resource ID of the AnnotationSpec that
            had been identified.
        display_name (str):
            The display name of the AnnotationSpec that
            had been identified.
        time_segment_start (~.duration.Duration):
            The beginning, inclusive, of the video's time
            segment in which the object instance has been
            detected. Expressed as a number of seconds as
            measured from the start of the video, with
            fractions up to a microsecond precision, and
            with "s" appended at the end.
        time_segment_end (~.duration.Duration):
            The end, inclusive, of the video's time
            segment in which the object instance has been
            detected. Expressed as a number of seconds as
            measured from the start of the video, with
            fractions up to a microsecond precision, and
            with "s" appended at the end.
        confidence (~.wrappers.FloatValue):
            The Model's confidence in correction of this
            prediction, higher value means higher
            confidence.
        frames (Sequence[~.io_format.VideoObjectTrackingPredictionResult.Frame]):
            All of the frames of the video in which a
            single object instance has been detected. The
            bounding boxes in the frames identify the same
            object.
    """

    class Frame(proto.Message):
        r"""The fields ``xMin``, ``xMax``, ``yMin``, and ``yMax`` refer to a
        bounding box, i.e. the rectangle over the video frame pinpointing
        the found AnnotationSpec. The coordinates are relative to the frame
        size, and the point 0,0 is in the top left of the frame.

        Attributes:
            time_offset (~.duration.Duration):
                A time (frame) of a video in which the object
                has been detected. Expressed as a number of
                seconds as measured from the start of the video,
                with fractions up to a microsecond precision,
                and with "s" appended at the end.
            x_min (~.wrappers.FloatValue):
                The leftmost coordinate of the bounding box.
            x_max (~.wrappers.FloatValue):
                The rightmost coordinate of the bounding box.
            y_min (~.wrappers.FloatValue):
                The topmost coordinate of the bounding box.
            y_max (~.wrappers.FloatValue):
                The bottommost coordinate of the bounding
                box.
        """

        time_offset = proto.Field(proto.MESSAGE, number=1, message=duration.Duration,)

        x_min = proto.Field(proto.MESSAGE, number=2, message=wrappers.FloatValue,)

        x_max = proto.Field(proto.MESSAGE, number=3, message=wrappers.FloatValue,)

        y_min = proto.Field(proto.MESSAGE, number=4, message=wrappers.FloatValue,)

        y_max = proto.Field(proto.MESSAGE, number=5, message=wrappers.FloatValue,)

    id = proto.Field(proto.STRING, number=1)

    display_name = proto.Field(proto.STRING, number=2)

    time_segment_start = proto.Field(
        proto.MESSAGE, number=3, message=duration.Duration,
    )

    time_segment_end = proto.Field(proto.MESSAGE, number=4, message=duration.Duration,)

    confidence = proto.Field(proto.MESSAGE, number=5, message=wrappers.FloatValue,)

    frames = proto.RepeatedField(proto.MESSAGE, number=6, message=Frame,)


class TextExtractionPredictionResult(proto.Message):
    r"""Prediction output format for Text Extraction.

    Attributes:
        ids (Sequence[int]):
            The resource IDs of the AnnotationSpecs that
            had been identified, ordered by the confidence
            score descendingly.
        display_names (Sequence[str]):
            The display names of the AnnotationSpecs that
            had been identified, order matches the IDs.
        text_segment_start_offsets (Sequence[int]):
            The start offsets, inclusive, of the text
            segment in which the AnnotationSpec has been
            identified. Expressed as a zero-based number of
            characters as measured from the start of the
            text snippet.
        text_segment_end_offsets (Sequence[int]):
            The end offsets, inclusive, of the text
            segment in which the AnnotationSpec has been
            identified. Expressed as a zero-based number of
            characters as measured from the start of the
            text snippet.
        confidences (Sequence[float]):
            The Model's confidences in correctness of the
            predicted IDs, higher value means higher
            confidence. Order matches the Ids.
    """

    ids = proto.RepeatedField(proto.INT64, number=1)

    display_names = proto.RepeatedField(proto.STRING, number=2)

    text_segment_start_offsets = proto.RepeatedField(proto.INT64, number=3)

    text_segment_end_offsets = proto.RepeatedField(proto.INT64, number=4)

    confidences = proto.RepeatedField(proto.FLOAT, number=5)


__all__ = tuple(sorted(__protobuf__.manifest))
