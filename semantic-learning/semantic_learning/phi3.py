
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.ollama.ollama_settings import OllamaSettings
from semantic_kernel.connectors.ai.ollama import OllamaChatCompletion
from semantic_kernel.connectors.ai.ollama.ollama_prompt_execution_settings import OllamaPromptExecutionSettings


from semantic_kernel.utils.logging import setup_logging

from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.contents.chat_history import ChatHistory

import logging
import asyncio

async def main():
    kernel = Kernel()
    print("running")

    chat_completion = OllamaChatCompletion(
        ai_model_id="phi3:mini",
        host="http://127.0.0.1:11434"
    )
    
    kernel.add_service(chat_completion)
    
    setup_logging()
    logging.getLogger("kernel").setLevel(logging.DEBUG)

    execution_settings = OllamaPromptExecutionSettings()
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


if __name__ == "__main__":
    asyncio.run(main())

