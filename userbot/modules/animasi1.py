

from time import sleep
from userbot import CMD_HELP, bot, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, my_cmd
from telethon import events
import asyncio


@my_cmd(pattern="hua$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        e = await edit_or_reply(e, "أ‿أ")
        await e.edit("╥﹏╥")
        await e.edit("(;﹏;)")
        await e.edit("(ToT)")
        await e.edit("(┳Д┳)")
        await e.edit("(ಥ﹏ಥ)")
        await e.edit("（；へ：）")
        await e.edit("(T＿T)")
        await e.edit("（πーπ）")
        await e.edit("(Ｔ▽Ｔ)")
        await e.edit("(⋟﹏⋞)")
        await e.edit("（ｉДｉ）")
        await e.edit("(´Д⊂ヽ")
        await e.edit("(;Д;)")
        await e.edit("（>﹏<）")
        await e.edit("(TдT)")
        await e.edit("(つ﹏⊂)")
        await e.edit("༼☯﹏☯༽")
        await e.edit("(ノ﹏ヽ)")
        await e.edit("(ノAヽ)")
        await e.edit("(╥_╥)")
        await e.edit("(T⌓T)")
        await e.edit("(༎ຶ⌑༎ຶ)")
        await e.edit("(☍﹏⁰)｡")
        await e.edit("(ಥ_ʖಥ)")
        await e.edit("(つд⊂)")
        await e.edit("(≖͞_≖̥)")
        await e.edit("(இ﹏இ`｡)")
        await e.edit("༼ಢ_ಢ༽")
        await e.edit("༼ ༎ຶ ෴ ༎ຶ༽")


@my_cmd(pattern='huh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    xnxx = await edit_or_reply(typew, "`\n(\\_/)`"
                               "`\n(●_●)`"
                               "`\n />❤️ *Ini Buat Kamu`")
    sleep(3)
    await xnxx.edit("`\n(\\_/)`"
                    "`\n(●_●)`"
                    "`\n/>💔  *Aku Ambil Lagi`")
    sleep(2)
    await xnxx.edit("`\n(\\_/)`"
                    "`\n(●_●)`"
                    "`\n💔<\\  *Terimakasih`")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "ceritacinta":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita ❤️ Cinta` ",
            "  😐             😕 \n/👕\\         <👗\\ \n 👖               /|",
            "  😉          😳 \n/👕\\       /👗\\ \n  👖            /|",
            "  😚            😒 \n/👕\\         <👗> \n  👖             /|",
            "  😍         ☺️ \n/👕\\      /👗\\ \n  👖          /|",
            "  😍          😍 \n/👕\\       /👗\\ \n  👖           /|",
            "  😘   😊 \n /👕\\/👗\\ \n   👖   /|",
            " 😳  😁 \n /|\\ /👙\\ \n /     / |",
            "😈    /😰\\ \n<|\\      👙 \n /🍆    / |",
            "😅 \n/(),✊😮 \n /\\         _/\\/|",
            "😎 \n/\\_,__😫 \n  //    //       \\",
            "😖 \n/\\_,💦_😋  \n  //         //        \\",
            "  😭      ☺️ \n  /|\\   /(👶)\\ \n  /!\\   / \\ ",
            "`TAMAT 😅`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "canda":

        await event.edit(input_str)

        animation_chars = [
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀  ⠀   ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Kamu    ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀⠀   ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀      ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Pasti   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__|⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Belum   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀         ⡇\n  ⠙⢿⣯⠄⠀⠀(x)⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀     ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀   ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Mandi  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀⠀__ ⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀   ⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀ ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Bwhaha  ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀  ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀|__| ⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`",
            "`⠀⠀⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀\n ⠀⣴⠿⠏⠀⠀⠀⠀⠀  ⠀⢳⡀⠀⡏⠀⠀    ⠀⢷\n⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀  ⠀     ⡇\n⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿  ⣸ Canda   ⡇\n ⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀   ⣿  ⢹⠀        ⡇\n  ⠙⢿⣯⠄⠀⠀****⠀⠀⡿ ⠀⡇⠀⠀⠀⠀    ⡼\n⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀   ⠘⠤⣄⣠⠞⠀\n⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀\n⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀\n⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀ ⠀⣄⢸⠀⠀⠀⠀⠀⠀`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@my_cmd(pattern='nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    xnxx = await edit_or_reply(typew, "`\n(\\_/)`"
                               "`\n(●_●)`"
                               "`\n />💖 *Ini Buat Kamu`")
    sleep(2)
    await xnxx.edit("`\n(\\_/)`"
                    "`\n(●_●)`"
                    "`\n💖<\\  *Tapi Bo'ong Hiyahiyahiya`")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "owner":

        await event.edit(input_str)

        animation_chars = [
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬜⬛⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬜⬜⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬜⬛⬛⬜⬛\n⬛⬛⬛⬛⬛⬛"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])

CMD_HELP.update({
    "animasi1":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}nah` ; `{cmd}huh` ; `{cmd}owner`\
    \n↳ : Cobain Sendiri.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}bunga` ; `{cmd}buah`\
    \n↳ : animasi.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}waktu`\
    \n↳ : animasi.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}hua`\
    \n↳ : nangis.\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ceritacinta` ; `{cmd}canda`\
    \n↳ : liat sendiri"
})
