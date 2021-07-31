""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.rhelp` Atau Bisa `.help` atau Minta Bantuan Ke:\n"
        "\n[MONDAR](t.me/monajedah)"
        "\n\n[SUPPORT](https://t.me/siniajaloh)"
        "\n\n[CHANNEL](https://t.me/familynvn)")


@register(outgoing=True, pattern="^.mvars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/mondar111/UBOT/UBOT/varshelper.txt)")


CMD_HELP.update({
    "monhelper":
    "`.helpmy`\
\nPenjelasan: Bantuan Untuk MON-UBOT.\
\n`.mvars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
