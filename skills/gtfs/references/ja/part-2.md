## TRP — 便（Trips）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| TRP_001 | trip_idが重複 | 致命的 | 仕様 |
| TRP_002 | route_idがroutes.txtに存在しない | 致命的 | 仕様 |
| TRP_003 | service_idがカレンダーに存在しない | 致命的 | 仕様 |
| TRP_004 | shape_idがshapes.txtに存在しない | 高 | 仕様 |
| TRP_005 | direction_idが無効 | 中 | 仕様 |
| TRP_006 | wheelchair_accessibleが無効 | 低 | 仕様 |
| TRP_007 | bikes_allowedが無効 | 低 | 仕様 |
| TRP_032 | cars_allowedが無効 | 低 | 仕様 |
| TRP_011 | trip_headsignが未設定 | 高 | 品質 |
| TRP_012 | 双方向路線でdirection_idが不足 | 低 | 品質 |
| TRP_013 | 路線に便が1本のみ | 情報 | 分析 |
| TRP_014 | trip_short_nameが長すぎる | 情報 | 品質 |
| TRP_015 | block_idが便をまとめていない | 低 | 品質 |
| TRP_017 | 頻度ベースの便にstop_timesなし | 中 | 品質 |
| TRP_019 | 連続サービス中にshape_idが必須 | 高 | 仕様 |
| TRP_020 | trip_headsignが中間停留所名と一致 | 情報 | 分析 |
| TRP_021 | bikes_allowed（自転車可否）が未設定 | 情報 | 品質 |
| TRP_022 | block内での便時刻の重複 | 高 | 相互運用 |
| TRP_023 | 今後7日間にアクティブな便なし | 低 | 品質 |
| TRP_024 | block内での路線タイプの不一致 | 低 | 品質 |
| TRP_025 | 車椅子対応情報が未設定の便の割合が高い | 情報 | 品質 |
| TRP_026 | アクティブ日付セットが空の便 | 中 | 分析 |
| TRP_028 | 一部の便で車椅子対応情報が未設定 | 情報 | 品質 |
| TRP_029 | すべての便で車椅子対応情報が未報告 | 情報 | 品質 |
| TRP_031 | route_idが不足 | 致命的 | 仕様 |
| TRP_034 | safe_duration項目が数値でない | 中 | 仕様 |
| TRP_035 | trips.txtのservice_idが空 | 致命的 | 仕様 |

