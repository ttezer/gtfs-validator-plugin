## TRP — Trips (Seferler)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| TRP_001 | trip_id eksik veya yineleniyor | KRİTİK | Spec |
| TRP_002 | route_id bulunamadı | KRİTİK | Spec |
| TRP_003 | service_id bulunamadı | KRİTİK | Spec |
| TRP_004 | shape_id bulunamadı | YÜKSEK | Spec |
| TRP_005 | direction_id geçersiz | ORTA | Spec |
| TRP_006 | wheelchair_accessible geçersiz | DÜŞÜK | Spec |
| TRP_007 | bikes_allowed geçersiz | DÜŞÜK | Spec |
| TRP_032 | cars_allowed geçersiz | DÜŞÜK | Spec |
| TRP_011 | Sefer yön adı girilmemiş | YÜKSEK | Quality |
| TRP_012 | Çift yönlü rotada direction_id eksik | DÜŞÜK | Quality |
| TRP_013 | Hat tek seferlik | BİLGİ | Analytics |
| TRP_014 | trip_short_name çok uzun | BİLGİ | Quality |
| TRP_015 | block_id hiçbir seferi gruplamıyor | DÜŞÜK | Quality |
| TRP_017 | Frekans tabanlı sefer stop_times'ta eksik | ORTA | Quality |
| TRP_019 | Continuous servis aktifken shape_id eksik | YÜKSEK | Spec |
| TRP_020 | trip_headsign ara durak adıyla eşleşiyor | BİLGİ | Analytics |
| TRP_021 | Bisiklet izni (bikes_allowed) belirtilmemiş | BİLGİ | Quality |
| TRP_022 | Block içinde çakışan sefer saatleri | YÜKSEK | Interop |
| TRP_023 | Önümüzdeki 7 günde aktif sefer yok | DÜŞÜK | Quality |
| TRP_024 | Block içinde tutarsız rota tipi | DÜŞÜK | Quality |
| TRP_025 | Tekerlekli sandalye erişilebilirlik bilgisi eksik seferlerin oranı yüksek | BİLGİ | Quality |
| TRP_026 | Aktif tarihi olmayan sefer (service_id geçerli ama aktif gün seti boş) | ORTA | Analytics |
| TRP_028 | Bazı seferler tekerlekli sandalye erişilebilirliği işaretlememiş | BİLGİ | Quality |
| TRP_029 | Hiçbir sefer tekerlekli sandalye erişilebilirliği bildirmemiş | BİLGİ | Quality |
| TRP_031 | route_id eksik | KRİTİK | Spec |
| TRP_034 | safe_duration alanı sayı değil | ORTA | Spec |
| TRP_035 | trips.txt'te service_id boş | KRİTİK | Spec |

