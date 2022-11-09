# LANG: HINDI [INDIA 🇮🇳] LANG CODE: HND                            >>  copyright ©️ 2021 nabilanavab  <<                                         fileName : lang/hnd.py
#                                       Thank: nabilanavab                                               E-mail: nabilanavab@gmail.com

from configs.config import settings

# PM स्वागत संदेश (घर A, B, C, D...)
HOME = {
    "HomeA": """अरे [{}](tg://user?id={})..!!
यह बॉट आपको पीडीएफ के . के साथ कई काम करने में मदद करेगा

कुछ प्रमुख विशेषताएं हैं:\n◍ `छवियों को पीडीएफ में बदलें`
◍ `पीडीएफ को छवियों में बदलें`\n◍ `फाइलों को पीडीएफ में बदलें`""",
    "HomeACB" : {
        "⚙️ सेटिंग्स ⚙️" : "Home|B", "⚠️ हेल्प ️⚠️" : "Home|C",
        "📢 चैनल 📢" : f"{str(settings.OWNED_CHANNEL)}",
        "🌟 स्रोत कोड 🌟" : f"{str(settings.SOURCE_CODE)}",
        "🚶 पास 🚶" : "close|mee"
    },
    "HomeAdminCB" : {
        "⚙️ सेटिंग्स ⚙️" : "Home|B", "⚠️ हेल्प ️⚠️" : "Home|C",
        "📢 चैनल 📢" : f"{str(settings.OWNED_CHANNEL)}",
        "🌟 स्रोत कोड 🌟" : f"{str(settings.SOURCE_CODE)}",
        "🗽 STATUS 🗽" : f"status|home", "🚶 पास 🚶" : "close|mee"
    },
    "HomeB" : """सेटिंग पेज ⚙️\n\nउपयोगकर्ता का नाम : {}
उपयोगकर्ता आईडी: {}\nउपयोगकर्ता नाम: {}\nशामिल होने की तिथि: {}\n
भाषा : {}\nएपीआई : {}
अंगूठा : {}\nकैप्शन : {}\nफ़ाइल का नाम : {}""",
    "HomeBCB" : {
        "🌍 भाषा 🌎" : "set|lang", "📍 थंबनेल 📍" : "set|thumb",
        "📈 नाम 📈" : "set|fname", "💩 एपीआई 💩" : "set|api",
        "📅 कैप्शन 📅" : "set|capt", "« घर वापिस जा रहा हूँ «" : "Home|B2A"
    },
    "HomeC" : """🪂 **सहायता संदेश** 🪂:
```
कुछ मुख्य विशेषताएं हैं:
 ◍ छवियों को पीडीएफ में बदलें\n ◍ पीडीएफ मैनुपल्शंस\n ◍ पीडीएफ में कई लोकप्रिय कोडेक्स
 
पीडीएफ फाइल को संशोधित करें:
 ◍ PDF⥃इमेज [सभी, रेंज, पेज]\n ◍ PDF से DOCS [png, jpg, jpeg]\n ◍ IMAGES⥃PDF\n ◍ PDF METADATA\n ◍ PDF⥃TEXT\n ◍ TEXT⥃PDF\n ◍ पीडीएफ फाइल को कंप्रेस करें
 ◍ स्प्लिट पीडीएफ [रेंज, पेज]\n ◍ मर्ज पीडीएफ\n ◍ स्टैम्प जोड़ें\n ◍ पीडीएफ का नाम बदलें\n ◍ पीडीएफ को घुमाएं\n ◍ एनक्रिप्ट/डिक्रिप्ट पीडीएफ\n ◍ पीडीएफ फॉर्मेटर \n ◍ पीडीएफ⥃JSON/TXT फाइल
 ◍ PDF⥃HTML [वेब दृश्य]\n ◍ URL⥃PDF\n ◍ PDF⥃ZIP/TAR/RAR [सभी, श्रेणी, पृष्ठ]\nऔर भी बहुत कुछ.. ```""",
    "HomeCCB" : {"« वापस घर «": "Home|A", "🛈 निर्देश 🛈": "Home|D"},
    "HomeD" : """`चूंकि यह एक मुफ्त सेवा है, मैं गारंटी नहीं दे सकता कि मैं इस सेवा को कब तक बनाए रख सकता हूं..`😝
 
️⚠️ निर्देश ️⚠️:
🛈 __कृपया बॉट व्यवस्थापकों को गाली देने की कोशिश न करें__ 😒
🛈 __यहां स्पैम न करें, स्थायी प्रतिबंध लग सकता है 🎲__।
🛈 __पोर्न सामग्री भी आपको स्थायी प्रतिबंध देगी 💯__

**शुरू करने के लिए कोई भी चित्र भेजें: 😁**""",
    "HomeDCB" : {"⚠️ हेल्प ️⚠️" : "Home|C", "» बैक होम »" : "Home|A"}
}

