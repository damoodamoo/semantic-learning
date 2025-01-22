from semantic_kernel.connectors.memory.azure_ai_search import AzureAISearchStore, AzureAISearchCollection

from semantic_kernel.functions import kernel_function

from hotel import HotelSampleClass

class HotelSearchPlugin:

    vector_store = AzureAISearchStore(
        api_key="cJsydWvWMqZStMy3vazLYCfqXYVWmxxj9xzyHZqh7OAzSeDO3I8G",
        search_endpoint="https://damoo-search.search.windows.net"
    )

    collection: AzureAISearchCollection = vector_store.get_collection("hotels-sample-index", HotelSampleClass)

    @kernel_function(
        name="hotel_search",
        description="Finds a hotel from the DB"
    )
    async def search_hotels(self, query: str):
        print("running Azure AI Text Search..." + query)
        results = await self.collection.text_search(query)
        return results