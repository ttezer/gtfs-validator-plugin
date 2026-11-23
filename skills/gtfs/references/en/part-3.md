## TRF — Transfers

| Rule | Title | Severity | Class |
|---|---|---|---|
| TRF_001 | from_stop_id missing | CRITICAL | Spec |
| TRF_002 | to_stop_id missing | CRITICAL | Spec |
| TRF_003 | from_stop_id or to_stop_id not found | CRITICAL | Spec |
| TRF_004 | transfer_type invalid | HIGH | Spec |
| TRF_005 | min_transfer_time missing | CRITICAL | Spec |
| TRF_006 | from_trip_id not found | CRITICAL | Spec |
| TRF_007 | to_trip_id not found | CRITICAL | Spec |
| TRF_008 | from_route_id not found | CRITICAL | Spec |
| TRF_009 | to_route_id not found | CRITICAL | Spec |
| TRF_010 | Transfer time too long | MEDIUM | Analytics |
| TRF_011 | Transfer defined but distance is far | INFO | Quality |
| TRF_012 | Duplicate transfer record | CRITICAL | Spec |
| TRF_013 | Transfer type inconsistent with context | CRITICAL | Quality |
| TRF_014 | No trip for in-seat transfer | HIGH | Spec |
| TRF_015 | in-seat transfer invalid | HIGH | Quality |
| TRF_016 | Transfer condition conflicting | CRITICAL | Spec |
| TRF_017 | Trip transfer on wrong route | HIGH | Spec |
| TRF_018 | Trip transfer references the same trip | MEDIUM | Quality |
| TRF_019 | Different route_type in in-seat transfer | MEDIUM | Interop |
| TRF_020 | Transfer walking speed is too fast | MEDIUM | Quality |
| TRF_021 | Transfer endpoint is not a stop or station | CRITICAL | Spec |
| TRF_022 | Conflicting calendars in a 1-to-n trip continuation | HIGH | Spec |
| TRF_023 | Conflicting calendars in an n-to-1 trip continuation | HIGH | Spec |

## GGL — Google Transit Compatibility

| Rule | Title | Severity | Class |
|---|---|---|---|
| GGL_001 | transfer_type=4/5 not supported by Google Transit | LOW | Interop |
| GGL_002 | ic_price (Google-specific) invalid value | LOW | Interop |

## FAR — Fare Attributes

| Rule | Title | Severity | Class |
|---|---|---|---|
| FAR_001 | Duplicate fare_id | CRITICAL | Spec |
| FAR_002 | price missing or invalid | CRITICAL | Spec |
| FAR_003 | currency_type missing | CRITICAL | Spec |
| FAR_004 | payment_method invalid | CRITICAL | Spec |
| FAR_005 | transfers invalid | CRITICAL | Spec |
| FAR_006 | transfer_duration invalid | MEDIUM | Spec |
| FAR_008 | agency_id not found | CRITICAL | Spec |
| FAR_010 | Overlapping fare rules | MEDIUM | Quality |
| FAR_011 | payment_method missing | CRITICAL | Spec |
| FAR_013 | price does not carry the currency's ISO 4217 decimal places | INFO | Quality |
| FAR_012 | fare_id missing | CRITICAL | Spec |

## FRL — Fare Rules

| Rule | Title | Severity | Class |
|---|---|---|---|
| FRL_001 | fare_id not found | CRITICAL | Spec |
| FRL_002 | route_id not found | CRITICAL | Spec |
| FRL_003 | origin_id invalid | CRITICAL | Spec |
| FRL_004 | destination_id invalid | CRITICAL | Spec |
| FRL_005 | contains_id invalid | CRITICAL | Spec |
| FRL_006 | No fare rules defined | INFO | Quality |
| FRL_007 | Fare rule logical inconsistency | MEDIUM | Quality |
| FRL_008 | No fare defined for all routes | INFO | Quality |
| FRL_009 | Origin/destination fare coverage incomplete | MEDIUM | Quality |

## RCT — Rider Categories (Fares v2)

| Rule | Title | Severity | Class |
|---|---|---|---|
| RCT_001 | Duplicate rider_category_id | CRITICAL | Spec |
| RCT_002 | rider_category_name missing | CRITICAL | Spec |
| RCT_003 | is_default_fare_category invalid | CRITICAL | Spec |
| RCT_004 | min_age or max_age invalid (GTFS extension field — not in the official spec) | MEDIUM | Quality |
| RCT_005 | max_age less than min_age | MEDIUM | Quality |
| RCT_006 | fare_product does not have exactly one default rider category | MEDIUM | Spec |
| RCT_007 | eligibility_url is invalid | LOW | Spec |
| RCT_008 | rider_category_id is empty | CRITICAL | Spec |

## FMD — Fare Media (Fares v2)

