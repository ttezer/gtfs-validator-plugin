## SHP — Shapes (Güzergah Şekilleri)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| SHP_001 | shape_id eksik | KRİTİK | Spec |
| SHP_002 | shape_pt_lat eksik veya geçersiz | KRİTİK | Spec |
| SHP_003 | shape_pt_lon eksik veya geçersiz | KRİTİK | Spec |
| SHP_004 | shape_pt_sequence eksik veya geçersiz | KRİTİK | Spec |
| SHP_005 | shape_dist_traveled geriye gidiyor | KRİTİK | Spec |
| SHP_006 | Güzergah şekli yalnızca tek noktadan oluşuyor | DÜŞÜK | Quality |
| SHP_008 | shape_pt_sequence yineleniyor | KRİTİK | Spec |
| SHP_009 | Güzergah şekli kendisiyle kesişiyor | BİLGİ | Analytics |
| SHP_010 | Tekrarlanan shape noktası (ardışık özdeş koordinat) | DÜŞÜK | Quality |
| SHP_012 | Güzergah şekli sefer duraklarından çok uzak | YÜKSEK | Analytics |
| SHP_014 | İlk veya son durak güzergah ucundan uzakta | BİLGİ | Analytics |
| SHP_015 | Güzergah şekli istatistiksel olarak çok az nokta | ORTA | Quality |
| SHP_016 | Güzergah şekli yön bilgisiyle uyumsuz | YÜKSEK | Quality |
| SHP_017 | Durak sırası güzergah şekliyle çelişiyor | BİLGİ | Analytics |
| SHP_018 | Güzergah şekli sefer tarafından referanslanmıyor | DÜŞÜK | Quality |
| SHP_019 | Güzergah şeklinin seferleri durak zamanı içermiyor | ORTA | Quality |
| SHP_020 | Güzergah şeklinde tekrarlayan nokta | BİLGİ | Analytics |
| SHP_021 | shape_dist_traveled negatif veya sayı değil | DÜŞÜK | Spec |
| SHP_022 | Durak güzergah şeklinde belirsiz konumda | YÜKSEK | Quality |
| SHP_023 | shape_dist_traveled aynı değere sahip art arda iki nokta aynı koordinatta | ORTA | Quality |
| SHP_024 | Duraktan şekle mesafe shape_dist_traveled ile tutarsız | ORTA | Quality |
| SHP_025 | Sefer stop_times mesafesi şeklin toplam mesafesini aşıyor | ORTA | Quality |
| SHP_026 | Shape aşırı fazla noktaya sahip (>5000) | BİLGİ | Analytics |
| SHP_028 | Aynı shape_dist_traveled, farklı koordinat | YÜKSEK | Spec |
| SHP_029 | Aynı shape_dist_traveled, çok küçük koordinat farkı (eşik altı) | BİLGİ | Quality |
| SHP_030 | stop_times shape_dist_traveled kullanıyor ancak shapes.txt'te shape mesafeleri eksik | ORTA | Quality |

## FRQ — Frequencies (Frekanslar)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| FRQ_001 | trip_id bulunamadı | KRİTİK | Spec |
| FRQ_002 | start_time geçersiz | KRİTİK | Spec |
| FRQ_003 | end_time geçersiz | KRİTİK | Spec |
| FRQ_004 | headway_secs eksik veya geçersiz | KRİTİK | Spec |
| FRQ_005 | end_time start_time'dan önce | KRİTİK | Quality |
| FRQ_006 | headway_secs çok uzun | ORTA | Analytics |
| FRQ_007 | exact_times geçersiz | ORTA | Spec |
| FRQ_008 | headway_secs sıfır (geçersiz frekans) | KRİTİK | Spec |
| FRQ_009 | Frekans aralığı çok kısa | ORTA | Quality |
| FRQ_010 | Çok sık frekans (sıkışma riski) | BİLGİ | Analytics |
| FRQ_011 | Frequencies dönemleri zaman aralığı çakışıyor | YÜKSEK | Spec |
| FRQ_012 | exact_times=1 iken end_time headway sınırına denk geliyor | DÜŞÜK | Spec |

