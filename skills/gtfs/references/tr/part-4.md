## PTH — Pathways (Geçitler)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| PTH_001 | pathway_id yineleniyor | KRİTİK | Spec |
| PTH_002 | from_stop_id bulunamadı | KRİTİK | Spec |
| PTH_003 | to_stop_id bulunamadı | KRİTİK | Spec |
| PTH_004 | pathway_mode eksik veya geçersiz | KRİTİK | Spec |
| PTH_005 | is_bidirectional eksik | KRİTİK | Spec |
| PTH_006 | length geçersiz | ORTA | Spec |
| PTH_007 | traversal_time geçersiz | ORTA | Spec |
| PTH_008 | stair_count eksik | DÜŞÜK | Quality |
| PTH_009 | max_slope eksik | DÜŞÜK | Quality |
| PTH_010 | min_width geçersiz | DÜŞÜK | Spec |
| PTH_011 | Geçit döngü oluşturuyor | YÜKSEK | Quality |
| PTH_012 | İstasyona erişilebilir yol yok | YÜKSEK | Spec |
| PTH_013 | Erişilebilir yol analizi | BİLGİ | Analytics |
| PTH_014 | Geçit istasyon sınırını aşıyor | KRİTİK | Quality |
| PTH_015 | Geçit hedefi erişilemeyen durakta | ORTA | Analytics |
| PTH_016 | Çıkış kapısı çift yönlü tanımlanmış | YÜKSEK | Spec |
| PTH_017 | max_slope sayı değil | ORTA | Spec |
| PTH_018 | signposted_as çok uzun | DÜŞÜK | Quality |
| PTH_019 | Generic node tek pathway'e bağlı (dead-end) | ORTA | Quality |
| PTH_020 | pathway_id eksik | KRİTİK | Spec |
| PTH_021 | from_stop_id eksik | KRİTİK | Spec |
| PTH_022 | to_stop_id eksik | KRİTİK | Spec |
| PTH_023 | pathway_mode eksik | KRİTİK | Spec |
| PTH_024 | is_bidirectional eksik | KRİTİK | Spec |
| PTH_025 | Önerilen pathway length bilgisi eksik | DÜŞÜK | Quality |
| PTH_030 | Boarding area'sı olan platforma pathway atanmış | DÜŞÜK | Spec |
| PTH_029 | Önerilen pathway traversal_time bilgisi eksik | DÜŞÜK | Quality |
| PTH_026 | Pathway uç noktası istasyon | KRİTİK | Spec |
| PTH_031 | Pathway uç noktası sokaktan erişilen durak (stop_access=1) | KRİTİK | Spec |
| PTH_027 | stair_count geçersiz (sıfır veya tam sayı değil) | ORTA | Spec |
| PTH_028 | max_slope yürüme yolu dışında kullanılmış | DÜŞÜK | Quality |

## LVL — Levels (Katlar)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| LVL_001 | level_id yineleniyor | KRİTİK | Spec |
| LVL_002 | level_index geçersiz | KRİTİK | Spec |
| LVL_003 | level_name eksik | DÜŞÜK | Quality |
| LVL_004 | Kullanılmayan level | DÜŞÜK | Quality |
| LVL_005 | level_name çok uzun | ORTA | Quality |
| LVL_006 | Asansör bağlantısındaki durakta level_id eksik | ORTA | Quality |
| LVL_007 | level_index eksik | KRİTİK | Spec |
| LVL_008 | level_id eksik | KRİTİK | Spec |

## FIN — Feed Info

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| FIN_001 | feed_publisher_name eksik | KRİTİK | Spec |
| FIN_002 | feed_publisher_url eksik veya geçersiz | KRİTİK | Spec |
| FIN_003 | feed_lang eksik | KRİTİK | Spec |
| FIN_004 | default_lang geçersiz | ORTA | Spec |
| FIN_005 | feed_start_date geçersiz | ORTA | Spec |
| FIN_006 | feed_end_date geçersiz format (geçmiş tarih için FIN_010 kullanın) | YÜKSEK | Spec |
| FIN_007 | feed_version eksik | DÜŞÜK | Quality |
| FIN_008 | feed_contact_email geçersiz | DÜŞÜK | Spec |
| FIN_009 | feed_contact_url geçersiz | DÜŞÜK | Spec |
| FIN_010 | Feed geçerlilik süresi dolmuş | YÜKSEK | Analytics |
| FIN_012 | feed_start_date feed_end_date'den sonra | DÜŞÜK | Spec |
| FIN_013 | fare_attributes.agency_id önerilen ama eksik | BİLGİ | Quality |
| FIN_014 | Feed geçerlilik tarihleri (feed_start_date/feed_end_date) eksik | DÜŞÜK | Quality |
| FIN_015 | Birden fazla feed_info kaydı | ORTA | Quality |
| FIN_016 | feed_start_date gelecekte (feed henüz aktif değil) | DÜŞÜK | Quality |
| FIN_017 | Feed çok uzak gelecekte sona eriyor | BİLGİ | Quality |
| FIN_018 | feed_contact_email ve feed_contact_url ikisi de eksik | DÜŞÜK | Quality |
| FIN_019 | Feed'in geçerlilik süresi 7 gün içinde dolacak | DÜŞÜK | Quality |
| FIN_020 | Feed geçerlilik penceresi 7 günden kısa | BİLGİ | Quality |

