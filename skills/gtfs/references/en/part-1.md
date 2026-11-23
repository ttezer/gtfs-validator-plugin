## ARC — Archive / File Level

| Rule | Title | Severity | Class |
|---|---|---|---|
| ARC_001 | ZIP archive could not be opened | CRITICAL | Spec |
| ARC_002 | File cannot be read as UTF-8 | CRITICAL | Quality |
| ARC_003 | UTF-8 encoding error in optional file | MEDIUM | Quality |
| ARC_004 | Required file missing | CRITICAL | Spec |
| ARC_006 | Optional GTFS file present | INFO | Analytics |
| ARC_007 | Unrecognized non-GTFS file | INFO | Quality |
| ARC_008 | Calendar file missing (calendar.txt and calendar_dates.txt) | CRITICAL | Spec |
| ARC_031 | feed_info.txt missing while translations.txt is present | CRITICAL | Spec |
| ARC_009 | Optional file has no data rows | INFO | Quality |
| ARC_010 | File contains UTF-8 BOM | INFO | Quality |
| ARC_011 | File size (info) | INFO | Analytics |
| ARC_012 | Row column count does not match header | CRITICAL | Spec |
| ARC_013 | CSV parse error | CRITICAL | Spec |
| ARC_014 | Leading/trailing whitespace in header | MEDIUM | Quality |
| ARC_015 | Duplicate header column | CRITICAL | Interop |
| ARC_025 | Required column missing from header | CRITICAL | Spec |
| ARC_017 | Unknown column (not defined in GTFS specification) | INFO | Quality |
| ARC_018 | Empty data row | MEDIUM | Quality |
| ARC_019 | Empty column name in header | HIGH | Quality |
| ARC_020 | Recommended GTFS file missing (shapes.txt or feed_info.txt) | LOW | Quality |
| ARC_021 | Non-printable or problematic character in field | LOW | Quality |
| ARC_022 | File row count exceeds the 1,000,000 informational threshold | INFO | Analytics |
| ARC_023 | Nested ZIP file inside GTFS archive | MEDIUM | Quality |
| ARC_024 | GTFS .txt file in subdirectory (will not be parsed) | MEDIUM | Spec |
| ARC_026 | Malformed end-of-line characters | MEDIUM | Spec |
| ARC_027 | ZIP entry lacks user read permission | INFO | Quality |
| ARC_028 | GTFS publishing URL does not end with a .zip filename | LOW | Quality |
| ARC_029 | Zip-bomb protection triggered | CRITICAL | Quality |
| ARC_030 | Tab or line break in a field value | HIGH | Spec |
| ARC_032 | HTML markup or character escape in a field value | HIGH | Spec |
| ARC_033 | Unescaped quotation mark in a field value (RFC 4180) | HIGH | Spec |
| ARC_034 | Header row repeated as a data row | HIGH | Spec |
| ARC_035 | Required file is empty | CRITICAL | Spec |
| ARC_036 | ZIP stream header contradicts the central directory | LOW | Quality |
| ARC_037 | Non-ASCII character in an ID field | LOW | Quality |

## BKR — Booking Rules

