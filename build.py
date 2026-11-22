#!/usr/bin/env python3
"""Build the KeyboardsOnline GitHub Pages site - 25 keyboards, SEO + structured data.
Original site: https://keyboardsonline.net/
GitHub Pages base: https://onlinekeyboards.github.io/keyboardsonline
"""
import json, os, html
from pathlib import Path

ROOT = Path(__file__).parent
BASE = "https://onlinekeyboards.github.io/keyboardsonline"
ORIG = "https://keyboardsonline.net"
SITE_NAME = "KeyboardsOnline"

def esc(s): return html.escape(s, quote=True)

# rows: each key is "normal" or "normal|shift"
LANGS = [
 dict(slug="urdu-keyboard", name="Urdu", native="اردو", code="ur", dir="rtl", region="Asian",
  desc="Type Urdu online for free with this virtual Urdu keyboard. No installation needed — type, copy and paste Urdu text anywhere.",
  sample="السلام علیکم، یہ اردو کی بورڈ ہے۔",
  rows=[["1|!","2|@","3|#","4|$","5|%","6|^","7|&","8|*","9|(","0|)"],["ا","ب","پ","ت","ٹ","ث","ج","چ","ح","خ"],["د","ڈ","ذ","ر","ڑ","ز","ژ","س","ش","ص"],["ض","ط","ظ","ع","غ","ف","ق","ک","گ","ل"],["م","ن","و","ہ","ھ","ء","ی","ے","۔","،"]]),
 dict(slug="arabic-keyboard", name="Arabic", native="العربية", code="ar", dir="rtl", region="Middle Eastern",
  desc="Type Arabic online for free with this virtual Arabic keyboard. Type Arabic letters, copy your text and paste it anywhere.",
  sample="السلام عليكم، هذه لوحة مفاتيح عربية.",
  rows=[["1|!","2|@","3|#","4|$","5|%","6|^","7|&","8|*","9|(","0|)"],["ا","ب","ت","ث","ج","ح","خ","د","ذ","ر"],["ز","س","ش","ص","ض","ط","ظ","ع","غ","ف"],["ق","ك","ل","م","ن","ه","و","ي","ء","ة"],["ى","ً","ٌ","ٍ","َ","ُ","ِ","ّ","ْ","۔"]]),
 dict(slug="hindi-keyboard", name="Hindi", native="हिन्दी", code="hi", dir="ltr", region="Asian",
  desc="Type Hindi online for free with this virtual Hindi keyboard. Type in Devanagari, copy and paste Hindi text anywhere.",
  sample="नमस्ते, यह हिंदी कीबोर्ड है।",
  rows=[["अ","आ","इ","ई","उ","ऊ","ऋ","ए","ऐ","ओ"],["औ","क","ख","ग","घ","ङ","च","छ","ज","झ"],["ञ","ट","ठ","ड","ढ","ण","त","थ","द","ध"],["न","प","फ","ब","भ","म","य","र","ल","व"],["श","ष","स","ह","क्ष","त्र","ज्ञ","ा","ि","ी"],["ु","ू","ृ","े","ै","ो","ौ","ं","ः","।"]]),
 dict(slug="french-keyboard", name="French", native="Français", code="fr", dir="ltr", region="European",
  desc="Type French online for free with this virtual French keyboard. Type é, è, ê, à, ç and all French accents easily.",
  sample="Bonjour, ceci est un clavier français.",
  rows=[["1|&","2|é","3|\"","4|'","5|(","6|-","7|è","8|_","9|ç","0|à"],["a|A","z|Z","e|E","r|R","t|T","y|Y","u|U","i|I","o|O","p|P"],["q|Q","s|S","d|D","f|F","g|G","h|H","j|J","k|K","l|L","m|M"],["é|É","è|È","ê|Ê","ë|Ë","à|À","â|Â","î|Î","ô|Ô","ù|Ù","ç|Ç"]]),
 dict(slug="german-keyboard", name="German", native="Deutsch", code="de", dir="ltr", region="European",
  desc="Type German online for free with this virtual German keyboard. Type ä, ö, ü and ß with one click.",
  sample="Hallo, dies ist eine deutsche Tastatur.",
  rows=[["1|!","2|\"","3|§","4|$","5|%","6|&","7|/","8|(","9|)","0|="],["q|Q","w|W","e|E","r|R","t|T","z|Z","u|U","i|I","o|O","p|P"],["a|A","s|S","d|D","f|F","g|G","h|H","j|J","k|K","l|L","ö|Ö"],["y|Y","x|X","c|C","v|V","b|B","n|N","m|M","ä|Ä","ü|Ü","ß|ẞ"]]),
 dict(slug="spanish-keyboard", name="Spanish", native="Español", code="es", dir="ltr", region="European",
  desc="Type Spanish online for free with this virtual Spanish keyboard. Type ñ, á, é, í, ó, ú, ¿ and ¡ easily.",
  sample="Hola, este es un teclado en español.",
  rows=[["1|!","2|\"","3|·","4|$","5|%","6|&","7|/","8|(","9|)","0|="],["q|Q","w|W","e|E","r|R","t|T","y|Y","u|U","i|I","o|O","p|P"],["a|A","s|S","d|D","f|F","g|G","h|H","j|J","k|K","l|L","ñ|Ñ"],["z|Z","x|X","c|C","v|V","b|B","n|N","m|M","á|Á","é|É","í|Í"],["ó|Ó","ú|Ú","ü|Ü","¿","¡",",",".","-","_","?"]]),
 dict(slug="italian-keyboard", name="Italian", native="Italiano", code="it", dir="ltr", region="European",
  desc="Type Italian online for free with this virtual Italian keyboard. Type à, è, é, ì, ò and ù with one click.",
  sample="Ciao, questa è una tastiera italiana.",
  rows=[["1|!","2|\"","3|£","4|$","5|%","6|&","7|/","8|(","9|)","0|="],["q|Q","w|W","e|E","r|R","t|T","y|Y","u|U","i|I","o|O","p|P"],["a|A","s|S","d|D","f|F","g|G","h|H","j|J","k|K","l|L","ò|Ò"],["z|Z","x|X","c|C","v|V","b|B","n|N","m|M","à|À","è|È","é|É"],["ì|Ì","ù|Ù",",",".","-","_","?","'","\"",";"]]),
 dict(slug="russian-keyboard", name="Russian", native="Русский", code="ru", dir="ltr", region="European",
  desc="Type Russian online for free with this virtual Russian keyboard. Type in Cyrillic, copy and paste Russian text anywhere.",
  sample="Привет, это русская клавиатура.",
  rows=[["1|!","2|\"","3|№","4|;","5|%","6|:","7|?","8|*","9|(","0|)"],["й|Й","ц|Ц","у|У","к|К","е|Е","н|Н","г|Г","ш|Ш","щ|Щ","з|З"],["х|Х","ъ|Ъ","ф|Ф","ы|Ы","в|В","а|А","п|П","р|Р","о|О","л|Л"],["д|Д","ж|Ж","э|Э","я|Я","ч|Ч","с|С","м|М","и|И","т|Т","ь|Ь"],["б|Б","ю|Ю","ё|Ё",",",".","-","?","!","\"","'"]]),
 dict(slug="turkish-keyboard", name="Turkish", native="Türkçe", code="tr", dir="ltr", region="Middle Eastern",
  desc="Type Turkish online for free with this virtual Turkish keyboard. Type ç, ğ, ı, İ, ö, ş and ü easily.",
  sample="Merhaba, bu bir Türkçe klavyedir.",
  rows=[["1|!","2|'","3|^","4|+","5|%","6|&","7|/","8|(","9|)","0|="],["q|Q","w|W","e|E","r|R","t|T","y|Y","u|U","ı|I","o|O","p|P"],["a|A","s|S","d|D","f|F","g|G","h|H","j|J","k|K","l|L","ş|Ş"],["z|Z","x|X","c|C","v|V","b|B","n|N","m|M","ö|Ö","ç|Ç","ü|Ü"],["ğ|Ğ","İ|i",",",".","-","?","!","\"","'",";"]]),
 dict(slug="korean-keyboard", name="Korean", native="한국어", code="ko", dir="ltr", region="Asian",
  desc="Type Korean online for free with this virtual Korean keyboard. Type Hangul jamo and common Korean syllables.",
  sample="안녕하세요, 이것은 한국어 키보드입니다.",
  rows=[["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ"],["ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ","ㅏ"],["ㅐ","ㅑ","ㅒ","ㅓ","ㅖ","ㅗ","ㅘ","ㅙ","ㅚ","ㅛ"],["ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ","ㅕ","ㅖ"],["안","녕","하","세","요","감","사","합","니","다"]]),
 dict(slug="persian-keyboard", name="Persian", native="فارسی", code="fa", dir="rtl", region="Middle Eastern",
  desc="Type Persian (Farsi) online for free with this virtual Persian keyboard. Type پ, چ, ژ and گ easily.",
  sample="سلام، این یک صفحه کلید فارسی است.",
  rows=[["۱","۲","۳","۴","۵","۶","۷","۸","۹","۰"],["ا","ب","پ","ت","ث","ج","چ","ح","خ","د"],["ذ","ر","ز","ژ","س","ش","ص","ض","ط","ظ"],["ع","غ","ف","ق","ک","گ","ل","م","ن","و"],["ه","ی","ء","آ","اً","‌","۔","،","؟","!"]]),
 dict(slug="japanese-keyboard", name="Japanese", native="日本語", code="ja", dir="ltr", region="Asian",
  desc="Type Japanese online for free with this virtual Japanese keyboard. Type Hiragana, switch to Katakana, copy and paste.",
  sample="こんにちは、これは日本語キーボードです。",
  rows=[["あ|ア","い|イ","う|ウ","え|エ","お|オ","か|カ","き|キ","く|ク","け|ケ","こ|コ"],["さ|サ","し|シ","す|ス","せ|セ","そ|ソ","た|タ","ち|チ","つ|ツ","て|テ","と|ト"],["な|ナ","に|ニ","ぬ|ヌ","ね|ネ","の|ノ","は|ハ","ひ|ヒ","ふ|フ","へ|ヘ","ほ|ホ"],["ま|マ","み|ミ","む|ム","め|メ","も|モ","や|ヤ","ゆ|ユ","よ|ヨ","ら|ラ","り|リ"],["る|ル","れ|レ","ろ|ロ","わ|ワ","を|ヲ","ん|ン","ー","、","。","？"]]),
 dict(slug="chinese-keyboard", name="Chinese", native="中文", code="zh", dir="ltr", region="Asian",
  desc="Type Chinese online for free with this virtual Chinese keyboard. Click common Chinese characters or type Pinyin in the box.",
  sample="你好，这是一个中文键盘。",
  rows=[["你","好","是","的","一","在","不","了","有","和"],["人","这","中","大","为","上","个","国","我","以"],["要","他","时","来","用","们","生","到","作","地"],["于","出","就","分","对","成","会","可","主","发"],["年","动","同","工","也","能","下","过","子","说"],["谢","谢","请","问","中","国","学","习","爱","家"]]),
 dict(slug="portuguese-keyboard", name="Portuguese", native="Português", code="pt", dir="ltr", region="European",
  desc="Type Portuguese online for free with this virtual Portuguese keyboard. Type ã, õ, á, é, ç and â easily.",
  sample="Olá, este é um teclado em português.",
  rows=[["1|!","2|\"","3|#","4|$","5|%","6|&","7|/","8|(","9|)","0|="],["q|Q","w|W","e|E","r|R","t|T","y|Y","u|U","i|I","o|O","p|P"],["a|A","s|S","d|D","f|F","g|G","h|H","j|J","k|K","l|L","ç|Ç"],["z|Z","x|X","c|C","v|V","b|B","n|N","m|M","ã|Ã","õ|Õ","á|Á"],["é|É","í|Í","ó|Ó","ú|Ú","â|Â","ê|Ê","ô|Ô","à|À","ü|Ü","?"]]),
 dict(slug="english-keyboard", name="English", native="English", code="en", dir="ltr", region="European",
  desc="Type English online for free with this virtual English keyboard. A full QWERTY keyboard that works on any device.",
  sample="Hello, this is an English keyboard.",
  rows=[["1|!","2|@","3|#","4|$","5|%","6|^","7|&","8|*","9|(","0|)"],["q|Q","w|W","e|E","r|R","t|T","y|Y","u|U","i|I","o|O","p|P"],["a|A","s|S","d|D","f|F","g|G","h|H","j|J","k|K","l|L",";|:"],["z|Z","x|X","c|C","v|V","b|B","n|N","m|M",",|<",".|>","/|?"]]),
 dict(slug="vietnamese-keyboard", name="Vietnamese", native="Tiếng Việt", code="vi", dir="ltr", region="Asian",
  desc="Type Vietnamese online for free with this virtual Vietnamese keyboard. Type ă, â, đ, ê, ô, ơ and ư with tones.",
  sample="Xin chào, đây là bàn phím tiếng Việt.",
  rows=[["1|!","2|@","3|#","4|$","5|%","6|^","7|&","8|*","9|(","0|)"],["q|Q","w|W","e|E","r|R","t|T","y|Y","u|U","i|I","o|O","p|P"],["a|A","ă|Ă","â|Â","s|S","d|D","đ|Đ","f|F","g|G","h|H","j|J"],["k|K","l|L","z|Z","x|X","c|C","v|V","b|B","n|N","m|M","ê|Ê"],["ô|Ô","ơ|Ơ","ư|Ư","á|Á","à|À","ả|Ả","ã|Ã","ạ|Ạ","é|É","?"]]),
 dict(slug="polish-keyboard", name="Polish", native="Polski", code="pl", dir="ltr", region="European",
  desc="Type Polish online for free with this virtual Polish keyboard. Type ą, ć, ę, ł, ń, ó, ś, ź and ż easily.",
  sample="Cześć, to jest polska klawiatura.",
  rows=[["1|!","2|@","3|#","4|$","5|%","6|^","7|&","8|*","9|(","0|)"],["q|Q","w|W","e|E","r|R","t|T","y|Y","u|U","i|I","o|O","p|P"],["a|A","ą|Ą","s|S","ś|Ś","d|D","f|F","g|G","h|H","j|J","k|K"],["l|L","ł|Ł","z|Z","ź|Ź","ż|Ż","x|X","c|C","ć|Ć","v|V","b|B"],["n|N","ń|Ń","m|M","ó|Ó","ę|Ę",",",".","-","?","!"]]),
 dict(slug="thai-keyboard", name="Thai", native="ไทย", code="th", dir="ltr", region="Asian",
  desc="Type Thai online for free with this virtual Thai keyboard. Type Thai consonants, vowels and tone marks.",
  sample="สวัสดี นี่คือแป้นพิมพ์ภาษาไทย",
  rows=[["ก","ข","ฃ","ค","ฅ","ฆ","ง","จ","ฉ","ช"],["ซ","ฌ","ญ","ฎ","ฏ","ฐ","ฑ","ฒ","ณ","ด"],["ต","ถ","ท","ธ","น","บ","ป","ผ","ฝ","พ"],["ฟ","ภ","ม","ย","ร","ล","ว","ศ","ษ","ส"],["ห","ฬ","อ","ฮ","ะ","า","ิ","ี","ึ","ื"],["ุ","ู","เ","แ","โ","ใ","ไ","็","่","้"]]),
 dict(slug="bengali-keyboard", name="Bengali", native="বাংলা", code="bn", dir="ltr", region="Asian",
  desc="Type Bengali online for free with this virtual Bengali keyboard. Type in Bangla script, copy and paste anywhere.",
  sample="নমস্কার, এটি একটি বাংলা কীবোর্ড।",
  rows=[["অ","আ","ই","ঈ","উ","ঊ","ঋ","এ","ঐ","ও"],["ঔ","ক","খ","গ","ঘ","ঙ","চ","ছ","জ","ঝ"],["ঞ","ট","ঠ","ড","ঢ","ণ","ত","থ","দ","ধ"],["ন","প","ফ","ব","ভ","ম","য","র","ল","শ"],["ষ","স","হ","ড়","ঢ়","য়","া","ি","ী","ু"],["ূ","ৃ","ে","ৈ","ো","ৌ","ং","ঃ","।","?"]]),
 dict(slug="punjabi-keyboard", name="Punjabi", native="ਪੰਜਾਬੀ", code="pa", dir="ltr", region="Asian",
  desc="Type Punjabi online for free with this virtual Punjabi keyboard. Type in Gurmukhi script, copy and paste anywhere.",
  sample="ਸਤ ਸ੍ਰੀ ਅਕਾਲ, ਇਹ ਪੰਜਾਬੀ ਕੀਬੋਰਡ ਹੈ।",
  rows=[["ਅ","ਆ","ਇ","ਈ","ਉ","ਊ","ਏ","ਐ","ਓ","ਔ"],["ਕ","ਖ","ਗ","ਘ","ਙ","ਚ","ਛ","ਜ","ਝ","ਞ"],["ਟ","ਠ","ਡ","ਢ","ਣ","ਤ","ਥ","ਦ","ਧ","ਨ"],["ਪ","ਫ","ਬ","ਭ","ਮ","ਯ","ਰ","ਲ","ਵ","ਸ਼"],["ਹ","ੜ","ਾ","ਿ","ੀ","ੁ","ੂ","ੇ","ੈ","ੋ"],["ੌ","ੰ","ਂ","ੱ","।","?","!","'","\"","-"]]),
 dict(slug="tamil-keyboard", name="Tamil", native="தமிழ்", code="ta", dir="ltr", region="Asian",
  desc="Type Tamil online for free with this virtual Tamil keyboard. Type Tamil letters, copy and paste Tamil text anywhere.",
  sample="வணக்கம், இது ஒரு தமிழ் விசைப்பலகை.",
  rows=[["அ","ஆ","இ","ஈ","உ","ஊ","எ","ஏ","ஐ","ஒ"],["ஓ","ஔ","க","ங","ச","ஞ","ட","ண","த","ந"],["ப","ம","ய","ர","ல","வ","ழ","ள","ற","ன"],["ா","ி","ீ","ு","ூ","ெ","ே","ை","ொ","ோ"],["ௌ","்","ஂ","ஃ","ஸ","ஷ","ஜ","ஹ","க்ஷ","?"]]),
 dict(slug="telugu-keyboard", name="Telugu", native="తెలుగు", code="te", dir="ltr", region="Asian",
  desc="Type Telugu online for free with this virtual Telugu keyboard. Type Telugu letters, copy and paste anywhere.",
  sample="నమస్కారం, ఇది తెలుగు కీబోర్డ్.",
  rows=[["అ","ఆ","ఇ","ఈ","ఉ","ఊ","ఋ","ఎ","ఏ","ఐ"],["ఒ","ఓ","ఔ","క","ఖ","గ","ఘ","ఙ","చ","ఛ"],["జ","ఝ","ఞ","ట","ఠ","డ","ఢ","ణ","త","థ"],["ద","ధ","న","ప","ఫ","బ","భ","మ","య","ర"],["ల","వ","శ","ష","స","హ","ళ","క్ష","ా","ి"],["ీ","ు","ూ","ె","ే","ై","ొ","ో","ౌ","ం"]]),
 dict(slug="greek-keyboard", name="Greek", native="Ελληνικά", code="el", dir="ltr", region="European",
  desc="Type Greek online for free with this virtual Greek keyboard. Type α, β, γ and all Greek letters easily.",
  sample="Γεια σας, αυτό είναι ένα ελληνικό πληκτρολόγιο.",
  rows=[["1|!","2|@","3|#","4|$","5|%","6|^","7|&","8|*","9|(","0|)"],["α|Α","β|Β","γ|Γ","δ|Δ","ε|Ε","ζ|Ζ","η|Η","θ|Θ","ι|Ι","κ|Κ"],["λ|Λ","μ|Μ","ν|Ν","ξ|Ξ","ο|Ο","π|Π","ρ|Ρ","σ|Σ","τ|Τ","υ|Υ"],["φ|Φ","χ|Χ","ψ|Ψ","ω|Ω","ς","ά|Ά","έ|Έ","ή|Ή","ί|Ί","ό|Ό"],["ύ|Ύ","ώ|Ώ",",",".","-","?","!",";","\"","'"]]),
 dict(slug="hebrew-keyboard", name="Hebrew", native="עברית", code="he", dir="rtl", region="Middle Eastern",
  desc="Type Hebrew online for free with this virtual Hebrew keyboard. Type Hebrew letters, copy and paste anywhere.",
  sample="שלום, זוהי מקלדת עברית.",
  rows=[["1|!","2|@","3|#","4|$","5|%","6|^","7|&","8|*","9|(","0|)"],["א","ב","ג","ד","ה","ו","ז","ח","ט","י"],["כ","ל","מ","נ","ס","ע","פ","צ","ק","ר"],["ש","ת","ך","ם","ן","ף","ץ","װ","ױ","ײ"],["״","׵","׶","׷","׸","׹",",",".","?","!"]]),
 dict(slug="emoji-keyboard", name="Emoji", native="😀", code="en", dir="ltr", region="Other",
  desc="Type emoji online for free with this virtual emoji keyboard. Click any emoji to add it, then copy and paste anywhere.",
  sample="😀 🎉 ❤️ 👍 🌍",
  rows=[["😀","😃","😄","😁","😆","😅","😂","🤣","😊","😇"],["🙂","🙃","😉","😌","😍","🥰","😘","😗","😙","😚"],["😋","😛","😝","😜","🤪","🤨","🧐","🤓","😎","🤩"],["🥳","😏","😒","😞","😔","😟","😕","🙁","☹️","😣"],["😖","😫","😩","🥺","😢","😭","😤","😠","😡","🤯"],["❤️","🧡","💛","💚","💙","💜","🖤","🤍","🤎","💔"],["👍","👎","👌","✌️","🤞","🤟","🤘","👏","🙌","🙏"],["🌍","🌎","🌏","🌞","🌝","🌚","⭐","✨","🔥","💧"]]),
]

