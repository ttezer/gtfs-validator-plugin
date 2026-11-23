## TRN — Translations

| Rule | Title | Severity | Class |
|---|---|---|---|
| TRN_001 | table_name invalid value | CRITICAL | Spec |
| TRN_002 | field_name invalid for this table | CRITICAL | Spec |
| TRN_003 | language invalid | MEDIUM | Spec |
| TRN_004 | record_id not found | HIGH | Spec |
| TRN_005 | Duplicate translation | CRITICAL | Spec |
| TRN_006 | Translation record conflicting | CRITICAL | Spec |
| TRN_007 | Translation in same language as feed_lang | LOW | Quality |
| TRN_008 | translation value is empty | CRITICAL | Spec |
| TRN_009 | record_id and field_value cannot be used together | HIGH | Spec |
| TRN_010 | record_sub_id invalid | HIGH | Spec |
| TRN_011 | field_name is not translatable | HIGH | Spec |
| TRN_013 | Identity field cannot be used in feed_info translation | HIGH | Spec |
| TRN_014 | record_sub_id only valid for stop_times | HIGH | Spec |
| TRN_017 | stop_times translation missing record_sub_id — the row is ambiguous | MEDIUM | Spec |
| TRN_015 | record_id and field_value are both empty | HIGH | Spec |
| TRN_016 | field_value matches no record — the translation is never applied | MEDIUM | Spec |

## ATR — Attributions

| Rule | Title | Severity | Class |
|---|---|---|---|
| ATR_001 | attribution_id missing | HIGH | Quality |
| ATR_002 | organization_name missing | CRITICAL | Spec |
| ATR_003 | Attribution role not defined | HIGH | Spec |
| ATR_004 | is_producer invalid | CRITICAL | Spec |
| ATR_005 | is_operator invalid | CRITICAL | Spec |
| ATR_006 | is_authority invalid | CRITICAL | Spec |
| ATR_007 | attribution_url invalid | CRITICAL | Spec |
| ATR_008 | attribution_email invalid | LOW | Spec |
| ATR_009 | multiple attribution reference fields set | HIGH | Spec |
| ATR_010 | agency_id not found | LOW | Spec |
| ATR_011 | route_id not found | LOW | Spec |
| ATR_012 | trip_id not found | LOW | Spec |

## XFL — Cross-File / Semantic

| Rule | Title | Severity | Class |
|---|---|---|---|
| XFL_002 | Trip has no stop_times records | HIGH | Interop |
| XFL_006 | service_id contains only cancellation exceptions (no active days) | MEDIUM | Analytics |
| XFL_012 | Route with no operational trips | HIGH | Quality |
| XFL_013 | shape_id used in multiple directions | HIGH | Quality |
| XFL_014 | Invalid translation reference (source record not found) | MEDIUM | Quality |
| XFL_015 | Invalid reference in attribution | CRITICAL | Spec |
| XFL_016 | Translation references feed_info but feed_info.txt is missing | HIGH | Spec |
| XFL_019 | Network defined in two separate files (routes.network_id + networks.txt or route_networks.txt) | MEDIUM | Spec |
| XFL_020 | Invalid (from_trip_id/to_trip_id, route_id) pair in transfers | CRITICAL | Spec |
| XFL_021 | Invalid (from_trip_id/to_trip_id, stop_id) pair in transfers | HIGH | Interop |
| XFL_022 | location_group_id not found | CRITICAL | Spec |
| XFL_023 | stop_id not found (location_group_stops) | CRITICAL | Spec |
| XFL_024 | location_group_id not found (stop_times) | CRITICAL | Spec |
| XFL_025 | location_id not found (locations.geojson) | CRITICAL | Spec |
| XFL_031 | ID clash: stop_id, locations.geojson id and location_group_id share one namespace | CRITICAL | Spec |
| XFL_032 | location_groups.txt has an empty location_group_id | CRITICAL | Spec |
| XFL_033 | location_group_stops has an empty location_group_id | CRITICAL | Spec |
| XFL_034 | location_group_stops has an empty stop_id | CRITICAL | Spec |
| XFL_027 | route cemv=2 but applicable contactless product | INFO | Interop |
| XFL_028 | agency cemv=1 but no contactless media | INFO | Quality |
| XFL_029 | route cemv=1 but no contactless media | INFO | Quality |
| XFL_030 | contactless media but no cemv=1 | INFO | Quality |

## OPR — Operational Consistency

