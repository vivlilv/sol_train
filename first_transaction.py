import os

from dotenv import load_dotenv
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair
from solders.pubkey import Pubkey
load_dotenv()


async def main():
    # Connect to the Solana Mainnet
    client = AsyncClient("https://api.mainnet-beta.solana.com")
    secret = os.getenv("SECRET_KEY")
    print(secret)
    keypair = Keypair.from_base58_string(str(secret))
    print(keypair.pubkey()) 
    print(Pubkey.from_string(str(keypair.pubkey()))==keypair.pubkey())
    # response = await client.get_balance(pub_key)
    # print("Balance:", response.value/1_000_000_000)

    # Close the connection
    # await client.close()


import asyncio

asyncio.run(main())
