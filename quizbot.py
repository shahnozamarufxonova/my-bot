import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)

TOKEN = "8765824197:AAE6wJ2JiqAq6abAwm-j8J0iDMVg1tC18a4"

letters = ["A", "B", "C", "D"]

questions = [
    {
        "question": "Blokcheyn nima?",
        "correct": "Tarqatilgan ma’lumotlar bazasi",
        "wrong": [
            "Kompyuter virusi",
            "Grafik karta",
            "Brauzer"
        ]
    },
    {
        "question": "Har bir blokda odatda qaysi ma’lumotlar bo‘ladi?",
        "correct": "Tranzaksiyalar va xesh",
        "wrong": [
            "Faqat rasm",
            "Video fayl",
            "O‘yin ma’lumotlari"
        ]
    },
    {
        "question": "Kriptovalyuta qanday to‘lov tizimiga asoslanadi?",
        "correct": "Markazlashmagan tizim",
        "wrong": [
            "Faqat bank",
            "SMS tizimi",
            "Telefon tarmog‘i"
        ]
    },
    {
        "question": "Blokcheyn 1.0 asosan nima bilan bog‘liq?",
        "correct": "Bitcoin",
        "wrong": [
            "Instagram",
            "Video montaj",
            "Bulutli o‘yin"
        ]
    },
    {
        "question": "Blokcheyn 2.0 ning asosiy xususiyati nima?",
        "correct": "Smart shartnomalar",
        "wrong": [
            "Kameralar",
            "Printerlar",
            "Grafik dizayn"
        ]
    },
    {
        "question": "Ochiq blokcheynlarda kim ishtirok etishi mumkin?",
        "correct": "Hamma",
        "wrong": [
            "Faqat admin",
            "Faqat bank",
            "Faqat kompaniya"
        ]
    },
    {
    "question": "Yopiq blokcheynlar kimlar uchun ochiq bo‘ladi?",
    "correct": "Faqat ruxsat berilgan ishtirokchilar",
    "wrong": [
        "Hamma uchun",
        "Faqat talabalar uchun",
        "Faqat telefon egalari uchun"
    ]
},
{
    "question": "Kriptovalyutalarning muhim kamchiliklaridan biri qaysi?",
    "correct": "Narxning keskin o‘zgaruvchanligi",
    "wrong": [
        "Internet ishlatmasligi",
        "Faqat qog‘ozda ishlashi",
        "Printer talab qilishi"
    ]
},
{
    "question": "Ikki martalik sarf-xarajatlar muammosi nimani anglatadi?",
    "correct": "Bir mablag‘ni ikki marta ishlatish",
    "wrong": [
        "Ikki karta ishlatish",
        "Ikki monitor ulash",
        "Ikki parol kiritish"
    ]
},
{
    "question": "Kriptovalyutada tranzaksiyani amalga oshirish huquqi kimga tegishli?",
    "correct": "Yopiq kalit egasiga",
    "wrong": [
        "Faqat bankka",
        "Davlatga",
        "Internet provayderga"
    ]
},
{
    "question": "Kriptovalyutada anonimlik nimaga asoslanadi?",
    "correct": "Manzillar va kalitlarga",
    "wrong": [
        "Passportga",
        "Telefon raqamiga",
        "SIM kartaga"
    ]
},
{
    "question": "Blokcheyn 3.0 asosiy qo‘llanish sohasi qaysi?",
    "correct": "Davlat va biznes tizimlari",
    "wrong": [
        "Faqat o‘yinlar",
        "Video montaj",
        "Foto muharriri"
    ]
},
{
    "question": "Konsorsium blokcheynning asosiy xususiyati nima?",
    "correct": "Bir nechta tashkilot tomonidan boshqarilishi",
    "wrong": [
        "Faqat bitta foydalanuvchi ishlatishi",
        "Internetga ulanmasligi",
        "Faqat telefonlarda ishlashi"
    ]
},
{
    "question": "Kriptovalyutada tranzaksiyani bekor qilish nima uchun deyarli imkonsiz?",
    "correct": "Blokcheyn o‘zgarmasligi sababli",
    "wrong": [
        "Telefon o‘chib qolishi",
        "Printer ishlamasligi",
        "Brauzer yopilishi"
    ]
},
{
    "question": "Ochiq blokcheynda konsensus mexanizmining vazifasi nima?",
    "correct": "Tranzaksiyalarni tasdiqlash",
    "wrong": [
        "Rasm saqlash",
        "Video yuklash",
        "Musiqa tinglash"
    ]
},
{
    "question": "Kriptovalyuta kursining o‘zgarishi nimaga bog‘liq?",
    "correct": "Talab va taklifga",
    "wrong": [
        "Faqat ob-havoga",
        "Monitor hajmiga",
        "Printer tezligiga"
    ]
},
{
    "question": "Ikki martalik sarf-xarajatlar muammosini markazlashgan tizim qanday hal qiladi?",
    "correct": "Markaziy nazorat orqali",
    "wrong": [
        "Bluetooth orqali",
        "Wi-Fi o‘chirib",
        "Kamera yordamida"
    ]
},
{
    "question": "Bitkoin tizimida minimal uzatiladigan qiymat nima deb ataladi?",
    "correct": "Satoshi",
    "wrong": [
        "Dollar",
        "TokenX",
        "MiniCoin"
    ]
},
{
    "question": "Kriptovalyutaning inflyatsiyaga kam bog‘liqligi nimaga asoslanadi?",
    "correct": "Cheklangan emissiyaga",
    "wrong": [
        "Printer mavjudligiga",
        "Internet tezligiga",
        "Monitor sifatiga"
    ]
},
{
    "question": "Elliptik egri chiziq tenglamasi qanday ko‘rinishda beriladi?",
    "correct": "y² = x³ + ax + b",
    "wrong": [
        "x + y = z",
        "a² + b² = c²",
        "x² + y² = r²"
    ]
},
{
    "question": "Elliptik egri chiziqda diskriminant qanday shartni qanoatlantirishi kerak?",
    "correct": "0 ga teng bo‘lmasligi kerak",
    "wrong": [
        "1 ga teng bo‘lishi kerak",
        "Faqat musbat bo‘lishi kerak",
        "Faqat juft son bo‘lishi kerak"
    ]
},
{
    "question": "Elliptik egri chiziqda 0 nuqta nimani anglatadi?",
    "correct": "Cheksizlik nuqtasi",
    "wrong": [
        "Boshlang‘ich nuqta",
        "Markaz nuqtasi",
        "Koordinata boshi"
    ]
},
{
    "question": "P nuqtaning qarama-qarshi nuqtasi qanday olinadi?",
    "correct": "y koordinatasini teskarilash orqali",
    "wrong": [
        "x ni 0 qilish orqali",
        "Nuqtani o‘chirish orqali",
        "Faqat aylantirish orqali"
    ]
},
{
    "question": "P+Q+R=0 sharti qachon bajariladi?",
    "correct": "Nuqtalar bir chiziqda yotsa",
    "wrong": [
        "Nuqtalar teng bo‘lsa",
        "Faqat ikkita nuqta bo‘lsa",
        "Doira ichida bo‘lsa"
    ]
},
{
    "question": "P+0 ning qiymati nima?",
    "correct": "P",
    "wrong": [
        "0",
        "Q",
        "1"
    ]
},
{
    "question": "Agar P = −Q bo‘lsa, P+Q nima bo‘ladi?",
    "correct": "0 nuqta",
    "wrong": [
        "P",
        "Q",
        "1"
    ]
},
{
    "question": "Skalyar ko‘paytirish nima?",
    "correct": "Nuqtani o‘ziga bir necha marta qo‘shish",
    "wrong": [
        "Nuqtani bo‘lish",
        "Faqat x ni o‘zgartirish",
        "Grafik chizish"
    ]
},
{
    "question": "Chekli maydon qanday belgilanadi?",
    "correct": "Fp",
    "wrong": [
        "R2",
        "ABC",
        "XY"
    ]
},
{
    "question": "Modulyar qo‘shish misoli: (18+9) mod 23 = ?",
    "correct": "4",
    "wrong": [
        "5",
        "23",
        "27"
    ]
},
{
    "question": "Multiplikativ inversiya nima?",
    "correct": "Songa teskari element",
    "wrong": [
        "Kvadrat ildiz",
        "Oddiy qo‘shish",
        "Ikki baravar oshirish"
    ]
},
{
    "question": "SECP256k1 egri chizig‘i tenglamasi qanday?",
    "correct": "y² = x³ + 7",
    "wrong": [
        "x² + y² = 1",
        "y = mx + b",
        "a² + b² = c²"
    ]
},
{
    "question": "Ochiq kalit qanday hosil qilinadi?",
    "correct": "Yopiq kalitdan hisoblab",
    "wrong": [
        "Parol yozib",
        "Internetdan yuklab",
        "Tasodifiy rasm orqali"
    ]
},
{
    "question": "ECDSA nimaga xizmat qiladi?",
    "correct": "Raqamli imzo yaratishga",
    "wrong": [
        "Video montaj qilishga",
        "O‘yin o‘ynashga",
        "Rasm tahrirlashga"
    ]
},
{
    "question": "Yopiq kalit qanday bo‘ladi?",
    "correct": "Maxfiy saqlanadi",
    "wrong": [
        "Hammaga ochiq",
        "Faqat printerda bo‘ladi",
        "Brauzerga bog‘liq"
    ]
},
{
    "question": "Base58Check kodirovkasi nima uchun ishlatiladi?",
    "correct": "Manzil yaratish uchun",
    "wrong": [
        "Video siqish uchun",
        "Rasm chizish uchun",
        "Internet tezlatish uchun"
    ]
},
{
    "question": "Base58 da qaysi belgilar olib tashlangan?",
    "correct": "O‘xshash belgilar",
    "wrong": [
        "Faqat raqamlar",
        "Faqat unli harflar",
        "Barcha katta harflar"
    ]
},
{
    "question": "Checksum qanday hisoblanadi?",
    "correct": "Ikki marta xeshlash orqali",
    "wrong": [
        "Qo‘shish orqali",
        "Bo‘lish orqali",
        "Rasm aylantirish orqali"
    ]
},
{
    "question": "Hamyon manzili nimadan olinadi?",
    "correct": "Ochiq kalitdan",
    "wrong": [
        "Telefon raqamidan",
        "Paroldan",
        "Emaildan"
    ]
},
{
    "question": "Ochiq kalitni manzilga o‘girishda qaysi xesh ishlatiladi?",
    "correct": "SHA-256 va RIPEMD-160",
    "wrong": [
        "MD5",
        "CRC32",
        "AES"
    ]
},
{
    "question": "Elliptik egri chiziq Abel gruppasi ekanligini nima isbotlaydi?",
    "correct": "Qo‘shish amalining xossalari",
    "wrong": [
        "Printer tezligi",
        "Internet sifati",
        "Grafik karta"
    ]
},
{
    "question": "Geometrik qo‘shishda P+Q qanday aniqlanadi?",
    "correct": "Kesishgan nuqta orqali",
    "wrong": [
        "Tasodifiy son bilan",
        "Faqat x koordinata bilan",
        "Monitor yordamida"
    ]
},
{
    "question": "P=Q bo‘lganda m qanday topiladi?",
    "correct": "Hosila formulasi orqali",
    "wrong": [
        "Oddiy ayirish orqali",
        "Rasm chizish orqali",
        "Faqat taxmin bilan"
    ]
},
{
    "question": "Skalyar ko‘paytirishda “double and add” usuli nimani anglatadi?",
    "correct": "Ikki baravar oshirib qo‘shish",
    "wrong": [
        "Faqat ayirish",
        "Faqat ko‘paytirish",
        "Faqat bo‘lish"
    ]
},
{
    "question": "Fp maydonda elementlar oralig‘i qanday?",
    "correct": "0 dan p−1 gacha",
    "wrong": [
        "1 dan cheksizgacha",
        "Faqat juft sonlar",
        "Faqat manfiy sonlar"
    ]
},
{
    "question": "Bo‘lish amali qanday bajariladi?",
    "correct": "Teskari element orqali",
    "wrong": [
        "Oddiy kalkulyator bilan",
        "Faqat qo‘shish bilan",
        "Grafik yordamida"
    ]
},
{
    "question": "Multiplikativ inversiya qanday topiladi?",
    "correct": "Kengaytirilgan Evklid algoritmi orqali",
    "wrong": [
        "Rasm chizish orqali",
        "Faqat taxmin bilan",
        "Monitor orqali"
    ]
},
{
    "question": "SECP256k1 dagi p son qanday?",
    "correct": "Katta tub son",
    "wrong": [
        "Manfiy son",
        "Kasr son",
        "Tasodifiy harf"
    ]
},
{
    "question": "Generator nuqta G nimaga kerak?",
    "correct": "Kalitlar hosil qilish uchun",
    "wrong": [
        "Video yuklash uchun",
        "Rasm chizish uchun",
        "Printer boshqarish uchun"
    ]
},
{
    "question": "Nega ochiq kalitdan yopiq kalitni topish qiyin?",
    "correct": "Diskret logarifm muammosi sababli",
    "wrong": [
        "Internet sekinligi sababli",
        "Monitor sifati sababli",
        "Printer ishlamagani sababli"
    ]
},
{
    "question": "ECDSA imzosi nechta sondan iborat?",
    "correct": "2 ta",
    "wrong": [
        "1 ta",
        "4 ta",
        "10 ta"
    ]
},
{
    "question": "Base58Check da nol baytlar qanday ifodalanadi?",
    "correct": "1 belgisi bilan",
    "wrong": [
        "0 belgisi bilan",
        "A harfi bilan",
        "Bo‘sh joy bilan"
    ]
},
{
    "question": "Base58Check checksum qayerga qo‘shiladi?",
    "correct": "Oxiriga",
    "wrong": [
        "Boshiga",
        "O‘rtasiga",
        "Tasodifiy joyga"
    ]
},
{
    "question": "Siqilgan ochiq kalitda qaysi koordinata yoziladi?",
    "correct": "x koordinata",
    "wrong": [
        "y koordinata",
        "Faqat z koordinata",
        "Hech biri"
    ]
},
{
    "question": "0x02 prefiksi nimani bildiradi?",
    "correct": "y juft ekanini",
    "wrong": [
        "x manfiyligini",
        "Kalit noto‘g‘riligini",
        "Internet yo‘qligini"
    ]
},
{
    "question": "0x03 prefiksi nimani bildiradi?",
    "correct": "y toq ekanini",
    "wrong": [
        "x juft ekanini",
        "Kalit o‘chganini",
        "Monitor ishlashini"
    ]
},
{
    "question": "Hamyon manzilini hisoblashda nechta xesh ishlatiladi?",
    "correct": "2 ta",
    "wrong": [
        "1 ta",
        "5 ta",
        "10 ta"
    ]
},
{
    "question": "Base58Check ning asosiy maqsadi nima?",
    "correct": "Xatolarni kamaytirish",
    "wrong": [
        "Internetni tezlatish",
        "Video siqish",
        "Grafika yaratish"
    ]
},
{
    "question": "Skalyar ko‘paytirishda sikliklik nimani bildiradi?",
    "correct": "Nuqtalar takrorlanishini",
    "wrong": [
        "Internet aylanishini",
        "Rasm o‘zgarishini",
        "Printer ishlashini"
    ]
},
{
    "question": "kP = (k mod n)P xossasi nimani anglatadi?",
    "correct": "Siklik guruh mavjudligini",
    "wrong": [
        "Internet tezligini",
        "Monitor hajmini",
        "Parol uzunligini"
    ]
},
{
    "question": "Bitkoinda balans qanday aniqlanadi?",
    "correct": "UTXO lar yig‘indisi orqali",
    "wrong": [
        "Bank hisobi orqali",
        "Faqat kalkulyator bilan",
        "Telefon raqami bilan"
    ]
},
{
    "question": "Tranzaksiya qanday imzolanadi?",
    "correct": "Yopiq kalit bilan",
    "wrong": [
        "Ochiq kalit bilan",
        "Telefon orqali",
        "Printer yordamida"
    ]
},
{
    "question": "Tranzaksiya tarmoqqa qanday uzatiladi?",
    "correct": "Peer-to-peer uzellar orqali",
    "wrong": [
        "Faqat email bilan",
        "USB kabel bilan",
        "Bluetooth orqali"
    ]
},
{
    "question": "Tranzaksiyada input nima?",
    "correct": "Oldingi chiqishga havola",
    "wrong": [
        "Yangi blok",
        "Video fayl",
        "Monitor nomi"
    ]
},
{
    "question": "Tranzaksiyada output nima?",
    "correct": "Yangi egaga yuborilgan qiymat",
    "wrong": [
        "Printer javobi",
        "Internet tezligi",
        "Grafik fayl"
    ]
},
{
    "question": "Komissiya qanday hisoblanadi?",
    "correct": "Input va output farqi orqali",
    "wrong": [
        "Faqat blok soni bilan",
        "Rasm hajmi bilan",
        "Monitor sifati bilan"
    ]
},
{
    "question": "UTXO nima?",
    "correct": "Sarflanmagan tranzaksiya chiqishi",
    "wrong": [
        "Yangi blok turi",
        "Internet protokoli",
        "Grafik dastur"
    ]
},
{
        "question": "Bir output necha marta ishlatiladi?",
        "correct": "Faqat bir marta",
        "wrong": [
            "Cheksiz marta",
            "10 marta",
            "2 marta"
        ]
},
{
        "question": "Script qanday til?",
        "correct": "Stack asosidagi til",
        "wrong": [
            "Grafik til",
            "Sun’iy intellekt tili",
            "Operatsion tizim"
        ]
},
{
        "question": "Tranzaksiya qachon tasdiqlangan hisoblanadi?",
        "correct": "Blokka qo‘shilganda",
        "wrong": [
            "Yozilganda",
            "Ochilganda",
            "Internet uzilganda"
        ]
},
{
        "question": "Nega Bitkoinda umumiy balans jadvali mavjud emas?",
        "correct": "UTXO modeli ishlatilgani uchun",
        "wrong": [
            "Server yo‘qligi uchun",
            "Internet sustligi uchun",
            "GPU yetishmasligi uchun"
        ]
},
{
        "question": "Nima sababdan yuqori komissiya tezroq tasdiqlanishga olib keladi?",
        "correct": "Maynerlar foydaliroq tranzaksiyani tanlaydi",
        "wrong": [
            "Internet tezlashadi",
            "Blok hajmi kattalashadi",
            "Hash kamayadi"
        ]
},
{
        "question": "UTXO modelining afzalligi nimada?",
        "correct": "Parallel tekshiruv imkoniyati",
        "wrong": [
            "Internetni tezlashtiradi",
            "Grafikani yaxshilaydi",
            "Fayl hajmini oshiradi"
        ]
},
{
        "question": "ScriptSig va ScriptPubKey kombinatsiyasi nima qiladi?",
        "correct": "Tranzaksiyani tekshiradi",
        "wrong": [
            "Blok yaratadi",
            "Internet ulaydi",
            "Hashni o‘chiradi"
        ]
},
{
        "question": "Skript bajarilgandan keyin TRUE chiqsa nima bo‘ladi?",
        "correct": "Tranzaksiya haqiqiy hisoblanadi",
        "wrong": [
            "Blok o‘chadi",
            "Internet uziladi",
            "Kalit almashtiriladi"
        ]
},
{
        "question": "P2PKH skriptining asosiy vazifasi nima?",
        "correct": "Ochiq kalit xeshini tekshirish",
        "wrong": [
            "Blok qazish",
            "Server yaratish",
            "Hashni o‘zgartirish"
        ]
},
{
        "question": "OP_DUP nima qiladi?",
        "correct": "Stackdagi elementni nusxalaydi",
        "wrong": [
            "Blokni o‘chiradi",
            "Internetni uzadi",
            "Kalit yaratadi"
        ]
},
{
        "question": "OP_HASH160 qanday amal bajaradi?",
        "correct": "SHA-256 va RIPEMD-160 xeshi",
        "wrong": [
            "AES shifrlash",
            "RSA imzolash",
            "PNG siqish"
        ]
},
{
        "question": "OP_RETURN nima uchun ishlatiladi?",
        "correct": "Ma’lumot yozish uchun",
        "wrong": [
            "Blok qazish uchun",
            "Internet ulash uchun",
            "GPU boshqarish uchun"
        ]
},
{
        "question": "OP_RETURN bilan yozilgan chiqish qanday?",
        "correct": "Sarflanmaydigan",
        "wrong": [
            "Cheksiz",
            "Ikki martalik",
            "Shifrlangan"
        ]
},
{
        "question": "Bitkoin tarmog‘i qanday turdagi tarmoq?",
        "correct": "P2P tarmoq",
        "wrong": [
            "Markaziy tarmoq",
            "LAN printer tarmog‘i",
            "Bluetooth tarmog‘i"
        ]
},
{
        "question": "To‘liq uzel (full node) nima qiladi?",
        "correct": "Butun blokcheynni saqlaydi va tekshiradi",
        "wrong": [
            "Faqat internet ulaydi",
            "Grafika chizadi",
            "GPU sovutadi"
        ]
},
{
        "question": "SPV uzel qanday vazifani bajaradi?",
        "correct": "Faqat blok sarlavhalarini tekshiradi",
        "wrong": [
            "ASIC ishlab chiqaradi",
            "Serverni formatlaydi",
            "GPU tezlashtiradi"
        ]
},
{
        "question": "Version xabarining vazifasi nima?",
        "correct": "Uzel haqida ma’lumot almashish",
        "wrong": [
            "Blokni o‘chirish",
            "Hashni kamaytirish",
            "Kalit yaratish"
        ]
},
{
        "question": "Verack xabari nima qiladi?",
        "correct": "Ulanishni tasdiqlaydi",
        "wrong": [
            "Blok qaziydi",
            "GPU yoqadi",
            "Internet uzadi"
        ]
},
{
        "question": "Inv xabari nima uchun ishlatiladi?",
        "correct": "Yangi obyekt haqida xabar berish",
        "wrong": [
            "Serverni o‘chirish",
            "Disk formatlash",
            "Grafik yaratish"
        ]
},
{
        "question": "Getdata xabari nimani qiladi?",
        "correct": "Ma’lumot so‘raydi",
        "wrong": [
            "Blok yaratadi",
            "Hashni yashiradi",
            "GPU boshqaradi"
        ]
},
{
        "question": "Bitkoin uchun standart port qaysi?",
        "correct": "8333",
        "wrong": [
            "80",
            "21",
            "443"
        ]
},
{
        "question": "Getaddr xabari nima uchun ishlatiladi?",
        "correct": "Uzel manzillarini so‘rash uchun",
        "wrong": [
            "GPU ulash uchun",
            "Hashni o‘chirish uchun",
            "Server formatlash uchun"
        ]
},
{
        "question": "Addr xabari nimani qaytaradi?",
        "correct": "Uzel manzillarini",
        "wrong": [
            "Blok mukofotini",
            "Hash qiymatini",
            "GPU modelini"
        ]
},
{
        "question": "Bitkoin tarmog‘ining markazlashmaganligi nimani anglatadi?",
        "correct": "Bitta boshqaruvchi yo‘qligini",
        "wrong": [
            "Internet yo‘qligini",
            "GPU ishlamasligini",
            "Hash mavjud emasligini"
        ]
},
{
        "question": "Uzellar qanday qilib bir-birini topadi?",
        "correct": "Peer discovery orqali",
        "wrong": [
            "Printer orqali",
            "Bluetooth orqali",
            "USB orqali"
        ]
},
{
    "question": "Version va Verack almashinuvi nimani ta’minlaydi?",
    "correct": "Ulanishni o‘rnatishni",
    "wrong": [
        "Blokni yo‘qotishni",
        "GPU o‘chishini",
        "Hash kamayishini"
    ]
},
{
    "question": "Xabar formati qanday tuzilgan?",
    "correct": "Header va payload qismlaridan",
    "wrong": [
        "Faqat grafikadan",
        "Faqat videodan",
        "Faqat rasmdan"
    ]
},
{
    "question": "Getblocks xabari nima qaytaradi?",
    "correct": "Blok xeshlarini",
    "wrong": [
        "GPU ro‘yxatini",
        "Internet tezligini",
        "Monitor nomini"
    ]
},
{
    "question": "Headers xabari nima beradi?",
    "correct": "Blok sarlavhalarini",
    "wrong": [
        "To‘liq videolarni",
        "Grafik fayllarni",
        "GPU hashini"
    ]
},
{
    "question": "Nima sababdan sarlavhalar-birinchi usul tezroq?",
    "correct": "Kamroq ma’lumot uzatiladi",
    "wrong": [
        "GPU kuchliroq bo‘ladi",
        "Internet o‘chadi",
        "Disk to‘ladi"
    ]
},
{
    "question": "Tx xabari nimani bildiradi?",
    "correct": "Tranzaksiya ma’lumotini",
    "wrong": [
        "Blok mukofotini",
        "GPU modelini",
        "Operatsion tizimni"
    ]
},
{
    "question": "Reject xabari qachon keladi?",
    "correct": "Xato yoki noto‘g‘ri obyekt bo‘lsa",
    "wrong": [
        "Internet tezlashganda",
        "GPU qiziganda",
        "Monitor o‘chganda"
    ]
},
{
    "question": "Inv xabaridagi TYPE = MSG_BLOCK nimani bildiradi?",
    "correct": "Blok mavjudligini",
    "wrong": [
        "GPU mavjudligini",
        "Internet uzilganini",
        "Hash yo‘qligini"
    ]
},
{
    "question": "Blokcheyn nimaga o‘xshatiladi?",
    "correct": "Bog‘langan bloklar zanjiriga",
    "wrong": [
        "Grafik kartaga",
        "Printerga",
        "Routerga"
    ]
},
{
    "question": "Bloklar qanday bog‘lanadi?",
    "correct": "Oldingi blok xeshi orqali",
    "wrong": [
        "USB orqali",
        "Bluetooth orqali",
        "Monitor orqali"
    ]
},
{
    "question": "Genesis block nima?",
    "correct": "Birinchi blok",
    "wrong": [
        "Oxirgi blok",
        "GPU bloki",
        "Server bloki"
    ]
},
{
    "question": "Blok sarlavhasi nechta asosiy maydondan iborat?",
    "correct": "6 ta",
    "wrong": [
        "2 ta",
        "10 ta",
        "15 ta"
    ]
},
{
    "question": "Merkle root nima?",
    "correct": "Tranzaksiyalar xeshining yakuniy xeshi",
    "wrong": [
        "GPU kodi",
        "Internet paroli",
        "Server nomi"
    ]
},
{
    "question": "Merkle daraxti qanday tuzilma?",
    "correct": "Xesh daraxti",
    "wrong": [
        "Grafik jadval",
        "Operatsion tizim",
        "Tarmoq kabeli"
    ]
},
{
    "question": "Merkle daraxtida nechta tranzaksiya bo‘lishi kerak?",
    "correct": "Kamida bitta",
    "wrong": [
        "Faqat 100 ta",
        "Faqat 2 ta",
        "Faqat juft son"
    ]
},
{
    "question": "SPV uzel nima qiladi?",
    "correct": "Sarlavhalar orqali tekshiradi",
    "wrong": [
        "GPU ishlab chiqaradi",
        "Server formatlaydi",
        "Monitor boshqaradi"
    ]
},
{
    "question": "SPV ning asosiy afzalligi nima?",
    "correct": "Kam xotira ishlatishi",
    "wrong": [
        "GPU tezligi",
        "Internet kuchayishi",
        "Disk hajmi oshishi"
    ]
},
{
    "question": "Authentication path nima?",
    "correct": "Merkle isbot yo‘li",
    "wrong": [
        "Internet yo‘li",
        "GPU kabeli",
        "Server manzili"
    ]
},
{
    "question": "Timestamp nimani bildiradi?",
    "correct": "Blok yaratilgan vaqtni",
    "wrong": [
        "GPU haroratini",
        "Disk hajmini",
        "Internet tezligini"
    ]
},
{
    "question": "Timestamp tekshirishning birinchi sharti nima?",
    "correct": "Oldingi blok vaqtidan katta bo‘lishi",
    "wrong": [
        "GPU dan kichik bo‘lishi",
        "Hashga teng bo‘lishi",
        "Disk bilan bog‘liq bo‘lishi"
    ]
},
{
    "question": "Timestamp tekshirishning ikkinchi sharti nima?",
    "correct": "Kelajakdan juda oldinda bo‘lmasligi",
    "wrong": [
        "GPU bilan teng bo‘lishi",
        "Diskni to‘ldirishi",
        "Monitorni yoqishi"
    ]
},
{
    "question": "Blokni aniqlash uchun qaysi qiymat ishlatiladi?",
    "correct": "Blok xeshi",
    "wrong": [
        "GPU kodi",
        "Internet nomi",
        "Server hajmi"
    ]
},
{
    "question": "Nega blokcheynni o‘zgartirish qiyin?",
    "correct": "Har blok keyingi blok bilan bog‘langan",
    "wrong": [
        "GPU yo‘qligi uchun",
        "Internet sustligi uchun",
        "Disk kichikligi uchun"
    ]
},
{
    "question": "Merkle root o‘zgarsa nima bo‘ladi?",
    "correct": "Blok xeshi ham o‘zgaradi",
    "wrong": [
        "GPU kuyadi",
        "Monitor o‘chadi",
        "Internet yo‘qoladi"
    ]
},
{
    "question": "Nega oddiy xesh o‘rniga Merkle daraxti ishlatiladi?",
    "correct": "Tekshiruvni tezlashtirish uchun",
    "wrong": [
        "GPU ni sovutish uchun",
        "Diskni tozalash uchun",
        "Internetni uzish uchun"
    ]
},
{
    "question": "SPV qanday ishlaydi?",
    "correct": "Merkle proof orqali",
    "wrong": [
        "GPU orqali",
        "Bluetooth orqali",
        "Printer orqali"
    ]
},
{
    "question": "Authentication path nimani isbotlaydi?",
    "correct": "Tranzaksiya blok ichida ekanini",
    "wrong": [
        "GPU mavjudligini",
        "Internet tezligini",
        "Monitor sifatini"
    ]
},
{
    "question": "Nega tranzaksiya o‘zgarsa darhol aniqlanadi?",
    "correct": "Xesh qiymati o‘zgaradi",
    "wrong": [
        "GPU o‘chadi",
        "Disk kamayadi",
        "Printer ishlaydi"
    ]
},
{
    "question": "Timestamp kichik bo‘lishi mumkinmi?",
    "correct": "Ha, lekin cheklov bilan",
    "wrong": [
        "Yo‘q, hech qachon",
        "Faqat GPUda",
        "Faqat serverda"
    ]
},
{
    "question": "Nega turli kompyuterlarda vaqt farq qiladi?",
    "correct": "Soat sinxron emasligi sababli",
    "wrong": [
        "GPU kuchsizligi sababli",
        "Disk hajmi sababli",
        "Printer tufayli"
    ]
},
{
    "question": "Network adjusted time nima?",
    "correct": "Tarmoq bo‘yicha o‘rtacha vaqt",
    "wrong": [
        "GPU vaqti",
        "Disk tezligi",
        "Monitor chastotasi"
    ]
},
{
    "question": "Merkle daraxtida elementlar toq bo‘lsa nima qilinadi?",
    "correct": "Oxirgisi takrorlanadi",
    "wrong": [
        "O‘chirib yuboriladi",
        "GPUga yuboriladi",
        "Internetga yoziladi"
    ]
},
{
    "question": "Blok sarlavhasi nima uchun muhim?",
    "correct": "Blokni tekshirish uchun",
    "wrong": [
        "Grafika uchun",
        "Printer uchun",
        "Monitor uchun"
    ]
},
{
    "question": "Nega SPV mobil qurilmalarga mos?",
    "correct": "Kam resurs ishlatadi",
    "wrong": [
        "GPU kuchli bo‘ladi",
        "Diskni kengaytiradi",
        "Printer qo‘shadi"
    ]
},
{
    "question": "Blokni tekshirishda qaysi amal bajariladi?",
    "correct": "Xeshlash",
    "wrong": [
        "Formatlash",
        "Chop etish",
        "Animatsiya yaratish"
    ]
},
{
    "question": "Blokdagi tranzaksiya o‘zgartirilsa nima bo‘ladi?",
    "correct": "Merkle root o‘zgaradi",
    "wrong": [
        "GPU yonadi",
        "Monitor sinadi",
        "Disk o‘chadi"
    ]
},
{
    "question": "Getdata xabarida qanday tur ko‘rsatiladi?",
    "correct": "So‘ralayotgan obyekt turi",
    "wrong": [
        "GPU modeli",
        "Internet nomi",
        "Printer turi"
    ]
},
{
    "question": "Mayning nima?",
    "correct": "Yangi blok yaratish jarayoni",
    "wrong": [
        "Internet ulash",
        "Grafika chizish",
        "Disk tozalash"
    ]
},
{
    "question": "Mayningning asosiy maqsadlaridan biri nima?",
    "correct": "Tarmoq xavfsizligini ta’minlash",
    "wrong": [
        "GPU sotish",
        "Monitor ishlab chiqarish",
        "Printer ulash"
    ]
},
{
    "question": "Bitkoinda maksimal tanga soni qancha?",
    "correct": "21 million",
    "wrong": [
        "100 million",
        "1 milliard",
        "50 million"
    ]
},
{
    "question": "Blok mukofoti qanday o‘zgaradi?",
    "correct": "Vaqt o‘tishi bilan kamayadi",
    "wrong": [
        "Doim oshadi",
        "O‘zgarmaydi",
        "Tasodifiy bo‘ladi"
    ]
},
{
    "question": "PoW nimani anglatadi?",
    "correct": "Proof of Work",
    "wrong": [
        "Power of Web",
        "Proof of Wallet",
        "Packet of Work"
    ]
},
{
    "question": "Nonce nima?",
    "correct": "Xesh topish uchun o‘zgartiriladigan son",
    "wrong": [
        "GPU turi",
        "Internet kodi",
        "Monitor hajmi"
    ]
},
{
    "question": "Blok topish uchun o‘rtacha vaqt qancha?",
    "correct": "10 daqiqa",
    "wrong": [
        "1 soniya",
        "1 soat",
        "24 soat"
    ]
},
{
    "question": "Target nima?",
    "correct": "Topilishi kerak bo‘lgan maksimal xesh qiymati",
    "wrong": [
        "GPU tezligi",
        "Internet hajmi",
        "Disk formati"
    ]
},
{
    "question": "Difficulty nima?",
    "correct": "Mayning qiyinlik darajasi",
    "wrong": [
        "GPU narxi",
        "Monitor hajmi",
        "Printer sifati"
    ]
},
{
    "question": "Coinbase tranzaksiyasi nima?",
    "correct": "Mayner mukofoti tranzaksiyasi",
    "wrong": [
        "Bank kartasi",
        "Internet protokoli",
        "Grafik fayl"
    ]
},
{
    "question": "Blokdagi birinchi tranzaksiya nima?",
    "correct": "Coinbase tranzaksiyasi",
    "wrong": [
        "P2P tranzaksiya",
        "Hash tranzaksiya",
        "GPU tranzaksiya"
    ]
},
{
    "question": "Blok hajmi qancha?",
    "correct": "Taxminan 1 MB",
    "wrong": [
        "100 MB",
        "10 GB",
        "500 KB"
    ]
},
{
    "question": "Tranzaksiyalar qanday saralanadi?",
    "correct": "Komissiyaga qarab",
    "wrong": [
        "GPU rangiga qarab",
        "Monitor hajmiga qarab",
        "Printer modeliga qarab"
    ]
},
{
    "question": "Mayning qiyinligi qachon o‘zgaradi?",
    "correct": "Har 2016 blokdan keyin",
    "wrong": [
        "Har blokda",
        "Har soatda",
        "Har yilda"
    ]
},
{
    "question": "Fork nima?",
    "correct": "Blokcheynning bo‘linishi",
    "wrong": [
        "GPU turi",
        "Internet uzilishi",
        "Printer xatosi"
    ]
},
{
    "question": "Nega mayning zarur?",
    "correct": "Tarmoqni himoya qilish uchun",
    "wrong": [
        "Monitor ishlashi uchun",
        "Disk to‘lishi uchun",
        "Printer ulanishi uchun"
    ]
},
{
    "question": "Nega blok yaratish qiyin?",
    "correct": "Mos xesh topish kerakligi uchun",
    "wrong": [
        "GPU yo‘qligi uchun",
        "Internet sustligi uchun",
        "Monitor kichikligi uchun"
    ]
},
{
    "question": "Nega blok tekshirish oson?",
    "correct": "Xeshni qayta hisoblash kifoya",
    "wrong": [
        "GPU almashtiriladi",
        "Disk formatlanadi",
        "Printer o‘chadi"
    ]
},
{
    "question": "Nega target kichik bo‘lsa qiyinlik oshadi?",
    "correct": "Mos xesh topish ehtimoli kamayadi",
    "wrong": [
        "GPU kuchayadi",
        "Internet tezlashadi",
        "Disk kattalashadi"
    ]
},
{
    "question": "Nega ko‘p mayner bo‘lsa qiyinlik oshadi?",
    "correct": "Blok tez topila boshlaydi",
    "wrong": [
        "GPU kamayadi",
        "Printer ishlamaydi",
        "Monitor o‘chadi"
    ]
},
{
    "question": "Difficulty qanday hisoblanadi?",
    "correct": "Target orqali",
    "wrong": [
        "GPU orqali",
        "Internet orqali",
        "Printer orqali"
    ]
},
{
    "question": "Nega coinbase tranzaksiyasi UTXO ishlatmaydi?",
    "correct": "Yangi tanga yaratgani uchun",
    "wrong": [
        "GPU ishlatgani uchun",
        "Internet uzilgani uchun",
        "Disk to‘lgani uchun"
    ]
},
{
    "question": "Extra nonce nima uchun kerak?",
    "correct": "Qo‘shimcha xesh variantlari uchun",
    "wrong": [
        "Monitor yoqish uchun",
        "Printer ulash uchun",
        "Internet o‘chirish uchun"
    ]
},
{
    "question": "Nega CPU/GPU mayning foydasiz?",
    "correct": "ASIC qurilmalar kuchliroq bo‘lgani uchun",
    "wrong": [
        "Internet yo‘qligi uchun",
        "Disk kichikligi uchun",
        "Printer ishlamagani uchun"
    ]
},
{
    "question": "ASIC qurilma nima?",
    "correct": "Maxsus mayning qurilmasi",
    "wrong": [
        "Operatsion tizim",
        "Internet protokoli",
        "Grafik fayl"
    ]
},
{
    "question": "Fork paytida qaysi zanjir tanlanadi?",
    "correct": "Eng uzun zanjir",
    "wrong": [
        "Eng qisqa zanjir",
        "Birinchi zanjir",
        "Tasodifiy zanjir"
    ]
},
{
    "question": "Nega forklar vaqtinchalik?",
    "correct": "Tarmoq bitta zanjirni tanlaydi",
    "wrong": [
        "GPU o‘chadi",
        "Disk to‘ladi",
        "Printer ishlaydi"
    ]
},
{
    "question": "Nega komissiya muhim?",
    "correct": "Maynerlarga rag‘bat beradi",
    "wrong": [
        "Monitorni kuchaytiradi",
        "Printerni sovutadi",
        "Diskni kengaytiradi"
    ]
},
{
    "question": "Nega bloklar 10 daqiqada chiqadi?",
    "correct": "Tarmoq barqarorligi uchun",
    "wrong": [
        "GPU dam olishi uchun",
        "Printer ishlashi uchun",
        "Monitor yonishi uchun"
    ]
},
{
    "question": "Nega mayning xavfsizlikni oshiradi?",
    "correct": "Hujumni juda qimmat qiladi",
    "wrong": [
        "Internetni uzadi",
        "Diskni tozalaydi",
        "Printerni bloklaydi"
    ]
},
{
    "question": "Efirium nima?",
    "correct": "Smart shartnomali blokcheyn platforma",
    "wrong": [
        "GPU modeli",
        "Internet brauzeri",
        "Printer turi"
    ]
},
{
    "question": "Efiriumdagi valyuta qanday nomlanadi?",
    "correct": "Ether",
    "wrong": [
        "Bitcoin",
        "Litecoin",
        "Hashcoin"
    ]
},
{
    "question": "Efirium asosiy imkoniyati nima?",
    "correct": "Smart shartnomalar ishlatish",
    "wrong": [
        "Printer boshqarish",
        "Disk formatlash",
        "GPU sovutish"
    ]
},
{
    "question": "Efirium blokcheyni nimaga o‘xshatiladi?",
    "correct": "Global kompyuterga",
    "wrong": [
        "Printerga",
        "Routerga",
        "Monitorga"
    ]
},
{
    "question": "Xeshlash nima beradi?",
    "correct": "Ma’lumot yaxlitligini",
    "wrong": [
        "GPU tezligini",
        "Monitor sifatini",
        "Printer rangini"
    ]
},
{
    "question": "Bitkoin qaysi avlod blokcheyni?",
    "correct": "1-avlod",
    "wrong": [
        "2-avlod",
        "3-avlod",
        "4-avlod"
    ]
},
{
    "question": "Efirium qaysi avlod blokcheyni?",
    "correct": "2-avlod",
    "wrong": [
        "1-avlod",
        "3-avlod",
        "4-avlod"
    ]
},
{
    "question": "EVM nima?",
    "correct": "Ethereum Virtual Machine",
    "wrong": [
        "Electronic Visual Monitor",
        "Ether Value Model",
        "External Video Memory"
    ]
},
{
    "question": "Smart shartnoma qaysi tilda yoziladi?",
    "correct": "Solidity",
    "wrong": [
        "HTML",
        "Photoshop",
        "Excel"
    ]
},
{
    "question": "Smart shartnoma nima?",
    "correct": "Avtomatik bajariluvchi kod",
    "wrong": [
        "Printer drayveri",
        "GPU dasturi",
        "Internet kabeli"
    ]
},
{
    "question": "DAO nima?",
    "correct": "Markazlashmagan avtonom tashkilot",
    "wrong": [
        "GPU kompaniyasi",
        "Internet provayderi",
        "Printer tizimi"
    ]
},
{
    "question": "Efirium Classic qanday paydo bo‘lgan?",
    "correct": "Hard fork natijasida",
    "wrong": [
        "GPU yangilanishidan",
        "Internet uzilishidan",
        "Printer xatosidan"
    ]
},
{
    "question": "Efirium blok vaqti qancha?",
    "correct": "Taxminan 12 soniya",
    "wrong": [
        "10 daqiqa",
        "1 soat",
        "30 daqiqa"
    ]
},
{
    "question": "Gas nima?",
    "correct": "Hisoblash narxi birligi",
    "wrong": [
        "GPU turi",
        "Internet kodi",
        "Printer dasturi"
    ]
},
{
    "question": "Gas nimaga bog‘liq?",
    "correct": "Operatsiya murakkabligiga",
    "wrong": [
        "Monitor hajmiga",
        "Disk rangiga",
        "Printer tezligiga"
    ]
},
{
    "question": "1 gwei nimaga teng?",
    "correct": "0.000000001 ETH",
    "wrong": [
        "1 ETH",
        "0.1 ETH",
        "10 ETH"
    ]
},
{
    "question": "ERC-20 nima?",
    "correct": "Token standarti",
    "wrong": [
        "GPU modeli",
        "Internet porti",
        "Printer kodi"
    ]
},
{
    "question": "PoS nimani anglatadi?",
    "correct": "Proof of Stake",
    "wrong": [
        "Power of System",
        "Packet of Stake",
        "Proof of Speed"
    ]
},
{
    "question": "Validator nima qiladi?",
    "correct": "Bloklarni tasdiqlaydi",
    "wrong": [
        "Printer ulaydi",
        "GPU ishlab chiqaradi",
        "Monitor sozlaydi"
    ]
},
{
    "question": "Sharding nima?",
    "correct": "Tarmoqni bo‘laklarga ajratish",
    "wrong": [
        "Disk formatlash",
        "Printer ulash",
        "GPU sovutish"
    ]
},
{
    "question": "Nega Efirium markazlashmagan?",
    "correct": "Ko‘plab uzellar ishlagani uchun",
    "wrong": [
        "GPU yo‘qligi uchun",
        "Printer ishlamagani uchun",
        "Disk kichikligi uchun"
    ]
},
{
    "question": "Nega smart shartnomalarni o‘zgartirib bo‘lmaydi?",
    "correct": "Blockchain’da saqlangani uchun",
    "wrong": [
        "GPU bloklagani uchun",
        "Monitor o‘chgani uchun",
        "Printer ishlamagani uchun"
    ]
},
{
    "question": "Nega Efirium Bitkoin dan moslashuvchan?",
    "correct": "Smart shartnomalarni qo‘llashi uchun",
    "wrong": [
        "GPU kuchliroq uchun",
        "Disk kattaroq uchun",
        "Printer tezroq uchun"
    ]
},
{
    "question": "Holat (state) nima?",
    "correct": "Hisoblar va ma’lumotlar holati",
    "wrong": [
        "GPU harorati",
        "Printer modeli",
        "Monitor o‘lchami"
    ]
},
{
    "question": "Nega gas kerak?",
    "correct": "Resurs ishlatilishini cheklash uchun",
    "wrong": [
        "GPU sovutish uchun",
        "Printer yoqish uchun",
        "Disk tozalash uchun"
    ]
},
{
    "question": "Gas tugasa nima bo‘ladi?",
    "correct": "Tranzaksiya bekor bo‘ladi",
    "wrong": [
        "GPU yonadi",
        "Monitor sinadi",
        "Internet yo‘qoladi"
    ]
},
{
    "question": "Validator bo‘lish uchun nima kerak?",
    "correct": "Stake qilish",
    "wrong": [
        "Printer sotib olish",
        "GPU o‘chirish",
        "Disk formatlash"
    ]
},
{
    "question": "Nega PoS energiya tejaydi?",
    "correct": "Mayning talab qilinmagani uchun",
    "wrong": [
        "GPU kuchsizligi uchun",
        "Monitor o‘chishi uchun",
        "Printer ishlamagani uchun"
    ]
},
{
    "question": "Nega sharding tezlikni oshiradi?",
    "correct": "Parallel ishlov berish sababli",
    "wrong": [
        "GPU kamayishi sababli",
        "Disk kichrayishi sababli",
        "Printer sekinlashishi sababli"
    ]
},
{
    "question": "Nega barcha uzellar hamma narsani hisoblamaydi?",
    "correct": "Yuklamani kamaytirish uchun",
    "wrong": [
        "GPU yo‘qligi uchun",
        "Printer ishlashi uchun",
        "Monitor kattaligi uchun"
    ]
},
{
    "question": "Notarius nima qiladi?",
    "correct": "Ma’lumotni tasdiqlaydi",
    "wrong": [
        "GPU sotadi",
        "Disk yaratadi",
        "Printer yig‘adi"
    ]
},
{
    "question": "Attestatsiya nima?",
    "correct": "Validator tasdig‘i",
    "wrong": [
        "GPU modeli",
        "Printer kodi",
        "Monitor dasturi"
    ]
},
{
    "question": "Nega 2/3 imzo kerak?",
    "correct": "Konsensus xavfsizligi uchun",
    "wrong": [
        "GPU ishlashi uchun",
        "Disk kengayishi uchun",
        "Printer ulanishi uchun"
    ]
},
{
    "question": "Beacon chain nima?",
    "correct": "PoS boshqaruv zanjiri",
    "wrong": [
        "GPU zanjiri",
        "Printer tarmog‘i",
        "Monitor tizimi"
    ]
},
{
    "question": "Nega DAO buzildi?",
    "correct": "Smart shartnoma zaifligi sababli",
    "wrong": [
        "GPU kuyishi sababli",
        "Disk to‘lishi sababli",
        "Printer sinishi sababli"
    ]
},
{
    "question": "Hard fork nima?",
    "correct": "Mos kelmaydigan protokol yangilanishi",
    "wrong": [
        "GPU modeli",
        "Printer drayveri",
        "Monitor turi"
    ]
},
{
    "question": "Nega Efirium tokenlari kerak?",
    "correct": "Tarmoq operatsiyalari uchun",
    "wrong": [
        "GPU sovutish uchun",
        "Disk tozalash uchun",
        "Printer ulash uchun"
    ]
},
{
    "question": "Nega gas narxi o‘zgaradi?",
    "correct": "Tarmoq yuklamasiga bog‘liq",
    "wrong": [
        "GPU rangiga bog‘liq",
        "Monitor o‘lchamiga bog‘liq",
        "Printer modeliga bog‘liq"
    ]
},
{
    "question": "Nega murakkab shartnoma ko‘proq gas talab qiladi?",
    "correct": "Ko‘proq hisoblash bajarilgani uchun",
    "wrong": [
        "GPU sustligi uchun",
        "Disk kichikligi uchun",
        "Printer ishlashi uchun"
    ]
},
{
    "question": "Nega PoS xavfsiz?",
    "correct": "Hujumchi katta stake yo‘qotadi",
    "wrong": [
        "GPU kuchli bo‘lgani uchun",
        "Monitor tezligi uchun",
        "Printer sifati uchun"
    ]
},
{
    "question": "Kriptobirja nima?",
    "correct": "Kriptovalyuta savdo platformasi",
    "wrong": [
        "GPU zavodi",
        "Internet kabeli",
        "Printer markazi"
    ]
},
{
    "question": "Kriptobirjaning asosiy funksiyasi nima?",
    "correct": "Kriptovalyuta almashish",
    "wrong": [
        "Disk formatlash",
        "GPU yig‘ish",
        "Printer boshqarish"
    ]
},
{
    "question": "KYC nima?",
    "correct": "Foydalanuvchini tasdiqlash jarayoni",
    "wrong": [
        "GPU kodi",
        "Printer turi",
        "Monitor tizimi"
    ]
},
{
    "question": "Depozit nima?",
    "correct": "Hisobga mablag‘ kiritish",
    "wrong": [
        "GPU sotish",
        "Disk tozalash",
        "Printer yoqish"
    ]
},
{
    "question": "Order book nima?",
    "correct": "Buyurtmalar ro‘yxati",
    "wrong": [
        "GPU katalogi",
        "Monitor jadvali",
        "Printer fayli"
    ]
},
{
    "question": "CEX nima?",
    "correct": "Markazlashgan birja",
    "wrong": [
        "GPU turi",
        "Internet porti",
        "Printer kodi"
    ]
},
{
    "question": "DEX nima?",
    "correct": "Markazlashmagan birja",
    "wrong": [
        "GPU modeli",
        "Disk dasturi",
        "Printer protokoli"
    ]
},
{
    "question": "CEXda kim boshqaradi?",
    "correct": "Markaziy kompaniya",
    "wrong": [
        "Validatorlar",
        "Printerlar",
        "GPUlar"
    ]
},
{
    "question": "DEXda boshqaruv qanday?",
    "correct": "Smart shartnomalar orqali",
    "wrong": [
        "Printer orqali",
        "GPU orqali",
        "Monitor orqali"
    ]
},
{
    "question": "Kriptobirjada komissiya qancha bo‘ladi?",
    "correct": "Birjaga bog‘liq",
    "wrong": [
        "Doim 50%",
        "Doim bepul",
        "Faqat 1 so‘m"
    ]
},
{
    "question": "Nega kriptobirjalar muhim?",
    "correct": "Savdo imkonini beradi",
    "wrong": [
        "Printer yaratadi",
        "GPU ishlab chiqaradi",
        "Disk formatlaydi"
    ]
},
{
    "question": "Nega DEX xavfsizroq hisoblanadi?",
    "correct": "Foydalanuvchi mablag‘ni o‘zi boshqaradi",
    "wrong": [
        "GPU kuchliroq",
        "Printer tezroq",
        "Monitor kattaroq"
    ]
},
{
    "question": "Nega CEX qulayroq?",
    "correct": "Interfeysi sodda",
    "wrong": [
        "GPU ishlatmaydi",
        "Printer qo‘shadi",
        "Diskni tozalaydi"
    ]
},
{
    "question": "KYC nimani ta’minlaydi?",
    "correct": "Foydalanuvchini aniqlashni",
    "wrong": [
        "GPU sovutishni",
        "Printer ishlashini",
        "Monitor ulanishini"
    ]
},
{
    "question": "Nega kriptobirjalarda xakerlik xavfi bor?",
    "correct": "Ko‘p mablag‘ saqlangani uchun",
    "wrong": [
        "GPU sustligi uchun",
        "Disk kichikligi uchun",
        "Printer ishlashi uchun"
    ]
},
{
    "question": "2FA nima uchun kerak?",
    "correct": "Qo‘shimcha himoya uchun",
    "wrong": [
        "GPU tezlashtirish uchun",
        "Printer ulash uchun",
        "Monitor yoqish uchun"
    ]
},
{
    "question": "Cold wallet nima?",
    "correct": "Internetga ulanmagan hamyon",
    "wrong": [
        "GPU qurilma",
        "Printer modeli",
        "Disk turi"
    ]
},
{
    "question": "Nega narx o‘zgaruvchan?",
    "correct": "Talab va taklif sababli",
    "wrong": [
        "GPU harorati sababli",
        "Printer rangi sababli",
        "Disk hajmi sababli"
    ]
},
{
    "question": "Phishing nima?",
    "correct": "Soxta ma’lumot bilan aldash",
    "wrong": [
        "GPU mayningi",
        "Printer ulash",
        "Disk formatlash"
    ]
},
{
    "question": "Nega ishonchli birja tanlash muhim?",
    "correct": "Mablag‘ xavfsizligi uchun",
    "wrong": [
        "GPU tezligi uchun",
        "Monitor sifati uchun",
        "Printer hajmi uchun"
    ]
},
{
    "question": "NFT nima?",
    "correct": "Noyob raqamli aktiv",
    "wrong": [
        "GPU modeli",
        "Internet kabeli",
        "Printer drayveri"
    ]
},
{
    "question": "NFT qayerda yaratiladi?",
    "correct": "Blockchain’da",
    "wrong": [
        "Printerda",
        "Monitor ichida",
        "GPUda"
    ]
},
{
    "question": "NFTning asosiy xususiyati nima?",
    "correct": "Noyobligi",
    "wrong": [
        "GPU kuchi",
        "Printer tezligi",
        "Disk hajmi"
    ]
},
{
    "question": "ERC-721 nima?",
    "correct": "NFT standarti",
    "wrong": [
        "GPU modeli",
        "Printer kodi",
        "Disk tizimi"
    ]
},
{
    "question": "ERC-1155 nimaga imkon beradi?",
    "correct": "Bir nechta token turini boshqarishga",
    "wrong": [
        "GPU yig‘ishga",
        "Printer ulashga",
        "Disk o‘chirishga"
    ]
},
{
    "question": "Metadata nima?",
    "correct": "NFT haqidagi ma’lumot",
    "wrong": [
        "GPU kodi",
        "Printer modeli",
        "Monitor hajmi"
    ]
},
{
    "question": "Minting nima?",
    "correct": "NFT yaratish jarayoni",
    "wrong": [
        "GPU sovutish",
        "Printer ulash",
        "Disk formatlash"
    ]
},
{
    "question": "IPFS nima?",
    "correct": "Markazlashmagan fayl tizimi",
    "wrong": [
        "GPU turi",
        "Printer dasturi",
        "Monitor tizimi"
    ]
},
{
    "question": "NFT transfer qanday amalga oshadi?",
    "correct": "Blockchain tranzaksiyasi orqali",
    "wrong": [
        "Printer orqali",
        "GPU orqali",
        "Bluetooth orqali"
    ]
},
{
    "question": "Royalty nima?",
    "correct": "Muallif foizi",
    "wrong": [
        "GPU narxi",
        "Printer kodi",
        "Disk hajmi"
    ]
},
{
    "question": "Nega NFT almashtirib bo‘lmaydi?",
    "correct": "Har biri noyob bo‘lgani uchun",
    "wrong": [
        "GPU sustligi uchun",
        "Monitor kichikligi uchun",
        "Printer yo‘qligi uchun"
    ]
},
{
    "question": "Nega metadata muhim?",
    "correct": "NFT ma’lumotini saqlaydi",
    "wrong": [
        "GPUni boshqaradi",
        "Printerni yoqadi",
        "Diskni formatlaydi"
    ]
},
{
    "question": "Nega IPFS ishlatiladi?",
    "correct": "Fayllarni markazlashmagan saqlash uchun",
    "wrong": [
        "GPU sovutish uchun",
        "Printer yig‘ish uchun",
        "Disk kamaytirish uchun"
    ]
},
{
    "question": "Nega NFT kontenti blockchain’da emas?",
    "correct": "Hajm katta bo‘lgani uchun",
    "wrong": [
        "GPU ishlamagani uchun",
        "Printer yo‘qligi uchun",
        "Monitor kichikligi uchun"
    ]
},
{
    "question": "Nega ERC-1155 samaraliroq?",
    "correct": "Bir nechta tokenni bitta shartnomada boshqaradi",
    "wrong": [
        "GPU kuchliroq",
        "Printer tezroq",
        "Disk kattaroq"
    ]
},
{
    "question": "Phishing NFT sohasida qanday ishlaydi?",
    "correct": "Soxta havolalar orqali",
    "wrong": [
        "GPU orqali",
        "Printer orqali",
        "Disk orqali"
    ]
},
{
    "question": "Rug pull nima?",
    "correct": "Loyiha egalarining mablag‘ bilan qochishi",
    "wrong": [
        "GPU buzilishi",
        "Printer yonishi",
        "Monitor o‘chishi"
    ]
},
{
    "question": "Nega seed phrase muhim?",
    "correct": "Hamyonni tiklash uchun",
    "wrong": [
        "GPU yoqish uchun",
        "Disk formatlash uchun",
        "Printer ulash uchun"
    ]
},
{
    "question": "Nega metadata yo‘qolsa NFT qiymati tushadi?",
    "correct": "NFT haqidagi ma’lumot yo‘qoladi",
    "wrong": [
        "GPU kuchsizlanadi",
        "Printer ishlamaydi",
        "Monitor o‘chadi"
    ]
},
{
    "question": "Nega NFT mualliflik huquqini bermaydi?",
    "correct": "Faqat egalikni bildiradi",
    "wrong": [
        "GPU talab qiladi",
        "Printer ulaydi",
        "Diskni tozalaydi"
    ]
},
{
    "question": "DApps nima?",
    "correct": "Markazlashmagan ilovalar",
    "wrong": [
        "GPU dasturlari",
        "Printer tizimlari",
        "Monitor fayllari"
    ]
},
{
    "question": "DApps qayerda ishlaydi?",
    "correct": "Blockchain ustida",
    "wrong": [
        "Printer ichida",
        "GPU ichida",
        "Disk ichida"
    ]
},
{
    "question": "DAppsning asosiy xususiyati nima?",
    "correct": "Markazlashmaganligi",
    "wrong": [
        "GPU kuchi",
        "Printer sifati",
        "Monitor hajmi"
    ]
},
{
    "question": "DApps arxitekturasi nechta qatlamdan iborat?",
    "correct": "3 qatlam",
    "wrong": [
        "1 qatlam",
        "10 qatlam",
        "20 qatlam"
    ]
},
{
    "question": "Frontend nima?",
    "correct": "Foydalanuvchi interfeysi",
    "wrong": [
        "GPU yadrosi",
        "Printer mexanizmi",
        "Disk sektori"
    ]
},
{
    "question": "Backend DAppsda nima?",
    "correct": "Smart shartnoma",
    "wrong": [
        "GPU drayveri",
        "Printer kodi",
        "Monitor tizimi"
    ]
},
{
    "question": "Blokcheyn qatlami nima qiladi?",
    "correct": "Ma’lumotni saqlaydi",
    "wrong": [
        "Printer yig‘adi",
        "GPU sovutadi",
        "Monitor almashtiradi"
    ]
},
{
    "question": "Smart shartnoma qanday ishlaydi?",
    "correct": "Avtomatik bajariladi",
    "wrong": [
        "Qo‘lda ishlaydi",
        "Printer boshqaradi",
        "GPU yig‘adi"
    ]
},
{
    "question": "DAppsda tranzaksiya qanday amalga oshadi?",
    "correct": "Blockchain orqali",
    "wrong": [
        "Printer orqali",
        "GPU orqali",
        "Monitor orqali"
    ]
},
{
    "question": "Gas fee nima?",
    "correct": "Tranzaksiya to‘lovi",
    "wrong": [
        "GPU narxi",
        "Printer kodi",
        "Disk formati"
    ]
},
{
    "question": "Nega DApps markazlashmagan?",
    "correct": "Serverga bog‘liq emas",
    "wrong": [
        "GPU yo‘qligi uchun",
        "Printer ishlashi uchun",
        "Monitor kattaligi uchun"
    ]
},
{
    "question": "Nega DApps xavfsizroq?",
    "correct": "Ma’lumot o‘zgarmasligi uchun",
    "wrong": [
        "GPU tezligi uchun",
        "Printer sifati uchun",
        "Disk hajmi uchun"
    ]
},
{
    "question": "Nega markazlashgan tizimlar xavfli?",
    "correct": "Bitta nuqta ishdan chiqishi mumkin",
    "wrong": [
        "GPU sovishi mumkin",
        "Printer kuyishi mumkin",
        "Monitor sinishi mumkin"
    ]
},
{
    "question": "Nega smart shartnoma o‘zgarmaydi?",
    "correct": "Blockchain’da yozilgani uchun",
    "wrong": [
        "GPU o‘chishi uchun",
        "Printer ishlashi uchun",
        "Disk formatlanishi uchun"
    ]
},
{
    "question": "Nega DAppsda senzura yo‘q?",
    "correct": "Markaziy boshqaruv yo‘qligi uchun",
    "wrong": [
        "GPU kuchsizligi uchun",
        "Printer yo‘qligi uchun",
        "Monitor kichikligi uchun"
    ]
},
{
    "question": "Nega DApps sekin?",
    "correct": "Blockchain tasdiqlash vaqt talab qilgani uchun",
    "wrong": [
        "GPU yo‘qligi uchun",
        "Disk kichikligi uchun",
        "Printer ishlashi uchun"
    ]
},
{
    "question": "Nega gas narxi oshadi?",
    "correct": "Tarmoq yuklamasi ortgani uchun",
    "wrong": [
        "GPU rangi uchun",
        "Printer turi uchun",
        "Monitor hajmi uchun"
    ]
},
{
    "question": "Light node qanday ishlaydi?",
    "correct": "Faqat kerakli ma’lumotni yuklaydi",
    "wrong": [
        "GPU ishlab chiqaradi",
        "Printer yig‘adi",
        "Diskni o‘chiradi"
    ]
},
{
    "question": "Full node nima qiladi?",
    "correct": "Butun blockchainni saqlaydi",
    "wrong": [
        "GPU sotadi",
        "Printer ulaydi",
        "Monitor tuzatadi"
    ]
},
{
    "question": "Nega DApps kelajakda muhim?",
    "correct": "Markazlashmagan xizmatlar yaratadi",
    "wrong": [
        "GPU almashtiradi",
        "Printer kamaytiradi",
        "Disk yo‘q qiladi"
    ]
},
{
    "question": "Blokcheyn eng ko‘p qaysi sohada qo‘llaniladi?",
    "correct": "Moliyaviy sohada",
    "wrong": [
        "Printer sanoatida",
        "GPU ta’mirida",
        "Monitor ishlab chiqarishda"
    ]
},
{
    "question": "Logistika sohasida blokcheyn nimani ta’minlaydi?",
    "correct": "Kuzatuv va shaffoflikni",
    "wrong": [
        "GPU yig‘ishni",
        "Printer ishlab chiqarishni",
        "Disk formatlashni"
    ]
},
{
    "question": "Sog‘liqni saqlashda blokcheynning asosiy vazifasi nima?",
    "correct": "Tibbiy ma’lumotlarni xavfsiz saqlash",
    "wrong": [
        "GPU sovutish",
        "Printer boshqarish",
        "Monitor yig‘ish"
    ]
},
{
    "question": "Davlat xizmatlarida blokcheyn nimani oshiradi?",
    "correct": "Shaffoflikni",
    "wrong": [
        "GPU haroratini",
        "Printer tezligini",
        "Disk hajmini"
    ]
},
{
    "question": "P2P tarmoq nimani anglatadi?",
    "correct": "Teng uzellar tarmog‘i",
    "wrong": [
        "Printer tarmog‘i",
        "GPU tizimi",
        "Monitor aloqasi"
    ]
},
{
    "question": "Konsensus qatlami nima qiladi?",
    "correct": "Qoidalar bo‘yicha kelishuvni ta’minlaydi",
    "wrong": [
        "GPU ishlab chiqaradi",
        "Printer yig‘adi",
        "Disk o‘chiradi"
    ]
},
{
    "question": "Full node nima?",
    "correct": "Blockchainning to‘liq nusxasi",
    "wrong": [
        "GPU modeli",
        "Printer kodi",
        "Monitor dasturi"
    ]
},
{
    "question": "Light node nima qiladi?",
    "correct": "Qisman tekshiruv bajaradi",
    "wrong": [
        "GPU yaratadi",
        "Printer ulaydi",
        "Disk kengaytiradi"
    ]
},
{
    "question": "API nima uchun kerak?",
    "correct": "Tizimlar o‘rtasida aloqa uchun",
    "wrong": [
        "GPU sovutish uchun",
        "Printer yig‘ish uchun",
        "Monitor o‘chirish uchun"
    ]
},
{
    "question": "CRUD operatsiyalarida blokcheynda UPDATE mavjudmi?",
    "correct": "Yo‘q",
    "wrong": [
        "Ha",
        "Faqat GPUda",
        "Faqat printerda"
    ]
},
{
    "question": "Nega blokcheyn logistika uchun muhim?",
    "correct": "Mahsulotni kuzatish imkonini beradi",
    "wrong": [
        "GPU sotadi",
        "Printer yig‘adi",
        "Disk formatlaydi"
    ]
},
{
    "question": "Nega P2P tarmoq chidamli?",
    "correct": "Bitta markazga bog‘liq emas",
    "wrong": [
        "GPU kuchli",
        "Printer tez",
        "Monitor katta"
    ]
},
{
    "question": "PBFT algoritmi nimaga asoslangan?",
    "correct": "Vizantiya xatolariga bardoshlilikka",
    "wrong": [
        "GPU sovutishga",
        "Printer tezligiga",
        "Disk hajmiga"
    ]
},
{
    "question": "Nega yopiq blokcheyn tezroq?",
    "correct": "Ishtirokchilar soni kamroq",
    "wrong": [
        "GPU kattaroq",
        "Printer tezroq",
        "Disk kengroq"
    ]
},
{
    "question": "Raft algoritmi nimaga asoslangan?",
    "correct": "Lider orqali boshqaruvga",
    "wrong": [
        "GPU orqali",
        "Printer orqali",
        "Monitor orqali"
    ]
},
{
    "question": "Nega blokcheynda DELETE mavjud emas?",
    "correct": "Ma’lumot o‘zgarmasligi uchun",
    "wrong": [
        "GPU sustligi uchun",
        "Printer yo‘qligi uchun",
        "Monitor kichikligi uchun"
    ]
},
{
    "question": "Nega audit blokcheynda oson?",
    "correct": "Barcha yozuvlar saqlangani uchun",
    "wrong": [
        "GPU kuchli bo‘lgani uchun",
        "Printer ishlagani uchun",
        "Disk bo‘shligi uchun"
    ]
},
{
    "question": "Nega yopiq blokcheyn maxfiy?",
    "correct": "Ruxsat bilan kiriladi",
    "wrong": [
        "GPU ishlamagani uchun",
        "Printer o‘chirilgani uchun",
        "Monitor sindirilgani uchun"
    ]
},
{
    "question": "World State nima?",
    "correct": "Joriy ma’lumotlar holati",
    "wrong": [
        "GPU xotirasi",
        "Printer katalogi",
        "Monitor sozlamasi"
    ]
},
{
    "question": "Nega API Gateway kerak?",
    "correct": "So‘rovlarni boshqarish uchun",
    "wrong": [
        "GPU sovutish uchun",
        "Printer yig‘ish uchun",
        "Disk tozalash uchun"
    ]
},
]

