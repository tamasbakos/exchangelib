""" A dict to translate from IANA location name to Windows timezone name. Translations taken from
http://unicode.org/repos/cldr/trunk/common/supplemental/windowsZones.xml """
import re

import requests

from .util import to_xml

CLDR_WINZONE_URL = 'https://raw.githubusercontent.com/unicode-org/cldr/master/common/supplemental/windowsZones.xml'
DEFAULT_TERRITORY = '001'
CLDR_WINZONE_VERSION = '2020f'


def generate_map(timeout=10):
    """Helper method to update the map if the CLDR database is updated

    Args:
      timeout:  (Default value = 10)

    """
    r = requests.get(CLDR_WINZONE_URL, timeout=timeout)
    if r.status_code != 200:
        raise ValueError('Unexpected response: %s' % r)
    tz_map = {}
    timezones_elem = to_xml(r.content).find('windowsZones').find('mapTimezones')
    version = timezones_elem.get('typeVersion')
    for e in timezones_elem.findall('mapZone'):
        for location in re.split(r'\s+', e.get('type')):
            if e.get('territory') == DEFAULT_TERRITORY or location not in tz_map:
                # Prefer default territory. This is so MS_TIMEZONE_TO_IANA_MAP maps from MS timezone ID back to the
                # "preferred" region/location timezone name.
                if not location:
                    raise ValueError('Expected location')
                tz_map[location] = e.get('other'), e.get('territory')
    return version, tz_map


