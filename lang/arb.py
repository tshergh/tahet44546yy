# LANG: ARABIC LANG_CODE: ARB                                      >>  copyright ©️ 2021 nabilanavab  <<                                           fileName : lang/ARB.py
#                                        Thank: nabilanavab                                                   E-mail: nabilanavab@gmail.com

from configs.config import settings

# رسالة ترحيب مساءاً (المنزل أ , ب , ج , د ...)
HOME = {
    "HomeA": """مرحبًا [{}](tg://user?id={}) .. !!
سيساعدك هذا الروبوت على القيام بالعديد من الأشياء باستخدام ملفات pdf 🥳

بعض الميزات الرئيسية هي: \n◍ تحويل الصور إلى PDF
◍ `تحويل PDF إلى صور` \n◍` تحويل الملفات إلى pdf` """,
    "HomeACB": {
        "⚙️ الإعدادات ⚙️": "Home|B" , "⚠️ مساعدة ⚠️": "Home|C",
        "📢 القناة 📢": f"{str(settings.OWNED_CHANNEL)}",
        "🌟 بوت المحول 🌟": f"{str(settings.SOURCE_CODE)}",
        "🚶 اغلق 🚶": "close|mee"
    } ,
    "HomeAdminCB": {
        "⚙️ الإعدادات ⚙️": "Home|B" , "⚠️ مساعدة ⚠️": "Home|C",
        "📢 القناة 📢": f"{str(settings.OWNED_CHANNEL)}",
        "🌟 بوت المحول 🌟": f"{str(settings.SOURCE_CODE)}",
        "🗽 الحالة 🗽": "status|home", "🚶 اغلق 🚶": "close|mee"
    } ,
    "HomeB": """صفحة الإعدادات ⚙️ \n \n اسم المستخدم: {}
معرّف المستخدم: {} \n اسم المستخدم: {} \n تاريخ التسجيل: {} \n
اللغة: {} \n API: {}
الإبهام: {} \n التسمية التوضيحية: {} \n اسم الملف: {} """,
    "HomeBCB": {
        "🌍 اللغة 🌍": "set|lang", "📍 THUMB 📍": "set|thumb",
        "📈 الإسم 📈": "set|fname", "💩 API 💩": "set|api",
        "📅 تعليق 📅": "set|capt", "«العودة إلى الصفحة الرئيسية« ": "Home|B2A"
    } ,
    "HomeC": """🪂 ** رسالة مساعدة **:

``` بعض الميزات الرئيسية هي:
 ◍ تحويل الصور إلى PDF \n ◍ Manupultions PDF \n ◍ العديد من برامج الترميز الشائعة إلى pdf
 
تعديل ملف pdf:
 ◍ PDF⥃ الصور [الكل , النطاق , الصفحات] \n ◍ المستندات إلى PDF [png , jpg , jpeg] \n ◍ الصور PDF \n ◍ بيانات PDF الوصفية \n ◍ PDF⥃TEXT \n ◍ TEXT⥃PDF \n ◍ ضغط ملف pdf
 ◍ انقسام PDF [النطاق , الصفحات] \n ◍ دمج PDF \n ◍ إضافة طابع \n ◍ إعادة تسمية PDF \n ◍ تدوير PDF \n ◍ ENCRYPT / DECRYPT PDF \n ◍ PDF FORMATTER \n ◍ PDF⥃JSON / TXT FILE
 ◍ PDF⥃HTML [عرض الويب] \n ◍ URL⥃PDF \n ◍ PDF⥃ZIP / TAR / RAR [الكل , النطاق , الصفحات] \n وأكثر من ذلك بكثير .. """ ,
    "HomeCCB": {"« الرئيسية «": "Home|A", "🛈 تعليمات 🛈": "Home|D"},
    "HomeD": """` نظرًا لأن هذه خدمة مجانية , لا يمكنني ضمان المدة التي يمكنني خلالها الحفاظ على هذه الخدمة ..`😝
 
⚠️ تعليمات ⚠️:
🛈 __يرجى عدم محاولة إساءة استخدام إدارة Bot__ 😒
🛈 __لا ترسل بريدًا عشوائيًا هنا , فقد يؤدي ذلك إلى حظر دائم 🎲__.
🛈 __محتويات الاباحيه ايضا ستمنحك حظر دائم 💯__

** أرسل أي صورة لتبدأ: ** 😁 """,
    "HomeDCB": {"⚠️ مساعدة ⚠️": "Home|C", "» الرئيسية »": "Home|A"}
}

