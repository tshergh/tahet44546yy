# fileName : lang/__init__.py
# copyright ©️ 2021 nabilanavab

from configs.config import settings

langList = {
        "arb" : ["🅰🆁🅰🅱🅸🅲", "عربي"],
        "eng" : ["🅴🅽🅶🅻🅸🆂🅷", "English"],
        "mal" : ["🅼🅰🅻🅰🆈🅰🅻🅰🅼", "മലയാളം"],
        "uzb" : ["🆄🆉🅱🅴🅺🅸🆂🆃🅰🅽", "O'zbekiston"],
        "hnd" : ["🅷🅸🅽🅳🅸", "हिन्दी"],
        "rus" : ["🆁🆄🆂🆂🅸🅰🅽", "русский"],
        "frn" : ["🅵🆁🅴🅽🅲🅷", "française"],
        "spn" : ["🆂🅿🅰🅽🅸🆂🅷", "española"]
    }

# Display Lang in a Beutiful Way
async def disLang(lang):
    if lang in langList:
        return langList[lang][0]
    else:
        return langList[settings.DEFAULT_LANG][0]

# ===================================================================================================================================[NABIL A NAVAB -> TG: nabilanavab]
