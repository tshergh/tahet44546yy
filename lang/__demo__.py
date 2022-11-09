# fileName : lang/__demo__.py
# copyright ©️ 2021 nabilanavab

# ................................................................ Thank: @azik_developer [Telegram] ..................................................................

from configs.config import settings

# PM WELCOME MESSAGE (HOME A, B, C, D...)
HOME = {
    "HomeA" : """✅✅ [{}](tg://user?id={})..!!
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅ 🥳

✅✅✅✅✅✅✅✅✅✅✅✅:\n◍ `✅✅✅✅✅✅✅✅`
◍ `✅✅✅✅✅✅✅✅`\n◍ `✅✅✅✅✅✅✅✅`""",
    "HomeACB" : {
        "⚙️ ✅✅✅✅✅ ⚙️" : "Home|B", "⚠️ ✅✅✅✅✅ ⚠️" : "Home|C",
        "📢 ✅✅✅✅✅ 📢" : f"{str(settings.OWNED_CHANNEL)}",
        "🌟 ✅✅✅✅✅ 🌟" : f"{str(settings.SOURCE_CODE)}",
        "🚶 ✅✅✅✅✅ 🚶" : "close|mee"
    },
    "HomeAdminCB" : {
        "⚙️ ✅✅✅✅✅ ⚙️" : "Home|B", "⚠️ ✅✅✅✅✅ ⚠️" : "Home|C",
        "📢 ✅✅✅✅✅ 📢" : f"{str(settings.OWNED_CHANNEL)}",
        "🌟 ✅✅✅✅✅ 🌟" : f"{str(settings.SOURCE_CODE)}",
        "🗽 ✅✅✅✅✅ 🗽" : f"status|home", "🚶 ✅✅✅✅✅ 🚶" : "close|mee"
    },
    "HomeB" : """✅✅✅✅✅ ⚙️\n\n✅✅✅✅✅ : {}
✅✅✅✅✅ : {}\n✅✅✅✅✅ : {}\n✅✅✅✅✅ : {}\n
✅✅✅✅✅ : {}\n✅✅✅✅✅ : {}\n
✅✅✅✅✅ : {}\n✅✅✅✅✅ : {}\n✅✅✅✅✅: {}""",
    "HomeBCB" : {
        "🌍 ✅✅✅ 🌍" : "set|lang", "📍 ✅✅✅ 📍" : "set|thumb",
        "📈 ✅✅✅ 📈" : "set|fname", "💩 ✅✅✅ 💩" : "set|api",
        "📅 ✅✅✅ 📅" : "set|capt", "« ✅✅✅ «" : "Home|B2A"
    },
    "HomeC" : """🪂 ✅✅✅✅✅ 🪂:

✅✅✅✅✅

✅✅✅✅✅✅✅✅✅✅
✅✅✅✅✅✅✅✅✅✅
✅✅✅✅✅✅✅✅✅✅
✅✅✅✅✅✅✅✅✅✅
✅✅✅✅✅✅✅✅✅✅""",
    "HomeCCB" : {"« ✅✅✅✅✅ «" : "Home|A", "🛈 ✅✅✅✅✅ 🛈" : "Home|D"},
    "HomeD" : """✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅

⚠️ ✅✅✅✅✅ ⚠️:
🛈 ✅✅✅✅✅✅✅✅✅✅
🛈 ✅✅✅✅✅✅✅✅✅✅
🛈 ✅✅✅✅✅✅✅✅✅✅

✅✅✅✅✅✅✅✅✅✅""",
    "HomeDCB" : {"⚠️ ✅✅✅✅✅ ⚠️" : "Home|C", "» ✅✅✅✅✅ »" : "Home|A"}  
}

