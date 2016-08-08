from django.utils.translation import ugettext_lazy as _

GENDER = (
    (0, _('Неизвестно')),
    (1, _('Мужчина')),
    (2, _('Женщина'))
)

DEGREE = (
    (1, _('Очень слабая')),
    (2, _('Слабая')),
    (3, _('Средняя')),
    (4, _('Сильная')),
    (5, _('Очень сильная'))
)

CONTENT_RATING = (
    (0, _('Для всех возрастов.')),
    (1, _('Для детей.')),
    (2, _('Для подростков.')),
    (3, _('Для взрослых.')),
    (4, _('Только для взрослых.')),
)

ROLE = (
    (0, _('Unknown')),
    (1, _('Author')),
    (2, _('Illustrator')),
    (3, _('Contributor')),
    (4, _('Editor')),
    (5, _('Translator')),
    (6, _('Narrator')),
)

FORMATS = (
    (0, 'Unknown binding'),
    (1, 'Hardcover'),
    (2, 'Paperback'),
    (3, 'Kindle Edition'),
    (4, 'ebook'),
    (5, 'Mass Market Paperback'),
    (6, 'Nook'),
    (7, 'Library Binding'),
    (8, 'Audiobook'),
    (9, 'Audio CD'),
    (10, 'Audio Cassette'),
    (11, 'Audible Audio'),
    (12, 'CD-ROM'),
    (13, 'MP3 CD'),
    (14, 'Board book'),
    (15, 'Leather Bound'),
    (16, 'Unbound'),
    (17, 'Spiral-bound')
)

