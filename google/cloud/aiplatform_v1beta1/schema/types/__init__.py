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

from .annotation_spec_color import AnnotationSpecColor
from .geometry import Vertex
from .annotation_payload import (
    ImageClassificationAnnotation,
    ImageBoundingBoxAnnotation,
    ImageSegmentationAnnotation,
    TextClassificationAnnotation,
    TextExtractionAnnotation,
    TextSegment,
    TextSentimentAnnotation,
    VideoClassificationAnnotation,
    TimeSegment,
    VideoObjectTrackingAnnotation,
    VideoActionRecognitionAnnotation,
)
from .io_format import (
    ImageClassificationPredictionInstance,
    ImageObjectDetectionPredictionInstance,
    ImageSegmentationPredictionInstance,
    VideoClassificationPredictionInstance,
    VideoObjectTrackingPredictionInstance,
    VideoActionRecognitionPredictionInstance,
    TextClassificationPredictionInstance,
    TextSentimentPredictionInstance,
    TextExtractionPredictionInstance,
    ImageClassificationPredictionParams,
    ImageObjectDetectionPredictionParams,
    ImageSegmentationPredictionParams,
    VideoClassificationPredictionParams,
    VideoObjectTrackingPredictionParams,
    VideoActionRecognitionPredictionParams,
    PredictionResult,
    TextSentimentPredictionResult,
    ClassificationPredictionResult,
    ImageObjectDetectionPredictionResult,
    VideoClassificationPredictionResult,
    VideoObjectTrackingPredictionResult,
    TextExtractionPredictionResult,
)
from .saved_query_metadata import (
    TextSentimentSavedQueryMetadata,
    VisualInspectionClassificationLabelSavedQueryMetadata,
    VisualInspectionMaskSavedQueryMetadata,
)
from .automl_image_object_detection import (
    AutoMlImageObjectDetection,
    AutoMlImageObjectDetectionInputs,
    AutoMlImageObjectDetectionMetadata,
)
from .automl_image_segmentation import (
    AutoMlImageSegmentation,
    AutoMlImageSegmentationInputs,
    AutoMlImageSegmentationMetadata,
)
from .automl_video_object_tracking import (
    AutoMlVideoObjectTracking,
    AutoMlVideoObjectTrackingInputs,
)
from .export_evaluated_data_items_config import ExportEvaluatedDataItemsConfig
from .automl_forecasting import (
    AutoMlForecasting,
    AutoMlForecastingInputs,
    AutoMlForecastingMetadata,
)
from .automl_text_extraction import (
    AutoMlTextExtraction,
    AutoMlTextExtractionInputs,
)
from .automl_text_sentiment import (
    AutoMlTextSentiment,
    AutoMlTextSentimentInputs,
)
from .automl_video_action_recognition import (
    AutoMlVideoActionRecognition,
    AutoMlVideoActionRecognitionInputs,
)
from .automl_text_classification import (
    AutoMlTextClassification,
    AutoMlTextClassificationInputs,
)
from .automl_tables import (
    AutoMlTables,
    AutoMlTablesInputs,
    AutoMlTablesMetadata,
)
from .automl_video_classification import (
    AutoMlVideoClassification,
    AutoMlVideoClassificationInputs,
)
from .automl_image_classification import (
    AutoMlImageClassification,
    AutoMlImageClassificationInputs,
    AutoMlImageClassificationMetadata,
)
from .data_item_payload import (
    ImageDataItem,
    VideoDataItem,
    TextDataItem,
)
from .text_extraction import TextExtractionPredictionResult
from .time_series_forecasting import TimeSeriesForecastingPredictionResult
from .video_classification import VideoClassificationPredictionResult
from .tabular_classification import TabularClassificationPredictionResult
from .classification import ClassificationPredictionResult
from .text_sentiment import TextSentimentPredictionInstance
from .text_sentiment import TextSentimentPredictionResult
from .image_object_detection import ImageObjectDetectionPredictionResult
from .video_action_recognition import VideoActionRecognitionPredictionResult
from .video_object_tracking import VideoObjectTrackingPredictionResult
from .tabular_regression import TabularRegressionPredictionResult
from .image_segmentation import ImageSegmentationPredictionResult
from .text_extraction import TextExtractionPredictionInstance
from .image_classification import ImageClassificationPredictionInstance
from .video_classification import VideoClassificationPredictionInstance
from .image_object_detection import ImageObjectDetectionPredictionInstance
from .video_action_recognition import VideoActionRecognitionPredictionInstance
from .text_classification import TextClassificationPredictionInstance
from .video_object_tracking import VideoObjectTrackingPredictionInstance
from .image_segmentation import ImageSegmentationPredictionInstance
from .image_classification import ImageClassificationPredictionParams
from .video_classification import VideoClassificationPredictionParams
from .image_object_detection import ImageObjectDetectionPredictionParams
from .video_action_recognition import VideoActionRecognitionPredictionParams
from .video_object_tracking import VideoObjectTrackingPredictionParams
from .image_segmentation import ImageSegmentationPredictionParams
from .dataset_metadata import (
    ImageDatasetMetadata,
    TextDatasetMetadata,
    VideoDatasetMetadata,
    TablesDatasetMetadata,
    TimeSeriesDatasetMetadata,
)