## STM — 停車時刻（Stop Times）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| STM_001 | trip_idがtrips.txtに存在しない | 致命的 | 仕様 |
| STM_002 | stop_idがstops.txtに存在しない | 致命的 | 仕様 |
| STM_003 | arrival_timeの形式エラー | 致命的 | 仕様 |
| STM_004 | departure_timeの形式エラー | 致命的 | 仕様 |
| STM_005 | stop_sequenceが不足または無効 | 致命的 | 仕様 |
| STM_006 | stop_idが不足 | 致命的 | 仕様 |
| STM_007 | 出発時刻が到着時刻より前（departure_time < arrival_time） | 高 | 相互運用 |
| STM_008 | 停留所間で時刻が逆転 | 致命的 | 相互運用 |
| STM_009 | pickup_typeが無効 | 高 | 仕様 |
| STM_010 | drop_off_typeが無効 | 高 | 仕様 |
| STM_012 | 非現実的な速度 | 高 | 相互運用 |
| STM_014 | セグメントで速度超過 | 高 | 分析 |
| STM_015 | 最初の停留所にarrival_timeがない | 致命的 | 仕様 |
| STM_016 | 最後の停留所にarrival_timeがない | 致命的 | 仕様 |
| STM_017 | stop_timesにshape_dist_traveledなし | 中 | 品質 |
| STM_018 | stop_timesのcontinuous_pickupが無効 | 中 | 仕様 |
| STM_019 | stop_timesのcontinuous_drop_offが無効 | 中 | 仕様 |
| STM_020 | 距離 > 200mでの走行時間ゼロ | 高 | 品質 |
| STM_021 | 異なる停留所が同座標を共有 | 情報 | 分析 |
| STM_022 | timepointが無効 | 中 | 仕様 |
| STM_024 | shape_dist_traveled単位の不一致 | 情報 | 品質 |
| STM_025 | 短い区間時刻 | 情報 | 分析 |
| STM_026 | 停留所間距離が超過 | 情報 | 分析 |
| STM_028 | 便の総所要時間が上限超過 | 高 | 分析 |
| STM_029 | 便の総所要時間が下限未満 | 中 | 分析 |
| STM_030 | shape_dist_traveledが負または数値でない | 低 | 仕様 |
| STM_032 | 便内でstop_sequenceが重複 | 低 | 仕様 |
| STM_033 | 便に停留所が1つしかなく使用不可 | 高 | 相互運用 |
| STM_034 | arrival_timeとdeparture_timeのいずれか一方のみ定義 | 中 | 相互運用 |
| STM_035 | 同じ停留所に連続して停車（折返し・ループ） | 情報 | 分析 |
| STM_036 | stop_timesがtrip_id + stop_sequenceでソートされていない | 情報 | 品質 |
| STM_037 | Flexの乗降ウィンドウ内に時刻が設定されている | 高 | 仕様 |
| STM_038 | start_pickup_drop_off_window >= end_pickup_drop_off_window | 高 | 相互運用 |
| STM_039 | Flexコンテキストで乗降ウィンドウが不足 | 致命的 | 仕様 |
| STM_040 | Flex stop_timesで予約ルールIDが不足（仕様上は任意） | 中 | 品質 |
| STM_060 | トリップ内でゾーン・時間帯・乗降車が同時に重複 | 高 | 仕様 |
| STM_061 | 連続しない離れた停留所間の速度が不可能 | 高 | 相互運用 |
| STM_059 | pickup_type/drop_off_type=2 の場合は booking_rule_id を推奨 | 低 | 品質 |
| STM_041 | stop_idとlocation_id/group_idの同時使用不可 | 高 | 仕様 |
| STM_042 | stop_headsignにGoogleトランジット非対応の文字 | 低 | 相互運用 |
| STM_043 | 便の停留所数が極端に多い（>200） | 情報 | 分析 |
| STM_044 | stop_times行数が200万超（WASMパフォーマンス警告） | 情報 | 分析 |
| STM_045 | 便の出発時刻がサービス日の範囲を超過 | 情報 | 分析 |
| STM_046 | trip_idが不足 | 致命的 | 仕様 |
| STM_047 | timepoint=1だが到着/出発時刻なし | 致命的 | 仕様 |
| STM_048 | GTFSサービス日の深夜以降の時刻が00:xx | 高 | 仕様 |
| STM_049 | 同一行の深夜以降の出発が00:xx（GTFS Spec） | 高 | 仕様 |
| STM_050 | timepoint列はあるが値が空 | 低 | 品質 |
| STM_051 | Flexウィンドウでpickup_type 0/3禁止 | 高 | 仕様 |
| STM_052 | Flexウィンドウでdrop_off_type 0禁止 | 高 | 仕様 |
| STM_053 | 多数の連続停留所が同じ時刻 | 情報 | 分析 |
| STM_054 | Flexウィンドウでcontinuous_pickup禁止 | 高 | 仕様 |
| STM_055 | Flexウィンドウでcontinuous_drop_off禁止 | 高 | 仕様 |
| STM_056 | shape_dist_traveledが増加していない | 致命的 | 仕様 |
| STM_058 | Flexの受降車ウィンドウ時刻が無効 | 致命的 | 仕様 |

## PDW — 乗降ウィンドウ（Pickup/Drop-off Window）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| PDW_006 | 同一便・ゾーンで乗降ウィンドウが重複 | 中 | 分析 |