| Rule | Title | Severity | Class |
|---|---|---|---|
| OPR_001 | Route headway too long | MEDIUM | Analytics |
| OPR_003 | Trip bunching (minimum headway too small) | LOW | Analytics |
| OPR_004 | No weekend service | INFO | Analytics |
| OPR_005 | Unusual service frequency | INFO | Analytics |
| OPR_006 | Trip has too few stops (not functional) | HIGH | Analytics |
| OPR_007 | Repeated stop pattern within trip | INFO | Analytics |
| OPR_008 | Excessive speed in multiple segments | INFO | Analytics |
| OPR_009 | Night trip start time too late | INFO | Analytics |
| OPR_010 | Route accessibility or bicycle policy conflicts | MEDIUM | Analytics |
| OPR_011 | Service has no active days | HIGH | Analytics |
| OPR_012 | Service gap | MEDIUM | Analytics |
| OPR_013 | Route operates in one direction only (no return direction) | INFO | Analytics |
| OPR_014 | Average transfer time too long | MEDIUM | Analytics |
| OPR_015 | Route operates with a single shape only | INFO | Analytics |
| OPR_016 | No active service across the entire feed | INFO | Analytics |
| OPR_017 | Trip distance too short | MEDIUM | Analytics |
| OPR_019 | Route calendar overlap (multiple services on same day) | INFO | Analytics |
| OPR_020 | Route exception day overlap | LOW | Analytics |
| OPR_021 | Calendar override conflict: override and base simultaneously active | HIGH | Analytics |
| OPR_022 | Calendar override not applied: base service running on override day | HIGH | Analytics |
| OPR_023 | Calendar override gap: no service active within window | MEDIUM | Analytics |
| OPR_024 | Route has an extreme trip count | INFO | Analytics |
| OPR_025 | Feed average trip duration under 60 seconds | HIGH | Analytics |

## GEO — Geographic / Spatial

| Rule | Title | Severity | Class |
|---|---|---|---|
| GEO_002 | Stop too far from feed median | HIGH | Analytics |
| GEO_006 | Large jump in shape | HIGH | Analytics |
| GEO_007 | Critical jump in shape (3× threshold) | HIGH | Analytics |
| GEO_009 | Stop too far from shape route | HIGH | Quality |
| GEO_012 | Stop cluster (stops too close together) | MEDIUM | Analytics |
| GEO_013 | Feed geographic coverage summary | INFO | Analytics |
| GEO_014 | Feed geographic coverage too wide | INFO | Analytics |
| GEO_015 | Stop coordinates outside Japan bounds (feed_lang: ja) | MEDIUM | Quality |
| GEO_016 | Stop at or near Null Island (\|lat\|<0.1 and \|lon\|<0.1) | HIGH | Quality |
| GEO_017 | Shape point at or near Null Island | HIGH | Quality |
| GEO_018 | All feed stops within 200m radius (possible test data) | HIGH | Analytics |
| GEO_019 | Stop has integer (zero-precision) coordinates | MEDIUM | Quality |
| GEO_020 | Shape is degenerate — all points at the same location | HIGH | Quality |
| GEO_021 | More than 30% of stops share coordinates (systematic issue) | HIGH | Analytics |
| GEO_022 | Stop latitude near a pole (\|lat\| > 89) | HIGH | Quality |

## DQ — Data Quality / User Experience

| Rule | Title | Severity | Class |
|---|---|---|---|
| DQ_003 | Route description missing | INFO | Quality |
| DQ_004 | Route URL missing | INFO | Quality |
| DQ_005 | No valid service period | HIGH | Quality |
| DQ_005b | No trip has stop times | HIGH | Quality |
| DQ_005c | High proportion of stops without coordinates | HIGH | Quality |
| DQ_006 | High proportion of trips without shapes | HIGH | Quality |
| DQ_009 | No stop times in trips | INFO | Quality |
| DQ_010 | Agency not used by any route | INFO | Quality |
| DQ_011 | Only one stop exists | LOW | Quality |
| DQ_012 | Too many agencies, agency_id not used | LOW | Quality |
| DQ_013 | Too few trips | INFO | Analytics |
| DQ_016 | Extra whitespace in field value | MEDIUM | Quality |
| DQ_017 | Suspicious coordinate value | INFO | Quality |
| DQ_018 | All-caps value in recommended field | MEDIUM | Quality |
| DQ_019 | All-lowercase value in recommended field | MEDIUM | Quality |
| DQ_020 | Recommended field missing or empty | LOW | Quality |
| DQ_021 | Primary key duplicate (duplicate_key) | HIGH | Spec |
| DQ_022 | More than 80% of stops share the same stop_name | HIGH | Quality |