## STM — Stop Times (Geçiş Zamanları)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| STM_001 | trip_id bulunamadı | KRİTİK | Spec |
| STM_002 | stop_id bulunamadı | KRİTİK | Spec |
| STM_003 | arrival_time geçersiz format | KRİTİK | Spec |
| STM_004 | departure_time geçersiz format | KRİTİK | Spec |
| STM_005 | stop_sequence eksik veya geçersiz | KRİTİK | Spec |
| STM_006 | stop_id eksik (stop_times) | KRİTİK | Spec |
| STM_007 | Kalkış saati varış saatinden önce (departure_time < arrival_time) | YÜKSEK | Interop |
| STM_008 | Duraklar arası zaman geriye gidiyor | KRİTİK | Interop |
| STM_009 | pickup_type geçersiz | YÜKSEK | Spec |
| STM_010 | drop_off_type geçersiz | YÜKSEK | Spec |
| STM_012 | Duraklar arası hız gerçekçi değil | YÜKSEK | Interop |
| STM_014 | Segmentte aşırı hız | YÜKSEK | Analytics |
| STM_015 | İlk durakta arrival_time eksik | KRİTİK | Spec |
| STM_016 | Son durakta arrival_time eksik | KRİTİK | Spec |
| STM_017 | Sefer saatlerinde güzergah mesafesi eksik | ORTA | Quality |
| STM_018 | continuous_pickup geçersiz (stop_times) | ORTA | Spec |
| STM_019 | continuous_drop_off geçersiz (stop_times) | ORTA | Spec |
| STM_020 | Sıfır geçiş süresi (mesafe > 200m) | YÜKSEK | Quality |
| STM_021 | Duraklar arası mesafe sıfır veya negatif | BİLGİ | Analytics |
| STM_022 | timepoint geçersiz | ORTA | Spec |
| STM_024 | shape_dist_traveled birim tutarsızlığı | BİLGİ | Quality |
| STM_025 | Kısa segment zamanlaması | BİLGİ | Analytics |
| STM_026 | Durak arası mesafe aşırı uzun | BİLGİ | Analytics |
| STM_028 | Sefer süresi çok uzun | YÜKSEK | Analytics |
| STM_029 | Sefer süresi çok kısa | ORTA | Analytics |
| STM_030 | shape_dist_traveled negatif veya sayı değil | DÜŞÜK | Spec |
| STM_032 | Aynı seferde yinelenen stop_sequence değeri | DÜŞÜK | Spec |
| STM_033 | Tek duraklı sefer (kullanılamaz) | YÜKSEK | Interop |
| STM_034 | Varış veya kalkış zamanından yalnızca biri tanımlı | ORTA | Interop |
| STM_035 | Aynı durak ardışık iki kez ziyaret ediliyor (terminal/döngü) | BİLGİ | Analytics |
| STM_036 | stop_times trip_id + stop_sequence'a göre sıralı değil (unsorted_stop_times) | BİLGİ | Quality |
| STM_037 | Flex penceresinde arrival_time/departure_time yasak | YÜKSEK | Spec |
| STM_038 | start_pickup_drop_off_window >= end_pickup_drop_off_window | YÜKSEK | Interop |
| STM_039 | Flex bağlamında pickup/drop_off penceresi eksik | KRİTİK | Spec |
| STM_040 | Flex stop_times'ta pickup/drop_off_booking_rule_id eksik (spec'te Optional) | ORTA | Quality |
| STM_060 | Aynı seferde bölge, pencere ve pickup/drop_off eşzamanlı örtüşüyor | YÜKSEK | Spec |
| STM_061 | Ardışık olmayan uzak duraklar arası imkânsız hız | YÜKSEK | Interop |
| STM_059 | pickup_type/drop_off_type=2 iken booking_rule_id önerilir | DÜŞÜK | Quality |
| STM_041 | stop_id ile location_id/group_id aynı anda kullanılamaz | YÜKSEK | Spec |
| STM_042 | stop_headsign Google Transit tarafından desteklenmeyen karakter içeriyor | DÜŞÜK | Interop |
| STM_043 | Sefer aşırı fazla durağa sahip (>200) | BİLGİ | Analytics |
| STM_044 | Feed stop_times satır sayısı 2 milyonu aşıyor | BİLGİ | Analytics |
| STM_045 | Sefer kalkış saati servis günü penceresini aşıyor | BİLGİ | Analytics |
| STM_046 | trip_id eksik | KRİTİK | Spec |
| STM_047 | timepoint=1 ama arrival_time/departure_time eksik | KRİTİK | Spec |
| STM_048 | GTFS servis gününde gece yarısı sonrası saatler 00:xx yazılmış | YÜKSEK | Spec |
| STM_049 | GTFS servis gününde aynı satırda gece yarısı sonrası kalkış 00:xx | YÜKSEK | Spec |
| STM_050 | timepoint sütunu var ama değer boş | DÜŞÜK | Quality |
| STM_051 | Flex penceresinde pickup_type=0/3 yasak | YÜKSEK | Spec |
| STM_052 | Flex penceresinde drop_off_type=0 yasak | YÜKSEK | Spec |
| STM_053 | Çok sayıda ardışık durakta aynı zaman | BİLGİ | Analytics |
| STM_054 | Flex penceresinde continuous_pickup yasak | YÜKSEK | Spec |
| STM_055 | Flex penceresinde continuous_drop_off yasak | YÜKSEK | Spec |
| STM_056 | Güzergâh mesafesi artmıyor | KRİTİK | Spec |
| STM_058 | Flex pickup/drop-off penceresi saati geçersiz | KRİTİK | Spec |

## PDW — Pickup/Drop-off Window

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| PDW_006 | Aynı trip+zone'da örtüşen pickup/drop-off penceresi | ORTA | Analytics |