user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    random.shuffle(questions)

    user_data[chat_id] = {
        "current": 0,
        "score": 0
    }

    await send_question(update, chat_id)

async def send_question(update, chat_id):
    q = questions[user_data[chat_id]["current"]]

    options = q["wrong"] + [q["correct"]]
    random.shuffle(options)

    user_data[chat_id]["correct"] = options.index(q["correct"])

    text = f"❓ Savol {user_data[chat_id]['current'] + 1}\n\n"
    text += q["question"] + "\n\n"

    buttons = []

    for i, option in enumerate(options):
        text += f"{letters[i]}. {option}\n"
        buttons.append([letters[i]])

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    await update.message.reply_text(text, reply_markup=keyboard)

async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    text = update.message.text.upper()

    if text not in letters:
        await update.message.reply_text("Faqat A, B, C yoki D yuboring")
        return

    correct_index = user_data[chat_id]["correct"]

    if letters[correct_index] == text:
        user_data[chat_id]["score"] += 1
        await update.message.reply_text("✅ To‘g‘ri")
    else:
        await update.message.reply_text(
            f"❌ Noto‘g‘ri\nTo‘g‘ri javob: {letters[correct_index]}"
        )

    user_data[chat_id]["current"] += 1

    if user_data[chat_id]["current"] < len(questions):
        await send_question(update, chat_id)
    else:
        score = user_data[chat_id]["score"]
        total = len(questions)

        await update.message.reply_text(
            f"🎉 Test tugadi\nNatija: {score}/{total}"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, answer))

print("Bot ishlayapti...")
app.run_polling()