LANGUAGES = (
    ('unknown', _('Unknown')),
    ('abk', _('Abkhazian')),
    ('ace', _('Achinese')),
    ('ach', _('Acoli')),
    ('ada', _('Adangme')),
    ('ady', _('Adyghe; Adygei')),
    ('aar', _('Afar')),
    ('afh', _('Afrihili')),
    ('afr', _('Afrikaans')),
    ('afa', _('Afro-Asiatic (Other)')),
    ('ain', _('Ainu')),
    ('aka', _('Akan')),
    ('akk', _('Akkadian')),
    ('sqi', _('Albanian')),
    ('ale', _('Aleut')),
    ('alg', _('Algonquian languages')),
    ('tut', _('Altaic (Other)')),
    ('amh', _('Amharic')),
    ('anp', _('Angika')),
    ('apa', _('Apache languages')),
    ('ara', _('Arabic')),
    ('arg', _('Aragonese')),
    ('arp', _('Arapaho')),
    ('arw', _('Arawak')),
    ('hye', _('Armenian')),
    ('rup', _('Aromanian; Arumanian; Macedo-Romanian')),
    ('art', _('Artificial (Other)')),
    ('asm', _('Assamese')),
    ('ast', _('Asturian; Bable; Leonese; Asturleonese')),
    ('ath', _('Athapascan languages')),
    ('aus', _('Australian languages')),
    ('map', _('Austronesian (Other)')),
    ('ava', _('Avaric')),
    ('ave', _('Avestan')),
    ('awa', _('Awadhi')),
    ('aym', _('Aymara')),
    ('aze', _('Azerbaijani')),
    ('ban', _('Balinese')),
    ('bat', _('Baltic (Other)')),
    ('bal', _('Baluchi')),
    ('bam', _('Bambara')),
    ('bai', _('Bamileke languages')),
    ('bad', _('Banda languages')),
    ('bnt', _('Bantu (Other)')),
    ('bas', _('Basa')),
    ('bak', _('Bashkir')),
    ('eus', _('Basque')),
    ('btk', _('Batak languages')),
    ('bej', _('Beja; Bedawiyet')),
    ('bel', _('Belarusian')),
    ('bem', _('Bemba')),
    ('ben', _('Bengali')),
    ('ber', _('Berber (Other)')),
    ('bho', _('Bhojpuri')),
    ('bih', _('Bihari')),
    ('bik', _('Bikol')),
    ('bin', _('Bini; Edo')),
    ('bis', _('Bislama')),
    ('byn', _('Blin; Bilin')),
    ('zbl', _('Blissymbols; Blissymbolics; Bliss')),
    ('nob', _('Bokmål, Norwegian; Norwegian Bokmål')),
    ('bos', _('Bosnian')),
    ('bra', _('Braj')),
    ('bre', _('Breton')),
    ('bug', _('Buginese')),
    ('bul', _('Bulgarian')),
    ('bua', _('Buriat')),
    ('mya', _('Burmese')),
    ('cad', _('Caddo')),
    ('cat', _('Catalan; Valencian')),
    ('cau', _('Caucasian (Other)')),
    ('ceb', _('Cebuano')),
    ('cel', _('Celtic (Other)')),
    ('cai', _('Central American Indian (Other)')),
    ('khm', _('Central Khmer')),
    ('chg', _('Chagatai')),
    ('cmc', _('Chamic languages')),
    ('cha', _('Chamorro')),
    ('che', _('Chechen')),
    ('chr', _('Cherokee')),
    ('chy', _('Cheyenne')),
    ('chb', _('Chibcha')),
    ('nya', _('Chichewa; Chewa; Nyanja')),
    ('zho', _('Chinese')),
    ('chn', _('Chinook jargon')),
    ('chp', _('Chipewyan; Dene Suline')),
    ('cho', _('Choctaw')),
    ('chu', _('Church Slavic; Old Slavonic; Old Bulgarian;')),
    ('chk', _('Chuukese')),
    ('chv', _('Chuvash')),
    ('nwc', _('Classical Newari; Old Newari; Classical Nepal Bhasa')),
    ('syc', _('Classical Syriac')),
    ('cop', _('Coptic')),
    ('cor', _('Cornish')),
    ('cos', _('Corsican')),
    ('cre', _('Cree')),
    ('mus', _('Creek')),
    ('crp', _('Creoles and pidgins (Other)')),
    ('cpe', _('Creoles and pidgins, English based (Other)')),
    ('cpf', _('Creoles and pidgins, French-based (Other)')),
    ('cpp', _('Creoles and pidgins, Portuguese-based (Other)')),
    ('crh', _('Crimean Tatar; Crimean Turkish')),
    ('scr', _('Croatian')),
    ('cus', _('Cushitic (Other)')),
    ('cze', _('Czech')),
    ('dak', _('Dakota')),
    ('dan', _('Danish')),
    ('dar', _('Dargwa')),
    ('del', _('Delaware')),
    ('din', _('Dinka')),
    ('div', _('Divehi; Dhivehi; Maldivian')),
    ('doi', _('Dogri')),
    ('dgr', _('Dogrib')),
    ('dra', _('Dravidian (Other)')),
    ('dua', _('Duala')),
    ('nl', _('Dutch')),
    ('dum', _('Dutch, Middle (ca.1050-1350)')),
    ('dyu', _('Dyula')),
    ('dzo', _('Dzongkha')),
    ('frs', _('Eastern Frisian')),
    ('efi', _('Efik')),
    ('egy', _('Egyptian (Ancient)')),
    ('eka', _('Ekajuk')),
    ('elx', _('Elamite')),
    ('eng', _('English')),
    ('enm', _('English, Middle (1100-1500)')),
    ('ang', _('English, Old (ca.450-1100)')),
    ('myv', _('Erzya')),
    ('epo', _('Esperanto')),
    ('est', _('Estonian')),
    ('ewe', _('Ewe')),
    ('ewo', _('Ewondo')),
    ('fan', _('Fang')),
    ('fat', _('Fanti')),
    ('fao', _('Faroese')),
    ('pes', _('Farsi')),
    ('fij', _('Fijian')),
    ('fil', _('Filipino; Pilipino')),
    ('fin', _('Finnish')),
    ('fiu', _('Finno-Ugrian (Other)')),
    ('vls', _('Flemish')),
    ('fon', _('Fon')),
    ('fre', _('French')),
    ('frm', _('French, Middle (ca.1400-1600)')),
    ('fro', _('French, Old (842-ca.1400)')),
    ('fur', _('Friulian')),
    ('ful', _('Fulah')),
    ('gaa', _('Ga')),
    ('gla', _('Gaelic; Scottish Gaelic')),
    ('car', _('Galibi Carib')),
    ('glg', _('Galician')),
    ('lug', _('Ganda')),
    ('gay', _('Gayo')),
    ('gba', _('Gbaya')),
    ('gez', _('Geez')),
    ('kat', _('Georgian')),
    ('ger', _('German')),
    ('gmh', _('German, Middle High (ca.1050-1500)')),
    ('goh', _('German, Old High (ca.750-1050)')),
    ('gem', _('Germanic (Other)')),
    ('gil', _('Gilbertese')),
    ('gon', _('Gondi')),
    ('gor', _('Gorontalo')),
    ('got', _('Gothic')),
    ('grb', _('Grebo')),
    ('grc', _('Greek, Ancient (to 1453)')),
    ('gre', _('Greek, Modern (1453-)')),
    ('grn', _('Guarani')),
    ('guj', _('Gujarati')),
    ('gwi', _('Gwich&#39;in')),
    ('hai', _('Haida')),
    ('hat', _('Haitian; Haitian Creole')),
    ('hau', _('Hausa')),
    ('haw', _('Hawaiian')),
    ('heb', _('Hebrew')),
    ('her', _('Herero')),
    ('hil', _('Hiligaynon')),
    ('him', _('Himachali')),
    ('hin', _('Hindi')),
    ('hmo', _('Hiri Motu')),
    ('hit', _('Hittite')),
    ('hmn', _('Hmong')),
    ('hun', _('Hungarian')),
    ('hup', _('Hupa')),
    ('iba', _('Iban')),
    ('isl', _('Icelandic')),
    ('ido', _('Ido')),
    ('ibo', _('Igbo')),
    ('ijo', _('Ijo languages')),
    ('ilo', _('Iloko')),
    ('smn', _('Inari Sami')),
    ('inc', _('Indic (Other)')),
    ('ine', _('Indo-European (Other)')),
    ('ind', _('Indonesian')),
    ('inh', _('Ingush')),
    ('ina', _('Interlingua')),
    ('ile', _('Interlingue; Occidental')),
    ('iku', _('Inuktitut')),
    ('ipk', _('Inupiaq')),
    ('ira', _('Iranian (Other)')),
    ('gle', _('Irish')),
    ('mga', _('Irish, Middle (900-1200)')),
    ('sga', _('Irish, Old (to 900)')),
    ('iro', _('Iroquoian languages')),
    ('ita', _('Italian')),
    ('jpn', _('Japanese')),
    ('jav', _('Javanese')),
    ('jrb', _('Judeo-Arabic')),
    ('jpr', _('Judeo-Persian')),
    ('kbd', _('Kabardian')),
    ('kab', _('Kabyle')),
    ('kac', _('Kachin; Jingpho')),
    ('kal', _('Kalaallisut; Greenlandic')),
    ('xal', _('Kalmyk; Oirat')),
    ('kam', _('Kamba')),
    ('kan', _('Kannada')),
    ('kau', _('Kanuri')),
    ('kaa', _('Kara-Kalpak')),
    ('krc', _('Karachay-Balkar')),
    ('krl', _('Karelian')),
    ('kar', _('Karen languages')),
    ('kas', _('Kashmiri')),
    ('csb', _('Kashubian')),
    ('kaw', _('Kawi')),
    ('kaz', _('Kazakh')),
    ('kha', _('Khasi')),
    ('khi', _('Khoisan (Other)')),
    ('kho', _('Khotanese')),
    ('kik', _('Kikuyu; Gikuyu')),
    ('kmb', _('Kimbundu')),
    ('kin', _('Kinyarwanda')),
    ('kir', _('Kirghiz; Kyrgyz')),
    ('tlh', _('Klingon; tlhIngan-Hol')),
    ('kom', _('Komi')),
    ('kon', _('Kongo')),
    ('kok', _('Konkani')),
    ('kor', _('Korean')),
    ('kos', _('Kosraean')),
    ('kpe', _('Kpelle')),
    ('kro', _('Kru languages')),
    ('kua', _('Kuanyama; Kwanyama')),
    ('kum', _('Kumyk')),
    ('kur', _('Kurdish')),
    ('kru', _('Kurukh')),
    ('kut', _('Kutenai')),
    ('lad', _('Ladino')),
    ('lah', _('Lahnda')),
    ('lam', _('Lamba')),
    ('day', _('Land Dayak languages')),
    ('lao', _('Lao')),
    ('lat', _('Latin')),
    ('lav', _('Latvian')),
    ('lez', _('Lezghian')),
    ('lim', _('Limburgan; Limburger; Limburgish')),
    ('lin', _('Lingala')),
    ('lit', _('Lithuanian')),
    ('jbo', _('Lojban')),
    ('nds', _('Low German; Low Saxon; German, Low;')),
    ('dsb', _('Lower Sorbian')),
    ('loz', _('Lozi')),
    ('lub', _('Luba-Katanga')),
    ('lua', _('Luba-Lulua')),
    ('lui', _('Luiseno')),
    ('smj', _('Lule Sami')),
    ('lun', _('Lunda')),
    ('luo', _('Luo (Kenya and Tanzania)')),
    ('lus', _('Lushai')),
    ('ltz', _('Luxembourgish; Letzeburgesch')),
    ('mkd', _('Macedonian')),
    ('mad', _('Madurese')),
    ('mag', _('Magahi')),
    ('mai', _('Maithili')),
    ('mak', _('Makasar')),
    ('mlg', _('Malagasy')),
    ('msa', _('Malay')),
    ('mal', _('Malayalam')),
    ('mlt', _('Maltese')),
    ('mnc', _('Manchu')),
    ('mdr', _('Mandar')),
    ('man', _('Mandingo')),
    ('mni', _('Manipuri')),
    ('mno', _('Manobo languages')),
    ('glv', _('Manx')),
    ('mri', _('Maori')),
    ('arn', _('Mapudungun; Mapuche')),
    ('mar', _('Marathi')),
    ('chm', _('Mari')),
    ('mah', _('Marshallese')),
    ('mwr', _('Marwari')),
    ('mas', _('Masai')),
    ('myn', _('Mayan languages')),
    ('men', _('Mende')),
    ('wtm', _('Mewati')),
    ('mic', _('Mi&#39;kmaq; Micmac')),
    ('min', _('Minangkabau')),
    ('mwl', _('Mirandese')),
    ('moh', _('Mohawk')),
    ('mdf', _('Moksha')),
    ('mol', _('Moldavian')),
    ('mkh', _('Mon-Khmer (Other)')),
    ('lol', _('Mongo')),
    ('mon', _('Mongolian')),
    ('mos', _('Mossi')),
    ('mul', _('Multiple languages')),
    ('mun', _('Munda languages')),
    ('nqo', _('N&#39;Ko')),
    ('nah', _('Nahuatl languages')),
    ('nau', _('Nauru')),
    ('nav', _('Navajo; Navaho')),
    ('nde', _('Ndebele, North; North Ndebele')),
    ('nbl', _('Ndebele, South; South Ndebele')),
    ('ndo', _('Ndonga')),
    ('nap', _('Neapolitan')),
    ('new', _('Nepal Bhasa; Newari')),
    ('nep', _('Nepali')),
    ('nia', _('Nias')),
    ('nic', _('Niger-Kordofanian (Other)')),
    ('ssa', _('Nilo-Saharan (Other)')),
    ('niu', _('Niuean')),
    ('nog', _('Nogai')),
    ('non', _('Norse, Old')),
    ('nai', _('North American Indian')),
    ('frr', _('Northern Frisian')),
    ('sme', _('Northern Sami')),
    ('nno', _('Norwegian Nynorsk; Nynorsk, Norwegian')),
    ('nor', _('Norwegian')),
    ('nub', _('Nubian languages')),
    ('nym', _('Nyamwezi')),
    ('nyn', _('Nyankole')),
    ('nyo', _('Nyoro')),
    ('nzi', _('Nzima')),
    ('oci', _('Occitan (post 1500); Provençal')),
    ('arc', _('Official Aramaic; Imperial Aramaic')),
    ('oji', _('Ojibwa')),
    ('ori', _('Oriya')),
    ('orm', _('Oromo')),
    ('osa', _('Osage')),
    ('oss', _('Ossetian; Ossetic')),
    ('oto', _('Otomian languages')),
    ('pal', _('Pahlavi')),
    ('pau', _('Palauan')),
    ('pli', _('Pali')),
    ('pam', _('Pampanga; Kapampangan')),
    ('pag', _('Pangasinan')),
    ('pan', _('Panjabi; Punjabi')),
    ('pap', _('Papiamento')),
    ('paa', _('Papuan (Other)')),
    ('nso', _('Pedi; Sepedi; Northern Sotho')),
    ('per', _('Persian')),
    ('peo', _('Persian, Old (ca.600-400 B.C.)')),
    ('phi', _('Philippine (Other)')),
    ('phn', _('Phoenician')),
    ('pon', _('Pohnpeian')),
    ('pol', _('Polish')),
    ('por', _('Portuguese')),
    ('pra', _('Prakrit languages')),
    ('pro', _('Provençal, Old (to 1500)')),
    ('pus', _('Pushto; Pashto')),
    ('que', _('Quechua')),
    ('roa', _('Rhaeto-Romanic languages')),
    ('raj', _('Rajasthani')),
    ('rap', _('Rapanui')),
    ('rar', _('Rarotongan; Cook Islands Maori')),
    ('qaa', _('Reserved for local use')),
    ('rgn', _('Romagnolo')),
    ('roa', _('Romance (Other)')),
    ('rum', _('Romanian')),
    ('roh', _('Romansh')),
    ('rom', _('Romany')),
    ('run', _('Rundi')),
    ('rus', _('Russian')),
    ('sal', _('Salishan languages')),
    ('sam', _('Samaritan Aramaic')),
    ('smi', _('Sami languages (Other)')),
    ('smo', _('Samoan')),
    ('sad', _('Sandawe')),
    ('sag', _('Sango')),
    ('san', _('Sanskrit')),
    ('sat', _('Santali')),
    ('srd', _('Sardinian')),
    ('sas', _('Sasak')),
    ('sco', _('Scots')),
    ('sel', _('Selkup')),
    ('sem', _('Semitic (Other)')),
    ('srp', _('Serbian')),
    ('srr', _('Serer')),
    ('shn', _('Shan')),
    ('sna', _('Shona')),
    ('iii', _('Sichuan Yi; Nuosu')),
    ('scn', _('Sicilian')),
    ('sid', _('Sidamo')),
    ('sgn', _('Sign Languages')),
    ('bla', _('Siksika')),
    ('snd', _('Sindhi')),
    ('sin', _('Sinhala; Sinhalese')),
    ('sit', _('Sino-Tibetan (Other)')),
    ('sio', _('Siouan languages')),
    ('sms', _('Skolt Sami')),
    ('den', _('Slave (Athapascan)')),
    ('sla', _('Slavic (Other)')),
    ('slo', _('Slovak')),
    ('slv', _('Slovenian')),
    ('sog', _('Sogdian')),
    ('som', _('Somali')),
    ('son', _('Songhai languages')),
    ('snk', _('Soninke')),
    ('wen', _('Sorbian languages')),
    ('sot', _('Sotho, Southern')),
    ('sai', _('South American Indian (Other)')),
    ('alt', _('Southern Altai')),
    ('sma', _('Southern Sami')),
    ('spa', _('Spanish')),
    ('srn', _('Sranan Tongo')),
    ('suk', _('Sukuma')),
    ('sux', _('Sumerian')),
    ('sun', _('Sundanese')),
    ('sus', _('Susu')),
    ('sot', _('Sutu')),
    ('swa', _('Swahili')),
    ('ssw', _('Swati')),
    ('swe', _('Swedish')),
    ('gsw', _('Swiss German; Alemannic; Alsatian')),
    ('syr', _('Syriac')),
    ('tgl', _('Tagalog')),
    ('tah', _('Tahitian')),
    ('tai', _('Tai (Other)')),
    ('tgk', _('Tajik')),
    ('tmh', _('Tamashek')),
    ('tam', _('Tamil')),
    ('tat', _('Tatar')),
    ('tel', _('Telugu')),
    ('ter', _('Tereno')),
    ('tet', _('Tetum')),
    ('tha', _('Thai')),
    ('tib', _('Tibetan')),
    ('tig', _('Tigre')),
    ('tir', _('Tigrinya')),
    ('tem', _('Timne')),
    ('tiv', _('Tiv')),
    ('tli', _('Tlingit')),
    ('tpi', _('Tok Pisin')),
    ('tkl', _('Tokelau')),
    ('tog', _('Tonga (Nyasa)')),
    ('ton', _('Tonga (Tonga Islands)')),
    ('tsi', _('Tsimshian')),
    ('tso', _('Tsonga')),
    ('tsn', _('Tswana')),
    ('tum', _('Tumbuka')),
    ('tup', _('Tupi languages')),
    ('tur', _('Turkish')),
    ('ota', _('Turkish, Ottoman (1500-1928)')),
    ('tuk', _('Turkmen')),
    ('tvl', _('Tuvalu')),
    ('tyv', _('Tuvinian')),
    ('twi', _('Twi')),
    ('udm', _('Udmurt')),
    ('uga', _('Ugaritic')),
    ('uig', _('Uighur; Uyghur')),
    ('ukr', _('Ukrainian')),
    ('umb', _('Umbundu')),
    ('mis', _('Uncoded languages')),
    ('und', _('Undetermined')),
    ('hsb', _('Upper Sorbian')),
    ('urd', _('Urdu')),
    ('uzb', _('Uzbek')),
    ('vai', _('Vai')),
    ('ven', _('Venda')),
    ('vec', _('Vèneto')),
    ('vie', _('Vietnamese')),
    ('vol', _('Volapük')),
    ('vot', _('Votic')),
    ('wak', _('Wakashan languages')),
    ('wal', _('Walamo')),
    ('wln', _('Walloon')),
    ('war', _('Waray')),
    ('was', _('Washo')),
    ('wel', _('Welsh')),
    ('fry', _('Western Frisian')),
    ('wol', _('Wolof')),
    ('xho', _('Xhosa')),
    ('sah', _('Yakut')),
    ('yao', _('Yao')),
    ('yap', _('Yapese')),
    ('yid', _('Yiddish')),
    ('yor', _('Yoruba')),
    ('ypk', _('Yupik languages')),
    ('znd', _('Zande languages')),
    ('zap', _('Zapotec')),
    ('zza', _('Zaza; Dimili; Dimli; Kirdki; Kirmanjki; Zazaki')),
    ('zen', _('Zenaga')),
    ('zha', _('Zhuang; Chuang')),
    ('zul', _('Zulu')),
    ('zun', _('Zuni'))
)