CSS = """*{box-sizing:border-box}body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;line-height:1.6;color:#17202a;background:#f6f8fa}
a{color:#0b5fff;text-decoration:none}a:hover{text-decoration:underline}
header.site{background:#111827;color:#fff;padding:14px 20px;position:sticky;top:0;z-index:10}
header.site .wrap,main,.wrap{max-width:980px;margin:0 auto;padding:0 20px}
header.site .wrap{display:flex;gap:18px;align-items:center;flex-wrap:wrap;justify-content:space-between}
.logo{font-weight:800;font-size:20px;color:#fff}
nav a{color:#dbeafe;margin:0 8px;font-size:15px}
.hero{background:#fff;border-bottom:1px solid #e5e7eb;padding:36px 0 28px}
.hero h1{font-size:34px;line-height:1.2;margin:0 0 10px}
.hero p{font-size:18px;color:#374151;margin:0 0 16px}
.search{width:100%;padding:13px 14px;font-size:17px;border:2px solid #cbd5e1;border-radius:10px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px;margin:22px 0}
.card{background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:16px}
.card h3{margin:0 0 6px;font-size:18px}.card p{margin:0 0 10px;color:#4b5563;font-size:14px}
.btn{display:inline-block;background:#0b5fff;color:#fff;padding:9px 14px;border-radius:8px;font-weight:600;border:0;cursor:pointer}
.btn.secondary{background:#e5e7eb;color:#111827}
.btn:hover{text-decoration:none;opacity:.92}
textarea#output{width:100%;min-height:170px;padding:14px;font-size:20px;line-height:1.7;border:2px solid #cbd5e1;border-radius:12px;background:#fff;resize:vertical}
textarea#output:focus{outline:3px solid #bfdbfe;border-color:#0b5fff}
.toolbar{display:flex;gap:10px;flex-wrap:wrap;margin:12px 0}
.toolbar button{padding:10px 14px;border-radius:8px;border:1px solid #cbd5e1;background:#fff;font-weight:600;cursor:pointer;font-size:15px}
.toolbar button.primary{background:#0b5fff;color:#fff;border-color:#0b5fff}
.counts{color:#4b5563;font-size:14px;margin:6px 0 14px}
.keyboard{background:#111827;border-radius:14px;padding:14px;margin:10px 0 20px}
.kb-row{display:flex;gap:6px;margin-bottom:6px;flex-wrap:wrap;justify-content:center}
.kb-key{min-width:42px;min-height:48px;padding:8px 10px;font-size:19px;border-radius:8px;border:1px solid #374151;background:#1f2937;color:#fff;cursor:pointer;flex:1 0 auto}
.kb-key:hover{background:#374151}.kb-key.wide{flex:2 1 auto;background:#374151}
.kb-key.shift-on{background:#0b5fff}
.kb-key:active{transform:translateY(1px)}
section{background:#fff;border:1px solid #e5e7eb;border-radius:12px;padding:20px;margin:18px 0}
h2{font-size:24px;margin-top:0}h3{font-size:19px}
.breadcrumb{font-size:14px;color:#6b7280;margin:16px 0 0}
.faq details{border-top:1px solid #e5e7eb;padding:12px 0}.faq summary{font-weight:700;cursor:pointer}
footer.site{background:#111827;color:#cbd5e1;padding:28px 0;margin-top:30px}
footer.site a{color:#fff}.notice{background:#eff6ff;border:1px solid #bfdbfe;border-radius:10px;padding:12px 14px;margin:16px 0}
@media(max-width:640px){.hero h1{font-size:27px}.kb-key{min-width:34px;min-height:44px;font-size:17px;padding:6px 7px}textarea#output{font-size:18px}}
"""

