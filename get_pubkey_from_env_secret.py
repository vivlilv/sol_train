import os

from dotenv import load_dotenv
from solana.rpc.async_api import AsyncClient
from solders.keypair import Keypair
from solders.pubkey import Pubkey

load_dotenv()


async def main():
    secret = os.getenv("SECRET_KEY")
    print(secret)
    keypair = Keypair.from_base58_string(str(secret))
    print(keypair.pubkey())
    print(Pubkey.from_string(str(keypair.pubkey())) == keypair.pubkey())
    
import asyncio

asyncio.run(main())
