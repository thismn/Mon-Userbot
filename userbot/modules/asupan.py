# π Β© @tofik_dn
# β οΈ Do not remove credits


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
            caption=f"**α΄sα΄α΄α΄Ι΄ ΚΚ** [{owner}](tg://user?id={aing.id})",
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
        "asupan": f"πΎπ€π’π’ππ£π: `{cmd}asupan`\
        \nβ³ : Mengirim video asupan secara random.\
        \n\nπΎπ€π’π’ππ£π: `{cmd}asupanku`\
        \nβ³ : Untuk Mengirim video asupan secara random.\
    "
    }
)
