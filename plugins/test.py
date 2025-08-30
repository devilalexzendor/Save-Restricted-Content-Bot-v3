from pyrogram import Client, filters

# मान लो तुम्हारा shared_client.py Client return करता है
from shared_client import client  

@client.on_message(filters.command("ping"))
async def ping_pong(_, message):
    await message.reply_text("🏓 Pong! Bot is alive.")

async def run_test_plugin():
    print("Test plugin loaded ✅")