SETTINGS = {
    "default" : ["डिफ़ॉल्ट ", "कस्टम ✅"], "chgLang": {"सेटिंग ️ » चेंज लैंग ": "nabilanavab"},
    "error": "डेटाबेस से डेटा पुनर्प्राप्त करते समय कुछ गलत हुआ", "lang": "अब, कोई भी भाषा चुनें..",
    "ask" : ["अब, मुझे भेजो..", "अब, मुझे भेजो.. 😅\n\nजल्दी करो। मेरे पास टेक्स्ट पर जाने के लिए और समय नहीं है। 😏\n\n/cancel: रद्द करने के लिए"],
    "askApi" : "\n\nनीचे दिए गए लिंक को खोलें और मुझे गुप्त कोड भेजें:", "waitApi" : {"लिंक खोलें ✅" : "https://www.convertapi.com/a/signin"},
    "wait" : {"प्रतीक्षा कर रहा है..🥱" : "nabilanavab"}, "back" : {"« घर वापिस जा रहा हूँ «" : "Home|B2S"}, "errorCB" : {"« घर वापिस जा रहा हूँ «": "होम|बी2ए"},
    "result" : ["सेटिंग्स को अपडेट नहीं किया जा सकता ", "सेटिंग्स सफलतापूर्वक अपडेट किया गया ✅"], "cant": "इस सुविधा का उपयोग नहीं किया जा सकता ❌",
    "feedback" : "आप जैसे शानदार ग्राहकों की समीक्षाएं दूसरों की मदद करती हैं।\n@ta_ja199"
                 "\n\n{} भाषा में बग की रिपोर्ट करें:\n`• भाषा निर्दिष्ट करें\n• त्रुटि संदेश\n• नया संदेश`",
    "feedbtn" : {"रिपोर्ट लैंग एरर": settings.REPORT},
    "thumb" : [
        {"सेटिंग ️ » थंबनेल 📷" : "nabilanavab", "♻ जोड़ें ♻" : "set|thumb+", "« घर पर वापस जाएं «" : "Home|B"},
        {"सेटिंग ️ » थंबनेल 📷": "nabilanavab", "♻ चेंज ♻": "set|thumb+", "🗑 डिलीट 🗑" : "set|thumb-", "« बैक टू होम «": "Home|B2S"}
    ],
    "fname" : [
        {"सेटिंग ⚙️ » FNAME 📷" : "nabilanavab", "♻ जोड़ें ♻" : "set|fname+", "« होम टू होम «": "Home|B2S"},
        {"सेटिंग ⚙️ » FNAME 📷" : "nabilanavab", "♻ चेंज ♻" : "set|fname+", "🗑 डिलीट 🗑" : "set|fname-", "« वापस घर पर «" : "Home|B2S"}
    ],
    "api" : [
        {"सेटिंग ️ » एपीआई 📷" : "nabilanavab", "♻ जोड़ें ♻" : "set|api+", "« होम टू होम «": "Home|B2S"},
        {"सेटिंग ️ » एपीआई 📷" : "nabilanavab", "♻ चेंज ♻" : "set|api+", "🗑 डिलीट 🗑" : "set|api-", "« होम टू होम «": "Home|B2S"}
    ],
    "capt" : [
        {"सेटिंग ️ » कैप्शन " : "nabilanavab", "♻ जोड़ें ♻" : "set|capt+", "« होम टू होम «" : "Home|B2S"},
        {"सेटिंग ️ » कैप्शन " : "nabilanavab", "♻ चेंज ♻" : "set|capt+", "🗑 डिलीट 🗑" : "set|capt-", "« बैक टू होम «" : "Home|B2S"}
    ]
}

BOT_COMMAND = {"start" : "स्वागत संदेश..", "txt2pdf" : "टेक्स्ट पीडीएफ बनाएं"}