SETTINGS = {
    "default" : ["✅✅✅ ❌", "✅✅✅ ✅"], "chgLang" : {"✅✅✅ ⚙️ » ✅✅✅ 🌐" : "nabilanavab"},
    "error" : "✅✅✅✅✅✅✅✅✅✅", "lang" : "✅✅✅✅✅✅✅✅✅✅",
    "ask" : ["✅✅✅✅✅", "✅✅✅✅✅ 😅\n\n✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅ 😏"],
    "wait" : {"✅✅✅✅✅ 🥱" : "nabilanavab"}, "back" : {"« ✅✅✅✅✅ «" : "Home|B2S"}, "errorCB" : {"« ✅✅✅✅✅ «" : "Home|B2A"},
    "result" : ["✅✅✅✅✅ ❌", "✅✅✅✅✅ ✅"], "cant" : "✅✅✅✅✅ ❌",
    "feedback" : "✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅.\n@ta_ja199"
                 "\n\n✅✅✅✅✅ {} Lang:\n`• ✅✅✅✅✅\n• ✅✅✅✅✅\n• ✅✅✅✅✅`",
    "feedbtn" : {"✅✅✅✅✅" : "report"},
    "thumb" : [
        {"✅✅✅✅✅ ⚙️ » ✅✅✅✅✅ 📷" : "nabilanavab", "♻ ✅✅ ♻" : "set|thumb+", "« ✅✅✅✅✅ «" : "Home|B"},
        {"✅✅✅✅✅ ⚙️ » ✅✅✅✅✅ 📷" : "nabilanavab", "♻ ✅✅ ♻" : "set|thumb+", "🗑 ✅✅ 🗑" : "set|thumb-", "« ✅✅✅✅✅ «" : "Home|B2S"}
    ],
    "fname" : [
        {"✅✅✅✅✅ ⚙️ » ✅✅✅✅✅ 📷" : "nabilanavab", "♻ ✅✅ ♻" : "set|✅✅✅✅✅+", "« ✅✅✅✅✅ «" : "Home|B2S"},
        {"✅✅✅✅✅ ⚙️ » ✅✅✅✅✅ 📷" : "nabilanavab", "♻ ✅✅ ♻" : "set|fname+", "🗑 ✅✅ 🗑" : "set|fname-", "« ✅✅✅✅✅ «" : "Home|B2S"}
    ],
    "api" : [
        {"✅✅✅✅✅ ⚙️ » ✅✅✅ 📷" : "nabilanavab", "♻ ✅✅ ♻" : "set|api+", "« ✅✅✅✅✅ «" : "Home|B2S"},
        {"✅✅✅✅✅ ⚙️ » ✅✅✅ 📷" : "nabilanavab", "♻ ✅✅ ♻" : "set|api+", "🗑 ✅✅ 🗑" : "set|api-", "« ✅✅✅✅✅ «" : "Home|B2S"}
    ],
    "capt" : [
        {"✅✅✅✅✅ ⚙️ » ✅✅✅✅✅ 📷" : "nabilanavab", "♻ ✅✅ ♻" : "set|capt+", "« ✅✅✅✅✅ «" : "Home|B2S"},
        {"✅✅✅✅✅ ⚙️ » ✅✅✅✅✅ 📷" : "nabilanavab", "♻ ✅✅ ♻" : "set|capt+", "🗑 ✅✅ 🗑" : "set|capt-", "« ✅✅✅✅✅ «" : "Home|B2S"}
    ]
}

BOT_COMMAND = {
    "start" : "✅✅✅✅✅..", "txt2pdf" : "✅✅✅✅✅.."
}

HELP_CMD = {
    "userHELP" : """[✅✅✅✅✅]:\n
/start: ✅✅✅✅✅\n/cancel: ✅✅✅✅✅
/delete: ✅✅✅✅✅\n/txt2pdf: ✅✅✅✅✅""",
    "adminHelp" : """\n\n\n[✅✅✅✅✅]:\n
/send: ✅✅✅✅✅""",
    "footerHelp" : f"""\n\n\n✅✅✅✅✅: [i 💜 PDF]({str(settings.SOURCE_CODE)})
Bot: @i2pdfbot 💎\n[✅✅✅✅✅]({settings.OWNED_CHANNEL})""",
    "CB" : {"⚠️ ✅✅✅✅✅ ⚠️" : "close|all"}
}

