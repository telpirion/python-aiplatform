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
    manifest={
        "ImageDatasetMetadata",
        "TextDatasetMetadata",
        "VideoDatasetMetadata",
        "TablesDatasetMetadata",
        "TimeSeriesDatasetMetadata",
    },
)


class ImageDatasetMetadata(proto.Message):
    r"""The metadata of Datasets that contain Image DataItems.

    Attributes:
        data_item_schema_uri (str):
            Points to a YAML file stored on Google Cloud
            Storage describing payload of the Image
            DataItems that belong to this Dataset.
        gcs_bucket (str):
            Google Cloud Storage Bucket name that
            contains the blob data of this Dataset.
    """

    data_item_schema_uri = proto.Field(proto.STRING, number=1)

    gcs_bucket = proto.Field(proto.STRING, number=2)


class TextDatasetMetadata(proto.Message):
    r"""The metadata of Datasets that contain Text DataItems.

    Attributes:
        data_item_schema_uri (str):
            Points to a YAML file stored on Google Cloud
            Storage describing payload of the Text DataItems
            that belong to this Dataset.
        gcs_bucket (str):
            Google Cloud Storage Bucket name that
            contains the blob data of this Dataset.
    """

    data_item_schema_uri = proto.Field(proto.STRING, number=1)

    gcs_bucket = proto.Field(proto.STRING, number=2)


class VideoDatasetMetadata(proto.Message):
    r"""The metadata of Datasets that contain Video DataItems.

    Attributes:
        data_item_schema_uri (str):
            Points to a YAML file stored on Google Cloud
            Storage describing payload of the Video
            DataItems that belong to this Dataset.
        gcs_bucket (str):
            Google Cloud Storage Bucket name that
            contains the blob data of this Dataset.
    """

    data_item_schema_uri = proto.Field(proto.STRING, number=1)

    gcs_bucket = proto.Field(proto.STRING, number=2)


class TablesDatasetMetadata(proto.Message):
    r"""The metadata of Datasets that contain tables data.

    Attributes:
        input_config (~.dataset_metadata.TablesDatasetMetadata.InputConfig):

    """

    class InputConfig(proto.Message):
        r"""The tables Dataset's data source. The Dataset doesn't store
        the data directly, but only pointer(s) to its data.

        Attributes:
            gcs_source (~.dataset_metadata.TablesDatasetMetadata.GcsSource):

            bigquery_source (~.dataset_metadata.TablesDatasetMetadata.BigQuerySource):

        """

        gcs_source = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="source",
            message="TablesDatasetMetadata.GcsSource",
        )

        bigquery_source = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="source",
            message="TablesDatasetMetadata.BigQuerySource",
        )

    class GcsSource(proto.Message):
        r"""

        Attributes:
            uri (Sequence[str]):
                Google Cloud Storage URI to a input file,
                only .csv file is supported.
        """

        uri = proto.RepeatedField(proto.STRING, number=1)

    class BigQuerySource(proto.Message):
        r"""

        Attributes:
            uri (str):
                The URI of a BigQuery table.
        """

        uri = proto.Field(proto.STRING, number=1)

    input_config = proto.Field(proto.MESSAGE, number=1, message=InputConfig,)


class TimeSeriesDatasetMetadata(proto.Message):
    r"""The metadata of Datasets that contain time series data.

    Attributes:
        input_config (~.dataset_metadata.TimeSeriesDatasetMetadata.InputConfig):

        time_series_identifier_column (str):
            The column name of the time series identifier
            column that identifies the time series.
        time_column (str):
            The column name of the time column that
            identifies time order in the time series.
    """

    class InputConfig(proto.Message):
        r"""The time series Dataset's data source. The Dataset doesn't
        store the data directly, but only pointer(s) to its data.

        Attributes:
            gcs_source (~.dataset_metadata.TimeSeriesDatasetMetadata.GcsSource):

            bigquery_source (~.dataset_metadata.TimeSeriesDatasetMetadata.BigQuerySource):

        """

        gcs_source = proto.Field(
            proto.MESSAGE,
            number=1,
            oneof="source",
            message="TimeSeriesDatasetMetadata.GcsSource",
        )

        bigquery_source = proto.Field(
            proto.MESSAGE,
            number=2,
            oneof="source",
            message="TimeSeriesDatasetMetadata.BigQuerySource",
        )

    class GcsSource(proto.Message):
        r"""

        Attributes:
            uri (Sequence[str]):
                Google Cloud Storage URI to a input file,
                only .csv file is supported.
        """

        uri = proto.RepeatedField(proto.STRING, number=1)

    class BigQuerySource(proto.Message):
        r"""

        Attributes:
            uri (str):
                The URI of a BigQuery table.
        """

        uri = proto.Field(proto.STRING, number=1)

    input_config = proto.Field(proto.MESSAGE, number=1, message=InputConfig,)

    time_series_identifier_column = proto.Field(proto.STRING, number=2)

    time_column = proto.Field(proto.STRING, number=3)


__all__ = tuple(sorted(__protobuf__.manifest))