SETTINGS = {
    "default": [" إفتراضي ❌", "✅"], "chgLang": {"SETTING ⚙️» تغيير اللغة 🌐 ":" nabilanavab "},
    "error": "حدث خطأ ما أثناء استرداد البيانات من قاعدة البيانات" , "lang": "الآن , حدد أي لغة .." ,
    "ask": ["الآن , أرسل لي .." , "الآن , أرسل لي .. 😅 \n \n سريع.! ليس لدي المزيد من الوقت لاستعراض النص .. 😏 \n\n/cancel :  للإلغاء"] ,
    "askApi": "\n \n افتح الرابط أدناه وأرسل لي الرمز السري:", "waitApi": {"فتح الرابط ✅": "https://www.convertapi.com/a/signin"},
    "wait": {"أنتظر..🥱 ": "nabilanavab"}, "back": {"« الرئيسية «": "Home|B2S"}, "errorCB": {"«العودة إلى الصفحة الرئيسية« ": "Home|B2A"} ,
    "result": ["لا يمكن تحديث الإعدادات ❌" , "تم تحديث الإعدادات بنجاح ✅"] , "cant": "لا يمكن استخدام هذه الميزة ❌" ,
    "feedback": "تقييمات من عملاء رائعين مثلك تساعد الآخرين. \n @ta_ja199"
                 "\n \n الإبلاغ عن خطأ في {} اللغة: \n` • تحديد اللغة \n • رسالة الخطأ \n • رسالة جديدة`",
    "feedbtn": {"Report Lang Error": settings.REPORT},
    "thumb" : [
        {"ضبط ⚙️» THUMBNAIL 📷 ":"nabilanavab"," ♻ أضف ♻ ":"set|thumb+"," «الرئيسية« ":"Home|B"},
        {"ضبط ⚙️» THUMBNAIL 📷 ":"nabilanavab"," ♻ تغيير ♻ ":"set|thumb+"," حذف 🗑 ":"set|thumb-"," ««العودة إلى الصفحة الرئيسية« ":"Home|B2S"}
    ],
    "fname": [
        {"ضبط ⚙️» FNAME 📷 ":"nabilanavab"," ♻ أضف ♻ ":"set|fname+"," «الرئيسية« ":"Home|B2S"},
        {"ضبط ⚙️» FNAME 📷 ":"nabilanavab"," ♻ تغيير ♻ ":"set|fname+"," حذف 🗑 ":"set|fname-"," «العودة إلى الصفحة الرئيسية« ":"Home|B2S"}
    ] ,
    "api": [
        {"ضبط ⚙️» API 📷 ​​":"nabilanavab"," ♻ أضف ♻ ":"set|api+"," «الرئيسية« ":"Home|B2S"},
        {"ضبط ⚙️» API 📷 ​​":"nabilanavab"," ♻ تغيير ♻ ":"set|api+"," 🗑 حذف 🗑 ":"set|api-"," «العودة إلى الصفحة الرئيسية« ":"Home|B2S"}
    ] ,
    "capt": [
        {"الإعداد ⚙️» التسمية التوضيحية 📷":"nabilanavab"," ♻ أضف ♻ ":"set|capt+"," «العودة إلى الصفحة الرئيسية« ":"Home|B2S"},
        {"الإعداد ⚙️» التسمية التوضيحية 📷":"nabilanavab"," ♻ تغيير ♻ ":"set|capt+"," حذف 🗑 ":"set|capt-","«العودة إلى الصفحة الرئيسية« ":"Home|B2S"}
    ]
}

BOT_COMMAND = {"start": "رسالة ترحيب ..", "txt2pdf": "إنشاء ملف PDF نصي"}

