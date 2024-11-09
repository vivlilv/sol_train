from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey

async def main():
    # Connect to the Solana Devnet
    client = AsyncClient("https://api.mainnet-beta.solana.com")
    pub_address = str(input("Enter wallet to check balance:")) 
    # Fetch the balance of a sample public key
    try:
        pub_key = Pubkey.from_string(pub_address)
        response = await client.get_balance(pub_key)
        print(f"Balance: {response.value/1_000_000_000} SOL | {response.value/1_000_000_000*200} USD")
    except:
        print('Error: Invalid wallet entry, check the format to be base58')

    await client.close()

import asyncio
asyncio.run(main())