STATUS_MSG = {
    "HOME" : "`✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅ 💱.. `",
    "_HOME" : {
        "📊 ↓ ✅✅✅✅✅ ↓ 📊" : "nabilanavab", "📶 ✅✅✅✅✅ 📶" : "status|server",
        "🥥 ✅✅✅✅✅ 🥥" : "status|db", "🌝 ↓ ✅✅✅✅✅ ↓ 🌝": "nabilanavab",
        "💎 ✅✅✅✅✅ 💎" : "status|admin", "👤 ✅✅✅✅✅ 👤" : "status|users",
        "« ✅✅✅✅✅ «" : "Home|A"
    },
    "DB" : """📂 ✅✅✅✅✅ :\n\n**◍ ✅✅✅✅✅ :** `{}` 📍\n**◍ ✅✅✅✅✅ :** `{}` 📍""",
    "SERVER" : """**◍ ✅✅✅✅✅     :** `{}`
**◍ ✅✅✅✅✅     :** `{}({}%)`\n**◍ ✅✅✅✅✅      :** `{}`
**◍ ✅✅✅✅✅      :** `{}`%\n**◍ ✅✅✅✅✅     :** `{}`%
**◍ ✅✅✅✅✅  :** `{}`\n**◍ ✅✅✅✅✅     :** `{}`""",
    "BACK" : {"« ✅✅✅✅✅ «" : "status|home"}, "ADMIN" : "**✅✅✅✅✅:** __{}__\n",
    "USERS" : "✅✅✅✅✅:\n\n", "NO_DB" : "✅✅✅✅✅ 💩"
}

feedbackMsg = f"[✅✅✅✅✅ 📋]({settings.FEEDBACK})"

# GROUP WELCOME MESSAGE
HomeG = {
    "HomeA" : """✅✅✅✅✅.! 🖐️\n✅✅✅✅✅ {message.chat.title}\n
✅✅✅✅✅..\n✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅
✅✅✅✅✅✅✅✅✅✅\n\n✅✅✅✅✅ @ta_ja199 ✅✅✅✅✅ 😅""",
    "HomeACB" : {
        "🤠 ✅✅✅✅✅ 🤠": f"https://telegram.dog/{settings.OWNER_USERNAME}",
        "🛡️ ✅✅✅✅✅ 🛡": f"{settings.OWNED_CHANNEL}", "🌟 ✅✅✅✅✅ 🌟": f"{settings.SOURCE_CODE}"
    }
}

# BANNED USER UI
BAN = {
    "cbNotU" : "✅✅✅✅✅ 😏",
    "banCB" : {
        "✅✅✅✅✅": f"{settings.SOURCE_CODE}", "✅✅✅✅✅": f"{settings.SOURCE_CODE}",
        "✅✅✅✅✅": "https://t.me/i2pdfbotchannel"
    },
    "UCantUse" : """✅✅✅ {}\n\n✅✅✅✅✅✅✅✅✅✅ :(""",
    "UCantUseDB" : """✅✅✅ {}\n\n✅✅✅✅✅✅✅✅✅✅ :(\n\n✅✅✅✅✅: {}""",
    "GroupCantUse" : """{} ✅✅✅✅✅✅✅✅✅✅\n
✅✅✅✅✅✅✅✅✅✅.. 🤭""",
    "GroupCantUseDB" : """{} ✅✅✅✅✅✅✅✅✅✅\n
✅✅✅✅✅✅✅✅✅✅.. 🤭\n\n✅✅✅✅✅: {}""",
    "Force" : """✅✅✅✅✅ [{}](tg://user?id={})..!!\n
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅ 🚶\n
✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅!\n
✅✅✅✅✅ `"♻️ ✅✅✅✅✅ ♻️"` ✅✅✅✅✅.. 😅""",
    "ForceCB" : {"🌟 ✅✅✅✅✅ 🌟" : "{}", "♻️ ✅✅✅✅✅ ♻️" : "refresh"},
    "Fool" : "✅✅✅✅✅✅✅✅✅✅.. 🤭"
}