HELP_CMD = {
    "userHELP": """[رسائل أوامر المستخدم]: \n
/ البدء: للتحقق مما إذا كان Bot على قيد الحياة \n / إلغاء: إلغاء العمل الحالي
/ delete: مسح الصورة لقائمة انتظار pdf \n / txt2pdf: نص إلى pdf "" ",
    "تعليمات المسؤول": "" "\n \n \n [رسائل أوامر المسؤول]: \n
/ send: للبث , رسالة pm "" ",
    "footerHelp": f "" "\n \n \n رمز المصدر: [I2PDF] ({str (settings.SOURCE_CODE)})
البوت:@I2PDF 💎 \n [قناة الدعم] ({settings.OWNED_CHANNEL}) """,
    "CB": {"⚠️ اغلاق ⚠️": "close|all"}
}

STATUS_MSG = {
    "HOME": "الآن , حدد أي خيار أدناه للحصول على الحالة الحالية 💱 ..` ",
    "_HOME" : {
        "📊 ↓ SERVER ↓ 📊": "nabilanavab", "📶 STORAGE 📶": "status|server",
        "🥥 قاعدة البيانات 🥥": "status|db" , "🌝 ↓ الحصول على قائمة ↓ 🌝": "nabilanavab",
        "💎 المشرف 💎": "status|admin", "👤 المستخدمون 👤": "status|users",
        "« رجوع  «": "Home|A"
    } ,
    "DB": """📂 قاعدة البيانات: \n \n ** ◍ مستخدمو قاعدة البيانات: **` {} `📍 \n ** ◍ محادثات قاعدة البيانات: **` {} `📍""" ,
    "SERVER": """** ◍ المساحة الإجمالية: **` {} `
** ◍ المساحة المستخدمة: ** `{} ({}٪)` \n ** ◍ مساحة حرة: ** `{}`
** ◍ استخدام وحدة المعالجة المركزية: ** "{}`٪ \n ** ◍ استخدام ذاكرة الوصول العشوائي: ** `{}`٪
** ◍ العمل الحالي: ** `{}` \n ** ◍ معرف الرسالة: ** `{}""" ,
    "BACK": {"« عودة«": "status|home"}, "ADMIN": "** Total ADMIN: ** __ {} __ \n",
    "USERS": "المستخدمون: \n\n" , "NO_DB": "لم يتم تعيين قاعدة البيانات بعد 💩"
}

feedbackMsg = f"[اكتب تعليقًا 📋]({settings.FEEDBACK})"

# رسالة ترحيب المجموعة
HomeG = {
    "HomeA": """مرحبًا.! 🖐️ \n أنا جديد هنا {message.chat.title} \n
اسمحوا لي أن أقدم نفسي .. \n اسمي هو I2PDF , ويمكنني مساعدتك في القيام بالكثير
أشياء مع ملفات @ Telegram PDF \n \n شكرًا طاهر على هذا الروبوت الرائع 😅 """,
    "HomeACB": {
        "🤠 مالك البوت 🤠": f"https://telegram.dog/{settings.OWNER_USERNAME}",
        "🛡️ قناة البوت 🛡️": f"{settings.OWNED_CHANNEL}", "🌟 قناة البوت 🌟": f"{settings.SOURCE_CODE}"
    }
}

# واجهة مستخدم محظورة
BAN = {
    "cbNotU": "الرسالة ليست لك .. 😏",
    "banCB": {
        "إنشاء الروبوت الخاص بك": f"{settings.SOURCE_CODE}" , "البرنامج التعليمي": f"{settings.SOURCE_CODE}" ,
        "تحديث القناة": "https://t.me/i2pdfbotchannel"
    } ,
    "UCantUse": """مرحبًا {} \n \n لبعض الأسباب التي تجعلك لا تستطيع استخدام هذا BOT :(""",
    "UCantUseDB": """مرحبًا {} \n \n لبعض الأسباب التي تجعلك لا تستطيع استخدام هذا الروبوت: (\n \n السبب: {}""",
    "GroupCantUse": """{} لا تتوقع أبدًا استجابة جيدة مني \n
منعني المسؤولون من العمل هنا .. 🤭 """,
    "GroupCantUseDB": """{} لا تتوقع أبدًا استجابة جيدة مني \n
منعني المسؤولون من العمل هنا .. 🤭 \n \n السبب: {} """,
    "Force": """انتظر [{}](tg://user?id={}) .. !! \n
🚸| عذرا عزيزي | sorry dear
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه:
🔰|  You have to subscribe to the bot channel to be able to use it:
👇👇👇👇
 @i2pdfbotchannel""" ,
    "ForceCB": {"🌟 انظم في قناة 🌟": "{}", "♻️ تحديث ♻️": "Refresh"},
    "Fool": "لا يمكنك أن تخدعني. 🤭"
}