HELP_CMD = {
    "userHELP" : """[यूजर कमांड मेसेज]:\n
/start: यह जांचने के लिए कि क्या बॉट जीवित है\n/cancel: वर्तमान कार्य रद्द करें 
/delete: पीडीएफ कतार में छवि साफ़ करें\n/txt2pdf: पीडीएफ के लिए पाठ""",
    "adminHelp": """\n\n\n[व्यवस्थापक आदेश संदेश]:\n
/भेजें: प्रसारण के लिए, दोपहर संदेश """,
    "footerHelp" : f"""\n\n\nस्रोत-कोड: [i2pdf]({str(settings.SOURCE_CODE)})
बॉट: @i2pdfbot 💎\n[सपोर्ट चैनल]({settings.OWNED_CHANNEL})""",
    "CB": {"⚠️ बंद करें ️⚠️": "close|all"}
}

STATUS_MSG = {
    "HOME" : "'अब, वर्तमान स्थिति प्राप्त करने के लिए नीचे किसी भी विकल्प का चयन करें .. `",
    "_HOME" : {
        "📊 सर्वर 📊" : "nabilanavab", "📶 स्टोरेज 📶" : "status|server",
        "🥥 DATABASE 🥥" : "status|db", "🌝 GET LIST 🌝" : "nabilanavab",
        "💎 व्यवस्थापक 💎" : "status|admin", "👤 उपयोगकर्ता 👤" : "status|users",
        "« वापस «": "Home|A"
    },
    "DB" : """📂 डेटाबेस:\n\n**◍ डेटाबेस उपयोगकर्ता:** `{}` 📍\n**◍ डेटाबेस चैट:** `{}` """,
    "SERVER" : """**◍ कुल स्थान:** `{}`
**◍ प्रयुक्त स्थान:** `{}({}%)`\n**◍ खाली स्थान:** `{}`
**◍ CPU उपयोग:** `{}`%\n**◍ RAM उपयोग:** `{}`%
**◍ वर्तमान कार्य :** `{}`\n**◍ संदेश आईडी:** `{}`""",
    "BACK" : {"« वापस «": "स्थिति|होम"}, "ADMIN" : "**कुल व्यवस्थापक:** __{}__\n",
    "USERS" : "DB में सहेजे गए उपयोगकर्ता हैं:\n\n", "NO_DB" : "अभी तक कोई डेटाबेस सेट नहीं है 💩"
}

FeedbackMsg = f"[एक प्रतिक्रिया लिखें 📋]({settings.FEEDBACK})"

#समूह स्वागत संदेश
HomeG = {
    "HomeA" : """नमस्कार! ️\nमैं यहां नया हूं {message.chat.title}\n
मुझे अपना परिचय दें..\nमेरा नाम iLovePDF है, और मैं बहुत कुछ करने में आपकी मदद कर सकता हूँ
@Telegram PDF फ़ाइलों वाली चीज़ें\n\nइस शानदार बॉट के लिए @ta_ja199 को धन्यवाद""",
    "HomeACB" : {
        "🤠 बीओटी मालिक 🤠": f"https://telegram.dog/{settings.OWNER_USERNAME}",
        "🛡️ अपडेट चैनल 🛡️": f"{settings.OWNED_CHANNEL}", "🌟 सोर्स कोड | other 🌟": f"{settings.SOURCE_CODE}"
    }
}

# प्रतिबंधित यूजर यूआई
BAN = {
    "cbNotU" : "मैसेज नॉट फॉर यू.. 😏",
    "banCB" : {
        "अपना खुद का बॉट बनाएं": f"{settings.SOURCE_CODE}", "ट्यूटोरियल": f"{settings.SOURCE_CODE}",
        "अपडेट चैनल": "https://t.me/i2pdfbotchannel"
    },
    "UCantUse" : """अरे {}\n\nकिसी कारण से आप इस बॉट का उपयोग नहीं कर सकते :(""",
    "UCantUseDB" : """अरे {}\n\nकिसी कारण से आप इस बीओटी का उपयोग नहीं कर सकते :(\n\nकारण: {}""",
    "GroupCantUse" : """{} मुझसे कभी भी अच्छी प्रतिक्रिया की अपेक्षा न करें\n
व्यवस्थापकों ने मुझे यहां काम करने से प्रतिबंधित कर दिया.. """,
    "GroupCantUseDB" : """{} मुझसे कभी भी अच्छी प्रतिक्रिया की अपेक्षा न करें\n
व्यवस्थापकों ने मुझे यहां काम करने से प्रतिबंधित कर दिया.. 🤭\n\nकारण: {}""",
    "Force" : """रुको [{}](tg://user?id={})..!!\n
अत्यधिक ट्रैफ़िक के कारण केवल चैनल के सदस्य ही इस बॉट का उपयोग कर सकते हैं \n
इसका मतलब है कि मुझे इस्तेमाल करने के लिए आपको नीचे दिए गए चैनल से जुड़ना होगा!\n
ज्वाइन करने के बाद `"♻️ ताज़ा करें ♻️"` पर हिट करें.. """,
    "ForceCB": {"🌟 चैनल में शामिल हों 🌟": "{}", "♻️ ताज़ा करें ️♻️": "refresh"},
    "fool": "मूर्ख बनाने की कोशिश मत करो.. 🤭"
}