checkPdf = {
    "pg" : "`✅✅✅✅✅✅✅✅✅✅: •{}•` 🌟",   # never remove •{}•
    "pdf" : """`✅✅✅✅✅.?`\n\n✅✅✅✅✅ : `{}`\n✅✅✅✅✅ : `{}`""",
    "pdfCB" : {
        "⭐ ✅✅✅✅✅ ⭐" : "metaData", "🗳️ ✅✅✅✅✅ 🗳️" : "preview",
        "🖼️ ✅✅✅✅✅ 🖼️" : "pdf|img", "✏️ ✅✅✅✅✅ ✏️" : "pdf|txt",
        "🔐 ✅✅✅✅✅ 🔐" : "work|encrypt", "🔒 ✅✅✅✅✅ 🔓" : "work|decrypt",
        "🗜️ ✅✅✅✅✅ 🗜️" : "work|compress", "🤸 ✅✅✅✅✅ 🤸" : "pdf|rotate",
        "✂️ ✅✅✅✅✅ ✂️" : "pdf|split", "🧬 ✅✅✅✅✅ 🧬" : "merge", "™️ STAMP ™️" : "pdf|stp",
        "✏️ ✅✅✅✅✅ ✏️" : "work|rename", "📝 ✅✅✅✅✅ 📝" : "work|ocr",
         "🥷 ✅✅✅✅✅ 🥷" : "work|format", "🚫 ✅✅✅✅✅ 🚫" : "close|all"
    },
    "error" : """__✅✅✅✅✅✅✅✅✅✅__ 😏\n\n🐉  `✅✅✅✅✅`  🐉""",
    "errorCB" : {"❌ ✅✅✅✅✅ ❌" : "error", "🔸 ✅✅✅✅✅ 🔸" : "close|all"},
    "encrypt" : """`✅✅✅✅✅` 🔐\n\n✅✅✅✅✅: `{}`\n✅✅✅✅✅: `{}`""",   # never remove 🔐
    "encryptCB" : {"🔓 DECRYPT 🔓" : "work|decrypt"}
}

PROGRESS = {
    "progress" : """**\n✅✅✅ ✅ : **{0}/{1}\n**✅✅✅ 🚀:** {2}/s\n**✅✅✅ ⏳:** {3}""",
    "dlImage" : "`✅✅✅✅✅✅..⏳`", "upFile" : "`✅✅✅✅✅✅✅..`📤",
    "dlFile" : "`✅✅✅✅✅✅✅✅✅✅..` 📥", "upFileCB" : {"📤 ..✅✅✅✅✅.. 📤" : "nabilanavab"},
    "workInP" : "✅✅✅✅✅.. 🙇", "refresh" : {"♻️ ✅✅✅✅✅ ♻️" : "{}"},
    "takeTime" : """```⚙️ ✅✅✅✅✅..`\n`✅✅✅✅✅..```💛""",
    "cbPRO_D" : ["📤 ✅✅✅✅✅: {:.2f}% 📤", "🎯 ✅✅✅✅✅ 🎯"], "cbPRO_U" : ["📤 ✅✅✅✅✅: {:.2f}% 📤", "🎯 ✅✅✅✅✅ 🎯"]
}

GENERATE = {
    "deleteQueue" : "`✅✅✅✅✅✅✅✅..`🤧", "noQueue" : "`✅✅✅✅✅✅✅✅..`😲",
    "noImages" : "✅✅✅✅✅✅✅.!! 😒", "getFileNm" : "✅✅✅✅✅✅✅✅ 😒: ",
    "geting" : "✅✅✅: `{}`\n✅✅✅: `{}`", "getingCB" : {"📚 ✅✅✅✅✅✅.." : "nabilanavab"}
}