checkPdf = {
    "pg": "عدد الصفحات: • {} •` 🌟 ",
    "pdf": """` ماذا أفعل بهذا الملف .؟`\n\n اسم الملف: `{}` \n حجم الملف: `{}` """,
    "pdfCB": {
        "⭐ معلومات ⭐": "metaData", "عرض 🗳️": "preview",
        "🖼️ الصور 🖼️": "pdf|img", "✏️ نص ✏️": "pdf|txt",
        "🔐 تشفير 🔐": "work|encrypt", "🔒 فك تشفير 🔓": "work|decrypt",
        "🗜️ صغط 🗜️": "work|compress", "🤸 تدوير 🤸": "pdf|rotate",
        "✂️ تقسيم ✂️": "pdf|split", "🧬 دمج 🧬": "merge", "™ ️ ختم ™ ️": "pdf|stp",
        "✏️ إعادة تسمية ✏️": "work|rename", "📝 OCR 📝": "work|ocr",
         "🥷 تنسيق A4": "work|format", "🚫 اغلق 🚫": "close|all"
    } ,
    "error": """__ لا أفعل أي شيء بهذا الملف__ 😏 \n \n🐉` خطأ CODEC` 🐉 """,
    "errorCB": {"❌ ERROR IN CODEC ❌": "error", "🔸 اغلق 🔸": "close|all"},
    "encrypt": """` ملفك مشفر` 🔐 \n \n اسم الملف: `{}` \n حجم الملف: `{}` """,
    "encryptCB": {"🔓 فك تشفير 🔓": "work|decrypt"}
}

PROGRESS = {
    "progress": """** \n تم ✅: ** {0} / {1} \n ** السرعة 🚀: ** {2} / ثانية \n ** الوقت المقدر ⏳: ** {3}""" ,
    "dlImage": " جارٍ تنزيل صورتك ..⏳` ","upFile":" `بدء التحميل ...`📤",
    "dlFile": "` جارٍ تنزيل ملفك ..` 📥 ","upFileCB": {" 📤 .. UPLOADING|تحميل .. 📤 ":" nabilanavab "},
    "workInP": "العمل قيد التقدم .. 🙇", "refresh": {"♻️ تحديث ♻️": "{}"},
    "takeTime": """`العمل جاري ...` \n` قد يستغرق بعض الوقت ...`""",
    "cbPRO_D": ["📤 DOWNLOAD(تنزيل): {: .2f}٪ 📤", "🎯 CANCEL(الالغاء) 🎯"], "cbPRO_U": ["📤 UPLOADED(تحميل): {: .2f}٪ 📤", "🎯 CANCEL(الالغاء) 🎯"]
}

GENERATE = {
    "deleteQueue": "تم حذف قائمة الانتظار بنجاح ..`🤧", "noQueue": "لم يتم تأسيس قائمة انتظار ..`😲",
    "noImages": "لم يتم إنشاء صورة. !! 😒", "getFileNm": "الآن أرسل لي اسم ملف 😒:",
    "geting": "اسم الملف:` {} `\n الصفحات:` {} `", "getingCB": {"📚 GENERATING PDF ..": "nabilanavab"},
    "currDL ":" الصور {} التي تم تنزيلها 🥱 "
}