checkPdf = {
    "pg" : "`पृष्ठों की संख्या: •{}•` ",
    "pdf" : """ `मुझे इस फाइल के साथ क्या करना चाहिए?`\n\nफ़ाइल का नाम: `{}`\nफ़ाइल का आकार: `{}`""",
    "pdfCB" : {
        "⭐ मेटा पाउंड एटीए " : "metaData", "🗳️ पूर्वावलोकन 🗳️" : "preview",
        "🖼️ IMAGES ️" : "pdf|img", "✏️ TEXT ✏️" : "pdf|txt",
        "🔐 ENCRYPT " : "work|encrypt", "🔒 DECRYPT " : "work|decrypt",
        "🗜️ COMPRESS ️" : "work|compress", "🤸 ROTATE 🤸" : "pdf|rotate",
        "✂️ SPLIT ️" : "pdf|split", "   MERGE   ": "मर्ज", "™️ STAMP ™️" : "pdf|stp",
        "✏️ नाम बदलें ️": "work|rename", "📝 ओसीआर 📝": "work|ocr",
         "   A4 FORMAT   " : "work|format", "🚫 CLOSE " : "close|all"
    },
    "error" : """__मैं इस फ़ाइल के साथ कुछ नहीं करता__ 😏\n\n🐉 `कोडेक त्रुटि` 🐉""",
    "errorCB": {"❌ CODEC में त्रुटि ❌" : "error", "🔸 CLOSE 🔸": "close|all"},
    "encrypt": """`फ़ाइल एन्क्रिप्ट की गई है` 🔐\n\nफ़ाइल का नाम: `{}`\nफ़ाइल का आकार: `{}`""",
    "encryptCB" : {"🔓 DECRYPT " : "work|decrypt"}
}

PROGRESS = {
    "progress" : """**\nहो गया ✅ : **{0}/{1}\n**गति 🚀:** {2}/s\n**अनुमानित समय ⏳:** {3}""",
    "dlImage" : "`अपनी इमेज डाउनलोड कर रहा है..⏳`", "upFile" : "`अपलोड करना शुरू किया..`📤",
    "dlFile" : "`अपनी फाइल डाउनलोड कर रहा है..` ", "upFileCB" : {"📤 .. UPLOADING.. " : "nabilanavab"},
    "workInP": "कार्य प्रगति पर है.. 🙇", "refresh" : {"♻️ ताज़ा करें ️" : "{}"},
    "takeTime" : """```⚙️ कार्य प्रगति पर है..`\n`इसमें कुछ समय लग सकता है..```💛""",
    "cbPRO_D" : ["📤 डाउनलोड करें: {:.2f}% ", "🎯 CANCEL 🎯"], "cbPRO_U" : ["📤 UPLOADED: {:.2f}% ", "🎯 CANCEL 🎯"]
}

GENERATE = {
    "deleteQueue" : "`कतार सफलतापूर्वक हटाई गई..`🤧", "noQueue" : "`कोई कतार स्थापित नहीं..`😲",
    "noImages" : "कोई छवि स्थापित नहीं.!! 😒", "getFileNm" : "अब मुझे एक फ़ाइल नाम भेजें 😒: ",
    "geting" : "फ़ाइल का नाम: `{}`\nपृष्ठों: `{}`", "getingCB" : {"📚 पीडीएफ उत्पन्न करना.." : "nabilanavab"},
    "currDL" : "डाउनलोड की गई {} छवियां 🥱"
}

