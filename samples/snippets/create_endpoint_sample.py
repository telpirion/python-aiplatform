# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_create_endpoint_sample]
from google.cloud import aiplatform


def create_endpoint_sample(
    project: str,
    display_name: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
    timeout: int = 300,
):
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.EndpointServiceClient(client_options=client_options)
    endpoint = {"display_name": display_name}
    parent = f"projects/{project}/locations/{location}"
    response = client.create_endpoint(parent=parent, endpoint=endpoint)
    print("Long running operation:", response.operation.name)
    create_endpoint_response = response.result(timeout=timeout)
    print("create_endpoint_response:", create_endpoint_response)


# [END aiplatform_create_endpoint_sample]