| Rule | Title | Severity | Class |
|---|---|---|---|
| BKR_001 | Prior-day booking field set in prohibited context | HIGH | Spec |
| BKR_003 | prior_notice_start_time only valid with prior_notice_start_day | HIGH | Spec |
| BKR_004 | prior_notice fields prohibited for real-time booking | HIGH | Spec |
| BKR_005 | prior_notice_duration_max only valid with booking_type=1 | MEDIUM | Spec |
| BKR_006 | prior_notice_duration_min invalid (≤ 0 or non-numeric) | HIGH | Spec |
| BKR_007 | prior_notice_duration_min required for booking_type=1 | CRITICAL | Spec |
| BKR_008 | prior_notice_last_day required for booking_type=2 | CRITICAL | Spec |
| BKR_009 | prior_notice_last_time required for booking_type=2 | CRITICAL | Spec |
| BKR_010 | prior_notice_start_time required when prior_notice_start_day is set | HIGH | Spec |
| BKR_011 | prior_notice_last_day > prior_notice_start_day: invalid booking window | HIGH | Interop |
| BKR_012 | prior_notice_duration_min forbidden with booking_type=2 | MEDIUM | Spec |
| BKR_013 | prior_notice_last_time only valid with prior_notice_last_day | HIGH | Spec |
| BKR_014 | prior_notice_service_id only valid with booking_type=2 | HIGH | Spec |
| BKR_015 | prior_notice_service_id not found (calendar/calendar_dates) | CRITICAL | Spec |
| BKR_016 | booking_type missing or invalid | CRITICAL | Spec |
| BKR_017 | pickup_booking_rule_id not found (booking_rules) | CRITICAL | Spec |
| BKR_018 | drop_off_booking_rule_id not found (booking_rules) | CRITICAL | Spec |
| BKR_019 | booking_rule_id missing or duplicated | CRITICAL | Spec |
| BKR_024 | prior_notice_start_day forbidden with booking_type=1 and duration_max | MEDIUM | Spec |
| BKR_020 | booking_url is invalid | MEDIUM | Spec |
| BKR_021 | info_url is invalid | LOW | Spec |
| BKR_022 | phone_number is invalid | LOW | Quality |
| BKR_023 | prior_notice numeric field is not an integer | MEDIUM | Spec |
| BKR_025 | prior_notice time field is not a valid time | MEDIUM | Spec |

## AGN — Agency

| Rule | Title | Severity | Class |
|---|---|---|---|
| AGN_002 | agency_name missing | CRITICAL | Spec |
| AGN_003 | agency_url missing or invalid | CRITICAL | Spec |
| AGN_004 | agency_timezone missing or invalid | CRITICAL | Spec |
| AGN_005 | Timezone inconsistency across agencies | MEDIUM | Spec |
| AGN_006 | agency_lang invalid | LOW | Spec |
| AGN_007 | agency_phone invalid | LOW | Quality |
| AGN_008 | agency_fare_url invalid | LOW | Spec |
| AGN_009 | agency_email invalid | LOW | Spec |
| AGN_010 | Duplicate agency_id | CRITICAL | Spec |
| AGN_011 | Multiple agencies with no agency_id | CRITICAL | Spec |
| AGN_012 | cemv_support invalid (agency) | LOW | Spec |
| AGN_013 | Feed language and agency language mismatch | LOW | Interop |
| AGN_014 | Multiple agencies but agency.txt agency_id missing | CRITICAL | Spec |
| AGN_015 | agency_url uses insecure http | INFO | Quality |
| AGN_016 | agency_phone suspect/placeholder | INFO | Quality |
| AGN_017 | Inconsistent agency_lang across agencies | LOW | Interop |
| AGN_018 | agency_id empty in a single-agency feed | INFO | Quality |

## STP — Stops