document = {
    "refresh" : PROGRESS['refresh'], "inWork" : PROGRESS['workInP'], "reply" : checkPdf['pdf'],
    "replyCB" : checkPdf['pdfCB'], "download" : PROGRESS['dlFile'], "process" : "⚙️ Processing..",
    "takeTime" : PROGRESS['takeTime'], "upFile" : PROGRESS['upFile'], "dlImage" : PROGRESS['dlImage'],
    "big" : """अधिभार के कारण, पीडीएफ फाइलों के लिए मालिक की सीमा
\n`कृपया मुझे {}mb आकार` से कम की फ़ाइल भेजें""",
    "bigCB" : {"💎 2Gb सपोर्ट बॉट बनाएं " : "https://t.me/i2pdfbotchannel"},
    "imageAdded" : """`जोड़ा गया {} पेज/आपके pdf में..`🤓\n\nfileName: `{}.pdf`""",
    "setHdImg" : """अब इमेज टू पीडीएफ एचडी मोड में है 😈""",
    "setDefault": {"« डिफ़ॉल्ट गुणवत्ता पर वापस «" : "close|hd"},
    "error": """कुछ गलत हो गया.. 🐉\n\nत्रुटि: `{}`""",
    "noAPI" : "`कृपया कन्वर्ट एपीआई जोड़ें.. \n\nप्रारंभ » सेटिंग्स » एपीआई » जोड़ें/बदलें`",
    "useDOCKER" : "`फ़ाइल समर्थित नहीं है, docker का उपयोग करके bot को परिनियोजित करें",
    "fromFile" : "`Converted: {} to {}`", "unsupport" : "`unsupported file..🙄`",
    "generateRN" : {"जेनरेट 📚": "generate", "रीनाम ️✍️": "generateREN"},
    "generate" : {"जेनरेट 📚": "generate"}, "cancelCB": {"⟨ रद्द करें ": "close|me"}
}

noHelp = f"`कोई भी आपकी मदद करने वाला नहीं है` "

split = {
    "inWork" : PROGRESS['workInP'], "cancelCB" : document['cancelCB'],
    "download" : PROGRESS['dlFile'], "exit" : "`Process Canceled..` 😏",
    "button" : {
        "⚙️ पीडीएफ » स्प्लिट ↓" : "nabilanavab", "विथ इन रेंज   " : "split|R",
        "सिंगल पेज 🐛": "split|S", "« बैक «": "pdf"
    },
    "work" : ["रेंज", "सिंगल"], "over" : "`5 प्रयास खत्म .. प्रक्रिया रद्द ..`😏",
    "pyromodASK_1" : """__Pdf स्प्लिट » रेंज के अनुसार\nअब, रेंज दर्ज करें (प्रारंभ:अंत) :__
\n/निकास __करने के लिए__""",
    "completed": "`डाउनलोडिंग पूर्ण..` ✅",
    "error_1": "`सिंटैक्स एरर: JustNeedStartAndEnd `🚶",
    "error_2": "`वाक्यविन्यास त्रुटि: errorInEndingPageNumber `🚶",
    "error_3": "`सिंटैक्स त्रुटि: errorInStartingPageNumber `🚶",
    "error_4": "`सिंटैक्स एरर: पेजनंबरमस्टबीडिजिट` 🧠",
    "error_5": "`वाक्यविन्यास त्रुटि: noEndingPageNumber या notADigit` ",
    "error_6" : "`कोई नंबर नहीं ढूंढ सकता..`😏",
    "error_7" : "`कुछ गलत हो गया..`😅", "error_8" : "`{}..`😏 से कम संख्याएं दर्ज करें",
    "error_9" : "`पहला चेक पेजों की संख्या` ", "upload" : "⚙️ `अपलोड करना शुरू किया..` "
}