## TRF — Transfers (Aktarmalar)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| TRF_001 | from_stop_id eksik | KRİTİK | Spec |
| TRF_002 | to_stop_id eksik | KRİTİK | Spec |
| TRF_003 | from_stop_id veya to_stop_id bulunamadı | KRİTİK | Spec |
| TRF_004 | transfer_type geçersiz | YÜKSEK | Spec |
| TRF_005 | min_transfer_time eksik | KRİTİK | Spec |
| TRF_006 | from_trip_id bulunamadı | KRİTİK | Spec |
| TRF_007 | to_trip_id bulunamadı | KRİTİK | Spec |
| TRF_008 | from_route_id bulunamadı | KRİTİK | Spec |
| TRF_009 | to_route_id bulunamadı | KRİTİK | Spec |
| TRF_010 | Aktarma süresi çok uzun | ORTA | Analytics |
| TRF_011 | Aktarma tanımlandı ama mesafe uzak | BİLGİ | Quality |
| TRF_012 | Yinelenen aktarma kaydı | KRİTİK | Spec |
| TRF_013 | Aktarma türü bağlamla uyumsuz | KRİTİK | Quality |
| TRF_014 | in-seat aktarma için sefer yok | YÜKSEK | Spec |
| TRF_015 | in-seat aktarma geçersiz | YÜKSEK | Quality |
| TRF_016 | Aktarma koşulu çelişkili | KRİTİK | Spec |
| TRF_017 | Sefer aktarması yanlış hat | YÜKSEK | Spec |
| TRF_018 | Sefer aktarması aynı seferi gösteriyor | ORTA | Quality |
| TRF_019 | In-seat aktarmada farklı route_type | ORTA | Interop |
| TRF_020 | Aktarma için gereken yürüme hızı çok yüksek | ORTA | Quality |
| TRF_021 | Aktarma uç noktası durak veya istasyon değil | KRİTİK | Spec |
| TRF_022 | 1-to-n devamlılıkta devam seferlerinin takvimleri çelişiyor | YÜKSEK | Spec |
| TRF_023 | n-to-1 devamlılıkta gelen seferlerin takvimleri çelişiyor | YÜKSEK | Spec |

## GGL — Google Transit Uyumluluğu

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| GGL_001 | transfer_type=4/5 Google Transit tarafından desteklenmiyor | DÜŞÜK | Interop |
| GGL_002 | ic_price (Google-özel) geçersiz değer | DÜŞÜK | Interop |

## FAR — Fare Attributes (Ücret Özellikleri)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| FAR_001 | fare_id yineleniyor | KRİTİK | Spec |
| FAR_002 | price eksik veya geçersiz | KRİTİK | Spec |
| FAR_003 | currency_type eksik | KRİTİK | Spec |
| FAR_004 | payment_method geçersiz | KRİTİK | Spec |
| FAR_005 | transfers geçersiz | KRİTİK | Spec |
| FAR_006 | transfer_duration geçersiz | ORTA | Spec |
| FAR_008 | agency_id bulunamadı | KRİTİK | Spec |
| FAR_010 | Çakışan ücret kuralları | ORTA | Quality |
| FAR_011 | payment_method eksik | KRİTİK | Spec |
| FAR_013 | price para biriminin ISO 4217 ondalık basamak sayısını taşımıyor | BİLGİ | Quality |
| FAR_012 | fare_id eksik | KRİTİK | Spec |

## FRL — Fare Rules (Ücret Kuralları)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| FRL_001 | fare_id bulunamadı | KRİTİK | Spec |
| FRL_002 | route_id bulunamadı | KRİTİK | Spec |
| FRL_003 | origin_id geçersiz | KRİTİK | Spec |
| FRL_004 | destination_id geçersiz | KRİTİK | Spec |
| FRL_005 | contains_id geçersiz | KRİTİK | Spec |
| FRL_006 | Ücret kuralı tanımlı değil | BİLGİ | Quality |
| FRL_007 | Ücret kuralı mantıksal tutarsızlık | ORTA | Quality |
| FRL_008 | Tüm hatlar için ücret tanımlı değil | BİLGİ | Quality |
| FRL_009 | Bazı kalkış-varış bölge çiftleri için ücret eksik | ORTA | Quality |