## LOC — locations.geojson

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| LOC_001 | locations.geojson'da bilinmeyen veya geçersiz geometri tipi | YÜKSEK | Spec |
| LOC_012 | locations.geojson geçerli bir GeoJSON FeatureCollection değil | YÜKSEK | Spec |
| LOC_002 | Feature'da geometry null veya eksik | KRİTİK | Spec |
| LOC_003 | Feature'da 'id' property eksik | KRİTİK | Spec |
| LOC_004 | Polygon ring kapalı değil | ORTA | Spec |
| LOC_005 | FeatureCollection tamamen boş | DÜŞÜK | Quality |
| LOC_006 | Polygon alanı 500km²'yi aşıyor | BİLGİ | Quality |
| LOC_007 | FeatureCollection içinde yinelenen feature 'id' | ORTA | Spec |
| LOC_008 | Feature 'type' alanı eksik veya "Feature" değil | ORTA | Spec |
| LOC_009 | Feature 'properties' nesnesi eksik | ORTA | Spec |
| LOC_011 | Poligon geçersiz: ring kendini kesiyor veya delik dışarıda | YÜKSEK | Spec |
| LOC_010 | Geometry 'coordinates' eksik veya dizi değil — bölge geometrisi çözümlenemez | KRİTİK | Spec |

## CAL — Calendar (Takvim)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| CAL_001 | service_id yineleniyor | KRİTİK | Spec |
| CAL_002 | Takvim gün alanı geçersiz değer | KRİTİK | Spec |
| CAL_003 | start_date eksik veya geçersiz format | KRİTİK | Spec |
| CAL_004 | end_date eksik veya geçersiz format | KRİTİK | Spec |
| CAL_005 | start_date end_date'den sonra | KRİTİK | Interop |
| CAL_006 | Haftalık bazda tüm günler pasif (calendar_dates ile override mümkün) | BİLGİ | Quality |
| CAL_007 | Servis döneminde boşluk | BİLGİ | Analytics |
| CAL_008 | Servis tarihi yakında sona eriyor | BİLGİ | Analytics |
| CAL_009 | Feed'deki tüm takvim dönemleri sona ermiş | BİLGİ | Analytics |
| CAL_010 | Serviste aktif gün sayısı çok az | ORTA | Analytics |
| CAL_011 | Kullanılmayan servis | DÜŞÜK | Quality |
| CAL_012 | Yakın gelecekte servis boşluğu var | BİLGİ | Analytics |
| CAL_013 | Geçmiş tarihli servis dönemi | BİLGİ | Analytics |
| CAL_014 | Servis tarihleri feed_info geçerlilik aralığı dışında | BİLGİ | Interop |
| CAL_015 | Tüm takvim tarihleri gelecekte (bugün aktif sefer yok) | BİLGİ | Analytics |
| CAL_016 | Servis çok uzak bir gelecek tarihine kadar uzanıyor | BİLGİ | Quality |
| CAL_017 | Takvim henüz başlamamış (tüm aktif tarihler gelecekte) | BİLGİ | Analytics |
| CAL_018 | Servisin aktif haftanın günü yok (tüm günler 0, calendar_dates ile geçersiz kılınan yok) | BİLGİ | Quality |
| CAL_020 | Feed geçerlilik penceresi 5 yılı aşıyor | BİLGİ | Quality |
| CAL_021 | Servis bugünü kapsıyor ama yakın günlerde aktif sefer yok | BİLGİ | Analytics |
| CAL_022 | service_id eksik | KRİTİK | Spec |
| CAL_023 | Takvim end_date çok ileri (şüpheli) | ORTA | Quality |
| CAL_024 | Takvim önümüzdeki 7 günde aktif değil | BİLGİ | Analytics |
| CAL_025 | Takvim gün alanı boş (değer verilmemiş) | KRİTİK | Spec |

## CLD — Calendar Dates

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| CLD_001 | service_id eksik | KRİTİK | Spec |
| CLD_002 | date eksik veya geçersiz format | KRİTİK | Spec |
| CLD_003 | exception_type eksik veya geçersiz | KRİTİK | Spec |
| CLD_004 | calendar_dates-only serviste aktif gün (exception_type=1) tanımlı değil | YÜKSEK | Quality |
| CLD_005 | Tarih makul yıl aralığı dışında | BİLGİ | Quality |
| CLD_006 | Çok fazla istisna günü | BİLGİ | Analytics |
| CLD_007 | Aşırı takvim istisnası | BİLGİ | Analytics |