## LOC — locations.geojson

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| LOC_001 | locations.geojsonのジオメトリタイプが無効 | 高 | 仕様 |
| LOC_012 | locations.geojsonが有効なGeoJSON FeatureCollectionではない | 高 | 仕様 |
| LOC_002 | フィーチャーのgeometryがnullまたは欠如 | 致命的 | 仕様 |
| LOC_003 | フィーチャーに'id'プロパティが不足 | 致命的 | 仕様 |
| LOC_004 | Polygonリングが閉じていない | 中 | 仕様 |
| LOC_005 | FeatureCollectionが空 | 低 | 品質 |
| LOC_006 | Polygonの面積が500km²超 | 情報 | 品質 |
| LOC_007 | FeatureCollection内でフィーチャー'id'が重複 | 中 | 仕様 |
| LOC_008 | Featureの'type'が欠落または"Feature"でない | 中 | 仕様 |
| LOC_009 | Featureの'properties'オブジェクトが欠落 | 中 | 仕様 |
| LOC_011 | 不正なポリゴン: リングが自己交差、または穴が外側にあります | 高 | 仕様 |
| LOC_010 | Geometryの'coordinates'が欠落または配列でない | 致命的 | 仕様 |

## CAL — カレンダー（Calendar）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| CAL_001 | service_idが重複 | 致命的 | 仕様 |
| CAL_002 | 曜日フィールドの値が無効 | 致命的 | 仕様 |
| CAL_003 | start_dateが欠落または無効な形式 | 致命的 | 仕様 |
| CAL_004 | end_dateが欠落または無効な形式 | 致命的 | 仕様 |
| CAL_005 | start_dateがend_dateより後 | 致命的 | 相互運用 |
| CAL_006 | 週次スケジュールで全曜日が無効 | 情報 | 品質 |
| CAL_007 | サービス期間に空白あり | 情報 | 分析 |
| CAL_008 | サービス期間が間もなく終了 | 情報 | 分析 |
| CAL_009 | フィードの全カレンダー期間が終了 | 情報 | 分析 |
| CAL_010 | アクティブ日数が少なすぎる | 中 | 分析 |
| CAL_011 | 使用されていないサービス | 低 | 品質 |
| CAL_012 | 近い将来のサービス空白 | 情報 | 分析 |
| CAL_013 | サービス期間が終了（最終日が過去） | 情報 | 分析 |
| CAL_014 | カレンダー日付がfeed_info有効期間外 | 情報 | 相互運用 |
| CAL_015 | フィードの最初のサービス日が将来（本日アクティブな便なし） | 情報 | 分析 |
| CAL_016 | サービスが2年以上先まで続く | 情報 | 品質 |
| CAL_017 | カレンダーがまだ開始していない（すべてのアクティブ日が将来） | 情報 | 分析 |
| CAL_018 | アクティブな曜日なし（全曜日0、calendar_dates上書きなし） | 情報 | 品質 |
| CAL_020 | フィード有効期間が5年超 | 情報 | 品質 |
| CAL_021 | 本日は有効だが今後数日間運行なし | 情報 | 分析 |
| CAL_022 | service_idが不足 | 致命的 | 仕様 |
| CAL_023 | カレンダーのend_dateが遠い未来（疑わしい） | 中 | 品質 |
| CAL_024 | 今後7日間にアクティブでないカレンダー | 情報 | 分析 |
| CAL_025 | カレンダーの曜日フィールドが空 | 致命的 | 仕様 |

## CLD — カレンダー例外（Calendar Dates）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| CLD_001 | service_idが不足 | 致命的 | 仕様 |
| CLD_002 | 日付が欠落または形式が無効 | 致命的 | 仕様 |
| CLD_003 | exception_typeが不足または無効 | 致命的 | 仕様 |
| CLD_004 | calendar_datesのみのサービスにアクティブな日付なし | 高 | 品質 |
| CLD_005 | 日付が合理的な年の範囲外 | 情報 | 品質 |
| CLD_006 | 例外日が多すぎる | 情報 | 分析 |
| CLD_007 | カレンダー例外が多すぎる | 情報 | 分析 |