document = {
    "refresh" : PROGRESS['refresh'], "inWork" : PROGRESS['workInP'], "reply" : checkPdf['pdf'],
    "replyCB" : checkPdf['pdfCB'], "download" : PROGRESS['dlFile'], "process" : "⚙️ ✅✅✅✅✅..",
    "takeTime" : PROGRESS['takeTime'], "upFile" : PROGRESS['upFile'], "dlImage" : PROGRESS['dlImage'],
    "big" : """✅✅✅✅✅✅✅✅✅✅ {}✅ ✅✅✅✅✅✅✅✅✅✅ 🙇
\n`✅✅✅✅✅✅✅✅✅✅ {}✅ ✅✅✅✅` 🙃""",
    "bigCB" : {"💎 ✅✅✅✅✅✅✅✅✅✅ 💎" : "https://t.me/i2pdfbotchannel"},
    "imageAdded" : """`✅✅✅✅✅ {} ✅✅✅✅✅..`🤓\n\n✅✅✅✅✅: `{}.pdf`""",
    "error" : """✅✅✅✅✅✅✅✅.. 🐉\n\n✅✅✅✅✅: `{}`""",
    "noAPI" : "`✅✅✅✅✅✅✅✅✅✅.. ✅✅✅✅✅ 😒`",
    "useDOCKER" : "`✅✅✅✅✅✅✅✅✅✅`",
    "fromFile" : "`✅✅✅✅✅: {} to {}`", "unsupport" : "`✅✅✅✅✅✅✅✅✅✅..🙄`",
    "generateRN" : {"✅✅✅✅✅ 📚" : "generate", "✅✅✅✅✅ ✍️" : "generateREN"},
    "generate" : {"✅✅✅✅✅ 📚" : "generate"}, "cancelCB" : {"⟨ ✅✅✅✅✅ ⟩" : "close|me"}
}

noHelp = f"`✅✅✅✅✅✅✅✅✅✅` 😏"

split = {
    "inWork" : PROGRESS['workInP'], "cancelCB" : document['cancelCB'],
    "download" : PROGRESS['dlFile'], "exit" : "`P✅✅✅✅✅..` 😏",
    "button" : {
        "⚙️ ✅✅ » ✅✅✅ ↓" : "nabilanavab", "✅✅✅✅✅ 🦞" : "split|R",
        "✅✅✅✅✅ 🐛" : "split|S", "« ✅✅✅✅✅ «" : "pdf"
    },
    "work" : ["✅✅", "✅✅"], "over" : "`✅✅✅✅✅..`😏",
    "pyromodASK_1" : """__✅✅ » ✅✅✅✅\n✅✅✅✅✅ (✅✅:✅✅) :__
\n/exit __✅✅✅✅✅__""",
    "completed" : "`✅✅✅✅✅..` ✅",
    "error_1" : "`✅✅✅✅✅ `🚶",
    "error_2" : "`✅✅✅✅✅ `🚶",
    "error_3" : "`✅✅✅✅✅ `🚶",
    "error_4" : "`✅✅✅✅✅` 🧠",
    "error_5" : "`✅✅✅✅✅` 🚶",
    "error_6" : "`✅✅✅✅✅..`😏",
    "error_7" : "`S✅✅✅✅✅..`😅", "error_8" : "`✅✅✅✅✅ {}..`😏",
    "error_9" : "`✅✅✅✅✅` 😏", "upload" : "⚙️ `✅✅✅✅✅..` 📤"
}