| Rule | Title | Severity | Class |
|---|---|---|---|
| STP_001 | Duplicate stop_id | CRITICAL | Spec |
| STP_002 | stop_id is empty | CRITICAL | Spec |
| STP_003 | stop_name missing or stop_lat out of range | CRITICAL | Spec |
| STP_004 | stop_lat is not numeric | CRITICAL | Spec |
| STP_005 | stop_lon invalid or out of range | CRITICAL | Spec |
| STP_006 | stop_lat missing | CRITICAL | Spec |
| STP_007 | stop_lon missing | CRITICAL | Spec |
| STP_008 | location_type invalid | HIGH | Spec |
| STP_009 | parent_station not found | CRITICAL | Spec |
| STP_010 | parent_station is not location_type=1 | HIGH | Spec |
| STP_011 | parent_station required for entrance/exit/boarding area | CRITICAL | Spec |
| STP_012 | Station or entrance used in stop_times | CRITICAL | Spec |
| STP_013 | wheelchair_boarding invalid | LOW | Spec |
| STP_014 | stop_timezone invalid | MEDIUM | Spec |
| STP_015 | level_id not found | CRITICAL | Spec |
| STP_016 | Two stops at identical coordinates | MEDIUM | Quality |
| STP_017 | Two stops too close together | LOW | Quality |
| STP_018 | No stops found | CRITICAL | Spec |
| STP_019 | stop_name too long | INFO | Quality |
| STP_020 | Stop with no trips | MEDIUM | Analytics |
| STP_021 | Boarding area parent is not a platform | HIGH | Quality |
| STP_022 | stop_code missing | MEDIUM | Quality |
| STP_023 | tts_stop_name invalid | LOW | Quality |
| STP_024 | stop_access outside K2 compatibility range | INFO | Quality |
| STP_026 | stop_access invalid value | LOW | Spec |
| STP_028 | stop_code too long | INFO | Quality |
| STP_029 | Stop inside station but coordinate too far | MEDIUM | Quality |
| STP_030 | Parent station has no child stops | MEDIUM | Quality |
| STP_031 | Stop name and description are identical | INFO | Quality |
| STP_032 | parent_station missing for pathway-connected platform | MEDIUM | Quality |
| STP_033 | Stop zone_id missing (required for fare calculation) | INFO | Quality |
| STP_034 | stop_url matches agency URL | LOW | Quality |
| STP_035 | stop_url matches route URL | LOW | Quality |
| STP_036 | Station has parent_station (invalid) | LOW | Spec |
| STP_037 | Some stops have not set wheelchair boarding | INFO | Quality |
| STP_038 | No stops report wheelchair boarding | INFO | Quality |
| STP_039 | stop_code is duplicated | LOW | Quality |
| STP_040 | Stop name contains a redundant stop/station word | LOW | Quality |
| STP_044 | platform_code contains a redundant platform/track word | LOW | Quality |
| STP_045 | platform_code without parent_station | INFO | Quality |
| STP_046 | Stop without parent_station right next to a station | LOW | Quality |
| STP_047 | Two station records for the same place | LOW | Quality |
| STP_041 | Child stop name does not include the parent station name | LOW | Quality |
| STP_042 | stop_url is invalid | LOW | Spec |
| STP_043 | stop_access used in a forbidden context | MEDIUM | Spec |

## RTS — Routes

| Rule | Title | Severity | Class |
|---|---|---|---|
| RTS_001 | Duplicate route_id | CRITICAL | Spec |
| RTS_002 | agency_id not found | CRITICAL | Spec |
| RTS_003 | Both route_short_name and route_long_name missing | CRITICAL | Spec |
| RTS_004 | route_type missing or invalid | CRITICAL | Spec |
| RTS_005 | route_url invalid | MEDIUM | Spec |
| RTS_006 | route_color invalid hex color | MEDIUM | Spec |
| RTS_007 | route_text_color invalid hex color | MEDIUM | Spec |
| RTS_008 | Route color and text color have low contrast | MEDIUM | Quality |
| RTS_010 | route_short_name too long | LOW | Quality |
| RTS_011 | route_long_name too long | INFO | Quality |
| RTS_012 | Route with no trips | MEDIUM | Quality |
| RTS_013 | continuous_pickup invalid | LOW | Spec |
| RTS_016 | Route with no active service days | LOW | Quality |
| RTS_017 | Route with no shape defined | INFO | Quality |
| RTS_018 | continuous_drop_off invalid | LOW | Spec |
| RTS_019 | Duplicate route name | MEDIUM | Quality |
| RTS_020 | Route and agency share the same URL | INFO | Quality |
| RTS_021 | route_short_name exceeds Google Transit limit (6 characters) | LOW | Quality |
| RTS_022 | route_long_name contains route_short_name | LOW | Quality |
| RTS_023 | route_desc repeats a route name | INFO | Quality |
| RTS_024 | cemv_support invalid (route) | LOW | Spec |
| RTS_025 | routes.txt agency_id empty (recommended) | INFO | Quality |
| RTS_026 | Duplicate short route name | INFO | Quality |
| RTS_027 | Duplicate long route name | INFO | Quality |
| RTS_028 | continuous_pickup/drop_off forbidden on a Flex route | HIGH | Spec |
| RTS_029 | route_sort_order is invalid | LOW | Spec |
| RTS_030 | route_type uses an extended value outside the core enum | LOW | Interop |
| RTS_031 | route_id missing | CRITICAL | Spec |