JS = """document.addEventListener('DOMContentLoaded',function(){
 var out=document.getElementById('output');
 var dataEl=document.getElementById('kb-data');
 var shift=false;
 function updateCounts(){ if(!out) return; var t=out.value; var w=t.trim()?t.trim().split(/\\s+/).length:0;
  var c=document.getElementById('counts'); if(c) c.textContent=w+' words · '+t.length+' characters · '+t.replace(/\\s/g,'').length+' characters without spaces'; }
 function insertText(s){ if(!out) return; var s0=out.selectionStart||0, e=out.selectionEnd||0;
  out.value=out.value.slice(0,s0)+s+out.value.slice(e); var p=s0+s.length; out.focus(); out.setSelectionRange(p,p); updateCounts(); }
 function build(){ if(!dataEl||!out) return; var data=JSON.parse(dataEl.textContent); var kb=document.getElementById('keyboard'); if(!kb) return;
  kb.innerHTML=''; data.rows.forEach(function(row){ var r=document.createElement('div'); r.className='kb-row';
   row.forEach(function(k){ var parts=String(k).split('|'); var b=document.createElement('button'); b.type='button'; b.className='kb-key';
    b.textContent=shift&&parts[1]?parts[1]:parts[0]; b.dataset.normal=parts[0]; b.dataset.shift=parts[1]||parts[0];
    b.setAttribute('aria-label','Type '+parts[0]); b.addEventListener('click',function(){ insertText(b.dataset.shift&&shift?b.dataset.shift:b.dataset.normal); }); r.appendChild(b); });
   kb.appendChild(r); });
  var cr=document.createElement('div'); cr.className='kb-row';
  [['Shift','shift',1],['Space',' ',3],['Backspace','back',1],['Enter','enter',1]].forEach(function(x){
   var b=document.createElement('button'); b.type='button'; b.className='kb-key wide'+(x[0]==='Shift'&&shift?' shift-on':''); b.textContent=x[0];
   b.addEventListener('click',function(){ if(x[1]==='shift'){ shift=!shift; build(); } else if(x[1]==='back'){ if(out){ var s0=out.selectionStart||0,e=out.selectionEnd||0; if(s0!==e){ out.value=out.value.slice(0,s0)+out.value.slice(e); out.setSelectionRange(s0,s0);} else if(s0>0){ out.value=out.value.slice(0,s0-1)+out.value.slice(s0); out.setSelectionRange(s0-1,s0-1);} out.focus(); updateCounts(); } } else if(x[1]==='enter'){ insertText('\\n'); } else { insertText(' '); } });
   cr.appendChild(b); }); kb.appendChild(cr); }
 if(out){ out.addEventListener('input',updateCounts); updateCounts(); }
 build();
 var copyBtn=document.getElementById('copy-btn'); if(copyBtn&&out) copyBtn.addEventListener('click',function(){ var done=function(){ copyBtn.textContent='Copied!'; setTimeout(function(){copyBtn.textContent='Copy text';},1500); };
  if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(out.value).then(done).catch(function(){ out.select(); document.execCommand('copy'); done(); }); } else { out.select(); document.execCommand('copy'); done(); } });
 var clearBtn=document.getElementById('clear-btn'); if(clearBtn&&out) clearBtn.addEventListener('click',function(){ out.value=''; out.focus(); updateCounts(); });
 var dlBtn=document.getElementById('download-btn'); if(dlBtn&&out) dlBtn.addEventListener('click',function(){ var blob=new Blob([out.value],{type:'text/plain;charset=utf-8'}); var a=document.createElement('a'); a.href=URL.createObjectURL(blob); a.download='keyboardsonline-text.txt'; a.click(); setTimeout(function(){URL.revokeObjectURL(a.href);},1000); });
 var selBtn=document.getElementById('select-btn'); if(selBtn&&out) selBtn.addEventListener('click',function(){ out.focus(); out.select(); });
 var search=document.getElementById('kb-search'); if(search){ search.addEventListener('input',function(){ var q=search.value.toLowerCase(); document.querySelectorAll('.kb-card').forEach(function(card){ card.style.display=card.dataset.name.toLowerCase().includes(q)?'':'none'; }); }); }
});
"""

