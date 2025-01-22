# Copyright (c) Microsoft. All rights reserved.


from typing import Annotated, Any

from pydantic import BaseModel

from semantic_kernel.connectors.ai.open_ai import OpenAIEmbeddingPromptExecutionSettings
from semantic_kernel.data import (
    VectorStoreRecordDataField,
    VectorStoreRecordKeyField,
    VectorStoreRecordVectorField,
    vectorstoremodel,
)

###
# The data model used for this sample is based on the hotel data model from the Azure AI Search samples.
# When deploying a new index in Azure AI Search using the import wizard you can choose to deploy the 'hotel-samples'
# dataset, see here: https://learn.microsoft.com/en-us/azure/search/search-get-started-portal.
# This is the dataset used in this sample with some modifications.
# This model adds vectors for the 2 descriptions in English and French.
# Both are based on the 1536 dimensions of the OpenAI models.
# You can adjust this at creation time and then make the change below as well.
###


@vectorstoremodel
class HotelSampleClass(BaseModel):
    hotel_id: Annotated[str, None, VectorStoreRecordKeyField()] = None
    hotel_name: Annotated[str, None] = None
    description: Annotated[str, None] = None
    