## TRN — Translations (Çeviriler)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| TRN_001 | table_name geçersiz değer | KRİTİK | Spec |
| TRN_002 | field_name bu tablo için geçersiz | KRİTİK | Spec |
| TRN_003 | language geçersiz | ORTA | Spec |
| TRN_004 | record_id bulunamadı | YÜKSEK | Spec |
| TRN_005 | Çeviri yineleniyor | KRİTİK | Spec |
| TRN_006 | Çeviri kaydı çelişkili | KRİTİK | Spec |
| TRN_007 | Çeviri feed_lang ile aynı dilde | DÜŞÜK | Quality |
| TRN_008 | translation değeri boş | KRİTİK | Spec |
| TRN_009 | record_id ve field_value aynı anda kullanılamaz | YÜKSEK | Spec |
| TRN_010 | record_sub_id geçersiz | YÜKSEK | Spec |
| TRN_011 | field_name çevrilebilir değil | YÜKSEK | Spec |
| TRN_013 | feed_info çevirisinde kimlik alanı kullanılamaz | YÜKSEK | Spec |
| TRN_014 | record_sub_id yalnızca stop_times için geçerli | YÜKSEK | Spec |
| TRN_017 | stop_times çevirisinde record_sub_id eksik — hangi satır olduğu belirsiz | ORTA | Spec |
| TRN_015 | record_id ve field_value ikisi de boş | YÜKSEK | Spec |
| TRN_016 | field_value hiçbir kayıtla eşleşmiyor — çeviri uygulanmıyor | ORTA | Spec |

## ATR — Attributions (Atıflar)

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| ATR_001 | attribution_id eksik | YÜKSEK | Quality |
| ATR_002 | organization_name eksik | KRİTİK | Spec |
| ATR_003 | Attribution rolü tanımlanmamış | YÜKSEK | Spec |
| ATR_004 | is_producer geçersiz | KRİTİK | Spec |
| ATR_005 | is_operator geçersiz | KRİTİK | Spec |
| ATR_006 | is_authority geçersiz | KRİTİK | Spec |
| ATR_007 | attribution_url geçersiz | KRİTİK | Spec |
| ATR_008 | attribution_email geçersiz | DÜŞÜK | Spec |
| ATR_009 | attribution hedef alanları birlikte kullanılmış | YÜKSEK | Spec |
| ATR_010 | agency_id bulunamadı | DÜŞÜK | Spec |
| ATR_011 | route_id bulunamadı | DÜŞÜK | Spec |
| ATR_012 | trip_id bulunamadı | DÜŞÜK | Spec |

## XFL — Cross-File / Semantik

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| XFL_002 | Seferin stop_times kaydı yok | YÜKSEK | Interop |
| XFL_006 | service_id yalnızca iptal istisnası içeriyor (aktif gün yok) | ORTA | Analytics |
| XFL_012 | Çalıştırılabilir seferi olmayan hat | YÜKSEK | Quality |
| XFL_013 | shape_id birden fazla yönde kullanılıyor | YÜKSEK | Quality |
| XFL_014 | Geçersiz çeviri referansı (kaynak kayıt bulunamadı) | ORTA | Quality |
| XFL_015 | Attribution'da geçersiz referans | KRİTİK | Spec |
| XFL_016 | Çeviri feed_info'ya referans veriyor ama feed_info.txt eksik | YÜKSEK | Spec |
| XFL_019 | Ağ tanımı iki ayrı dosyada (routes.network_id + networks.txt veya route_networks.txt) | ORTA | Spec |
| XFL_020 | Transfers'de geçersiz (from_trip_id/to_trip_id, route_id) çifti | KRİTİK | Spec |
| XFL_021 | Transfers'de geçersiz (from_trip_id/to_trip_id, stop_id) çifti | YÜKSEK | Interop |
| XFL_022 | location_group_id bulunamadı (location_group_stops) | KRİTİK | Spec |
| XFL_023 | stop_id bulunamadı (location_group_stops) | KRİTİK | Spec |
| XFL_024 | location_group_id bulunamadı (stop_times) | KRİTİK | Spec |
| XFL_025 | location_id bulunamadı (locations.geojson) | KRİTİK | Spec |
| XFL_031 | Kimlik çakışması: stop_id / locations.geojson id / location_group_id ortak isim alanını paylaşır | KRİTİK | Spec |
| XFL_032 | location_groups.txt'te location_group_id boş | KRİTİK | Spec |
| XFL_033 | location_group_stops'ta location_group_id boş | KRİTİK | Spec |
| XFL_034 | location_group_stops'ta stop_id boş | KRİTİK | Spec |
| XFL_027 | cEMV bayrağı ile Fares v2 bilgisi farklı; Fares v2 bilgisi geçerlidir | BİLGİ | Interop |
| XFL_028 | agency cemv_support=1 ama contactless media yok | BİLGİ | Quality |
| XFL_029 | route cemv_support=1 ama contactless media yok | BİLGİ | Quality |
| XFL_030 | contactless media var ama cemv_support=1 yok | BİLGİ | Quality |

