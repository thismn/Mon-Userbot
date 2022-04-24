# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
# Kalo mau ngecopas, jangan hapus credit ya goblok

from pytgcalls import StreamType
from pytgcalls.exceptions import AlreadyJoinedError
from pytgcalls.types.input_stream import InputAudioStream, InputStream
from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, call_py, owner
from userbot.events import register
from userbot.utils import edit_delete, edit_or_reply, my_cmd

NO_ADMIN = "`Maaf Kamu Bukan Admin 👮`"


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


async def get_call(mon):
    monm = await mon.client(getchat(mon.chat_id))
    hehe = await mon.client(getvc(monm.full_chat.call, limit=1))
    return hehe.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@my_cmd(pattern="startvc$")
@register(pattern=r"^\.startvcs$", sudo=True)
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {owner} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`Memulai Obrolan Suara`")
    except Exception as ex:
        await edit_or_reply(c, f"**ERROR:** `{ex}`")


@my_cmd(pattern="stopvc$")
@register(pattern=r"^\.stopvcs$", sudo=True)
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {owner} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`Mematikan Obrolan Suara`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@my_cmd(pattern="vcinvite")
async def _(mon):
    await edit_or_reply(mon, "`Sedang Menginvite Member...`")
    users = []
    z = 0
    async for x in mon.client.iter_participants(mon.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await mon.client(invitetovc(call=await get_call(mon), users=p))
            z += 6
        except BaseException:
            pass
    await edit_or_reply(mon, f"`Menginvite {z} Member`")


@my_cmd(pattern="vctitle(?: |$)(.*)")
@register(pattern=r"^\.cvctitle$", sudo=True)
async def change_title(e):
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await edit_delete(e, f"**Maaf {me.first_name} Bukan Admin 👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")


@my_cmd(pattern="joinvc(?: |$)(.*)")
@register(pattern=r"^\.joinvcs(?: |$)(.*)", sudo=True)
async def _(event):
    Mon = await edit_or_reply(event, "`Processing...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Mon.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
    if chat_id:
        file = "./userbot/resources/audio-mon.mp3"
        try:
            await call_py.join_group_call(
                chat_id,
                InputStream(
                    InputAudioStream(
                        file,
                    ),
                ),
                stream_type=StreamType().local_stream,
            )
            await edit_delete(Mon,
                              f"**Join ke Obrolan Suara**\n➥ `{chat_id}`"
                              )
        except AlreadyJoinedError:
            return await edit_delete(
                Mon, "**INFO:** `akun anda sudah di obrolan suara`", 45
            )
        except Exception as e:
            return await Mon.edit(f"**INFO:** `{e}`")


@my_cmd(pattern="leavevc(?: |$)(.*)")
@register(pattern=r"^\.leavevcs(?: |$)(.*)", sudo=True)
async def vc_end(event):
    Mon = await edit_or_reply(event, "`Processing...`")
    if len(event.text.split()) > 1:
        chat_id = event.text.split()[1]
        try:
            chat_id = await event.client.get_peer_id(int(chat_id))
        except Exception as e:
            return await Mon.edit(f"**ERROR:** `{e}`")
    else:
        chat_id = event.chat_id
    if chat_id:
        try:
            await call_py.leave_group_call(chat_id)
            await edit_delete(
                Mon,
                f"**Turun dari Obrolan Suara**\n➥ `{chat_id}`",
            )
        except Exception as e:
            return await Mon.edit(f"**INFO:** `{e}`")


CMD_HELP.update(
    {
        "vcg": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}startvc`\
         \n↳ : Memulai Obrolan Suara.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}stopvc`\
         \n↳ : `Menghentikan Obrolan Suara.`\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vctittle <tittle vcg>`\
         \n↳ : `Mengubah tittle/judul Obrolan Suara.`\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}vcinvite`\
         \n↳ : Mengundang ke Obrolan Suara."
    }
)


CMD_HELP.update(
    {
        "vctools": f"**Plugin : **`vctools`\
      \n\n  •  **Syntax :** `{cmd}joinvc`\
      \n  •  **Function :** Melakukan Fake voice chat group.\
      \n\n  •  **Syntax :** `{cmd}leavevc`\
      \n  •  **Function :** Memberhentikan Fake voice chat group.\
      "
    }
)