| Rule | Title | Severity | Class |
|---|---|---|---|
| FMD_001 | Duplicate fare_media_id | CRITICAL | Spec |
| FMD_002 | fare_media_type missing or invalid | CRITICAL | Spec |
| FMD_003 | fare_media_name recommended for TransitCard/MobileApp | LOW | Quality |
| FMD_004 | fare_media_id is empty | CRITICAL | Spec |

## FPD — Fare Products (Fares v2)

| Rule | Title | Severity | Class |
|---|---|---|---|
| FPD_001 | Duplicate fare_products composite key | CRITICAL | Spec |
| FPD_002 | amount missing or not numeric | CRITICAL | Spec |
| FPD_003 | currency invalid ISO 4217 code | CRITICAL | Spec |
| FPD_004 | fare_media_id not found | CRITICAL | Spec |
| FPD_005 | rider_category_id not found | CRITICAL | Spec |
| FPD_007 | amount does not carry the currency's ISO 4217 decimal places | LOW | Spec |

## FLG — Fare Leg Rules (Fares v2)

| Rule | Title | Severity | Class |
|---|---|---|---|
| FLG_001 | fare_product_id not found | CRITICAL | Spec |
| FLG_002 | network_id not found | CRITICAL | Spec |
| FLG_003 | from_area_id not found | CRITICAL | Spec |
| FLG_004 | to_area_id not found | CRITICAL | Spec |
| FLG_005 | from_timeframe_group_id not found | CRITICAL | Spec |
| FLG_006 | to_timeframe_group_id not found | CRITICAL | Spec |
| FLG_007 | rule_priority invalid | MEDIUM | Spec |
| FLG_008 | fare_product_id missing | CRITICAL | Spec |

## FLJ

| Rule | Title | Severity | Class |
|---|---|---|---|
| FLJ_001 | from_network_id missing or not found | CRITICAL | Spec |
| FLJ_002 | to_network_id missing or not found | CRITICAL | Spec |
| FLJ_003 | from_stop_id missing or not found | CRITICAL | Spec |
| FLJ_004 | to_stop_id missing or not found | CRITICAL | Spec |

## FTR — Fare Transfer Rules (Fares v2)

| Rule | Title | Severity | Class |
|---|---|---|---|
| FTR_001 | fare_transfer_type missing or invalid | CRITICAL | Spec |
| FTR_002 | from_leg_group_id not found | CRITICAL | Spec |
| FTR_003 | to_leg_group_id not found | CRITICAL | Spec |
| FTR_004 | fare_product_id not found | CRITICAL | Spec |
| FTR_005 | duration_limit_type invalid | CRITICAL | Spec |
| FTR_006 | duration_limit invalid | MEDIUM | Spec |
| FTR_007 | duration_limit_type defined without duration_limit | MEDIUM | Spec |
| FTR_008 | transfer_count invalid | MEDIUM | Spec |
| FTR_009 | transfer_count required when leg groups equal | MEDIUM | Spec |
| FTR_010 | transfer_count forbidden when leg groups differ | MEDIUM | Spec |
| FTR_011 | duration_limit set but duration_limit_type missing | MEDIUM | Spec |

## ARS — Areas (Fares v2)

| Rule | Title | Severity | Class |
|---|---|---|---|
| ARS_001 | Duplicate area_id | CRITICAL | Spec |
| ARS_002 | areas.txt has an empty area_id | CRITICAL | Spec |

## SAR — Stop Areas (Fares v2)

| Rule | Title | Severity | Class |
|---|---|---|---|
| SAR_001 | area_id not found | CRITICAL | Spec |
| SAR_002 | stop_id not found | CRITICAL | Spec |
| SAR_003 | stop_areas has an empty area_id | CRITICAL | Spec |
| SAR_004 | stop_areas has an empty stop_id | CRITICAL | Spec |

## NET — Networks (Fares v2)

| Rule | Title | Severity | Class |
|---|---|---|---|
| NET_001 | Duplicate network_id | CRITICAL | Spec |
| NET_002 | route_networks.network_id is missing or not found | CRITICAL | Spec |
| NET_003 | route_networks.route_id is missing or not found | CRITICAL | Spec |
| NET_004 | networks.txt has an empty network_id | CRITICAL | Spec |

## TFR — Timeframes (Fares v2)

| Rule | Title | Severity | Class |
|---|---|---|---|
| TFR_001 | timeframe_group_id missing | CRITICAL | Spec |
| TFR_002 | service_id not found | CRITICAL | Spec |
| TFR_003 | start_time or end_time format error | HIGH | Spec |
| TFR_004 | end_time less than start_time | MEDIUM | Quality |
| TFR_005 | Overlapping time ranges within same group and service_id | MEDIUM | Spec |
| TFR_006 | start_time or end_time greater than 24:00:00 | CRITICAL | Spec |
| TFR_007 | Only one of start_time and end_time is specified | CRITICAL | Spec |
| TFR_008 | timeframes has an empty service_id | CRITICAL | Spec |

