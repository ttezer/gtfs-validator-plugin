## TRP — Trips

| Rule | Title | Severity | Class |
|---|---|---|---|
| TRP_001 | trip_id missing or duplicate | CRITICAL | Spec |
| TRP_002 | route_id not found | CRITICAL | Spec |
| TRP_003 | service_id not found | CRITICAL | Spec |
| TRP_004 | shape_id not found | HIGH | Spec |
| TRP_005 | direction_id invalid | MEDIUM | Spec |
| TRP_006 | wheelchair_accessible invalid | LOW | Spec |
| TRP_007 | bikes_allowed invalid | LOW | Spec |
| TRP_032 | cars_allowed invalid | LOW | Spec |
| TRP_011 | Trip headsign not set | HIGH | Quality |
| TRP_012 | direction_id missing on bidirectional route | LOW | Quality |
| TRP_013 | Route has only one trip | INFO | Analytics |
| TRP_014 | trip_short_name too long | INFO | Quality |
| TRP_015 | block_id groups no trips | LOW | Quality |
| TRP_017 | Frequency-based trip missing from stop_times | MEDIUM | Quality |
| TRP_019 | shape_id missing with continuous service active | HIGH | Spec |
| TRP_020 | trip_headsign matches intermediate stop name | INFO | Analytics |
| TRP_021 | Bicycle allowance (bikes_allowed) not specified | INFO | Quality |
| TRP_022 | Overlapping trip times within block | HIGH | Interop |
| TRP_023 | No active trips in the next 7 days | LOW | Quality |
| TRP_024 | Inconsistent route type within block | LOW | Quality |
| TRP_025 | High proportion of trips without wheelchair accessibility information | INFO | Quality |
| TRP_026 | Trip with empty active-date set | MEDIUM | Analytics |
| TRP_028 | Some trips have not set wheelchair accessibility | INFO | Quality |
| TRP_029 | No trips report wheelchair accessibility | INFO | Quality |
| TRP_031 | route_id missing | CRITICAL | Spec |
| TRP_034 | safe_duration field is not a number | MEDIUM | Spec |
| TRP_035 | trips.txt has an empty service_id | CRITICAL | Spec |

## STM — Stop Times

| Rule | Title | Severity | Class |
|---|---|---|---|
| STM_001 | trip_id not found | CRITICAL | Spec |
| STM_002 | stop_id not found | CRITICAL | Spec |
| STM_003 | arrival_time invalid format | CRITICAL | Spec |
| STM_004 | departure_time invalid format | CRITICAL | Spec |
| STM_005 | stop_sequence missing or invalid | CRITICAL | Spec |
| STM_006 | stop_id missing (stop_times) | CRITICAL | Spec |
| STM_007 | Departure time before arrival time | HIGH | Interop |
| STM_008 | Time decreases between stops | CRITICAL | Interop |
| STM_009 | pickup_type invalid | HIGH | Spec |
| STM_010 | drop_off_type invalid | HIGH | Spec |
| STM_012 | Unrealistic speed between stops | HIGH | Interop |
| STM_014 | Excessive speed in segment | HIGH | Analytics |
| STM_015 | First stop is missing arrival_time | CRITICAL | Spec |
| STM_016 | Last stop is missing arrival_time | CRITICAL | Spec |
| STM_017 | Shape distance missing in stop times | MEDIUM | Quality |
| STM_018 | continuous_pickup invalid (stop_times) | MEDIUM | Spec |
| STM_019 | continuous_drop_off invalid (stop_times) | MEDIUM | Spec |
| STM_020 | Zero travel time (distance > 200m) | HIGH | Quality |
| STM_021 | Distance between stops is zero or negative | INFO | Analytics |
| STM_022 | timepoint invalid | MEDIUM | Spec |
| STM_024 | shape_dist_traveled unit inconsistency | INFO | Quality |
| STM_025 | Short segment timing | INFO | Analytics |
| STM_026 | Excessive distance between stops | INFO | Analytics |
| STM_028 | Trip duration too long | HIGH | Analytics |
| STM_029 | Trip duration too short | MEDIUM | Analytics |
| STM_030 | shape_dist_traveled is negative or not a number | LOW | Spec |
| STM_032 | Duplicate stop_sequence within trip | LOW | Spec |
| STM_033 | Single-stop trip (unusable) | HIGH | Interop |
| STM_034 | Only one of arrival or departure time defined | MEDIUM | Interop |
| STM_035 | Same stop visited twice consecutively (terminal/loop) | INFO | Analytics |
| STM_036 | stop_times not sorted by trip_id + stop_sequence (unsorted_stop_times) | INFO | Quality |
| STM_037 | arrival_time/departure_time prohibited in Flex window | HIGH | Spec |
| STM_038 | start_pickup_drop_off_window >= end_pickup_drop_off_window | HIGH | Interop |
| STM_039 | Pickup/drop-off window missing in Flex context | CRITICAL | Spec |
| STM_040 | pickup/drop_off_booking_rule_id missing in Flex stop_times (Optional in the spec) | MEDIUM | Quality |
| STM_060 | Zone, window and pickup/drop-off overlap at once within a trip | HIGH | Spec |
| STM_061 | Impossible speed between distant non-consecutive stops | HIGH | Interop |
| STM_059 | booking_rule_id recommended when pickup_type/drop_off_type=2 | LOW | Quality |
| STM_041 | stop_id and location_id/group_id cannot be used together | HIGH | Spec |
| STM_042 | stop_headsign contains characters unsupported by Google Transit | LOW | Interop |
| STM_043 | Trip has extreme stop count (>200) | INFO | Analytics |
| STM_044 | Feed stop_times exceeds 2,000,000 rows (WASM performance warning) | INFO | Analytics |
| STM_045 | Trip departure time exceeds the service day window | INFO | Analytics |
| STM_046 | trip_id missing | CRITICAL | Spec |
| STM_047 | timepoint=1 without arrival/departure time | CRITICAL | Spec |
| STM_048 | After-midnight service-day times written as 00:xx (GTFS Spec) | HIGH | Spec |
| STM_049 | After-midnight departure written as 00:xx on the same row (GTFS Spec) | HIGH | Spec |
| STM_050 | timepoint column present but value empty | LOW | Quality |
| STM_051 | pickup_type 0/3 forbidden with Flex window | HIGH | Spec |
| STM_052 | drop_off_type 0 forbidden with Flex window | HIGH | Spec |
| STM_053 | Many consecutive stops have the same time | INFO | Analytics |
| STM_054 | continuous_pickup forbidden with Flex window | HIGH | Spec |
| STM_055 | continuous_drop_off forbidden with Flex window | HIGH | Spec |
| STM_056 | shape_dist_traveled does not increase | CRITICAL | Spec |
| STM_058 | Flex pickup/drop-off window time is invalid | CRITICAL | Spec |

