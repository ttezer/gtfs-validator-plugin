## DQ — Veri Kalitesi / Kullanıcı Deneyimi

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| DQ_003 | Hat açıklaması eksik | BİLGİ | Quality |
| DQ_004 | Hat URL'si eksik | BİLGİ | Quality |
| DQ_005 | Geçerli servis dönemi yok | YÜKSEK | Quality |
| DQ_005b | Hiçbir seferin durak zamanı yok | YÜKSEK | Quality |
| DQ_005c | Koordinatsız durak oranı çok yüksek | YÜKSEK | Quality |
| DQ_006 | Şekil olmayan sefer oranı çok yüksek | YÜKSEK | Quality |
| DQ_009 | Seferlerde durak zamanı yok | BİLGİ | Quality |
| DQ_010 | Acente hiçbir hatta kullanılmıyor | BİLGİ | Quality |
| DQ_011 | Yalnızca bir durak var | DÜŞÜK | Quality |
| DQ_012 | Çok fazla acente, agency_id kullanılmıyor | DÜŞÜK | Quality |
| DQ_013 | Çok az sefer | BİLGİ | Analytics |
| DQ_016 | Değerde fazladan boşluk karakteri | ORTA | Quality |
| DQ_017 | Şüpheli koordinat değeri | BİLGİ | Quality |
| DQ_018 | Önerilen alanda tamamen büyük harf (all-caps) | ORTA | Quality |
| DQ_019 | Önerilen alanda tamamen küçük harf (all-lowercase) | ORTA | Quality |
| DQ_020 | Önerilen alan eksik veya boş | DÜŞÜK | Quality |
| DQ_021 | Birincil anahtar yineleniyor — genel ikincil sinyal (STP_001/RTS_001 ile örtüşebilir) | YÜKSEK | Spec |
| DQ_022 | Durakların %80+'i aynı stop_name değerini paylaşıyor | YÜKSEK | Quality |

## VAT — Varlık Analitik Tespiti

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| VAT_001 | Hat güzergah benzerliği (muhtemel kopya hat) | ORTA | Analytics |
| VAT_002 | Aktarma merkezi tanımsız — çok sayıda hat geçiyor ama aktarma yok | BİLGİ | Analytics |
| VAT_003 | Sefer süresi istatistiksel aykırı değer | DÜŞÜK | Analytics |
| VAT_005 | İzole durak kümesi — ağ grafiğinde ana bileşenden kopuk duraklar | ORTA | Analytics |
| VAT_006 | Hizmet yoğunluğu dengesizliği — tek hat feed sefer sayısının büyük bölümünü oluşturuyor | BİLGİ | Analytics |
| VAT_007 | Terminus aktarma eksikliği — terminal durağa başka hat geliyor ama aktarma tanımlı değil | BİLGİ | Analytics |
| VAT_008 | Aynı shape feed hatlarının %30+'ında kullanılıyor | BİLGİ | Analytics |

## JPN

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| JPN_001 | GTFS-JP: durak adında kana (ja-Hrkt) okuması eksik | ORTA | Quality |
| JPN_002 | GTFS-JP: jp_office_id office_jp.txt'te tanımlı değil | YÜKSEK | Interop |
| JPN_003 | GTFS-JP: agency_jp.agency_id agency.txt'te tanımlı değil | YÜKSEK | Interop |
| JPN_004 | GTFS-JP: translations.txt eksik | YÜKSEK | Interop |
| JPN_005 | GTFS-JP: office_jp.office_name boş | YÜKSEK | Interop |
| JPN_006 | GTFS-JP: fare_attributes eksik veya farklı ücret profilleri için fare_rules eksik | ORTA | Quality |
| JPN_007 | GTFS-JP: feed_info.txt eksik | ORTA | Quality |
| JPN_008 | GTFS-JP: hat adının kana okuması eksik | ORTA | Quality |
| JPN_009 | GTFS-JP: trip_headsign kana okuması eksik | ORTA | Quality |
| JPN_010 | GTFS-JP: işletici adının kana okuması eksik | ORTA | Quality |
| JPN_011 | GTFS-JP: tek işletici olsa bile agency_id zorunlu | YÜKSEK | Interop |
| JPN_012 | GTFS-JP: agency_jp.agency_id eksik | YÜKSEK | Interop |
| JPN_013 | GTFS-JP: agency_zip_number biçimi geçersiz | ORTA | Quality |
| JPN_014 | GTFS-JP: office_jp.office_id eksik veya tekrarlı | YÜKSEK | Interop |
| JPN_015 | GTFS-JP legacy: routes_jp.route_id eksik, tekrarlı veya routes.txt içinde tanımsız | YÜKSEK | Interop |
| JPN_016 | GTFS-JP: pattern_jp veya legacy routes_jp route_update_date geçersiz | ORTA | Quality |
| JPN_017 | GTFS-JP: jp_pattern_id eksik veya tekrarlı | YÜKSEK | Interop |
| JPN_018 | GTFS-JP: jp_pattern_id tanımsız | YÜKSEK | Interop |
| JPN_019 | GTFS-JP: kana çeviri referansı geçersiz | ORTA | Interop |
| JPN_020 | GTFS-JP: ofis iletişim biçimi şüpheli | ORTA | Quality |
| JPN_021 | GTFS-JP: kana çevirisi tutarsız | ORTA | Quality |
| JPN_022 | GTFS-JP v4: ana alan zorunluluğu eksik | ORTA | Interop |
| JPN_023 | GTFS-JP: feed_lang ja değil | YÜKSEK | Interop |
| JPN_024 | GTFS-JP: agency_lang ja değil | YÜKSEK | Interop |
| JPN_025 | GTFS-JP: agency_timezone Asia/Tokyo değil | YÜKSEK | Interop |
| JPN_026 | GTFS-JP: ücret para birimi JPY değil | YÜKSEK | Interop |
| JPN_027 | GTFS-JP V3: route_type 3 değil | YÜKSEK | Interop |
| JPN_028 | GTFS-JP v3: zorunlu kana çevirisi eksik | ORTA | Quality |
| JPN_029 | GTFS-JP v4: önerilen kana çevirisi eksik | DÜŞÜK | Quality |
| JPN_030 | GTFS-JP v3: zorunlu Japonca çeviri eksik | ORTA | Quality |
| JPN_031 | GTFS-JP: bölgeye bağlı ücret kullanılan durakta zone_id eksik | YÜKSEK | Interop |
| JPN_032 | GTFS-JP V3: agency_id Corporate Number biçiminde değil | ORTA | Interop |
| JPN_033 | GTFS-JP: özel dosya veya alan adında ayrılmış jp ad alanı kullanılmış | ORTA | Interop |