## OPR — Operasyonel Tutarlılık

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| OPR_001 | Hat sefer sıklığı düşük | ORTA | Analytics |
| OPR_003 | Sefer sıkışması (minimum aralık çok küçük) | DÜŞÜK | Analytics |
| OPR_004 | Hafta sonu sefer yok | BİLGİ | Analytics |
| OPR_005 | Sıradışı sefer sıklığı | BİLGİ | Analytics |
| OPR_006 | Seferde çok az durak (işlevsel değil) | YÜKSEK | Analytics |
| OPR_007 | Sefer içinde tekrarlayan durak deseni | BİLGİ | Analytics |
| OPR_008 | Birden fazla segmentte aşırı hız | BİLGİ | Analytics |
| OPR_009 | Gece seferi başlangıç saati çok geç | BİLGİ | Analytics |
| OPR_010 | Hatta erişilebilirlik veya bisiklet politikası çelişiyor | ORTA | Analytics |
| OPR_011 | Serviste aktif gün yok | YÜKSEK | Analytics |
| OPR_012 | Servis boşluğu | ORTA | Analytics |
| OPR_013 | Hat tek yönde işliyor (karşı yön tanımlı değil) | BİLGİ | Analytics |
| OPR_014 | Ortalama aktarma süresi uzun | ORTA | Analytics |
| OPR_015 | Hat yalnızca tek güzergahla işliyor | BİLGİ | Analytics |
| OPR_016 | Feed genelinde aktif servis yok | BİLGİ | Analytics |
| OPR_017 | Sefer çok kısa mesafe | ORTA | Analytics |
| OPR_019 | Rota takvim çakışması (aynı günde birden fazla servis) | BİLGİ | Analytics |
| OPR_020 | Rota exception günü çakışması | DÜŞÜK | Analytics |
| OPR_021 | Takvim override çakışması: override ve base eş zamanlı aktif | YÜKSEK | Analytics |
| OPR_022 | Takvim override uygulanmamış: override gününde base servis çalışıyor | YÜKSEK | Analytics |
| OPR_023 | Takvim override boşluğu: pencere içinde hiçbir servis aktif değil | ORTA | Analytics |
| OPR_024 | Hat çok fazla sefer içeriyor | BİLGİ | Analytics |
| OPR_025 | Ortalama sefer süresi 60 saniyeden kısa | YÜKSEK | Analytics |

## GEO — Coğrafi / Uzamsal

| Kural | Başlık | Önem | Sınıf |
|---|---|---|---|
| GEO_002 | Durak feed medianından çok uzakta | YÜKSEK | Analytics |
| GEO_006 | Güzergah şeklinde büyük atlama | YÜKSEK | Analytics |
| GEO_007 | Güzergah şeklinde kritik atlama (3× eşik) | YÜKSEK | Analytics |
| GEO_009 | Durak shape güzergahından çok uzakta | YÜKSEK | Quality |
| GEO_012 | Duraksallar kümelenmesi (çok yakın duraklar) | ORTA | Analytics |
| GEO_013 | Feed coğrafi kapsam özeti | BİLGİ | Analytics |
| GEO_014 | Feed coğrafi kapsamı çok geniş | BİLGİ | Analytics |
| GEO_015 | Durak koordinatları Japonya sınırları dışında (feed_lang: ja) | ORTA | Quality |
| GEO_016 | Durak Null Island yakınında (\|lat\|<0.1 VE \|lon\|<0.1) | YÜKSEK | Quality |
| GEO_017 | Shape noktası Null Island yakınında | YÜKSEK | Quality |
| GEO_018 | Tüm feed durakları 200m içinde (test verisi) | YÜKSEK | Analytics |
| GEO_019 | Durak tam sayı koordinatlara sahip (hassasiyet sıfır) | ORTA | Quality |
| GEO_020 | Shape dejenere — tüm noktalar aynı koordinatta | YÜKSEK | Quality |
| GEO_021 | Durakların %30+ koordinatı paylaşıyor (sistematik hata) | YÜKSEK | Analytics |
| GEO_022 | Durak enlemi kutba aşırı yakın (\|lat\| > 89) | YÜKSEK | Quality |