__all__ = (
    "AnnotationSpecColor",
    "Vertex",
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
    "TextSentimentSavedQueryMetadata",
    "VisualInspectionClassificationLabelSavedQueryMetadata",
    "VisualInspectionMaskSavedQueryMetadata",
    "AutoMlImageObjectDetection",
    "AutoMlImageObjectDetectionInputs",
    "AutoMlImageObjectDetectionMetadata",
    "AutoMlImageSegmentation",
    "AutoMlImageSegmentationInputs",
    "AutoMlImageSegmentationMetadata",
    "AutoMlVideoObjectTracking",
    "AutoMlVideoObjectTrackingInputs",
    "ExportEvaluatedDataItemsConfig",
    "AutoMlForecasting",
    "AutoMlForecastingInputs",
    "AutoMlForecastingMetadata",
    "AutoMlTextExtraction",
    "AutoMlTextExtractionInputs",
    "AutoMlTextSentiment",
    "AutoMlTextSentimentInputs",
    "AutoMlVideoActionRecognition",
    "AutoMlVideoActionRecognitionInputs",
    "AutoMlTextClassification",
    "AutoMlTextClassificationInputs",
    "AutoMlTables",
    "AutoMlTablesInputs",
    "AutoMlTablesMetadata",
    "AutoMlVideoClassification",
    "AutoMlVideoClassificationInputs",
    "AutoMlImageClassification",
    "AutoMlImageClassificationInputs",
    "AutoMlImageClassificationMetadata",
    "ImageDataItem",
    "VideoDataItem",
    "TextDataItem",
    "TextExtractionPredictionResult",
    "TimeSeriesForecastingPredictionResult",
    "VideoClassificationPredictionResult",
    "TabularClassificationPredictionResult",
    "ClassificationPredictionResult",
    "TextSentimentPredictionInstance",
    "TextSentimentPredictionResult",
    "ImageObjectDetectionPredictionResult",
    "VideoActionRecognitionPredictionResult",
    "VideoObjectTrackingPredictionResult",
    "TabularRegressionPredictionResult",
    "ImageSegmentationPredictionResult",
    "TextExtractionPredictionInstance",
    "ImageClassificationPredictionInstance",
    "VideoClassificationPredictionInstance",
    "ImageObjectDetectionPredictionInstance",
    "VideoActionRecognitionPredictionInstance",
    "TextClassificationPredictionInstance",
    "VideoObjectTrackingPredictionInstance",
    "ImageSegmentationPredictionInstance",
    "ImageClassificationPredictionParams",
    "VideoClassificationPredictionParams",
    "ImageObjectDetectionPredictionParams",
    "VideoActionRecognitionPredictionParams",
    "VideoObjectTrackingPredictionParams",
    "ImageSegmentationPredictionParams",
    "ImageDatasetMetadata",
    "TextDatasetMetadata",
    "VideoDatasetMetadata",
    "TablesDatasetMetadata",
    "TimeSeriesDatasetMetadata",
)
