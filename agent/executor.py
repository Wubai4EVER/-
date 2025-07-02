import os
import asyncio
from solana.rpc.async_api import AsyncClient
from solana.keypair import Keypair
from solana.transaction import Transaction
from solana.system_program import TransferParams, transfer

class Executor:
    def __init__(self, rpc_url, secret_key_hex):
        self.client = AsyncClient(rpc_url)
        self.wallet = Keypair.from_secret_key(bytes.fromhex(secret_key_hex))

    async def send_sol(self, to_pubkey, amount_sol):
        tx = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=self.wallet.public_key,
                    to_pubkey=to_pubkey,
                    lamports=int(amount_sol * 1e9)
                )
            )
        )
        resp = await self.client.send_transaction(tx, self.wallet)
        await self.client.confirm_transaction(resp["result"])
        return resp

    async def execute_decision(self, decision):
        action = decision.get("action")
        if action == "buy":
            return await self.send_sol(decision["to"], decision["amount"])
        elif action == "sell":
            return await self.send_sol(decision["from"], decision["amount"])
        else:
            return {"status": "hold"}
