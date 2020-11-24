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

from . import schema
from .types.annotation_payload import ImageBoundingBoxAnnotation
from .types.annotation_payload import ImageClassificationAnnotation
from .types.annotation_payload import ImageSegmentationAnnotation
from .types.annotation_payload import TextClassificationAnnotation
from .types.annotation_payload import TextExtractionAnnotation
from .types.annotation_payload import TextSegment
from .types.annotation_payload import TextSentimentAnnotation
from .types.annotation_payload import TimeSegment
from .types.annotation_payload import VideoActionRecognitionAnnotation
from .types.annotation_payload import VideoClassificationAnnotation
from .types.annotation_payload import VideoObjectTrackingAnnotation
from .types.annotation_spec_color import AnnotationSpecColor
from .types.data_item_payload import ImageDataItem
from .types.data_item_payload import TextDataItem
from .types.data_item_payload import VideoDataItem
from .types.dataset_metadata import ImageDatasetMetadata
from .types.dataset_metadata import TablesDatasetMetadata
from .types.dataset_metadata import TextDatasetMetadata
from .types.dataset_metadata import TimeSeriesDatasetMetadata
from .types.dataset_metadata import VideoDatasetMetadata
from .types.geometry import Vertex
from .types.io_format import ClassificationPredictionResult
from .types.io_format import ImageClassificationPredictionInstance
from .types.io_format import ImageClassificationPredictionParams
from .types.io_format import ImageObjectDetectionPredictionInstance
from .types.io_format import ImageObjectDetectionPredictionParams
from .types.io_format import ImageObjectDetectionPredictionResult
from .types.io_format import ImageSegmentationPredictionInstance
from .types.io_format import ImageSegmentationPredictionParams
from .types.io_format import PredictionResult
from .types.io_format import TextClassificationPredictionInstance
from .types.io_format import TextExtractionPredictionInstance
from .types.io_format import TextExtractionPredictionResult
from .types.io_format import TextSentimentPredictionInstance
from .types.io_format import TextSentimentPredictionResult
from .types.io_format import VideoActionRecognitionPredictionInstance
from .types.io_format import VideoActionRecognitionPredictionParams
from .types.io_format import VideoClassificationPredictionInstance
from .types.io_format import VideoClassificationPredictionParams
from .types.io_format import VideoClassificationPredictionResult
from .types.io_format import VideoObjectTrackingPredictionInstance
from .types.io_format import VideoObjectTrackingPredictionParams
from .types.io_format import VideoObjectTrackingPredictionResult
from .types.saved_query_metadata import TextSentimentSavedQueryMetadata
from .types.saved_query_metadata import (
    VisualInspectionClassificationLabelSavedQueryMetadata,
)
from .types.saved_query_metadata import VisualInspectionMaskSavedQueryMetadata


__all__ = (
    "AnnotationSpecColor",
    "ClassificationPredictionResult",
    "ImageBoundingBoxAnnotation",
    "ImageClassificationAnnotation",
    "ImageClassificationPredictionInstance",
    "ImageClassificationPredictionParams",
    "ImageDataItem",
    "ImageDatasetMetadata",
    "ImageObjectDetectionPredictionInstance",
    "ImageObjectDetectionPredictionParams",
    "ImageObjectDetectionPredictionResult",
    "ImageSegmentationAnnotation",
    "ImageSegmentationPredictionInstance",
    "ImageSegmentationPredictionParams",
    "PredictionResult",
    "TablesDatasetMetadata",
    "TextClassificationAnnotation",
    "TextClassificationPredictionInstance",
    "TextDataItem",
    "TextDatasetMetadata",
    "TextExtractionAnnotation",
    "TextExtractionPredictionInstance",
    "TextExtractionPredictionResult",
    "TextSegment",
    "TextSentimentAnnotation",
    "TextSentimentPredictionInstance",
    "TextSentimentPredictionResult",
    "TextSentimentSavedQueryMetadata",
    "TimeSegment",
    "TimeSeriesDatasetMetadata",
    "Vertex",
    "VideoActionRecognitionAnnotation",
    "VideoActionRecognitionPredictionInstance",
    "VideoActionRecognitionPredictionParams",
    "VideoClassificationAnnotation",
    "VideoClassificationPredictionInstance",
    "VideoClassificationPredictionParams",
    "VideoClassificationPredictionResult",
    "VideoDataItem",
    "VideoDatasetMetadata",
    "VideoObjectTrackingAnnotation",
    "VideoObjectTrackingPredictionInstance",
    "VideoObjectTrackingPredictionParams",
    "VideoObjectTrackingPredictionResult",
    "VisualInspectionClassificationLabelSavedQueryMetadata",
    "VisualInspectionMaskSavedQueryMetadata",
    "schema",
)