pdf2IMG = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "uploadfile" : split["upload"],
    "toImage" : {
        "⚙️ PDF » IMAGES ↓" : "nabilanavab", "🖼 IMG 🖼" : "pdf|img|img",
        "📂 DOC 📂" : "pdf|img|doc", "🤐 ZIP 🤐" : "pdf|img|zip",
        "🎯 TAR 🎯" : "pdf|img|tar","« BACK «" : "pdf" 
    },
    "imgRange" : {
        "⚙️ PDF » IMAGES » {} ↓" : "nabilanavab", "🙄 ALL 🙄" : "p2img|{}A",
        "🤧 RANGE 🤧" : "p2img|{}R", "🌝 PAGES 🌝" : "p2img|{}S", "« BACK «" : "pdf|img"
    },
    "over" : "`5 अटेम्प्ट ओवर.. प्रोसेस कैंसिल ..`😏",
    "pyromodASK_1" : """__Pdf - Img›डॉक्टर » पृष्ठ:\nअब, श्रेणी दर्ज करें (प्रारंभ:अंत) :__
\n/निकास __करने के लिए__""",
    "pyromodASK_2" : """"__Pdf - Img›डॉक्टर » पेज:\nअब, __ (,) से अलग किए गए पेज नंबर दर्ज करें:
\n/निकास __करने के लिए__""",
    "exit": "`प्रक्रिया रद्द ..` 😏",
    "error_1": "`सिंटैक्स एरर: JustNeedStartAndEnd `🚶",
    "error_2": "`वाक्यविन्यास त्रुटि: errorInEndingPageNumber `🚶",
    "error_3": "`सिंटैक्स त्रुटि: errorInStartingPageNumber `🚶",
    "error_4": "`सिंटैक्स एरर: पेजनंबरमस्टबीडिजिट` 🧠",
    "error_5": "`वाक्यविन्यास त्रुटि: noEndingPageNumber या notADigit` 🚶",
    "error_6" : "`कोई नंबर नहीं ढूंढ सकता..`😏", "error_7" : "`कुछ गलत हो गया..`😅",
    "error_8" : "`PDF में केवल {} पेज' 💩", "error_9" : "`1 पेजों की संख्या की जांच करें` 😏",
    "error_10" : "__कुछ प्रतिबंधों के कारण Bot ZIP के रूप में केवल 50 पेज भेजता है..__😅",
    "total" : "`कुल पृष्ठ: {}..⏳`", "upload" : "'अपलोडिंग: {}/{} पृष्ठ..` 🐬",
    "current" : "'रूपांतरित: {}/{} पृष्ठ.. 🤞`", "complete" : "'अपलोडिंग पूर्ण.. `🏌️",
    "canceledAT" : "`रद्द किया गया {}/{} पेजों पर..` 🙄", "cbAns" : "⚙️ Okeyda, Canceling..",
    "cancelCB" : {"💤 CANCEL 💤" : "close|P2I"}, # संपादन योग्य:
    "canceledCB" : {"🍄 CANCELED 🍄" : "close|P2IDONE"},
    "completed" : {"😎 COMPLETED 😎" : "close|P2ICOMP"}
}

merge = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "upload" : PROGRESS['upFile'],
    "load" : "__Overload के कारण आप एक बार में केवल 5 pdfs मर्ज कर सकते हैं__",
    "sizeLoad" : "`केवल ओवरलोड बॉट के कारण %sMb pdfs को सपोर्ट करता है..", # रिमूवल %s शो एरर
    "pyromodASK" : """__MERGE pdfs » कतार में कुल pdfs: {}__

/exit __रद्द करने के लिए__
/merge __ को मर्ज करने__""",
    "exit": "`प्रक्रिया रद्द..` 😏", "total": "`कुल पीडीएफ़: {} 💡",
    "current" : "__Pdf डाउनलोड करना प्रारंभ किया: {} 📥__", "cancel" : "`मर्ज प्रक्रिया रद्द .. `",
    "started" : "__Merging Started.. __ ", "caption" : "`मर्ज किए गए pdf 🙂`",
    "error": "`फ़ाइल एन्क्रिप्ट की गई हो सकती है..`\n\nकारण: {}"
}

metaData = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "download" : PROGRESS['dlFile'],   # [❌]
    "read" : "कृपया इस संदेश को फिर से पढ़ें.. 🥴"
}

preview = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'], "error" : document['error'],
    "download" : PROGRESS['dlFile'], "_" : "PDF में केवल {} पृष्ठ हैं 🤓\n\n",
    "__" : "पीडीएफ पेज: {}\n\n", "total" : "`कुल पेज: {}..` ",
    "album" : "`एक एल्बम तैयार कर रहा है..` 🤹", "upload" : f"`अपलोडिंग: पूर्वावलोकन पेज.. `"
}