document = {
    "refresh": PROGRESS['refresh'] , "inWork": PROGRESS['workInP'] , "reply": checkPdf['pdf'] ,
    "replyCB": checkPdf['pdfCB'], "download": PROGRESS['dlFile'], "process": "⚙️ يعالج..",
    "takeTime": PROGRESS['takeTime'], "upFile": PROGRESS['upFile'], "dlImage": PROGRESS['dlImage'],
    "big": """بسبب الحمل الزائد , حدود المالك {} ميغابايت لملفات pdf 🙇
\n` ارجوك ارسل لي ملف اقل من {} ميغا بايت الحجم` 🙃 """,
    "bigCB": {"💎قناة البوت 💎": "https://t.me/i2pdfbotchannel"},
    "imageAdded": """تمت إضافة {} صفحة / صفحة إلى ملف pdf الخاص بك ..`🤓 \n \n اسم الملف:` {} .pdf` """,
    "setHdImg": """الآن صورة إلى PDF في وضع HD""",
    "setDefault": {"« رجوع إلى الجودة الافتراضية «": "close|hd"},
    "error": """حدث خطأ ما .. 🐉 \n\n الخطأ:` {} """,
    "noAPI": "` الرجاء إضافة تحويل API .. 💩 \n\n ابدأ »الإعدادات» api »add / change`",
    "useDOCKER": " الملف غير مدعوم , انشر الروبوت باستخدام docker` ",
    "fromFile": "` تم التحويل: {} إلى {} `", "unsupport": "` ملف غير مدعوم..🙄` ",
    "generateRN": {"إنشاء 📚": "إنشاء" , "إعادة تسمية ✍️": "إنشاء REN"} ,
    "generate": {"إنشاء 📚": "إنشاء"} , "cancelCB": {"⟨اغلق⟩": "close|me"}
}

noHelp = "`لن يساعدك أحد` 😏 "

split = {
    "inWork": PROGRESS['workInP'], "cancelCB": document['cancelCB'] ,
    "download": PROGRESS['dlFile'], "exit": "` Process Canceled..` 😏 ",
    "button" : {
        "⚙️ PDF» SPLIT ↓ ":" nabilanavab "," مع في النطاق 🦞 ":"split|R",
        "صفحة واحدة 🐛": "split|S", "« عودة «": "pdf"
    } ,
    "work": ["النطاق" , "واحد"] , "أكثر من": " 5 محاولة .. تم إلغاء العملية ..`😏 ",
    "pyromodASK_1": """ __Pdf انقسام »حسب النطاق \n الآن , أدخل النطاق (البداية: النهاية): __
\n /exit __لإلغاء__ """,
    "completed": "اكتمل التنزيل ..` ✅",
    "error_1": "خطأ في بناء الجملة: justNeedStartAndEnd` ",
    "error_2": "خطأ في بناء الجملة: errorInEndingPageNumber` ",
    "error_3": "خطأ في بناء الجملة: errorInStartingPageNumber` ",
    "error_4": "خطأ في بناء الجملة: pageNumberMustBeADigit` 🧠",
    "error_5": "خطأ في بناء الجملة: noEndingPageNumber Or notADigit` 🚶",
    "error_6": " تعذر العثور على أي رقم ..`😏 ",
    "error_7": "حدث خطأ ما ..`😅", "error_8": "أدخل أرقامًا أقل من {} ..` 😏 ",
    "error_9": " التحقق الأول من عدد الصفحات` 😏 ","upload":" ⚙️ `بدء التحميل ...` 📤"
}