## RCT — Rider Categories (Yolcu Kategorileri, Fares v2)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| RCT_001 | rider_category_id yineleniyor | KRİTİK | Spec |
| RCT_002 | rider_category_name eksik | KRİTİK | Spec |
| RCT_003 | is_default_fare_category geçersiz | KRİTİK | Spec |
| RCT_004 | min_age veya max_age geçersiz (GTFS uzantı alanı — resmî spec'te yok) | ORTA | Quality |
| RCT_005 | max_age min_age'den küçük | ORTA | Quality |
| RCT_006 | fare_product başına varsayılan yolcu kategorisi sayısı bir değil | ORTA | Spec |
| RCT_007 | eligibility_url geçersiz | DÜŞÜK | Spec |
| RCT_008 | rider_category_id boş | KRİTİK | Spec |

## FMD — Fare Media (Ücret Medyası, Fares v2)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| FMD_001 | fare_media_id yineleniyor | KRİTİK | Spec |
| FMD_002 | fare_media_type eksik veya geçersiz | KRİTİK | Spec |
| FMD_003 | TransitCard/MobileApp için fare_media_name tavsiye edilir | DÜŞÜK | Quality |
| FMD_004 | fare_media_id boş | KRİTİK | Spec |

## FPD — Fare Products (Ücret Ürünleri, Fares v2)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| FPD_001 | fare_products bileşik anahtarı yineleniyor | KRİTİK | Spec |
| FPD_002 | amount eksik veya sayısal değil | KRİTİK | Spec |
| FPD_003 | currency geçersiz ISO 4217 kodu | KRİTİK | Spec |
| FPD_004 | fare_media_id bulunamadı | KRİTİK | Spec |
| FPD_005 | rider_category_id bulunamadı | KRİTİK | Spec |
| FPD_007 | amount para biriminin ISO 4217 ondalık basamak sayısını taşımıyor | DÜŞÜK | Spec |

## FLG — Fare Leg Rules (Fares v2)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| FLG_001 | fare_product_id bulunamadı | KRİTİK | Spec |
| FLG_002 | network_id bulunamadı | KRİTİK | Spec |
| FLG_003 | from_area_id bulunamadı | KRİTİK | Spec |
| FLG_004 | to_area_id bulunamadı | KRİTİK | Spec |
| FLG_005 | from_timeframe_group_id bulunamadı | KRİTİK | Spec |
| FLG_006 | to_timeframe_group_id bulunamadı | KRİTİK | Spec |
| FLG_007 | rule_priority geçersiz | ORTA | Spec |
| FLG_008 | fare_product_id eksik | KRİTİK | Spec |

## FLJ

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| FLJ_001 | from_network_id eksik veya bulunamadı | KRİTİK | Spec |
| FLJ_002 | to_network_id eksik veya bulunamadı | KRİTİK | Spec |
| FLJ_003 | from_stop_id eksik veya bulunamadı | KRİTİK | Spec |
| FLJ_004 | to_stop_id eksik veya bulunamadı | KRİTİK | Spec |

## FTR — Fare Transfer Rules (Fares v2)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| FTR_001 | fare_transfer_type eksik veya geçersiz | KRİTİK | Spec |
| FTR_002 | from_leg_group_id bulunamadı | KRİTİK | Spec |
| FTR_003 | to_leg_group_id bulunamadı | KRİTİK | Spec |
| FTR_004 | fare_product_id bulunamadı | KRİTİK | Spec |
| FTR_005 | duration_limit_type geçersiz | KRİTİK | Spec |
| FTR_006 | duration_limit geçersiz | ORTA | Spec |
| FTR_007 | duration_limit_type duration_limit olmadan tanımlı | ORTA | Spec |
| FTR_008 | transfer_count geçersiz | ORTA | Spec |
| FTR_009 | leg grupları aynıyken transfer_count zorunlu | ORTA | Spec |
| FTR_010 | leg grupları farklıyken transfer_count tanımlanamaz | ORTA | Spec |
| FTR_011 | duration_limit tanımlı ama duration_limit_type eksik | ORTA | Spec |

## ARS — Areas (Bölgeler, Fares v2)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| ARS_001 | area_id yineleniyor | KRİTİK | Spec |
| ARS_002 | areas.txt'te area_id boş | KRİTİK | Spec |

## SAR — Stop Areas (Durak Bölgeleri, Fares v2)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| SAR_001 | area_id bulunamadı | KRİTİK | Spec |
| SAR_002 | stop_id bulunamadı | KRİTİK | Spec |
| SAR_003 | stop_areas'ta area_id boş | KRİTİK | Spec |
| SAR_004 | stop_areas'ta stop_id boş | KRİTİK | Spec |

## NET — Networks (Ağlar, Fares v2)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| NET_001 | network_id yineleniyor | KRİTİK | Spec |
| NET_002 | route_networks.network_id eksik veya bulunamadı | KRİTİK | Spec |
| NET_003 | route_networks.route_id eksik veya bulunamadı | KRİTİK | Spec |
| NET_004 | networks.txt'te network_id boş | KRİTİK | Spec |

## TFR — Timeframes (Zaman Dilimleri, Fares v2)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| TFR_001 | timeframe_group_id eksik | KRİTİK | Spec |
| TFR_002 | service_id bulunamadı | KRİTİK | Spec |
| TFR_003 | start_time veya end_time format hatası | YÜKSEK | Spec |
| TFR_004 | end_time start_time'dan küçük | ORTA | Quality |
| TFR_005 | Aynı grup ve service_id içinde örtüşen zaman aralıkları | ORTA | Spec |
| TFR_006 | start_time veya end_time 24:00:00'dan büyük | KRİTİK | Spec |
| TFR_007 | start_time ve end_time yalnızca biri tanımlı | KRİTİK | Spec |
| TFR_008 | timeframes'te service_id boş | KRİTİK | Spec |