stamp = {
    "stamp" : {
        "⚙️ PDF » STAMP ↓" : "nabilanavab",
        "नॉट फॉर पब्लिक रिलीज़ 🤧" : "pdf|stp|10",
        "सार्वजनिक रिलीज़ के लिए 🥱" : "pdf|stp|8",
        "गोपनीय 🤫" : "pdf|stp|2", "विभागीय 🤝" : "pdf|stp|3",
        "प्रायोगिक 🔬" : "pdf|stp|4", "समाप्त 🐀" : "pdf|stp|5",
        "अंतिम 🔧" : "pdf|stp|6", "टिप्पणी के लिए ️🗯️" : "pdf|stp|7",
        "अस्वीकृत 😒" : "pdf|stp|9", "स्वीकृत 😷" : "pdf|stp|0",
        "बिक ✊" : "pdf|stp|11", "टॉप सीक्रेट " : "pdf|stp|12",
        "ड्राफ़्ट 👀" : "pdf|stp|13", "AsIs 🤏" : "pdf|stp|1",
        "« वापस «": "pdf"
    },
    "स्टाम्पए" : {
        "⚙️ पीडीएफ » टिकट » रंग ↓" : "nabilanavab",
        "रेड ❤️" : "spP|{}|r", "ब्लू 💙" : "spP|{}|b",
        "ग्रीन 💚" : "spP|{}|g", "येलो 💛" : "spP|{}|c1",
        "पिंक 💜" : "spP|{}|c2", "ह्यू 💚" : "spP|{}|c3",
        "व्हाइट 🤍" : "spP|{}|c4", "ब्लैक 🖤" : "spP|{}|c5",
        "« वापस «": "pdf|stp"
    },
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "upload" : PROGRESS['upFile'],
    "stamping" : "`शुरूआत स्टांपिंग..` 💠", "caption" : """मुद्रित पीडीएफ़\nरंग : `{}`\nannot : `{}`"""
}

work = {
    "inWork" : PROGRESS['workInP'], "process" : document['process'],
    "download" : PROGRESS['dlFile'], "takeTime" : PROGRESS['takeTime'],
    "upload" : PROGRESS['upFile'], "button" : document['cancelCB'],
    "rot360" : "आपको कुछ बड़ी समस्या है..🙂", "ocrError" : "मालिक प्रतिबंधित ",
    "largeNo" : "5 पेज से कम की पीडीएफ फाइल भेजें.. ",
    "pyromodASK_1" : """__PDF {} »\nअब, कृपया पासवर्ड दर्ज करें :__\n\n/exit __रद्द करने के लिए __""",
    "pyromodASK_2" : """__पीडीएफ का नाम बदलें »\nअब, कृपया नया नाम दर्ज करें:__\n\n/exit __रद्द करने के लिए __""",
    "exit" : "`प्रक्रिया रद्द .. `😏", "ren_caption" : "__नया नाम:__ `{}`",
    "notENCRYPTED" : "`फाइल एनक्रिप्टेड नहीं है..` ",
    "compress" : "⚙️ `संपीड़ित करना शुरू किया.. ️\nइसमें कुछ समय लग सकता है..`💛",
    "decrypt" : "⚙️ `डिक्रिप्ट करना शुरू किया.. \nइसमें कुछ समय लग सकता है..`💛",
    "encrypt" : "⚙️ `एन्क्रिप्ट करना शुरू किया.. 🔐\nइसमें कुछ समय लग सकता है..`💛",
    "ocr" : "⚙️ `OCR Layer जोड़ना.. ️\nइसमें कुछ समय लग सकता है..`💛",
    "format" : "⚙️ `फ़ॉर्मैट करना शुरू किया.. \nइसमें कुछ समय लग सकता है..`💛",
    "rename" : "⚙️ `पीडीएफ का नाम बदलना.. ️\nइसमें कुछ समय लग सकता है..`💛",
    "rot" : "⚙️ `पीडीएफ को घुमा रहा है.. \nइसमें कुछ समय लग सकता है..`💛",
    "pdfTxt" : "⚙️ `पाठ्य निकालना.. \nइसमें कुछ समय लग सकता है..`💛",
    "fileNm" : "पुराना फ़ाइल नाम: {}\nनया फ़ाइल नाम: {}",
    "rotate" : {
        "⚙️ PDF » ROTTE ↓" : "nabilanavab", "90°" : "work|rot90", "180°" : "work|rot180",
        "270°" : "work|rot270", "360°" : "work|rot360", "« Back «" : "pdf"
    },
    "txt" : {
        "⚙️ PDF » TXT " : "nabilanavab", "📜 MESSAGE 📜" : "work|M", "   TXT FIL " : "work|T",
        "🌐 HTML " : "work|H", "🎀 JSON " : "work|J", "« Back «": "pdf"
    }
}

