# Exercise 23: Strings, Bytes, and Character Encodings

# What does "encode" mean though? It's nothing more than an agreed upon standard for how a sequence of bits should represent a number. 
# Today we call a "byte" a sequence of 8 bits (1s and 0s).
# Once you have bytes you can start to store and display text by deciding on another convention for how a number maps to a letter.
# The most popular convention ended up being American Standard Code for Information Interchange, or ASCII. 
# This standard maps a number to a letter. 90 is Z, which in bits is 1011010, which gets mapped to the ASCII table inside the computer.
# The problem with ASCII is that it only encodes English and maybe a few other similar languages. 
# Remember that a byte can hold 256 numbers (0-255, or 00000000-11111111).
# Different countries created their own encoding conventions for their languages, and that mostly worked, but many encodings could only handle one language. 
# That meant if you want to put the title of an American English book in the middle of a Thai sentence you were kind of in trouble. You'd need one encoding for Thai and for English.
# To solve this problem a group of people created Unicode. It is meant to be a "universal encoding" of all human languages. 
# The solution Unicode provides is like the ASCII table, but it's huge by comparison. You can use 32 bits to encode a Unicode character (2^32).
# We now have a convention for encoding any characters we want, but 32 bits is 4 bytes (32/8 == 4) which means there is so much wasted space in most text we want to encode. 
# The solution is to use a clever convention to encode most common characters using 8 bits, and then "escape" into larger numbers when we need to encode more characters. 
# That means we have one more convention that is nothing more than a compression encoding, allowing for most common characters to use 8 bits, and then escape out into 16 or 32 bits as needed.
# The conventions for encoding text in Python is called "utf-8", which means "Unicode Transformation Format 8 Bits" and is a convention for encoding Unicode characters into sequences of bytes.

# The ex23.py script is told to translate the name "Аҧсшәа" to the utf-8 encoding. 
# On the left is b'\xd0\x90\xd2\xa7\xd1\x81\xd1\x88\xd3\x99\xd0\xb0' which is the sequence of bytes that encode this utf-8 string. 
# The b'' syntax is how you tell Python, "This here is a sequence of raw bytes with no encoding convention given." 
# The b'' bytes could be anything. An image file, UTF-8 string, UTF-32, Big5, as long as it fits into a sequence of bytes. 
# Your entire file should be UTF-8 encoding, so if you're used to a different encoding (Big5, Koi8, etc.) then you'll need to change your text editor.

# In Python a string is a UTF-8 encoded sequence of characters for displaying or working with text. 
# The bytes are then the "raw" sequence of bytes that Python uses to store this UTF-8 string, and starts with a b' to tell Python you are working with raw bytes. 

# All you need to remember is if you have raw bytes then you must use .decode() to get the string.
 # "DBES" which stands for "Decode Bytes Encode Strings". 
 #I say "dee bez" in my head when I have to convert bytes and strings. When you have bytes and need a string, "Decode Bytes". When you have a string and need bytes, "Encode Strings"
import sys

encoding, errors = sys.argv[1:]

languages = [
    "Afrikaans", "አማርኛ", "Аҧсшәа", "العربية",
    "Aragonés", "Arpetan", "Azərbaycanca", "Bamanankan",
    "বাংলা", "Bân-lâm-gú", "Беларуская", "Български",
    "Boarisch", "Bosanski", "Буряад", "Català",
    "Чӑвашла", "Čeština", "Cymraeg", "Dansk",
    "Deutsch", "Eesti", "Ελληνικά", "Español",
    "Esperanto", "فارسی", "Français", "Frysk",
    "Gaelg", "Gàidhlig", "Galego", "한국어",
    "Հայերեն", "हिन्दी", "Hrvatski", "Ido",
    "Interlingua", "Italiano", "עברית", "ಕನ್ನಡ",
    "Kapampangan", "ქართული", "Қазақша", "Kreyòl ayisyen",
    "Latgaļu", "Latina", "Latviešu", "Lëtzebuergesch",
    "Lietuvių", "Magyar", "Македонски", "Malti",
    "मराठी", "მარგალური", "مازِرونی", "Bahasa Melayu",
    "Монгол", "Nederlands", "नेपाल भाषा", "日本語",
    "Norsk bokmål", "Nouormand", "Occitan", "Oʻzbekcha/ўзбекча",
    "ਪੰਜਾਬੀ", "پنجابی", "پښتو", "Plattdüütsch",
    "Polski", "Português", "Română", "Romani",
    "Русский", "Seeltersk", "Shqip", "Simple English",
    "Slovenčina", "کوردیی ناوەندی", "Српски / srpski",
    "Suomi", "Svenska", "Tagalog", "தமிழ்", "ภาษาไทย",
    "Taqbaylit", "Татарча/tatarça", "తెలుగు", "Тоҷикӣ",
    "Türkçe", "Українська", "اردو", "Tiếng Việt",
    "Võro", "文言", "吴语", "ייִדיש", "中文"
]

def run(language_list, encoding, errors):
    if language_list:
        next_lang = language_list.pop()
        raw_bytes = next_lang.encode(encoding, errors=errors)
        cooked_string = raw_bytes.decode(encoding, errors=errors)

        print(raw_bytes, "<===>", cooked_string)

        return run(language_list, encoding, errors)

run(languages, encoding, errors)

