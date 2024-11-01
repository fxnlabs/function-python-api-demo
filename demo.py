import asyncio, logging, os, sys

from apigateway.v1 import APIGatewayServiceStub, ChatCompleteMessage
from grpclib.client import Channel
from dotenv import load_dotenv

logging.basicConfig()

# Load .env file
load_dotenv()

async def main():
    # Get API key from environment variable
    api_key = os.environ.get('FXN_API_KEY')

    channel = Channel('api.function.network')
    service = APIGatewayServiceStub(channel, metadata=[('authorization', f'Bearer {api_key}')])

    # Create a text embedding
    embed_response = await service.embed(
        model='baai/bge-small-en-v1.5',
        input='Embed me so I can use it for RAG Pipelines',
    )

    print(f"Embedding vector count: {len(embed_response.data[0].embedding)}")

    # Stream a chat completion response
    chat_complete_response = service.chat_complete_stream(
        model='meta/llama-3-8b-instruct',
        message=[
            ChatCompleteMessage(
                role='user',
                content='Who was Ada Lovelace? Be concise.',
            ),
        ],
    )

    async for chunk in chat_complete_response:
        sys.stdout.write(chunk.response.content)
        sys.stdout.flush()
    print()

    # Close connection when done
    channel.close()


if __name__ == "__main__":
    asyncio.run(main())