PROCESS = {
    "ocr" : "OCR जोड़ा गया", "decryptError" : "__ फ़ाइल को __ `{}` ️ के साथ डिक्रिप्ट नहीं कर सकता",
    "decrypted" : "__डिक्रिप्टेड फाइल__", "एन्क्रिप्टेड" : "__पेज नंबर__: {}\n__key__ : ||{}|| 🔐",
    "compressed" : """`मूल आकार: {}\nसंकुचित आकार: {}\n\nअनुपात: {:.2f}%`""",
    "cantCompress" : "फाइल को ज्यादा कंप्रेस नहीं किया जा सकता..🤐",
    "pgNoError" : """__किसी कारण से A4 फ़ॉर्मेटिंग 5 से कम पृष्ठों वाले पीडीएफ़ के लिए समर्थन करता है__\n\nकुल पृष्ठ: {} ⭐""",
    "ocrError" : "`पहले से ही एक टेक्स्ट लेयर है.. `😏",
    "90" : "__Rotated 90°__", "180" : "__Rotated 180°__", "270" : "__Rotated 270°__",
    "formatted" : "A4 Formatted File", "M" : "♻ Extracted {} Pages ",
    "H": "एचटीएमएल फाइल", "T": "TXT फाइल", "J": "JSON फाइल"
}

pdf2TXT = {
    "upload" : PROGRESS["upFile"], "exit" : split['exit'], "nothing" : "Nothing to create.. ",
    "TEXT" : "`पाठ्य संदेशों से पीडीएफ बनाएं »`", "start" : "txt को पीडीएफ में बदलना शुरू किया..🎉",
    "font_btn" : {
        "TXT@PDF » SET FONT" : "nabilanavab", "Times" : "pdf|font|t", "Courier" : "pdf|font|c", "Helvetica (Default)" : "pdf|font|h ",
        "Symbol" : "pdf|font|s", "Zapfdingbats" : "pdf|font|z", "🚫 CLOSE 🚫" : "close|me"
    },
    "size_btn" : { "TXT@PDF » {} » SET SCALE" : "nabilanavab", "Portarate" : "t2p|{}|p", "Landscape" : "t2p|{}|l", "« Back «": "pdf|T2P"},
    "askT" : "__TEXT TO PDF » अब, कृपया एक शीर्षक दर्ज करें:__\n\n/निकास __रद्द करने के लिए__\n/__छोड़ने के लिए __छोड़ें__",
    "askC" : "__TEXT TO PDF » अब, कृपया पैराग्राफ दर्ज करें {}:__\n\n/बाहर निकलें __रद्द करने के लिए__\n/__बनाने के लिए__"
}

URL = {
    "get": {"🧭 PDF फ़ाइल प्राप्त करें 🧭" : "getFile"}, "close": HELP_CMD ['CB'], "notPDF": "`एक PDF फ़ाइल नहीं",
    "error" : "🐉 कुछ गलत हुआ 🐉\n\nत्रुटि: `{}`\n\nNB: समूहों में, बॉट केवल समूह में शामिल होने के बाद भेजे गए दस्तावेज़ प्राप्त कर सकते हैं =)",
    "done" : "```लगभग हो गया.. ✅\nअब, अपलोड करना शुरू किया.. ```", "_error_" : "मुझे कोई यूआरएल या डायरेक्ट टेलीग्राम पीडीएफ लिंक भेजें",
    "openCB": {"ब्राउज़र में खोलें": "{}"}, "_error": "`कुछ बात गलत हो गई = (`\n\n`{}`",
    "_get" : "[ओपन चैट]({})\n\n**चैट के बारे में ↓**\nचैट प्रकार : {}\nचैट नाम : {}\nचैट यूएसआर : @{}\n"
             "चैट आईडी: {}\nतिथि: {}\n\n**मीडिया के बारे में ↓**\nमीडिया: {}\nफ़ाइल का नाम: {}\nफ़ाइल का आकार: {}\n\nफ़ाइल प्रकार: {}"
}

getFILE = {
    "inWork" : PROGRESS['workInP'], "big" : "{}mb से कम का pdf url भेजें", "wait" : "रुको.. मुझे.. ",
    "dl" : {"📥 ..DOWNLOADING.. " : "nabilanavab"}, "up" : {"📤 ..UPLOADING.. " : "nabilanavab"},
    "complete": {"😎 पूर्ण  😎" : f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "यह फीचर अंडर डेवलपमेंट ⛷️", "एरर एनेन परांजिल .. फिर क्या.. ",
    "प्रक्रिया रद्द .. ", "फ़ाइल एन्क्रिप्ट नहीं की गई .. ", "इसके बारे में कुछ भी आधिकारिक नहीं .. ", "🎉 पूर्ण .. "
]

inline_query = {
    "TOP": {"अब, भाषा चुनें ➟": "nabilanavab"}, "capt": "भाषा सेट करें ️⚙️", "des": "द्वारा: @ta_ja199 ❤"
}

# ===================================================================================================================================[NABIL A NAVAB -> TG: nabilanavab]