def head(title, desc, canonical, prefix, extra_jsonld=None, og_type="website"):
    jld = extra_jsonld or ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="KeyboardsOnline">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="theme-color" content="#111827">
<link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{prefix}assets/css/style.css">
{jld}</head>
"""

def header(prefix):
    return f"""<body>
<header class="site"><div class="wrap"><a class="logo" href="{prefix}">🌍 KeyboardsOnline</a><nav><a href="{prefix}">Home</a><a href="{prefix}keyboards/">All Keyboards</a><a href="{prefix}about-keyboardsonline/">About</a><a href="{prefix}contact-keyboardsonline/">Contact</a></nav></div></header>
<main>
"""

def footer(prefix):
    return f"""</main>
<footer class="site"><div class="wrap"><p><strong>KeyboardsOnline</strong> — free online keyboards for 100+ languages. Type in your browser, copy and paste anywhere. No installation, no signup.</p><p>Original site: <a href="{ORIG}/">KeyboardsOnline.net</a> · <a href="{prefix}privacy-policy/">Privacy Policy</a> · <a href="{prefix}about-keyboardsonline/">About</a> · <a href="{prefix}contact-keyboardsonline/">Contact</a></p><p>This GitHub Pages version is a free, open mirror built from the original site. For the full site with 100+ keyboards, visit <a href="{ORIG}/">https://keyboardsonline.net/</a>.</p></div></footer>
<script src="{prefix}assets/js/keyboard.js" defer></script>
</body>
</html>
"""

def jsonld(obj):
    return '<script type="application/ld+json">\n' + json.dumps(obj, ensure_ascii=False, indent=2) + '\n</script>'

def write(path, content):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    print("wrote", path, len(content))

# assets
write("assets/css/style.css", CSS)
write("assets/js/keyboard.js", JS)
write("assets/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#111827"/><text x="32" y="42" font-size="32" text-anchor="middle">⌨️</text></svg>')
write(".nojekyll", "")
write("README.md", f"""# KeyboardsOnline — GitHub Pages