pdf2IMG = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "uploadfile" : split["upload"],
    "toImage" : {
        "⚙️ ✅✅ » ✅✅✅ ↓" : "nabilanavab", "🖼 ✅✅ 🖼" : "pdf|img|img",
        "📂 ✅✅ 📂" : "pdf|img|doc", "🤐 ✅✅ 🤐" : "pdf|img|zip",
        "🎯 ✅✅ 🎯" : "pdf|img|tar","« ✅✅ «" : "pdf" 
    },
    "imgRange" : {
        "⚙️ ✅✅ » I✅✅ » {} ↓" : "nabilanavab", "🙄 ✅✅✅ 🙄" : "p2img|{}A",
        "🤧 ✅✅ 🤧" : "p2img|{}R", "🌝 ✅✅✅ 🌝" : "p2img|{}S", "« ✅✅✅ «" : "pdf|img"
    },
    "over" : "`✅✅✅✅✅✅✅✅✅✅..`😏",
    "pyromodASK_1" : """__✅✅ - ✅✅›✅✅ » ✅✅:\n✅✅✅✅✅✅✅✅ (✅✅:✅✅) :__
\n/exit __✅✅✅✅__""",
    "pyromodASK_2" : """"__✅✅ - ✅✅›✅✅ » ✅✅:\n✅✅✅✅✅✅✅✅✅✅✅✅✅✅__ (,) :
\n/exit __✅✅✅✅__""",
    "exit" : "`✅✅✅✅✅✅..` 😏",
    "error_1" : "`✅✅✅✅✅✅✅✅ `🚶",
    "error_2" : "`✅✅✅✅✅✅✅✅ `🚶",
    "error_3" : "`✅✅✅✅✅✅✅✅ `🚶",
    "error_4" : "`✅✅✅✅✅✅✅✅` 🧠",
    "error_5" : "`✅✅✅✅✅✅✅✅` 🚶",
    "error_6" : "`✅✅✅✅✅✅✅✅..`😏", "error_7" : "`✅✅✅✅✅✅..`😅",
    "error_8" : "`✅✅✅✅ {} ✅✅` 💩", "error_9" : "`✅✅✅✅✅✅` 😏",
    "error_10" : "__✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅..__😅",
    "total" : "`✅✅✅✅: {}..⏳`", "upload" : "`✅✅✅✅: {}/{} ✅✅✅✅✅✅.. 🐬`",
    "current" : "`✅✅✅✅: {}/{} ✅✅.. 🤞`", "complete" : "`✅✅✅✅✅✅.. `🏌️",
    "canceledAT" : "`✅✅✅✅ {}/{} ✅✅..` 🙄", "cbAns" : "⚙️ ✅✅✅✅.. ",
    "cancelCB" : {"💤 ✅✅✅✅ 💤" : "close|P2I"},     # EDITABLE: ❌
    "canceledCB" : {"🍄 ✅✅✅✅ 🍄" : "close|P2IDONE"},
    "completed" : {"😎 ✅✅✅✅ 😎" : "close|P2ICOMP"}
}

merge = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "upload" : PROGRESS['upFile'],
    "load" : "__✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅__",
    "sizeLoad" : "`✅✅✅✅✅✅✅✅✅✅✅✅ %s✅ ✅✅✅..", # removing %s show error
    "pyromodASK" : """__✅✅✅✅✅✅✅✅✅✅✅✅: {}__

/exit __✅✅✅✅✅✅__
/merge __✅✅✅✅✅✅__""",
    "exit" : "`✅✅✅✅..` 😏", "total" : "`✅✅✅✅✅✅ : {} 💡",
    "current" : "__✅✅✅✅✅✅ : {} 📥__", "cancel" : "`✅✅✅✅✅✅.. 😏`",
    "started" : "__✅✅✅✅✅✅.. __ 🪄", "caption" : "`✅✅✅✅✅✅ 🙂`",
    "error" : "`✅✅✅✅✅✅..`\n\n✅✅✅✅: {}"
}

metaData = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "download" : PROGRESS['dlFile'],   # [❌]
    "read" : "✅✅✅✅✅✅✅✅✅✅✅✅✅✅.. 🥴"
}

preview = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "error" : document['error'],
    "download" : PROGRESS['dlFile'], "_" : "✅✅✅✅ {} ✅✅ 🤓\n\n",
    "__" : "✅✅✅✅: {}\n\n", "total" : "`✅✅✅✅: {}..` 🤌",
    "album" : "`✅✅✅✅✅✅..` 🤹", "upload" : f"`✅✅✅✅✅✅.. 🐬`"
}

