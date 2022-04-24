# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import edit_or_reply, my_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo


@my_cmd(pattern="asupan$")
async def _(event):
    await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@AsupanKyyUserbot", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**ᴀsᴜᴘᴀɴ ʙʏ** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video.")


@my_cmd(pattern="asupanku$")
async def _(event):
    await edit_or_reply(event, "`Processing...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tedeasupancache", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**__Ini kak videonya.__**",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video.")


CMD_HELP.update(
    {
        "asupan": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}asupan`\
        \n↳ : Mengirim video asupan secara random.\
        \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}asupanku`\
        \n↳ : Untuk Mengirim video asupan secara random.\
    "
    }
)