Free online keyboards for 100+ languages. This repository contains a static, SEO-optimized GitHub Pages version with **25 working keyboards** to start.

Original site: {ORIG}/

## Live site (GitHub Pages)
{BASE}/

Enable GitHub Pages in the repository: Settings → Pages → Deploy from a branch → `main` / `/ (root)`.

## What's inside
- `index.html` — homepage with search and all 25 keyboards
- `keyboards/` — index of all keyboards
- `<language>-keyboard/` — one page per keyboard, with a working on-screen keyboard, copy / clear / download, word & character counts, FAQ and structured data
- `assets/css/style.css`, `assets/js/keyboard.js` — shared styles and keyboard logic
- `sitemap.xml`, `robots.txt`, `.nojekyll`

## SEO
Every page has a unique title and meta description, canonical URL, Open Graph / Twitter tags, semantic HTML, fast static assets, and JSON-LD structured data (WebSite, WebApplication, BreadcrumbList, FAQPage).

## Add another keyboard
Copy an existing `<language>-keyboard/` page, update its title, description, layout rows in the `kb-data` JSON block, and FAQ, then add it to `index.html`, `keyboards/index.html` and `sitemap.xml`.
""")

# homepage
cards = "".join(
    f'<article class="card kb-card" data-name="{esc(l["name"]+" "+l["native"]+" keyboard")}"><h3>{esc(l["name"])} Keyboard</h3><p>{esc(l["native"])} · {esc(l["desc"][:90])}…</p><a class="btn" href="{l["slug"]}/">Open {esc(l["name"])} keyboard →</a></article>'
    for l in LANGS)
home_jld = jsonld({
 "@context":"https://schema.org","@type":"WebSite","name":"KeyboardsOnline","alternateName":"Online Keyboards",
 "url":BASE+"/","inLanguage":"en",
 "description":"Free online keyboards for 100+ languages. Type in Urdu, Arabic, Hindi, French, Spanish, German, Russian and many more directly in your browser.",
 "publisher":{"@type":"Organization","name":"KeyboardsOnline","url":ORIG+"/"},
 "potentialAction":{"@type":"SearchAction","target":BASE+"/keyboards/?q={search_term_string}","query-input":"required name=search_term_string"}
})
home_faq = jsonld({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {"@type":"Question","name":"What is an online keyboard?","acceptedAnswer":{"@type":"Answer","text":"An online keyboard is a browser-based tool that helps you type in another language without installing keyboard software."}},
 {"@type":"Question","name":"Is KeyboardsOnline free?","acceptedAnswer":{"@type":"Answer","text":"Yes. KeyboardsOnline offers free online keyboards and language tools."}},
 {"@type":"Question","name":"Can I use these keyboards on mobile?","acceptedAnswer":{"@type":"Answer","text":"Yes. The keyboards are designed to work on mobile phones, tablets, laptops and desktop computers."}},
 {"@type":"Question","name":"Do I need to install anything?","acceptedAnswer":{"@type":"Answer","text":"No. Everything works directly in your browser."}},
 {"@type":"Question","name":"Can I copy and paste the text?","acceptedAnswer":{"@type":"Answer","text":"Yes. You can copy your typed text and paste it into documents, emails, websites, social media or messaging apps."}}]})
write("index.html",
 head("Online Keyboards for 100+ Languages | KeyboardsOnline","Type in Urdu, Arabic, Hindi, French, Spanish, German, Russian and many more languages directly in your browser. Free, no installation, no signup — just search, type, copy and paste.",BASE+"/","",home_jld+"\n"+home_faq)
 + header("")
 + f"""<section class="hero"><h1>Online Keyboards for Every Language</h1><p>Type in Urdu, Arabic, Hindi, French, Spanish, German, Russian and many more languages directly in your browser. No installation, no signup — just search, type, copy and paste.</p><label for="kb-search">Search keyboards</label><input id="kb-search" class="search" type="search" placeholder="Search keyboards — try Urdu, Arabic, Hindi…" aria-label="Search keyboards"></section>