stamp = {
    "stamp" : {
        "⚙️ ✅ » ✅✅ ↓" : "nabilanavab",
        "Not For Public Release 🤧" : "pdf|stp|10",
        "For Public Release 🥱" : "pdf|stp|8",
        "Confidential 🤫" : "pdf|stp|2", "Departmental 🤝" : "pdf|stp|3",
        "Experimental 🔬" : "pdf|stp|4", "Expired 🐀" : "pdf|stp|5",
        "Final 🔧" : "pdf|stp|6", "For Comment 🗯️" : "pdf|stp|7",
        "Not Approved 😒" : "pdf|stp|9", "Approved 🥳" : "pdf|stp|0",
        "Sold ✊" : "pdf|stp|11", "Top Secret 😷" : "pdf|stp|12",
        "Draft 👀" : "pdf|stp|13", "AsIs 🤏" : "pdf|stp|1",
        "« ✅✅ «" : "pdf"
    },
    "stampA" : {
        "⚙️ ✅ » ✅✅ » ✅✅ ↓" : "nabilanavab",
        "✅✅ ❤️" : "spP|{}|r", "✅✅ 💙" : "spP|{}|b",
        "✅✅ 💚" : "spP|{}|g", "✅✅ 💛" : "spP|{}|c1",
        "✅✅ 💜" : "spP|{}|c2", "✅✅ 💚" : "spP|{}|c3",
        "✅✅ 🤍" : "spP|{}|c4", "✅✅ 🖤" : "spP|{}|c5",
        "« Back «" : "pdf|stp"
    },
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "upload" : PROGRESS['upFile'],
    "stamping" : "`✅✅..` 💠", "caption" : """✅✅✅\n✅✅✅ : `{}`\n✅✅✅ : `{}`"""
}

work = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "takeTime" : PROGRESS['takeTime'],
    "upload" : PROGRESS['upFile'], "button" : document['cancelCB'],
    "rot360" : "✅✅✅✅✅✅✅✅..🙂", "ocrError" : "✅✅✅✅✅✅ 😎🤏",
    "largeNo" : "✅✅✅✅✅✅✅✅.. 🙄",
    "pyromodASK_1" : """__✅✅✅✅ {} »\n✅✅, ✅✅✅✅✅✅✅✅ :__\n\n/exit __✅✅✅✅✅✅__""",
    "pyromodASK_2" : """__R✅✅✅✅✅✅ »\n✅✅, ✅✅✅✅✅✅✅✅:__\n\n/exit __✅✅✅✅__""",
    "exit" : "`✅✅✅✅✅✅.. `😏", "ren_caption" : "__✅✅✅✅:__ `{}`", 
    "notENCRYPTED" : "`✅✅✅✅✅✅..` 👀",
    "compress" : "⚙️ `✅✅✅✅✅✅.. 🌡️\n✅✅✅✅✅✅..`💛",
    "decrypt" : "⚙️ `✅✅✅✅✅✅.. 🔓\n✅✅✅✅✅✅..`💛",
    "encrypt" : "⚙️ `✅✅✅✅✅✅.. 🔐\n✅✅✅✅✅✅..`💛",
    "ocr" : "⚙️ `✅✅✅✅✅✅.. ✍️\n✅✅✅✅✅✅..`💛",
    "format" : "⚙️ `✅✅✅✅✅✅.. 🤘\n✅✅✅✅✅✅..`💛",
    "rename" : "⚙️ `✅✅✅✅✅✅.. ✏️\nI✅✅✅✅✅✅..`💛",
    "rot" : "⚙️ `✅✅✅✅✅✅.. 🤸\n✅✅✅✅✅✅..`💛",
    "pdfTxt" : "⚙️ `✅✅✅✅✅✅.. 🐾\n✅✅✅✅✅✅..`💛",
    "fileNm" : "✅✅✅✅✅✅: {}\nN✅✅✅✅✅✅: {}",
    "rotate" : {
        "⚙️ ✅✅ » ✅✅ ↓" : "nabilanavab", "90°" : "work|rot90", "180°" : "work|rot180",
        "270°" : "work|rot270", "360°" : "work|rot360", "« ✅✅ «" : "pdf"
    },
    "txt" : {
        "⚙️ ✅✅ » ✅✅ ↓" : "nabilanavab", "📜 ✅✅ 📜" : "work|M", "🧾 ✅✅ 🧾" : "work|T",
        "🌐 ✅✅ 🌐" : "work|H", "🎀 ✅✅ 🎀" : "work|J", "« ✅✅ «" : "pdf"
    }
}