pdf2IMG = {
    "inWork": PROGRESS['workInP'], "process": document['process'],
    "download": PROGRESS['dlFile'], "uploadfile": split["upload"],
    "toImage": {
        "⚙️ PDF» صور ↓ ":"nabilanavab"," 🖼 صورة 🖼 ":"pdf|img|img",
        "📂 ملف 📂": "pdf|img|doc", "🤐 ZIP 🤐": "pdf|img|zip" ,
        "🎯 TAR 🎯": "pdf|img|tar", "« عودة «": "pdf"
    } ,
    "imgRange": {
        "⚙️ PDF» صور »{} ↓": "nabilanavab", "🙄 ALL 🙄": "p2img|{}A",
        "🤧 نطاق 🤧": "p2img|{}R", "🌝 صفحات 🌝": "p2img|{}S", "« عودة«": "pdf|img"
    } ,
    "over": " 5 محاولات .. تم إلغاء العملية ..`😏 ",
    "pyromodASK_1": """ __Pdf - Img ›Doc» الصفحات: \n الآن , أدخل النطاق (البداية: النهاية): __
\n / خروج __لإلغاء__ """,
    "pyromodASK_2": """ __Pdf - Img ›Doc» الصفحات: \n الآن , أدخل أرقام الصفحات مفصولة بـ__ (,):
\n / خروج __لإلغاء__ """,
    "exit": "إلغاء العملية ..` 😏",
    "error_1": "خطأ في بناء الجملة: justNeedStartAndEnd` ",
    "error_2": "خطأ في بناء الجملة: errorInEndingPageNumber` ",
    "error_3": "خطأ في بناء الجملة: errorInStartingPageNumber` ",
    "error_4": "خطأ في بناء الجملة: pageNumberMustBeADigit` 🧠",
    "error_5": "خطأ في بناء الجملة: noEndingPageNumber Or notADigit` 🚶",
    "error_6": " تعذر العثور على أي رقم ..`😏 "," error_7 ":" `حدث خطأ ما ..`😅",
    "error_8": "يحتوي` PDF فقط على {} صفحات` 💩 "," error_9 ":" التحقق الأول من عدد الصفحات` 😏 ",
    "error_10": "__بسبب بعض القيود يرسل البوت 50 صفحة فقط على هيئة ZIP ..__ 😅",
    "total": "` إجمالي الصفحات: {} .. ⏳` ","upload":" `تحميل: {} / {} صفحات .. 🐬`",
    "Current": "` تم تحويلها: {} / {} صفحات .. 🤞` ","complete":" اكتمل التحميل .. `🏌️",
    "cancelledAT": "` تم الإلغاء عند {} / {} من الصفحات..` 🙄 ","cbAns":" ⚙️ Okeyda, Canceling .. ",
    "CancelCB": {"💤 الالغاء 💤": "close|P2I"}, # EDITABLE: ❌
    "canceledCB": {"🍄 ألغيت 🍄": "close|P2IDONE"},
    "completed": {"😎 منجز 😎": "close|P2ICOMP"}
}

merge = {
    "inWork": PROGRESS['workInP'] , "process": document['process'] , "upload": PROGRESS['upFile'] ,
    "load": "__بسبب التحميل الزائد , يمكنك فقط دمج 5 ملفات PDF في وقت واحد__" ,
    "sizeLoad": "بسبب التحميل الزائد للبوت فقط دعم٪ sMb pdfs .." , # إزالة٪ s عرض خطأ
    "pyromodASK": """__MERGE pdfs» إجمالي ملفات PDF في قائمة الانتظار: {} __

/exit __لإلغاء__
/merge __لدمج__ """,
    "exit": "إلغاء العملية..` 😏", "total": "إجمالي ملفات PDF: {} 💡",
    "current": "__بدأ تنزيل ملف PDF: {} 📥__", "cancel": "إلغاء عملية الدمج .. 😏`",
    "started": "__ بدأ الدمج .. __ 🪄", "caption": "` pdf مدمج 🙂` ",
    "error": "قد يكون ملف مشفر ...` \n \n السبب: {}"
}

metaData = {
    "inWork": PROGRESS ['workInP'], "process": document['process'], "download": PROGRESS['dlFile'], # [❌]
    "read": "الرجاء قراءة هذه الرسالة مرة أخرى .. 🥴"
}

المعاينة = {
    "inWork": PROGRESS ['workInP'] , "process": document['process'] , "error": document['error'] ,
    "download": PROGRESS ['dlFile'], "_": "يحتوي ملف PDF على {} صفحات فقط 🤓 \n \n",
    "__": "صفحات PDF: {} \n \n", "total": "إجمالي الصفحات: {} ..` 🤌 ",
    "album": "تحضير ألبوم ..` 🤹", "upload": f"` تحميل: معاينة الصفحات .. 🐬` "
}