## PTH — Pathways

| Rule | Title | Severity | Class |
|---|---|---|---|
| PTH_001 | Duplicate pathway_id | CRITICAL | Spec |
| PTH_002 | from_stop_id not found | CRITICAL | Spec |
| PTH_003 | to_stop_id not found | CRITICAL | Spec |
| PTH_004 | pathway_mode missing or invalid | CRITICAL | Spec |
| PTH_005 | is_bidirectional missing | CRITICAL | Spec |
| PTH_006 | length invalid | MEDIUM | Spec |
| PTH_007 | traversal_time invalid | MEDIUM | Spec |
| PTH_008 | stair_count missing | LOW | Quality |
| PTH_009 | max_slope missing | LOW | Quality |
| PTH_010 | min_width invalid | LOW | Spec |
| PTH_011 | Pathway forms a loop | HIGH | Quality |
| PTH_012 | No accessible pathway to station | HIGH | Spec |
| PTH_013 | Accessible pathway analysis | INFO | Analytics |
| PTH_014 | Pathway crosses station boundary | CRITICAL | Quality |
| PTH_015 | Pathway leads to an unreachable stop | MEDIUM | Analytics |
| PTH_016 | Exit defined as bidirectional | HIGH | Spec |
| PTH_017 | max_slope is not a number | MEDIUM | Spec |
| PTH_018 | signposted_as too long | LOW | Quality |
| PTH_019 | Generic node connected to single pathway (dead-end) | MEDIUM | Quality |
| PTH_020 | pathway_id missing | CRITICAL | Spec |
| PTH_021 | from_stop_id missing | CRITICAL | Spec |
| PTH_022 | to_stop_id missing | CRITICAL | Spec |
| PTH_023 | pathway_mode missing | CRITICAL | Spec |
| PTH_024 | is_bidirectional missing | CRITICAL | Spec |
| PTH_025 | Recommended pathway length missing | LOW | Quality |
| PTH_030 | Pathway assigned to a platform that has boarding areas | LOW | Spec |
| PTH_029 | Recommended pathway traversal_time missing | LOW | Quality |
| PTH_026 | Pathway endpoint is a station | CRITICAL | Spec |
| PTH_031 | Pathway endpoint is a street-accessed stop (stop_access=1) | CRITICAL | Spec |
| PTH_027 | stair_count is invalid (zero or not an integer) | MEDIUM | Spec |
| PTH_028 | max_slope used outside a walkway | LOW | Quality |

## LVL — Levels

| Rule | Title | Severity | Class |
|---|---|---|---|
| LVL_001 | Duplicate level_id | CRITICAL | Spec |
| LVL_002 | level_index invalid | CRITICAL | Spec |
| LVL_003 | level_name missing | LOW | Quality |
| LVL_004 | Unused level | LOW | Quality |
| LVL_005 | level_name too long | MEDIUM | Quality |
| LVL_006 | level_id missing on elevator-connected stop | MEDIUM | Quality |
| LVL_007 | level_index missing | CRITICAL | Spec |
| LVL_008 | level_id missing | CRITICAL | Spec |

## FIN — Feed Info

| Rule | Title | Severity | Class |
|---|---|---|---|
| FIN_001 | feed_publisher_name missing | CRITICAL | Spec |
| FIN_002 | feed_publisher_url missing or invalid | CRITICAL | Spec |
| FIN_003 | feed_lang missing | CRITICAL | Spec |
| FIN_004 | default_lang invalid | MEDIUM | Spec |
| FIN_005 | feed_start_date invalid | MEDIUM | Spec |
| FIN_006 | feed_end_date invalid or past | HIGH | Spec |
| FIN_007 | feed_version missing | LOW | Quality |
| FIN_008 | feed_contact_email invalid | LOW | Spec |
| FIN_009 | feed_contact_url invalid | LOW | Spec |
| FIN_010 | Feed validity expired | HIGH | Analytics |
| FIN_012 | feed_start_date is after feed_end_date | LOW | Spec |
| FIN_013 | fare_attributes.agency_id recommended but missing | INFO | Quality |
| FIN_014 | Feed validity dates (feed_start_date/feed_end_date) missing | LOW | Quality |
| FIN_015 | Multiple feed_info records | MEDIUM | Quality |
| FIN_016 | feed_start_date in the future (feed not yet active) | LOW | Quality |
| FIN_017 | Feed expires in the very distant future | INFO | Quality |
| FIN_018 | Both feed_contact_email and feed_contact_url missing | LOW | Quality |
| FIN_019 | Feed validity expires within 7 days | LOW | Quality |
| FIN_020 | Feed validity window shorter than 7 days | INFO | Quality |