<div class="notice">Looking for the full site with 100+ keyboards? Visit the original site: <a href="{ORIG}/"><strong>https://keyboardsonline.net/</strong></a></div>
<section><h2>Start Typing in Your Language</h2><p>Open any online keyboard below and type instantly without installing software. This GitHub Pages edition starts with 25 keyboards.</p><div class="grid">{cards}</div></section>
<section><h2>Simple, Fast &amp; Privacy Friendly</h2><p><strong>⚡ Fast Typing:</strong> Open a keyboard and start typing immediately.<br><strong>📱 Works Everywhere:</strong> Use on mobile, tablet, laptop, desktop, Android, iPhone and Windows.<br><strong>🔒 Privacy Friendly:</strong> Your typed text stays in your browser.<br><strong>📋 Copy &amp; Paste:</strong> Copy your text and paste it into any app or website.</p></section>
<section><h2>Free Online Keyboards and Language Tools</h2><p>KeyboardsOnline.net helps you type in different languages directly from your browser. You can choose a language keyboard, type your text, copy it, and use it anywhere without installing extra software. The site is designed for students, writers, translators, language learners, social media users and anyone who needs quick multilingual typing. Each keyboard has its own dedicated page, while the homepage helps users quickly find the right keyboard or tool.</p></section>
<section class="faq"><h2>Frequently Asked Questions</h2><details><summary>What is an online keyboard?</summary><p>An online keyboard is a browser-based tool that helps you type in another language without installing keyboard software.</p></details><details><summary>Is KeyboardsOnline free?</summary><p>Yes. KeyboardsOnline offers free online keyboards and language tools.</p></details><details><summary>Can I use these keyboards on mobile?</summary><p>Yes. The keyboards are designed to work on mobile phones, tablets, laptops and desktop computers.</p></details><details><summary>Do I need to install anything?</summary><p>No. Everything works directly in your browser.</p></details><details><summary>Can I copy and paste the text?</summary><p>Yes. You can copy your typed text and paste it into documents, emails, websites, social media or messaging apps.</p></details></section>
"""
 + footer(""))

# keyboards index
idx_cards = "".join(f'<article class="card"><h3>{esc(l["name"])} Keyboard</h3><p>{esc(l["native"])} · {esc(l["region"])}</p><a class="btn" href="../{l["slug"]}/">Open {esc(l["name"])} keyboard →</a></article>' for l in LANGS)
write("keyboards/index.html",
 head("All Online Keyboards | KeyboardsOnline","Browse all 25 free online keyboards on this GitHub Pages site — Urdu, Arabic, Hindi, French, Spanish, German, Russian, Japanese, Korean, Chinese and more.",BASE+"/keyboards/","../",
 jsonld({"@context":"https://schema.org","@type":"CollectionPage","name":"All Online Keyboards","url":BASE+"/keyboards/","isPartOf":{"@type":"WebSite","name":"KeyboardsOnline","url":BASE+"/"},
 "hasPart":[{"@type":"WebApplication","name":l["name"]+" Keyboard","url":BASE+"/"+l["slug"]+"/"} for l in LANGS]}))
 + header("../")
 + f"""<p class="breadcrumb"><a href="../">Home</a> › All Keyboards</p><section class="hero"><h1>All Online Keyboards</h1><p>Browse the 25 keyboards in this edition. For the full collection of 100+ keyboards, visit <a href="{ORIG}/keyboards/">KeyboardsOnline.net — All Keyboards</a>.</p></section><div class="grid">{idx_cards}</div>