## PDW — Pickup/Drop-off Window

| Rule | Title | Severity | Class |
|---|---|---|---|
| PDW_006 | Overlapping pickup/drop-off window for same trip+zone | MEDIUM | Analytics |

## LOC — locations.geojson

| Rule | Title | Severity | Class |
|---|---|---|---|
| LOC_001 | Unknown or invalid geometry type in locations.geojson | HIGH | Spec |
| LOC_012 | locations.geojson is not a valid GeoJSON FeatureCollection | HIGH | Spec |
| LOC_002 | Feature has null or missing geometry | CRITICAL | Spec |
| LOC_003 | Feature missing required 'id' property | CRITICAL | Spec |
| LOC_004 | Polygon ring is not closed | MEDIUM | Spec |
| LOC_005 | FeatureCollection has no features | LOW | Quality |
| LOC_006 | Polygon area exceeds 500km² | INFO | Quality |
| LOC_007 | Duplicate feature 'id' in FeatureCollection | MEDIUM | Spec |
| LOC_008 | Feature 'type' member missing or not "Feature" | MEDIUM | Spec |
| LOC_009 | Feature 'properties' object missing | MEDIUM | Spec |
| LOC_011 | Invalid polygon: a ring self-intersects or a hole lies outside | HIGH | Spec |
| LOC_010 | Geometry 'coordinates' missing or not an array — the zone geometry cannot be resolved | CRITICAL | Spec |

## CAL — Calendar

| Rule | Title | Severity | Class |
|---|---|---|---|
| CAL_001 | Duplicate service_id | CRITICAL | Spec |
| CAL_002 | Calendar day field invalid value | CRITICAL | Spec |
| CAL_003 | start_date invalid | CRITICAL | Spec |
| CAL_004 | end_date invalid | CRITICAL | Spec |
| CAL_005 | start_date is after end_date | CRITICAL | Interop |
| CAL_006 | Weekly schedule has all days disabled | INFO | Quality |
| CAL_007 | Gap in service period | INFO | Analytics |
| CAL_008 | Service expires soon | INFO | Analytics |
| CAL_009 | All feed services have expired | INFO | Analytics |
| CAL_010 | Service has too few active days | MEDIUM | Analytics |
| CAL_011 | Unused service | LOW | Quality |
| CAL_012 | Service gap in the near future | INFO | Analytics |
| CAL_013 | Expired service period | INFO | Analytics |
| CAL_014 | Service dates outside feed_info validity range | INFO | Interop |
| CAL_015 | All calendar dates in the future (no active trips today) | INFO | Analytics |
| CAL_016 | Service extends to a very distant future date | INFO | Quality |
| CAL_017 | Calendar has not yet started (all active dates in the future) | INFO | Analytics |
| CAL_018 | Service has no active weekdays (all days 0, none overridden by calendar_dates) | INFO | Quality |
| CAL_020 | Feed validity window exceeds 5 years | INFO | Quality |
| CAL_021 | Active today but no service in the upcoming days | INFO | Analytics |
| CAL_022 | service_id missing | CRITICAL | Spec |
| CAL_023 | Calendar end_date far in the future (suspect) | MEDIUM | Quality |
| CAL_024 | Calendar inactive in the next 7 days | INFO | Analytics |
| CAL_025 | Calendar day field is empty | CRITICAL | Spec |