stamp = {
    "stamp": {
        "⚙️ PDF» STAMP ↓ ":"nabilanavab",
        "ليس للنشر العام 🤧": "pdf|stp|10",
        "للإصدار العام 🥱": "pdf|stp|8",
        "سري 🤫": "pdf|stp|2", "Departmental 🤝": "pdf|stp|3",
        "التجريبية 🔬": "pdf|stp|4", "انتهاء الصلاحية 🐀": "pdf|stp|5",
        "نهائي 🔧": "pdf|stp|6", "للتعليق 🗯️": "pdf|stp|7",
        "غير معتمد 😒": "pdf|stp|9", "موافق عليه 🥳": "pdf|stp|0",
        "تم البيع ✊": "pdf|stp|11", "سري للغاية 😷": "pdf|stp|12",
        "مسودة 👀": "pdf|stp|13", "AsIs 🤏": "pdf|stp|1",
        "« رجوع «": "pdf"
    } ,
    "stampA": {
        "⚙️ PDF» STAMP »COLOR ↓": "nabilanavab" ,
        "أحمر ❤️": "spP|{}|r", "أزرق 💙": "spP|{}|b" ,
        "أخضر 💚": "spP|{}|g", "Yellow 💛": "spP|{}|c1",
        "الوردي 💜": "spP|{}|c2" , "Hue 💚": "spP|{}|c3" ,
        "أبيض 🤍": "spP|{}|c4", "أسود 🖤": "spP|{}|c5" ,
        "« رجوع «": "pdf|stp"
    } ,
    "inWork": PROGRESS['workInP'], "process": document['process'],
    "download": PROGRESS['dlFile'] , "upload": PROGRESS['upFile'] ,
    "stamping": "بدء ختم..` 💠", "caption": """pdf مختوم \n اللون:` {} `\n لا:` {} `"""
}

work = {
    "inWork": PROGRESS['workInP'], "process": document['process'],
    "download": PROGRESS['dlFile'], "takeTime": PROGRESS ['takeTime'],
    "upload": PROGRESS['upFile'], "button": document['cancelCB'] ,
    "rot360": "لديك مشكلة كبيرة ..🙂" , "ocrError": "مالك مقيد 😎🤏" ,
    "largeNo": "أرسل ملف pdf أقل من 5 صفحات .. 🙄",
    "pyromodASK_1": """ __PDF {} »\n الآن , الرجاء إدخال كلمة المرور: __ \n \n / exit __ لإلغاء__""",
    "pyromodASK_2": """ __إعادة تسمية PDF »\n الآن , الرجاء إدخال الاسم الجديد: __ \n \n / خروج __ لإلغاء__""" ,
    "exit": "إلغاء العملية .. 😏 ","ren_caption":" __الاسم الجديد: __ `{}` ",
    "notENCRYPTED": "` الملف غير مشفر ..` 👀 ",
    "compress": "` بدأ الضغط .. 🌡️ \n قد يستغرق بعض الوقت ..`💛 ",
    "decrypt": "⚙️` بدأ فك التشفير .. 🔓 \n قد يستغرق بعض الوقت ..`💛 ",
    "encrypt": "⚙️` بدأ التشفير .. 🔐 \n قد يستغرق بعض الوقت ..`💛 ",
    "ocr": "⚙️` أضافة طبقةOCR .. ✍️ \n قد يستغرق بعض الوقت ..`💛 ",
    "format": "⚙️` بدء التنسيق .. 🤘 \n قد يستغرق بعض الوقت ..`💛 ",
    "rename": "⚙️` إعادة تسمية PDf .. ✏️ \n قد يستغرق بعض الوقت ..`💛 ",
    "rot": "⚙️` تدوير PDf .. 🤸 \n قد يستغرق بعض الوقت ..`💛 ",
    "pdfTxt": "⚙️` استخراج النص .. 🐾 \n قد يستغرق بعض الوقت ..`💛 ",
    "fileNm": "اسم الملف القديم: {} \n اسم الملف الجديد: {}",
    "rotate" : {
        "⚙️ PDF» تدوير ↓ ":"nabilanavab"," 90 ° ":"work|rot90"," 180 ° ":"work|rot180",
        " 270 ° ": "work|rot270", "360 °": "work|rot360", "« عودة«": "pdf"
    } ,
    "txt" : {
        "⚙️ PDF» نص ↓ ":"nabilanavab"," 📜 رسالة 📜 ":"work|M"," 🧾 ملف نصي 🧾 ":"work|T",
        "🌐 HTML 🌐": "work|H", "🎀 JSON 🎀": "work|J", "« عودة«": "pdf"
    }
}