# This map is generated irregularly from generate_map(). Do not edit manually - make corrections to
# IANA_TO_MS_TIMEZONE_MAP instead. We provide this map to avoid hammering the CLDR_WINZONE_URL.
#
# This list was generated from CLDR_WINZONE_URL version CLDR_WINZONE_VERSION.
CLDR_TO_MS_TIMEZONE_MAP = {
    'Africa/Abidjan': ('Greenwich Standard Time', 'CI'),
    'Africa/Accra': ('Greenwich Standard Time', 'GH'),
    'Africa/Addis_Ababa': ('E. Africa Standard Time', 'ET'),
    'Africa/Algiers': ('W. Central Africa Standard Time', 'DZ'),
    'Africa/Asmera': ('E. Africa Standard Time', 'ER'),
    'Africa/Bamako': ('Greenwich Standard Time', 'ML'),
    'Africa/Bangui': ('W. Central Africa Standard Time', 'CF'),
    'Africa/Banjul': ('Greenwich Standard Time', 'GM'),
    'Africa/Bissau': ('Greenwich Standard Time', 'GW'),
    'Africa/Blantyre': ('South Africa Standard Time', 'MW'),
    'Africa/Brazzaville': ('W. Central Africa Standard Time', 'CG'),
    'Africa/Bujumbura': ('South Africa Standard Time', 'BI'),
    'Africa/Cairo': ('Egypt Standard Time', '001'),
    'Africa/Casablanca': ('Morocco Standard Time', '001'),
    'Africa/Ceuta': ('Romance Standard Time', 'ES'),
    'Africa/Conakry': ('Greenwich Standard Time', 'GN'),
    'Africa/Dakar': ('Greenwich Standard Time', 'SN'),
    'Africa/Dar_es_Salaam': ('E. Africa Standard Time', 'TZ'),
    'Africa/Djibouti': ('E. Africa Standard Time', 'DJ'),
    'Africa/Douala': ('W. Central Africa Standard Time', 'CM'),
    'Africa/El_Aaiun': ('Morocco Standard Time', 'EH'),
    'Africa/Freetown': ('Greenwich Standard Time', 'SL'),
    'Africa/Gaborone': ('South Africa Standard Time', 'BW'),
    'Africa/Harare': ('South Africa Standard Time', 'ZW'),
    'Africa/Johannesburg': ('South Africa Standard Time', '001'),
    'Africa/Juba': ('E. Africa Standard Time', 'SS'),
    'Africa/Kampala': ('E. Africa Standard Time', 'UG'),
    'Africa/Khartoum': ('Sudan Standard Time', '001'),
    'Africa/Kigali': ('South Africa Standard Time', 'RW'),
    'Africa/Kinshasa': ('W. Central Africa Standard Time', 'CD'),
    'Africa/Lagos': ('W. Central Africa Standard Time', '001'),
    'Africa/Libreville': ('W. Central Africa Standard Time', 'GA'),
    'Africa/Lome': ('Greenwich Standard Time', 'TG'),
    'Africa/Luanda': ('W. Central Africa Standard Time', 'AO'),
    'Africa/Lubumbashi': ('South Africa Standard Time', 'CD'),
    'Africa/Lusaka': ('South Africa Standard Time', 'ZM'),
    'Africa/Malabo': ('W. Central Africa Standard Time', 'GQ'),
    'Africa/Maputo': ('South Africa Standard Time', 'MZ'),
    'Africa/Maseru': ('South Africa Standard Time', 'LS'),
    'Africa/Mbabane': ('South Africa Standard Time', 'SZ'),
    'Africa/Mogadishu': ('E. Africa Standard Time', 'SO'),
    'Africa/Monrovia': ('Greenwich Standard Time', 'LR'),
    'Africa/Nairobi': ('E. Africa Standard Time', '001'),
    'Africa/Ndjamena': ('W. Central Africa Standard Time', 'TD'),
    'Africa/Niamey': ('W. Central Africa Standard Time', 'NE'),
    'Africa/Nouakchott': ('Greenwich Standard Time', 'MR'),
    'Africa/Ouagadougou': ('Greenwich Standard Time', 'BF'),
    'Africa/Porto-Novo': ('W. Central Africa Standard Time', 'BJ'),
    'Africa/Sao_Tome': ('Sao Tome Standard Time', '001'),
    'Africa/Tripoli': ('Libya Standard Time', '001'),
    'Africa/Tunis': ('W. Central Africa Standard Time', 'TN'),
    'Africa/Windhoek': ('Namibia Standard Time', '001'),
    'America/Adak': ('Aleutian Standard Time', '001'),
    'America/Anchorage': ('Alaskan Standard Time', '001'),
    'America/Anguilla': ('SA Western Standard Time', 'AI'),
    'America/Antigua': ('SA Western Standard Time', 'AG'),
    'America/Araguaina': ('Tocantins Standard Time', '001'),
    'America/Argentina/La_Rioja': ('Argentina Standard Time', 'AR'),
    'America/Argentina/Rio_Gallegos': ('Argentina Standard Time', 'AR'),
    'America/Argentina/Salta': ('Argentina Standard Time', 'AR'),
    'America/Argentina/San_Juan': ('Argentina Standard Time', 'AR'),
    'America/Argentina/San_Luis': ('Argentina Standard Time', 'AR'),
    'America/Argentina/Tucuman': ('Argentina Standard Time', 'AR'),
    'America/Argentina/Ushuaia': ('Argentina Standard Time', 'AR'),
    'America/Aruba': ('SA Western Standard Time', 'AW'),
    'America/Asuncion': ('Paraguay Standard Time', '001'),
    'America/Bahia': ('Bahia Standard Time', '001'),
    'America/Bahia_Banderas': ('Central Standard Time (Mexico)', 'MX'),
    'America/Barbados': ('SA Western Standard Time', 'BB'),
    'America/Belem': ('SA Eastern Standard Time', 'BR'),
    'America/Belize': ('Central America Standard Time', 'BZ'),
    'America/Blanc-Sablon': ('SA Western Standard Time', 'CA'),
    'America/Boa_Vista': ('SA Western Standard Time', 'BR'),
    'America/Bogota': ('SA Pacific Standard Time', '001'),
    'America/Boise': ('Mountain Standard Time', 'US'),
    'America/Buenos_Aires': ('Argentina Standard Time', '001'),
    'America/Cambridge_Bay': ('Mountain Standard Time', 'CA'),
    'America/Campo_Grande': ('Central Brazilian Standard Time', 'BR'),
    'America/Cancun': ('Eastern Standard Time (Mexico)', '001'),
    'America/Caracas': ('Venezuela Standard Time', '001'),
    'America/Catamarca': ('Argentina Standard Time', 'AR'),
    'America/Cayenne': ('SA Eastern Standard Time', '001'),
    'America/Cayman': ('SA Pacific Standard Time', 'KY'),
    'America/Chicago': ('Central Standard Time', '001'),
    'America/Chihuahua': ('Mountain Standard Time (Mexico)', '001'),
    'America/Coral_Harbour': ('SA Pacific Standard Time', 'CA'),
    'America/Cordoba': ('Argentina Standard Time', 'AR'),
    'America/Costa_Rica': ('Central America Standard Time', 'CR'),
    'America/Creston': ('Yukon Standard Time', 'CA'),
    'America/Cuiaba': ('Central Brazilian Standard Time', '001'),
    'America/Curacao': ('SA Western Standard Time', 'CW'),
    'America/Danmarkshavn': ('UTC', 'GL'),
    'America/Dawson': ('Yukon Standard Time', 'CA'),
    'America/Dawson_Creek': ('Yukon Standard Time', 'CA'),
    'America/Denver': ('Mountain Standard Time', '001'),
    'America/Detroit': ('Eastern Standard Time', 'US'),
    'America/Dominica': ('SA Western Standard Time', 'DM'),
    'America/Edmonton': ('Mountain Standard Time', 'CA'),
    'America/Eirunepe': ('SA Pacific Standard Time', 'BR'),
    'America/El_Salvador': ('Central America Standard Time', 'SV'),
    'America/Fort_Nelson': ('Yukon Standard Time', 'CA'),
    'America/Fortaleza': ('SA Eastern Standard Time', 'BR'),
    'America/Glace_Bay': ('Atlantic Standard Time', 'CA'),
    'America/Godthab': ('Greenland Standard Time', '001'),
    'America/Goose_Bay': ('Atlantic Standard Time', 'CA'),
    'America/Grand_Turk': ('Turks And Caicos Standard Time', '001'),
    'America/Grenada': ('SA Western Standard Time', 'GD'),
    'America/Guadeloupe': ('SA Western Standard Time', 'GP'),
    'America/Guatemala': ('Central America Standard Time', '001'),
    'America/Guayaquil': ('SA Pacific Standard Time', 'EC'),
    'America/Guyana': ('SA Western Standard Time', 'GY'),
    'America/Halifax': ('Atlantic Standard Time', '001'),
    'America/Havana': ('Cuba Standard Time', '001'),
    'America/Hermosillo': ('US Mountain Standard Time', 'MX'),
    'America/Indiana/Knox': ('Central Standard Time', 'US'),
    'America/Indiana/Marengo': ('US Eastern Standard Time', 'US'),
    'America/Indiana/Petersburg': ('Eastern Standard Time', 'US'),
    'America/Indiana/Tell_City': ('Central Standard Time', 'US'),
    'America/Indiana/Vevay': ('US Eastern Standard Time', 'US'),
    'America/Indiana/Vincennes': ('Eastern Standard Time', 'US'),
    'America/Indiana/Winamac': ('Eastern Standard Time', 'US'),
    'America/Indianapolis': ('US Eastern Standard Time', '001'),
    'America/Inuvik': ('Mountain Standard Time', 'CA'),
    'America/Iqaluit': ('Eastern Standard Time', 'CA'),
    'America/Jamaica': ('SA Pacific Standard Time', 'JM'),
    'America/Jujuy': ('Argentina Standard Time', 'AR'),
    'America/Juneau': ('Alaskan Standard Time', 'US'),
    'America/Kentucky/Monticello': ('Eastern Standard Time', 'US'),
    'America/Kralendijk': ('SA Western Standard Time', 'BQ'),
    'America/La_Paz': ('SA Western Standard Time', '001'),
    'America/Lima': ('SA Pacific Standard Time', 'PE'),
    'America/Los_Angeles': ('Pacific Standard Time', '001'),
    'America/Louisville': ('Eastern Standard Time', 'US'),
    'America/Lower_Princes': ('SA Western Standard Time', 'SX'),
    'America/Maceio': ('SA Eastern Standard Time', 'BR'),
    'America/Managua': ('Central America Standard Time', 'NI'),
    'America/Manaus': ('SA Western Standard Time', 'BR'),
    'America/Marigot': ('SA Western Standard Time', 'MF'),
    'America/Martinique': ('SA Western Standard Time', 'MQ'),
    'America/Matamoros': ('Central Standard Time', 'MX'),
    'America/Mazatlan': ('Mountain Standard Time (Mexico)', 'MX'),
    'America/Mendoza': ('Argentina Standard Time', 'AR'),
    'America/Menominee': ('Central Standard Time', 'US'),
    'America/Merida': ('Central Standard Time (Mexico)', 'MX'),
    'America/Metlakatla': ('Alaskan Standard Time', 'US'),
    'America/Mexico_City': ('Central Standard Time (Mexico)', '001'),
    'America/Miquelon': ('Saint Pierre Standard Time', '001'),
    'America/Moncton': ('Atlantic Standard Time', 'CA'),
    'America/Monterrey': ('Central Standard Time (Mexico)', 'MX'),
    'America/Montevideo': ('Montevideo Standard Time', '001'),
    'America/Montreal': ('Eastern Standard Time', 'CA'),
    'America/Montserrat': ('SA Western Standard Time', 'MS'),
    'America/Nassau': ('Eastern Standard Time', 'BS'),
    'America/New_York': ('Eastern Standard Time', '001'),
    'America/Nipigon': ('Eastern Standard Time', 'CA'),
    'America/Nome': ('Alaskan Standard Time', 'US'),
    'America/Noronha': ('UTC-02', 'BR'),
    'America/North_Dakota/Beulah': ('Central Standard Time', 'US'),
    'America/North_Dakota/Center': ('Central Standard Time', 'US'),
    'America/North_Dakota/New_Salem': ('Central Standard Time', 'US'),
    'America/Ojinaga': ('Mountain Standard Time', 'MX'),
    'America/Panama': ('SA Pacific Standard Time', 'PA'),
    'America/Pangnirtung': ('Eastern Standard Time', 'CA'),
    'America/Paramaribo': ('SA Eastern Standard Time', 'SR'),
    'America/Phoenix': ('US Mountain Standard Time', '001'),
    'America/Port-au-Prince': ('Haiti Standard Time', '001'),
    'America/Port_of_Spain': ('SA Western Standard Time', 'TT'),
    'America/Porto_Velho': ('SA Western Standard Time', 'BR'),
    'America/Puerto_Rico': ('SA Western Standard Time', 'PR'),
    'America/Punta_Arenas': ('Magallanes Standard Time', '001'),
    'America/Rainy_River': ('Central Standard Time', 'CA'),
    'America/Rankin_Inlet': ('Central Standard Time', 'CA'),
    'America/Recife': ('SA Eastern Standard Time', 'BR'),
    'America/Regina': ('Canada Central Standard Time', '001'),
    'America/Resolute': ('Central Standard Time', 'CA'),
    'America/Rio_Branco': ('SA Pacific Standard Time', 'BR'),
    'America/Santa_Isabel': ('Pacific Standard Time (Mexico)', 'MX'),
    'America/Santarem': ('SA Eastern Standard Time', 'BR'),
    'America/Santiago': ('Pacific SA Standard Time', '001'),
    'America/Santo_Domingo': ('SA Western Standard Time', 'DO'),
    'America/Sao_Paulo': ('E. South America Standard Time', '001'),
    'America/Scoresbysund': ('Azores Standard Time', 'GL'),
    'America/Sitka': ('Alaskan Standard Time', 'US'),
    'America/St_Barthelemy': ('SA Western Standard Time', 'BL'),
    'America/St_Johns': ('Newfoundland Standard Time', '001'),
    'America/St_Kitts': ('SA Western Standard Time', 'KN'),
    'America/St_Lucia': ('SA Western Standard Time', 'LC'),
    'America/St_Thomas': ('SA Western Standard Time', 'VI'),
    'America/St_Vincent': ('SA Western Standard Time', 'VC'),
    'America/Swift_Current': ('Canada Central Standard Time', 'CA'),
    'America/Tegucigalpa': ('Central America Standard Time', 'HN'),
    'America/Thule': ('Atlantic Standard Time', 'GL'),
    'America/Thunder_Bay': ('Eastern Standard Time', 'CA'),
    'America/Tijuana': ('Pacific Standard Time (Mexico)', '001'),
    'America/Toronto': ('Eastern Standard Time', 'CA'),
    'America/Tortola': ('SA Western Standard Time', 'VG'),
    'America/Vancouver': ('Pacific Standard Time', 'CA'),
    'America/Whitehorse': ('Yukon Standard Time', '001'),
    'America/Winnipeg': ('Central Standard Time', 'CA'),
    'America/Yakutat': ('Alaskan Standard Time', 'US'),
    'America/Yellowknife': ('Mountain Standard Time', 'CA'),
    'Antarctica/Casey': ('Central Pacific Standard Time', 'AQ'),
    'Antarctica/Davis': ('SE Asia Standard Time', 'AQ'),
    'Antarctica/DumontDUrville': ('West Pacific Standard Time', 'AQ'),
    'Antarctica/Macquarie': ('Tasmania Standard Time', 'AU'),
    'Antarctica/Mawson': ('West Asia Standard Time', 'AQ'),
    'Antarctica/McMurdo': ('New Zealand Standard Time', 'AQ'),
    'Antarctica/Palmer': ('SA Eastern Standard Time', 'AQ'),
    'Antarctica/Rothera': ('SA Eastern Standard Time', 'AQ'),
    'Antarctica/Syowa': ('E. Africa Standard Time', 'AQ'),
    'Antarctica/Vostok': ('Central Asia Standard Time', 'AQ'),
    'Arctic/Longyearbyen': ('W. Europe Standard Time', 'SJ'),
    'Asia/Aden': ('Arab Standard Time', 'YE'),
    'Asia/Almaty': ('Central Asia Standard Time', '001'),
    'Asia/Amman': ('Jordan Standard Time', '001'),
    'Asia/Anadyr': ('Russia Time Zone 11', 'RU'),
    'Asia/Aqtau': ('West Asia Standard Time', 'KZ'),
    'Asia/Aqtobe': ('West Asia Standard Time', 'KZ'),
    'Asia/Ashgabat': ('West Asia Standard Time', 'TM'),
    'Asia/Atyrau': ('West Asia Standard Time', 'KZ'),
    'Asia/Baghdad': ('Arabic Standard Time', '001'),
    'Asia/Bahrain': ('Arab Standard Time', 'BH'),
    'Asia/Baku': ('Azerbaijan Standard Time', '001'),
    'Asia/Bangkok': ('SE Asia Standard Time', '001'),
    'Asia/Barnaul': ('Altai Standard Time', '001'),
    'Asia/Beirut': ('Middle East Standard Time', '001'),
    'Asia/Bishkek': ('Central Asia Standard Time', 'KG'),
    'Asia/Brunei': ('Singapore Standard Time', 'BN'),
    'Asia/Calcutta': ('India Standard Time', '001'),
    'Asia/Chita': ('Transbaikal Standard Time', '001'),
    'Asia/Choibalsan': ('Ulaanbaatar Standard Time', 'MN'),
    'Asia/Colombo': ('Sri Lanka Standard Time', '001'),
    'Asia/Damascus': ('Syria Standard Time', '001'),
    'Asia/Dhaka': ('Bangladesh Standard Time', '001'),
    'Asia/Dili': ('Tokyo Standard Time', 'TL'),
    'Asia/Dubai': ('Arabian Standard Time', '001'),
    'Asia/Dushanbe': ('West Asia Standard Time', 'TJ'),
    'Asia/Famagusta': ('GTB Standard Time', 'CY'),
    'Asia/Gaza': ('West Bank Standard Time', 'PS'),
    'Asia/Hebron': ('West Bank Standard Time', '001'),
    'Asia/Hong_Kong': ('China Standard Time', 'HK'),
    'Asia/Hovd': ('W. Mongolia Standard Time', '001'),
    'Asia/Irkutsk': ('North Asia East Standard Time', '001'),
    'Asia/Jakarta': ('SE Asia Standard Time', 'ID'),
    'Asia/Jayapura': ('Tokyo Standard Time', 'ID'),
    'Asia/Jerusalem': ('Israel Standard Time', '001'),
    'Asia/Kabul': ('Afghanistan Standard Time', '001'),
    'Asia/Kamchatka': ('Russia Time Zone 11', '001'),
    'Asia/Karachi': ('Pakistan Standard Time', '001'),
    'Asia/Katmandu': ('Nepal Standard Time', '001'),
    'Asia/Khandyga': ('Yakutsk Standard Time', 'RU'),
    'Asia/Krasnoyarsk': ('North Asia Standard Time', '001'),
    'Asia/Kuala_Lumpur': ('Singapore Standard Time', 'MY'),
    'Asia/Kuching': ('Singapore Standard Time', 'MY'),
    'Asia/Kuwait': ('Arab Standard Time', 'KW'),
    'Asia/Macau': ('China Standard Time', 'MO'),
    'Asia/Magadan': ('Magadan Standard Time', '001'),
    'Asia/Makassar': ('Singapore Standard Time', 'ID'),
    'Asia/Manila': ('Singapore Standard Time', 'PH'),
    'Asia/Muscat': ('Arabian Standard Time', 'OM'),
    'Asia/Nicosia': ('GTB Standard Time', 'CY'),
    'Asia/Novokuznetsk': ('North Asia Standard Time', 'RU'),
    'Asia/Novosibirsk': ('N. Central Asia Standard Time', '001'),
    'Asia/Omsk': ('Omsk Standard Time', '001'),
    'Asia/Oral': ('West Asia Standard Time', 'KZ'),
    'Asia/Phnom_Penh': ('SE Asia Standard Time', 'KH'),
    'Asia/Pontianak': ('SE Asia Standard Time', 'ID'),
    'Asia/Pyongyang': ('North Korea Standard Time', '001'),
    'Asia/Qatar': ('Arab Standard Time', 'QA'),
    'Asia/Qostanay': ('Central Asia Standard Time', 'KZ'),
    'Asia/Qyzylorda': ('Qyzylorda Standard Time', '001'),
    'Asia/Rangoon': ('Myanmar Standard Time', '001'),
    'Asia/Riyadh': ('Arab Standard Time', '001'),
    'Asia/Saigon': ('SE Asia Standard Time', 'VN'),
    'Asia/Sakhalin': ('Sakhalin Standard Time', '001'),
    'Asia/Samarkand': ('West Asia Standard Time', 'UZ'),
    'Asia/Seoul': ('Korea Standard Time', '001'),
    'Asia/Shanghai': ('China Standard Time', '001'),
    'Asia/Singapore': ('Singapore Standard Time', '001'),
    'Asia/Srednekolymsk': ('Russia Time Zone 10', '001'),
    'Asia/Taipei': ('Taipei Standard Time', '001'),
    'Asia/Tashkent': ('West Asia Standard Time', '001'),
    'Asia/Tbilisi': ('Georgian Standard Time', '001'),
    'Asia/Tehran': ('Iran Standard Time', '001'),
    'Asia/Thimphu': ('Bangladesh Standard Time', 'BT'),
    'Asia/Tokyo': ('Tokyo Standard Time', '001'),
    'Asia/Tomsk': ('Tomsk Standard Time', '001'),
    'Asia/Ulaanbaatar': ('Ulaanbaatar Standard Time', '001'),
    'Asia/Urumqi': ('Central Asia Standard Time', 'CN'),
    'Asia/Ust-Nera': ('Vladivostok Standard Time', 'RU'),
    'Asia/Vientiane': ('SE Asia Standard Time', 'LA'),
    'Asia/Vladivostok': ('Vladivostok Standard Time', '001'),
    'Asia/Yakutsk': ('Yakutsk Standard Time', '001'),
    'Asia/Yekaterinburg': ('Ekaterinburg Standard Time', '001'),
    'Asia/Yerevan': ('Caucasus Standard Time', '001'),
    'Atlantic/Azores': ('Azores Standard Time', '001'),
    'Atlantic/Bermuda': ('Atlantic Standard Time', 'BM'),
    'Atlantic/Canary': ('GMT Standard Time', 'ES'),
    'Atlantic/Cape_Verde': ('Cape Verde Standard Time', '001'),
    'Atlantic/Faeroe': ('GMT Standard Time', 'FO'),
    'Atlantic/Madeira': ('GMT Standard Time', 'PT'),
    'Atlantic/Reykjavik': ('Greenwich Standard Time', '001'),
    'Atlantic/South_Georgia': ('UTC-02', 'GS'),
    'Atlantic/St_Helena': ('Greenwich Standard Time', 'SH'),
    'Atlantic/Stanley': ('SA Eastern Standard Time', 'FK'),
    'Australia/Adelaide': ('Cen. Australia Standard Time', '001'),
    'Australia/Brisbane': ('E. Australia Standard Time', '001'),
    'Australia/Broken_Hill': ('Cen. Australia Standard Time', 'AU'),
    'Australia/Currie': ('Tasmania Standard Time', 'AU'),
    'Australia/Darwin': ('AUS Central Standard Time', '001'),
    'Australia/Eucla': ('Aus Central W. Standard Time', '001'),
    'Australia/Hobart': ('Tasmania Standard Time', '001'),
    'Australia/Lindeman': ('E. Australia Standard Time', 'AU'),
    'Australia/Lord_Howe': ('Lord Howe Standard Time', '001'),
    'Australia/Melbourne': ('AUS Eastern Standard Time', 'AU'),
    'Australia/Perth': ('W. Australia Standard Time', '001'),
    'Australia/Sydney': ('AUS Eastern Standard Time', '001'),
    'CST6CDT': ('Central Standard Time', 'ZZ'),
    'EST5EDT': ('Eastern Standard Time', 'ZZ'),
    'Etc/GMT': ('UTC', '001'),
    'Etc/GMT+1': ('Cape Verde Standard Time', 'ZZ'),
    'Etc/GMT+10': ('Hawaiian Standard Time', 'ZZ'),
    'Etc/GMT+11': ('UTC-11', '001'),
    'Etc/GMT+12': ('Dateline Standard Time', '001'),
    'Etc/GMT+2': ('UTC-02', '001'),
    'Etc/GMT+3': ('SA Eastern Standard Time', 'ZZ'),
    'Etc/GMT+4': ('SA Western Standard Time', 'ZZ'),
    'Etc/GMT+5': ('SA Pacific Standard Time', 'ZZ'),
    'Etc/GMT+6': ('Central America Standard Time', 'ZZ'),
    'Etc/GMT+7': ('US Mountain Standard Time', 'ZZ'),
    'Etc/GMT+8': ('UTC-08', '001'),
    'Etc/GMT+9': ('UTC-09', '001'),
    'Etc/GMT-1': ('W. Central Africa Standard Time', 'ZZ'),
    'Etc/GMT-10': ('West Pacific Standard Time', 'ZZ'),
    'Etc/GMT-11': ('Central Pacific Standard Time', 'ZZ'),
    'Etc/GMT-12': ('UTC+12', '001'),
    'Etc/GMT-13': ('UTC+13', '001'),
    'Etc/GMT-14': ('Line Islands Standard Time', 'ZZ'),
    'Etc/GMT-2': ('South Africa Standard Time', 'ZZ'),
    'Etc/GMT-3': ('E. Africa Standard Time', 'ZZ'),
    'Etc/GMT-4': ('Arabian Standard Time', 'ZZ'),
    'Etc/GMT-5': ('West Asia Standard Time', 'ZZ'),
    'Etc/GMT-6': ('Central Asia Standard Time', 'ZZ'),
    'Etc/GMT-7': ('SE Asia Standard Time', 'ZZ'),
    'Etc/GMT-8': ('Singapore Standard Time', 'ZZ'),
    'Etc/GMT-9': ('Tokyo Standard Time', 'ZZ'),
    'Etc/UTC': ('UTC', 'ZZ'),
    'Europe/Amsterdam': ('W. Europe Standard Time', 'NL'),
    'Europe/Andorra': ('W. Europe Standard Time', 'AD'),
    'Europe/Astrakhan': ('Astrakhan Standard Time', '001'),
    'Europe/Athens': ('GTB Standard Time', 'GR'),
    'Europe/Belgrade': ('Central Europe Standard Time', 'RS'),
    'Europe/Berlin': ('W. Europe Standard Time', '001'),
    'Europe/Bratislava': ('Central Europe Standard Time', 'SK'),
    'Europe/Brussels': ('Romance Standard Time', 'BE'),
    'Europe/Bucharest': ('GTB Standard Time', '001'),
    'Europe/Budapest': ('Central Europe Standard Time', '001'),
    'Europe/Busingen': ('W. Europe Standard Time', 'DE'),
    'Europe/Chisinau': ('E. Europe Standard Time', '001'),
    'Europe/Copenhagen': ('Romance Standard Time', 'DK'),
    'Europe/Dublin': ('GMT Standard Time', 'IE'),
    'Europe/Gibraltar': ('W. Europe Standard Time', 'GI'),
    'Europe/Guernsey': ('GMT Standard Time', 'GG'),
    'Europe/Helsinki': ('FLE Standard Time', 'FI'),
    'Europe/Isle_of_Man': ('GMT Standard Time', 'IM'),
    'Europe/Istanbul': ('Turkey Standard Time', '001'),
    'Europe/Jersey': ('GMT Standard Time', 'JE'),
    'Europe/Kaliningrad': ('Kaliningrad Standard Time', '001'),
    'Europe/Kiev': ('FLE Standard Time', '001'),
    'Europe/Kirov': ('Russian Standard Time', 'RU'),
    'Europe/Lisbon': ('GMT Standard Time', 'PT'),
    'Europe/Ljubljana': ('Central Europe Standard Time', 'SI'),
    'Europe/London': ('GMT Standard Time', '001'),
    'Europe/Luxembourg': ('W. Europe Standard Time', 'LU'),
    'Europe/Madrid': ('Romance Standard Time', 'ES'),
    'Europe/Malta': ('W. Europe Standard Time', 'MT'),
    'Europe/Mariehamn': ('FLE Standard Time', 'AX'),
    'Europe/Minsk': ('Belarus Standard Time', '001'),
    'Europe/Monaco': ('W. Europe Standard Time', 'MC'),
    'Europe/Moscow': ('Russian Standard Time', '001'),
    'Europe/Oslo': ('W. Europe Standard Time', 'NO'),
    'Europe/Paris': ('Romance Standard Time', '001'),
    'Europe/Podgorica': ('Central Europe Standard Time', 'ME'),
    'Europe/Prague': ('Central Europe Standard Time', 'CZ'),
    'Europe/Riga': ('FLE Standard Time', 'LV'),
    'Europe/Rome': ('W. Europe Standard Time', 'IT'),
    'Europe/Samara': ('Russia Time Zone 3', '001'),
    'Europe/San_Marino': ('W. Europe Standard Time', 'SM'),
    'Europe/Sarajevo': ('Central European Standard Time', 'BA'),
    'Europe/Saratov': ('Saratov Standard Time', '001'),
    'Europe/Simferopol': ('Russian Standard Time', 'UA'),
    'Europe/Skopje': ('Central European Standard Time', 'MK'),
    'Europe/Sofia': ('FLE Standard Time', 'BG'),
    'Europe/Stockholm': ('W. Europe Standard Time', 'SE'),
    'Europe/Tallinn': ('FLE Standard Time', 'EE'),
    'Europe/Tirane': ('Central Europe Standard Time', 'AL'),
    'Europe/Ulyanovsk': ('Astrakhan Standard Time', 'RU'),
    'Europe/Uzhgorod': ('FLE Standard Time', 'UA'),
    'Europe/Vaduz': ('W. Europe Standard Time', 'LI'),
    'Europe/Vatican': ('W. Europe Standard Time', 'VA'),
    'Europe/Vienna': ('W. Europe Standard Time', 'AT'),
    'Europe/Vilnius': ('FLE Standard Time', 'LT'),
    'Europe/Volgograd': ('Volgograd Standard Time', '001'),
    'Europe/Warsaw': ('Central European Standard Time', '001'),
    'Europe/Zagreb': ('Central European Standard Time', 'HR'),
    'Europe/Zaporozhye': ('FLE Standard Time', 'UA'),
    'Europe/Zurich': ('W. Europe Standard Time', 'CH'),
    'Indian/Antananarivo': ('E. Africa Standard Time', 'MG'),
    'Indian/Chagos': ('Central Asia Standard Time', 'IO'),
    'Indian/Christmas': ('SE Asia Standard Time', 'CX'),
    'Indian/Cocos': ('Myanmar Standard Time', 'CC'),
    'Indian/Comoro': ('E. Africa Standard Time', 'KM'),
    'Indian/Kerguelen': ('West Asia Standard Time', 'TF'),
    'Indian/Mahe': ('Mauritius Standard Time', 'SC'),
    'Indian/Maldives': ('West Asia Standard Time', 'MV'),
    'Indian/Mauritius': ('Mauritius Standard Time', '001'),
    'Indian/Mayotte': ('E. Africa Standard Time', 'YT'),
    'Indian/Reunion': ('Mauritius Standard Time', 'RE'),
    'MST7MDT': ('Mountain Standard Time', 'ZZ'),
    'PST8PDT': ('Pacific Standard Time', 'ZZ'),
    'Pacific/Apia': ('Samoa Standard Time', '001'),
    'Pacific/Auckland': ('New Zealand Standard Time', '001'),
    'Pacific/Bougainville': ('Bougainville Standard Time', '001'),
    'Pacific/Chatham': ('Chatham Islands Standard Time', '001'),
    'Pacific/Easter': ('Easter Island Standard Time', '001'),
    'Pacific/Efate': ('Central Pacific Standard Time', 'VU'),
    'Pacific/Enderbury': ('UTC+13', 'KI'),
    'Pacific/Fakaofo': ('UTC+13', 'TK'),
    'Pacific/Fiji': ('Fiji Standard Time', '001'),
    'Pacific/Funafuti': ('UTC+12', 'TV'),
    'Pacific/Galapagos': ('Central America Standard Time', 'EC'),
    'Pacific/Gambier': ('UTC-09', 'PF'),
    'Pacific/Guadalcanal': ('Central Pacific Standard Time', '001'),
    'Pacific/Guam': ('West Pacific Standard Time', 'GU'),
    'Pacific/Honolulu': ('Hawaiian Standard Time', '001'),
    'Pacific/Johnston': ('Hawaiian Standard Time', 'UM'),
    'Pacific/Kiritimati': ('Line Islands Standard Time', '001'),
    'Pacific/Kosrae': ('Central Pacific Standard Time', 'FM'),
    'Pacific/Kwajalein': ('UTC+12', 'MH'),
    'Pacific/Majuro': ('UTC+12', 'MH'),
    'Pacific/Marquesas': ('Marquesas Standard Time', '001'),
    'Pacific/Midway': ('UTC-11', 'UM'),
    'Pacific/Nauru': ('UTC+12', 'NR'),
    'Pacific/Niue': ('UTC-11', 'NU'),
    'Pacific/Norfolk': ('Norfolk Standard Time', '001'),
    'Pacific/Noumea': ('Central Pacific Standard Time', 'NC'),
    'Pacific/Pago_Pago': ('UTC-11', 'AS'),
    'Pacific/Palau': ('Tokyo Standard Time', 'PW'),
    'Pacific/Pitcairn': ('UTC-08', 'PN'),
    'Pacific/Ponape': ('Central Pacific Standard Time', 'FM'),
    'Pacific/Port_Moresby': ('West Pacific Standard Time', '001'),
    'Pacific/Rarotonga': ('Hawaiian Standard Time', 'CK'),
    'Pacific/Saipan': ('West Pacific Standard Time', 'MP'),
    'Pacific/Tahiti': ('Hawaiian Standard Time', 'PF'),
    'Pacific/Tarawa': ('UTC+12', 'KI'),
    'Pacific/Tongatapu': ('Tonga Standard Time', '001'),
    'Pacific/Truk': ('West Pacific Standard Time', 'FM'),
    'Pacific/Wake': ('UTC+12', 'UM'),
    'Pacific/Wallis': ('UTC+12', 'WF'),
}

# Add timezone names used by IANA that are not found in the CLDR.
# Use 'noterritory' unless you want to override the standard mapping
# (in which case, '001').
# TODO: A full list of the IANA names missing in CLDR can be found with:
#
#    sorted(set(zoneinfo.available_timezones()) - set(CLDR_TO_MS_TIMEZONE_MAP))
#
IANA_TO_MS_TIMEZONE_MAP = dict(
    CLDR_TO_MS_TIMEZONE_MAP,
    **{
        'Asia/Kolkata': ('India Standard Time', 'noterritory'),
        'GMT': ('UTC', 'noterritory'),
        'UTC': ('UTC', 'noterritory'),
    }
)

# Reverse map from Microsoft timezone ID to IANA timezone name. Non-CLDR timezone ID's can be added here.
MS_TIMEZONE_TO_IANA_MAP = dict(
    {v[0]: k for k, v in IANA_TO_MS_TIMEZONE_MAP.items() if v[1] == DEFAULT_TERRITORY},
    **{
        'tzone://Microsoft/Utc': 'UTC',
    }
)