## VAT — Entity Analytics Detection

| Rule | Title | Severity | Class |
|---|---|---|---|
| VAT_001 | Route shape similarity (likely duplicate route) | MEDIUM | Analytics |
| VAT_002 | Transfer hub undefined — many routes pass but no transfers defined | INFO | Analytics |
| VAT_003 | Trip duration statistical outlier | LOW | Analytics |
| VAT_005 | Isolated stop cluster — stops disconnected from main network component | MEDIUM | Analytics |
| VAT_006 | Service density imbalance — single route accounts for large proportion of feed trips | INFO | Analytics |
| VAT_007 | Terminal transfer missing — another route serves the terminus but no transfer defined | INFO | Analytics |
| VAT_008 | Same shape used by more than 30% of routes | INFO | Analytics |

## JPN

| Rule | Title | Severity | Class |
|---|---|---|---|
| JPN_001 | GTFS-JP: stop name missing kana (ja-Hrkt) reading | MEDIUM | Quality |
| JPN_002 | GTFS-JP: jp_office_id not defined in office_jp.txt | HIGH | Interop |
| JPN_003 | GTFS-JP: agency_jp agency_id not defined in agency.txt | HIGH | Interop |
| JPN_004 | GTFS-JP: translations.txt missing | HIGH | Interop |
| JPN_005 | GTFS-JP: office_jp office_name empty | HIGH | Interop |
| JPN_006 | GTFS-JP: fare files missing | MEDIUM | Quality |
| JPN_007 | GTFS-JP: feed_info.txt missing | MEDIUM | Quality |
| JPN_008 | GTFS-JP: route_long_name kana reading missing | MEDIUM | Quality |
| JPN_009 | GTFS-JP: trip_headsign kana reading missing | MEDIUM | Quality |
| JPN_010 | GTFS-JP: agency_name kana reading missing | MEDIUM | Quality |
| JPN_011 | GTFS-JP: agency_id required even with one agency | HIGH | Interop |
| JPN_012 | GTFS-JP: agency_jp agency_id missing | HIGH | Interop |
| JPN_013 | GTFS-JP: agency_zip_number format invalid | MEDIUM | Quality |
| JPN_014 | GTFS-JP: office_jp office_id missing or duplicated | HIGH | Interop |
| JPN_015 | GTFS-JP legacy: routes_jp route_id invalid | HIGH | Interop |
| JPN_016 | GTFS-JP: pattern_jp or legacy routes_jp route_update_date invalid | MEDIUM | Quality |
| JPN_017 | GTFS-JP: jp_pattern_id missing or duplicated | HIGH | Interop |
| JPN_018 | GTFS-JP: jp_pattern_id undefined | HIGH | Interop |
| JPN_019 | GTFS-JP: kana translation reference invalid | MEDIUM | Interop |
| JPN_020 | GTFS-JP: office contact format suspicious | MEDIUM | Quality |
| JPN_021 | GTFS-JP: kana translation inconsistent | MEDIUM | Quality |
| JPN_022 | GTFS-JP v4: required core field missing | MEDIUM | Interop |
| JPN_023 | GTFS-JP: feed_lang is not ja | HIGH | Interop |
| JPN_024 | GTFS-JP: agency_lang is not ja | HIGH | Interop |
| JPN_025 | GTFS-JP: agency_timezone is not Asia/Tokyo | HIGH | Interop |
| JPN_026 | GTFS-JP: fare currency is not JPY | HIGH | Interop |
| JPN_027 | GTFS-JP V3: route_type is not 3 | HIGH | Interop |
| JPN_028 | GTFS-JP v3: required kana translation missing | MEDIUM | Quality |
| JPN_029 | GTFS-JP v4: recommended kana translation missing | LOW | Quality |
| JPN_030 | GTFS-JP v3: required Japanese translation missing | MEDIUM | Quality |
| JPN_031 | GTFS-JP: zone_id missing at a stop served by zone-based fares | HIGH | Interop |
| JPN_032 | GTFS-JP V3: agency_id is not in Corporate Number format | MEDIUM | Interop |
| JPN_033 | GTFS-JP: reserved jp namespace used by a custom file or field | MEDIUM | Interop |
