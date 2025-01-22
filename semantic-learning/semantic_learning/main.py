from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.utils.logging import setup_logging
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.contents.chat_history import ChatHistory

import logging
import asyncio
from time_plugin import TimePlugin
from hotel_search_plugin import HotelSearchPlugin

async def main():
    kernel = Kernel()
    print("running")

    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),
        "https://cognitiveservices.azure.com/.default"
    )

    chat_completion = AzureChatCompletion(
        deployment_name="gpt-4o",
        ad_token_provider=token_provider,
        endpoint="https://aisadrdm3.openai.azure.com/",
        api_version="2024-05-01-preview"
    )
    
    kernel.add_service(chat_completion)
    
    # add the current time
    kernel.add_plugin(
        plugin=TimePlugin(),
        plugin_name="time")
    
    kernel.add_plugin(
        plugin=HotelSearchPlugin(),
        plugin_name="hotel_search"
    )

    setup_logging()
    logging.getLogger("kernel").setLevel(logging.DEBUG)

    execution_settings = AzureChatPromptExecutionSettings()
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    history = ChatHistory()

    userInput = None
    while True:
        userInput = input("User > ")

        if userInput == "exit":
            break

        history.add_user_message(userInput)

        result = await chat_completion.get_chat_message_content(
            chat_history=history,
            settings=execution_settings,
            kernel=kernel
        )

        print("Assistant > " + str(result))

        history.add_message(result)


# @kernel.filter(filter_type=FilterTypes.FUNCTION_INVOCATION)
# async def log_search_filter(context: FunctionInvocationContext, next: Coroutine[FunctionInvocationContext, Any, None]):
#     if context.function.plugin_name == "time":
#         print(f"Calling time ({context.function.name}) with arguments:")
#         for arg in context.arguments:
#             if arg in ("user_input", "chat_history"):
#                 continue
#             print(f'  {arg}: "{context.arguments[arg]}"')
#         await next(context)
#     else:
#         await next(context)


if __name__ == "__main__":
    asyncio.run(main())