""" + footer("../"))

# keyboard pages
for i,l in enumerate(LANGS):
    slug=l["slug"]; url=f"{BASE}/{slug}/"; orig=f"{ORIG}/{slug}/"
    related=[x for x in LANGS if x is not l][:4]
    rel_html="".join(f'<li><a href="../{x["slug"]}/">{esc(x["name"])} Keyboard</a></li>' for x in related)
    title=f"{l['name']} Keyboard Online — Free {l['name']} Typing | KeyboardsOnline"
    jld_obj={"@context":"https://schema.org","@graph":[
      {"@type":"WebPage","name":title,"url":url,"inLanguage":"en","isPartOf":{"@type":"WebSite","name":"KeyboardsOnline","url":BASE+"/"},
       "breadcrumb":{"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":BASE+"/"},{"@type":"ListItem","position":2,"name":"All Keyboards","item":BASE+"/keyboards/"},{"@type":"ListItem","position":3,"name":l["name"]+" Keyboard","item":url}]}},
      {"@type":"WebApplication","name":l["name"]+" Keyboard","alternateName":l["name"]+" Online Keyboard","url":url,"applicationCategory":"UtilitiesApplication","operatingSystem":"Any","browserRequirements":"Requires JavaScript","inLanguage":l["code"],"isAccessibleForFree":True,
       "offers":{"@type":"Offer","price":"0","priceCurrency":"USD"},
       "description":l["desc"]},
      {"@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":f"How do I type in {l['name']} online?","acceptedAnswer":{"@type":"Answer","text":f"Open this {l['name']} keyboard, click the on-screen keys or type on your physical keyboard, then copy your text."}},
        {"@type":"Question","name":f"Is the {l['name']} keyboard free?","acceptedAnswer":{"@type":"Answer","text":f"Yes, this {l['name']} keyboard is completely free to use, with no installation or signup."}},
        {"@type":"Question","name":f"Can I copy {l['name']} text from here?","acceptedAnswer":{"@type":"Answer","text":"Yes. Use the Copy text button, or select the text and copy it to paste into any app, document or website."}}]}
    ]}
    layout=json.dumps({"rows":l["rows"]}, ensure_ascii=False)
    write(f"{slug}/index.html",
     head(title,l["desc"],url,"../",jsonld(jld_obj),"website")
     + header("../")
     + f"""<p class="breadcrumb"><a href="../">Home</a> › <a href="../keyboards/">All Keyboards</a> › {esc(l['name'])} Keyboard</p>
