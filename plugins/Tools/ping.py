"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import HNDLR
from plugins.Tools.help_func.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "എന്തിനാടാ start ഉണ്ടാകുമ്പോൾ എന്നെ നേക്കി എൻ്റെ വായിൽ ഉള്ളത് കേൾക്കുന്നത്... എന്നാ പരിപാടിയാ..." 
HELP = "ദൈവമേ എന്നെ മാത്രം രക്ഷിക്കണേ...."
REPO = "നമ്മൾ നമ്മൾ പോലുമറിയാതെ അധോലോകം ആയി മാറിക്കഴിഞ്ഞിരിക്കുന്നു ഷാജിയേട്ടാ..."
# -- Constants End -- #


@Client.on_message(filters.command("alive", HNDLR) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("help", HNDLR) & f_onw_fliter)
async def help_me(_, message):
    await message.reply_text(HELP)


@Client.on_message(filters.command("ping", HNDLR) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", HNDLR) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)