## CLD — Calendar Dates

| Rule | Title | Severity | Class |
|---|---|---|---|
| CLD_001 | service_id missing | CRITICAL | Spec |
| CLD_002 | date invalid format | CRITICAL | Spec |
| CLD_003 | exception_type missing or invalid | CRITICAL | Spec |
| CLD_004 | Calendar-dates-only service has no active dates | HIGH | Quality |
| CLD_005 | Date out of range | INFO | Quality |
| CLD_006 | Too many exception days | INFO | Analytics |
| CLD_007 | Excessive calendar exceptions | INFO | Analytics |

## SHP — Shapes

| Rule | Title | Severity | Class |
|---|---|---|---|
| SHP_001 | shape_id missing | CRITICAL | Spec |
| SHP_002 | shape_pt_lat missing or invalid | CRITICAL | Spec |
| SHP_003 | shape_pt_lon missing or invalid | CRITICAL | Spec |
| SHP_004 | shape_pt_sequence missing or invalid | CRITICAL | Spec |
| SHP_005 | shape_dist_traveled decreases | CRITICAL | Spec |
| SHP_006 | Shape consists of a single point only | LOW | Quality |
| SHP_008 | Duplicate shape_pt_sequence | CRITICAL | Spec |
| SHP_009 | Shape self-intersects | INFO | Analytics |
| SHP_010 | Repeated shape point (consecutive identical coordinates) | LOW | Quality |
| SHP_012 | Shape too far from trip stops | HIGH | Analytics |
| SHP_014 | First or last stop far from shape endpoint | INFO | Analytics |
| SHP_015 | Shape has statistically too few points | MEDIUM | Quality |
| SHP_016 | Shape direction inconsistent with trip direction | HIGH | Quality |
| SHP_017 | Stop sequence conflicts with shape | INFO | Analytics |
| SHP_018 | Shape not referenced by any trip | LOW | Quality |
| SHP_019 | Shape's trips have no stop times | MEDIUM | Quality |
| SHP_020 | Repeated point in shape | INFO | Analytics |
| SHP_021 | shape_dist_traveled is negative or not a number | LOW | Spec |
| SHP_022 | Stop position ambiguous on shape | HIGH | Quality |
| SHP_023 | Consecutive points with same shape_dist_traveled at same coordinates | MEDIUM | Quality |
| SHP_024 | Stop-to-shape distance inconsistent with shape_dist_traveled | MEDIUM | Quality |
| SHP_025 | Trip stop_times distance exceeds total shape distance | MEDIUM | Quality |
| SHP_026 | Shape has extreme point count (>5,000) | INFO | Analytics |
| SHP_028 | Same shape_dist_traveled with different coordinates | HIGH | Spec |
| SHP_029 | Same shape_dist_traveled, tiny coordinate difference | INFO | Quality |
| SHP_030 | stop_times uses shape_dist_traveled but shape distances are missing | MEDIUM | Quality |

## FRQ — Frequencies

| Rule | Title | Severity | Class |
|---|---|---|---|
| FRQ_001 | trip_id not found | CRITICAL | Spec |
| FRQ_002 | start_time invalid | CRITICAL | Spec |
| FRQ_003 | end_time invalid | CRITICAL | Spec |
| FRQ_004 | headway_secs missing or invalid | CRITICAL | Spec |
| FRQ_005 | end_time is before start_time | CRITICAL | Quality |
| FRQ_006 | headway_secs too long | MEDIUM | Analytics |
| FRQ_007 | exact_times invalid | MEDIUM | Spec |
| FRQ_008 | headway_secs is zero (invalid frequency) | CRITICAL | Spec |
| FRQ_009 | Frequency interval too short | MEDIUM | Quality |
| FRQ_010 | Very high frequency (bunching risk) | INFO | Analytics |
| FRQ_011 | Overlapping frequency periods | HIGH | Spec |
| FRQ_012 | exact_times=1 with end_time on a headway boundary | LOW | Spec |
