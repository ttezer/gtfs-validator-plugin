## ARC — Arşiv / Dosya Seviyesi

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| ARC_001 | ZIP arşivi açılamadı | KRİTİK | Spec |
| ARC_002 | Dosya UTF-8 ile okunamıyor | KRİTİK | Quality |
| ARC_003 | İsteğe bağlı dosyada UTF-8 kodlama hatası | ORTA | Quality |
| ARC_004 | Zorunlu dosya eksik | KRİTİK | Spec |
| ARC_006 | İsteğe bağlı GTFS dosyası mevcut | BİLGİ | Analytics |
| ARC_007 | GTFS dışı tanınmayan dosya | BİLGİ | Quality |
| ARC_008 | Takvim dosyası eksik (calendar.txt ve calendar_dates.txt) | KRİTİK | Spec |
| ARC_031 | translations.txt varken feed_info.txt eksik | KRİTİK | Spec |
| ARC_009 | Opsiyonel dosyada veri satırı yok | BİLGİ | Quality |
| ARC_010 | Dosya UTF-8 BOM içeriyor | BİLGİ | Quality |
| ARC_011 | Dosya boyutu (bilgi) | BİLGİ | Analytics |
| ARC_012 | Satır sütun sayısı başlıkla uyuşmuyor | KRİTİK | Spec |
| ARC_013 | CSV ayrıştırma hatası | KRİTİK | Spec |
| ARC_014 | Başlıkta baştaki/sondaki boşluk | ORTA | Quality |
| ARC_015 | Yinelenen başlık sütunu | KRİTİK | Interop |
| ARC_025 | Zorunlu sütun başlıkta hiç yok (header'da eksik) | KRİTİK | Spec |
| ARC_017 | Bilinmeyen sütun (GTFS spesifikasyonunda tanımlı değil) | BİLGİ | Quality |
| ARC_018 | Boş veri satırı | ORTA | Quality |
| ARC_019 | Başlıkta boş sütun adı | YÜKSEK | Quality |
| ARC_020 | Önerilen GTFS dosyası eksik (shapes.txt veya feed_info.txt) | DÜŞÜK | Quality |
| ARC_021 | Alanda yazdırılamaz veya sorunlu karakter | DÜŞÜK | Quality |
| ARC_022 | Dosya satır sayısı 1.000.000 bilgi eşiğini aşıyor | BİLGİ | Analytics |
| ARC_023 | ZIP içinde iç içe ZIP dosyası | ORTA | Quality |
| ARC_024 | GTFS .txt dosyası alt dizinde (parse edilemez) | ORTA | Spec |
| ARC_026 | Dosyada hatalı satır sonu karakteri | ORTA | Spec |
| ARC_027 | ZIP girdisinde kullanıcı okuma izni yok | BİLGİ | Quality |
| ARC_028 | GTFS yayın URL'si .zip dosya adıyla bitmiyor | DÜŞÜK | Quality |
| ARC_029 | Sıkıştırma koruması: arşiv zip-bomb sınırını aştı | KRİTİK | Quality |
| ARC_030 | Alan değerinde sekme veya satır sonu karakteri | YÜKSEK | Spec |
| ARC_032 | Alan değerinde HTML etiketi veya kaçış dizisi | YÜKSEK | Spec |
| ARC_033 | Alan değerinde kaçırılmamış tırnak (RFC 4180) | YÜKSEK | Spec |
| ARC_034 | Başlık satırı veri satırı olarak tekrarlanmış | YÜKSEK | Spec |
| ARC_035 | Zorunlu dosya boş | KRİTİK | Spec |
| ARC_036 | ZIP akış başlığı merkez diziniyle çelişiyor | DÜŞÜK | Quality |
| ARC_037 | ID alanında ASCII dışı karakter | DÜŞÜK | Quality |

## BKR — Booking Rules (Rezervasyon Kuralları)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| BKR_001 | Önceki gün rezervasyon alanı yasak bağlamda dolu | YÜKSEK | Spec |
| BKR_003 | prior_notice_start_time yalnızca prior_notice_start_day ile kullanılabilir | YÜKSEK | Spec |
| BKR_004 | Anlık rezervasyonda prior_notice alanları yasak | YÜKSEK | Spec |
| BKR_005 | prior_notice_duration_max yalnızca booking_type=1 ile geçerli (booking_type=0/2 ile yasak) | ORTA | Spec |
| BKR_006 | prior_notice_duration_min geçersiz (≤ 0 veya sayısal değil) | YÜKSEK | Spec |
| BKR_007 | booking_type=1 için prior_notice_duration_min zorunlu | KRİTİK | Spec |
| BKR_008 | booking_type=2 için prior_notice_last_day zorunlu | KRİTİK | Spec |
| BKR_009 | booking_type=2 için prior_notice_last_time zorunlu | KRİTİK | Spec |
| BKR_010 | prior_notice_start_day belirtilmişse prior_notice_start_time zorunlu | YÜKSEK | Spec |
| BKR_011 | prior_notice_last_day > prior_notice_start_day: rezervasyon penceresi geçersiz | YÜKSEK | Interop |
| BKR_012 | booking_type=2 iken prior_notice_duration_min yasak | ORTA | Spec |
| BKR_013 | prior_notice_last_time yalnızca prior_notice_last_day ile kullanılabilir | YÜKSEK | Spec |
| BKR_014 | prior_notice_service_id yalnızca booking_type=2 ile kullanılabilir | YÜKSEK | Spec |
| BKR_015 | prior_notice_service_id bulunamadı (calendar/calendar_dates) | KRİTİK | Spec |
| BKR_016 | booking_type eksik veya geçersiz | KRİTİK | Spec |
| BKR_017 | pickup_booking_rule_id bulunamadı (booking_rules) | KRİTİK | Spec |
| BKR_018 | drop_off_booking_rule_id bulunamadı (booking_rules) | KRİTİK | Spec |
| BKR_019 | booking_rule_id eksik veya yineleniyor | KRİTİK | Spec |
| BKR_024 | booking_type=1 ve duration_max varken prior_notice_start_day yasak | ORTA | Spec |
| BKR_020 | booking_url geçersiz | ORTA | Spec |
| BKR_021 | info_url geçersiz | DÜŞÜK | Spec |
| BKR_022 | phone_number geçersiz | DÜŞÜK | Quality |
| BKR_023 | prior_notice sayı alanı tam sayı değil | ORTA | Spec |
| BKR_025 | prior_notice zaman alanı geçerli saat değil | ORTA | Spec |

## AGN — Agency (İşletici)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| AGN_002 | agency_name eksik | KRİTİK | Spec |
| AGN_003 | agency_url eksik veya geçersiz | KRİTİK | Spec |
| AGN_004 | agency_timezone eksik veya geçersiz | KRİTİK | Spec |
| AGN_005 | Kuruluşlar arası saat dilimi tutarsızlığı | ORTA | Spec |
| AGN_006 | agency_lang geçersiz | DÜŞÜK | Spec |
| AGN_007 | agency_phone geçersiz | DÜŞÜK | Quality |
| AGN_008 | agency_fare_url geçersiz | DÜŞÜK | Spec |
| AGN_009 | agency_email geçersiz | DÜŞÜK | Spec |
| AGN_010 | agency_id yineleniyor | KRİTİK | Spec |
| AGN_011 | Birden fazla kuruluşta agency_id yok | KRİTİK | Spec |
| AGN_012 | cemv_support geçersiz (agency) | DÜŞÜK | Spec |
| AGN_013 | Feed dili ve ajans dili uyuşmuyor | DÜŞÜK | Interop |
| AGN_014 | Birden fazla kuruluş var ama agency.txt agency_id eksik | KRİTİK | Spec |
| AGN_015 | agency_url güvensiz http (https önerilir) | BİLGİ | Quality |
| AGN_016 | agency_phone şüpheli/yer-tutucu numara | BİLGİ | Quality |
| AGN_017 | Agency'ler arası agency_lang tutarsız | DÜŞÜK | Interop |
| AGN_018 | Tek kuruluşta agency_id boş | BİLGİ | Quality |

## STP — Stops (Duraklar)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| STP_001 | stop_id yineleniyor | KRİTİK | Spec |
| STP_002 | stop_id boş | KRİTİK | Spec |
| STP_003 | stop_name eksik veya stop_lat/stop_lon aralık dışı (aynı ID altında iki ayrı koşul) | KRİTİK | Spec |
| STP_004 | stop_lat sayısal değil | KRİTİK | Spec |
| STP_005 | stop_lon geçersiz veya aralık dışı | KRİTİK | Spec |
| STP_006 | stop_lat eksik | KRİTİK | Spec |
| STP_007 | stop_lon eksik | KRİTİK | Spec |
| STP_008 | location_type geçersiz | YÜKSEK | Spec |
| STP_009 | parent_station bulunamadı | KRİTİK | Spec |
| STP_010 | parent_station location_type=1 değil | YÜKSEK | Spec |
| STP_011 | Giriş/çıkış/boarding için parent_station zorunlu | KRİTİK | Spec |
| STP_012 | stop_times'ta istasyon veya giriş kullanılmış | KRİTİK | Spec |
| STP_013 | wheelchair_boarding geçersiz | DÜŞÜK | Spec |
| STP_014 | stop_timezone geçersiz | ORTA | Spec |
| STP_015 | level_id bulunamadı | KRİTİK | Spec |
| STP_016 | İki durak tam aynı koordinatta | ORTA | Quality |
| STP_017 | İki durak birbirine çok yakın | DÜŞÜK | Quality |
| STP_018 | Hiç durak yok | KRİTİK | Spec |
| STP_019 | stop_name çok uzun | BİLGİ | Quality |
| STP_020 | Hiç sefer geçmeyen durak | ORTA | Analytics |
| STP_021 | Boarding area parent'ı platform değil | YÜKSEK | Quality |
| STP_022 | stop_code eksik | ORTA | Quality |
| STP_023 | tts_stop_name geçersiz | DÜŞÜK | Quality |
| STP_024 | stop_access enum aralığı dışında değer (K2 ham alan kontrolü) | BİLGİ | Quality |
| STP_026 | stop_access geçersiz değer | DÜŞÜK | Spec |
| STP_028 | stop_code çok uzun | BİLGİ | Quality |
| STP_029 | Durak istasyon içinde ama koordinat çok uzakta | ORTA | Quality |
| STP_030 | Üst istasyonun alt durağı yok | ORTA | Quality |
| STP_031 | Durak adı ve açıklaması aynı | BİLGİ | Quality |
| STP_032 | Pathway bağlantılı platform için parent_station eksik | ORTA | Quality |
| STP_033 | Durak zone_id eksik (ücret hesabı için gerekli) | BİLGİ | Quality |
| STP_034 | stop_url acente URL'siyle aynı | DÜŞÜK | Quality |
| STP_035 | stop_url hat URL'siyle aynı | DÜŞÜK | Quality |
| STP_036 | İstasyonun (location_type=1) parent_station değeri var | DÜŞÜK | Spec |
| STP_037 | Bazı duraklar tekerlekli sandalye erişilebilirliği (wheelchair_boarding) bildirmemiş | BİLGİ | Quality |
| STP_038 | Hiçbir durak tekerlekli sandalye erişilebilirliği (wheelchair_boarding) bildirmemiş | BİLGİ | Quality |
| STP_039 | stop_code birden fazla durakta kullanılıyor | DÜŞÜK | Quality |
| STP_040 | Durak adı gereksiz genel stop/station sözcüğü içeriyor | DÜŞÜK | Quality |
| STP_044 | platform_code gereksiz 'platform/track' sözcüğü içeriyor | DÜŞÜK | Quality |
| STP_045 | platform_code var ama parent_station boş | BİLGİ | Quality |
| STP_046 | parent_station boş durak bir istasyonun hemen yanında | DÜŞÜK | Quality |
| STP_047 | Aynı yer için iki istasyon kaydı | DÜŞÜK | Quality |
| STP_041 | Alt durak adı üst istasyon adını içermiyor | DÜŞÜK | Quality |
| STP_042 | stop_url geçersiz | DÜŞÜK | Spec |
| STP_043 | stop_access yasak bağlamda kullanılmış | ORTA | Spec |

## RTS — Routes (Hatlar)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| RTS_001 | route_id yineleniyor | KRİTİK | Spec |
| RTS_002 | agency_id bulunamadı | KRİTİK | Spec |
| RTS_003 | route_short_name ve route_long_name ikisi de eksik | KRİTİK | Spec |
| RTS_004 | route_type eksik veya geçersiz | KRİTİK | Spec |
| RTS_005 | route_url geçersiz | ORTA | Spec |
| RTS_006 | route_color geçersiz hex renk | ORTA | Spec |
| RTS_007 | route_text_color geçersiz hex renk | ORTA | Spec |
| RTS_008 | Hat rengi ve metin rengi kontrast düşük | ORTA | Quality |
| RTS_010 | route_short_name çok uzun | DÜŞÜK | Quality |
| RTS_011 | route_long_name çok uzun | BİLGİ | Quality |
| RTS_012 | Seferi olmayan hat | ORTA | Quality |
| RTS_013 | continuous_pickup geçersiz | DÜŞÜK | Spec |
| RTS_016 | Hiçbir aktif servis günü olmayan hat | DÜŞÜK | Quality |
| RTS_017 | Shape tanımlı olmayan hat | BİLGİ | Quality |
| RTS_018 | continuous_drop_off geçersiz | DÜŞÜK | Spec |
| RTS_019 | Yinelenen hat adı | ORTA | Quality |
| RTS_020 | Hat ve acente aynı URL'yi paylaşıyor | BİLGİ | Quality |
| RTS_021 | Kısa hat adı Google Transit eşiğini (6 karakter) aşıyor | DÜŞÜK | Quality |
| RTS_022 | Uzun hat adı kısa adı içeriyor | DÜŞÜK | Quality |
| RTS_023 | Hat açıklaması hat adının kopyası | BİLGİ | Quality |
| RTS_024 | cemv_support geçersiz (route) | DÜŞÜK | Spec |
| RTS_025 | routes.txt agency_id boş (önerilen) | BİLGİ | Quality |
| RTS_026 | Yinelenen kısa hat adı | BİLGİ | Quality |
| RTS_027 | Yinelenen uzun hat adı | BİLGİ | Quality |
| RTS_028 | Flex pencereli rotada continuous_pickup/drop_off yasak | YÜKSEK | Spec |
| RTS_029 | route_sort_order geçersiz | DÜŞÜK | Spec |
| RTS_030 | route_type çekirdek enum dışında genişletilmiş değer | DÜŞÜK | Interop |
| RTS_031 | route_id eksik | KRİTİK | Spec |