<section class="hero"><h1>{esc(l['name'])} Keyboard Online — Free {esc(l['name'])} Typing</h1><p>{esc(l['desc'])}</p><p><strong>{esc(l['native'])}</strong> · Example: <span lang="{l['code']}" dir="{l['dir']}">{esc(l['sample'])}</span></p></section>
<div class="notice">Also on the original site: <a href="{orig}">{esc(l['name'])} Keyboard on KeyboardsOnline.net</a></div>
<label for="output"><strong>Type in {esc(l['name'])} here</strong></label>
<textarea id="output" lang="{l['code']}" dir="{l['dir']}" placeholder="Click the keyboard below or type here… {esc(l['sample'])}" aria-label="{esc(l['name'])} text input"></textarea>
<p class="counts" id="counts">0 words · 0 characters</p>
<div class="toolbar"><button type="button" id="copy-btn" class="primary">Copy text</button><button type="button" id="select-btn">Select all</button><button type="button" id="download-btn">Download .txt</button><button type="button" id="clear-btn">Clear</button></div>
<script id="kb-data" type="application/json">{layout}</script>
<div id="keyboard" class="keyboard" role="group" aria-label="{esc(l['name'])} on-screen keyboard"></div>
<p><small>Tip: click a key to insert it at the cursor. Use Shift for the second character on each key, Backspace to delete, and Space / Enter as normal. Your text never leaves your browser.</small></p>
<section><h2>How to use this {esc(l['name'])} keyboard</h2><ol><li>Click the keys above, or type directly in the text box.</li><li>Use <strong>Shift</strong> on the on-screen keyboard for alternate characters.</li><li>Click <strong>Copy text</strong> and paste your {esc(l['name'])} text into WhatsApp, Facebook, Word, email or any other app.</li><li>Use <strong>Download .txt</strong> to save your text as a file.</li></ol></section>
<section class="faq"><h2>{esc(l['name'])} Keyboard — FAQs</h2><details><summary>How do I type in {esc(l['name'])} online?</summary><p>Open this {esc(l['name'])} keyboard, click the on-screen keys or type on your physical keyboard, then copy your text.</p></details><details><summary>Is the {esc(l['name'])} keyboard free?</summary><p>Yes, this {esc(l['name'])} keyboard is completely free to use, with no installation or signup.</p></details><details><summary>Can I copy {esc(l['name'])} text from here?</summary><p>Yes. Use the Copy text button, or select the text and copy it to paste into any app, document or website.</p></details></section>
<section><h2>Related keyboards</h2><ul>{rel_html}</ul><p>See <a href="../keyboards/">all 25 keyboards</a> or the full site at <a href="{ORIG}/">KeyboardsOnline.net</a>.</p></section>
""" + footer("../"))

# simple pages
def simple(slug, title, desc, body_html):
    url=f"{BASE}/{slug}/"
    return (head(title, desc, url, "../",
      jsonld({"@context":"https://schema.org","@type":"WebPage","name":title,"url":url,"isPartOf":{"@type":"WebSite","name":"KeyboardsOnline","url":BASE+"/"}}))
     + header("../") + f'<p class="breadcrumb"><a href="../">Home</a> › {esc(title.split(" | ")[0])}</p><section class="hero"><h1>{esc(title.split(" | ")[0])}</h1><p>{esc(desc)}</p></section><section>{body_html}</section>' + footer("../"))

write("about-keyboardsonline/index.html", simple("about-keyboardsonline","About KeyboardsOnline | KeyboardsOnline","About KeyboardsOnline — free online keyboards for 100+ languages, built to make typing in any language simple, fast and private.",
 "<p>KeyboardsOnline helps you type in different languages directly from your browser. Choose a language keyboard, type your text, copy it, and use it anywhere without installing extra software.</p><p>This GitHub Pages edition starts with 25 keyboards. The original, full site is at <a href=\""+ORIG+"/\">https://keyboardsonline.net/</a>.</p><p>It is designed for students, writers, translators, language learners, social media users and anyone who needs quick multilingual typing.</p>"))
write("contact-keyboardsonline/index.html", simple("contact-keyboardsonline","Contact KeyboardsOnline | KeyboardsOnline","Contact KeyboardsOnline — get in touch about the free online keyboards, suggestions or corrections.",
 "<p>Questions, suggestions or a keyboard you'd like added? Visit the original site's contact page: <a href=\""+ORIG+"/contact-keyboardsonline/\">KeyboardsOnline.net — Contact</a>.</p><p>You can also open an issue on this GitHub repository.</p>"))
write("privacy-policy/index.html", simple("privacy-policy","Privacy Policy | KeyboardsOnline","Privacy Policy for KeyboardsOnline — your typed text stays in your browser and is not collected by this site.",
 "<p>This site does not collect, store or send the text you type. All typing happens locally in your browser.</p><p>GitHub Pages, the host for this version, may collect standard web-server logs. See the full policy on the original site: <a href=\""+ORIG+"/privacy-policy/\">KeyboardsOnline.net — Privacy Policy</a>.</p>"))

write("404.html",
 head("Page Not Found | KeyboardsOnline","The page you were looking for is not on this GitHub Pages site. Try the homepage or the full site at keyboardsonline.net.",BASE+"/404.html","",
 jsonld({"@context":"https://schema.org","@type":"WebPage","name":"Page Not Found","url":BASE+"/404.html"}))
 + header("") + '<section class="hero"><h1>Page not found</h1><p>That page isn\'t here. Try the <a href="./">homepage</a> or <a href="./keyboards/">all keyboards</a>, or the full site at <a href="'+ORIG+'/">KeyboardsOnline.net</a>.</p></section>' + footer(""))

# sitemap + robots
urls=[BASE+"/"]+[f"{BASE}/{l['slug']}/" for l in LANGS]+[BASE+"/keyboards/",BASE+"/about-keyboardsonline/",BASE+"/contact-keyboardsonline/",BASE+"/privacy-policy/"]
sitemap='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f'  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>{"1.0" if u==BASE+"/" else "0.8"}</priority></url>\n' for u in urls) + '</urlset>\n'
write("sitemap.xml", sitemap)
write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")

print("DONE", len(LANGS), "keyboards,", len(urls), "urls")