PROCESS = {
    "ocr" : "✅✅", "decryptError" : "__✅✅__ ||{}||` 🕸️",
    "decrypted" : "__✅✅__", "encrypted" : "__✅✅✅✅__: {}\n__✅✅__ 🔐: ||{}||",
    "compressed" : """`✅✅✅✅ : {}\n✅✅✅✅ : {}\n\n✅✅✅✅ : {:.2f} %`""",
    "cantCompress" : "✅✅✅✅✅✅..🤐",
    "pgNoError" : """__✅✅✅✅✅✅✅✅✅✅__\n\n✅✅✅✅✅✅: {} ⭐""",
    "ocrError" : "`✅✅✅✅✅✅✅✅.. `😏",
    "90" : "__✅✅✅✅ 90°__", "180" : "__Rotated 180°__", "270" : "__✅✅✅✅ 270°__",
    "formatted" : "✅✅✅✅", "M" : "♻ ✅✅ {} ✅✅ ♻",
    "H" : "✅✅✅✅", "T" : "TXT File", "J" : "✅✅✅✅"
}

pdf2TXT = {
    "upload" : PROGRESS["upFile"], "exit" : split['exit'], "nothing" : "✅✅✅✅.. 😏",
    "TEXT" : "`✅✅✅✅✅✅✅✅✅✅✅✅ »`", "start" : "✅✅✅✅✅✅✅✅✅✅..🎉",
    "font_btn" : {
        "✅✅ » ✅✅" : "nabilanavab", "Times" : "pdf|font|t", "Courier" : "pdf|font|c", "Helvetica (Default)" : "pdf|font|h",
        "Symbol" : "pdf|font|s", "Zapfdingbats" : "pdf|font|z", "🚫 ✅✅ 🚫" : "close|me"
    },
    "size_btn" : { "✅✅ » {} » ✅✅" : "nabilanavab", "Portarate" : "t2p|{}|p", "Landscape" : "t2p|{}|l", "« ✅✅ «": "pdf|T2P"},
    "askT" : "__✅✅✅✅ » ✅✅✅✅✅✅:__\n\n/exit __✅✅✅✅__\n/skip __✅✅✅✅__",
    "askC" : "__✅✅✅✅ » ✅✅✅✅✅✅ {}:__\n\n/exit __✅✅✅✅__\n/create __✅✅✅✅__"
}

URL = {
    "get" : {"🧭 ✅✅✅✅ 🧭" : "getFile"}, "close" : HELP_CMD['CB'],
    "start" : "```✅✅✅✅✅✅..\n✅✅✅✅✅✅``` ✨", "notPDF" : "`✅✅✅✅✅✅",
    "error" : "🐉 ✅✅✅✅ 🐉\n\n✅✅: `{}`\n\n✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅ =)",
    "done" : "```✅✅✅✅.. ✅\n✅✅, ✅✅✅✅.. 📤```", "_error_" : "✅✅✅✅✅✅✅✅✅✅✅✅",
    "openCB" : {"✅✅✅✅" : "{}"}, "_error" : "`✅✅✅✅✅✅ =(`\n\n`{}`",
    "_get" : "[✅✅✅✅]({})\n\n**✅✅✅✅ ↓**\n✅✅   : {}\n✅✅ : {}\n✅✅    : @{}\n"
             "✅✅        : {}\n✅✅ : {}\n\n**✅✅ ↓**\n✅✅       : {}\n✅✅ : {}\n✅✅   : {}\n\n✅✅ : {}"
}

getFILE = {
    "inWork" : PROGRESS['workInP'], "big" : "✅✅✅✅✅✅✅✅ {}✅", "wait" : "✅✅✅✅✅✅.. 😜",
    "dl" : {"📥 ..✅✅✅✅.. 📥" : "nabilanavab"}, "up" : {"📤 ..✅✅✅✅..  📤" : "nabilanavab"},
    "complete" : {"😎 ✅✅✅✅ 😎" : f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "✅✅✅✅✅✅✅✅ ⛷️", "✅✅✅✅✅✅.. ✅✅✅✅.. 😏",
    "✅✅✅✅✅✅.. 😏", "✅✅✅✅✅✅.. 👀", "✅✅✅✅✅✅.. 😅", "🎉 ✅✅✅✅✅✅.. 🏃"
]

inline_query = {
    "TOP" : { "✅✅, ✅✅✅✅✅✅ ➟" : "nabilanavab" }, "capt" : "✅✅✅✅✅✅ ⚙️", "des" : "By: @ta_ja199 ❤"
}