PROCESS = {
    "ocr": "OCR added", "decryptError": "__Cannot فك تشفير الملف بـ__` {} `🕸️",
    "decrypted": "__ملف مشفر__" , "encrypted": "__رقم الصفحة__: {} \n__ المفتاح__ 🔐: || {} ||",
    "compressed": """الحجم الأصلي: {} \n الحجم المضغوط: {} \n \n النسبة: {: .2f}٪""" ,
    "cantCompress": "لا يمكن ضغط الملف أكثر ..🤐",
    "pgNoError": "" "__لسبب ما يدعم تنسيق A4 لملفات pdf التي تحتوي على أقل من 5 صفحات __ \n \n إجمالي الصفحات: {} ⭐" "",
    "ocrError": "لديك طبقة نص بالفعل ..` 😏 ",
    "90": "__تدوير 90 درجة __" , "180": "__تدوير 180 درجة __" , "270": "__تدوير 270 درجة __" ,
    "formatted": "تنسيق A4" , "M": "♻ مستخرج {} الصفحات ♻" ,
    "H": "ملف HTML" , "T": "ملف TXT" , "J": "ملف JSON"
}

pdf2TXT = {
    "upload": PROGRESS["upFile"] , "exit": split['exit'] , "nothing": "لا شيء لإنشاء .. 😏" ,
    "TEXT": "` إنشاء ملف PDF من الرسائل النصية »` ","start":" بدأ تحويل النص إلى ملف PDF..🎉 ",
    "font_btn": {
        "TXT @ PDF» SET FONT":"nabilanavab"," Times ":"pdf|font|t"," Courier ":"pdf|font|c"," Helvetica (افتراضي) ":"pdf|font|h",
        "Symbol": "pdf|font|s", "Zapfdingbats": "pdf|font|z", "🚫 اغلق 🚫": "close|me"
    } ,
    "size_btn": {"TXT @ PDF» {} »SET SCALE": "nabilanavab", "Portarate": "t2p|{}|p", "Landscape": "t2p|{}|l", "« رجوع «": "pdf|T2P"},
    "askT": "__TEXT TO PDF» الآن , الرجاء إدخال العنوان: __ \n \n / خروج __ لإلغاء __ \n / تخطي __للتخطي__ ",
    "askC": "__TEXT TO PDF» الآن , الرجاء إدخال فقرة {}: __ \n \n / خروج __ لإلغاء __ \n / إنشاء __لإنشاء _ "
}

URL = {
    "get": {"🧭 احصل على ملف PDF 🧭": "getFile"}, "close": HELP_CMD ['CB'], "notPDF": "ليس ملف PDF" ,
    "error": "🐉 حدث خطأ ما \n \n الخطأ:` {} `\n \nNB: في المجموعات , لا يمكن للبرامج الآلية جلب المستندات إلا بعد الانضمام إلى المجموعة =)",
    "done": "` `انتهى تقريبًا .. ✅ \n الآن , بدأ التحميل .. 📤 `" , "_error_": "أرسل لي أي عنوان url أو روابط pdf مباشرة برقية" ,
    "openCB": {"افتح متصفح": "{}"}, "_error": "` هناك خطأ ما = (`\n \n` {}` ",
    "_get": "[فتح الدردشة] ({}) \n \n ** حول الدردشة ↓ ** \n نوع الدردشة: {} \n اسم الدردشة: {} \n الدردشة Usr: @ {} \n"
             "معرف الدردشة: {} \n التاريخ: {} \n \n ** حول الوسائط ↓ ** \n الوسائط: {} \n اسم الملف: {} \n حجم الملف: {} \n \n نوع الملف: {}"
}

getFILE = {
    "inWork": PROGRESS ['workInP'], "big": "أرسل pdf url أقل من {} ميغابايت", "انتظر": "انتظر .. دعني .. 😜",
    "dl": {"📥 .. تنزيل .. 📥": "nabilanavab"}, "up": {"📤 ..تحميل .. 📤": "nabilanavab"},
    "complete": {"😎 مكتمل 😎": f"{str(settings.SOURCE_CODE)}"}
}

cbAns = [
    "هذه الميزة قيد التطوير ⛷️" , "Error annenn paranjille .. ثم ماذا .. 😏" ,
    "تم إلغاء العملية .. 😏" , "الملف غير مشفر .. 👀" , "لا شيء رسمي بخصوصه .. 😅" , "🎉 مكتمل .. 🏃"
]

inline_query = {
    "TOP": {"الآن ، حدد اللغة ➟": "nabilanavab"}, "capt": "لغة مجموعة⚙️", "des": "By:@ta_ja199 ❤"
}

# ===================================================================================================================================[NABIL A NAVAB -> TG: nabilanavab]
