## SHP — 形状（Shapes）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| SHP_001 | shape_idが不足 | 致命的 | 仕様 |
| SHP_002 | shape_pt_latが不足または無効 | 致命的 | 仕様 |
| SHP_003 | shape_pt_lonが不足または無効 | 致命的 | 仕様 |
| SHP_004 | shape_pt_sequenceが不足または無効 | 致命的 | 仕様 |
| SHP_005 | shape_dist_traveledが減少 | 致命的 | 仕様 |
| SHP_006 | 形状点が1つしかない（最小2点必要） | 低 | 品質 |
| SHP_008 | shape_pt_sequence値が重複 | 致命的 | 仕様 |
| SHP_009 | 形状が自己交差している | 情報 | 分析 |
| SHP_010 | 連続する座標が同一 | 低 | 品質 |
| SHP_012 | 形状が便の停留所から遠すぎる | 高 | 分析 |
| SHP_014 | 最初または最後の停留所が形状端点から遠い | 情報 | 分析 |
| SHP_015 | 形状の点数が統計的に少なすぎる | 中 | 品質 |
| SHP_016 | 形状の方向が便方向と不一致 | 高 | 品質 |
| SHP_017 | 停留所順序が形状順序と矛盾 | 情報 | 分析 |
| SHP_018 | どの便にも参照されていない形状 | 低 | 品質 |
| SHP_019 | この形状を使用する便にstop_timesなし | 中 | 品質 |
| SHP_020 | 形状に重複点 | 情報 | 分析 |
| SHP_021 | shape_dist_traveledが負または数値でない | 低 | 仕様 |
| SHP_022 | 形状上の停留所位置が曖昧 | 高 | 品質 |
| SHP_023 | 連続する点が同座標で同一のshape_dist_traveled | 中 | 品質 |
| SHP_024 | shape_dist_traveledと形状距離が不一致 | 中 | 品質 |
| SHP_025 | stop_timesの距離が形状の総長を超過 | 中 | 品質 |
| SHP_026 | 形状の点数が極端に多い（>5,000） | 情報 | 分析 |
| SHP_028 | 同一shape_dist_traveledで座標が異なる | 高 | 仕様 |
| SHP_029 | 同一shape_dist_traveled、座標差が微小 | 情報 | 品質 |
| SHP_030 | stop_timesでshape_dist_traveledを使用しているが、形状距離が不足 | 中 | 品質 |

## FRQ — 頻度（Frequencies）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| FRQ_001 | trip_idがtrips.txtに存在しない | 致命的 | 仕様 |
| FRQ_002 | start_timeが無効 | 致命的 | 仕様 |
| FRQ_003 | end_timeが無効 | 致命的 | 仕様 |
| FRQ_004 | headway_secsが不足または無効 | 致命的 | 仕様 |
| FRQ_005 | end_timeがstart_timeより前 | 致命的 | 品質 |
| FRQ_006 | headway_secsが長すぎる | 中 | 分析 |
| FRQ_007 | exact_timesが無効 | 中 | 仕様 |
| FRQ_008 | headway_secsがゼロ（無効な頻度） | 致命的 | 仕様 |
| FRQ_009 | 頻度間隔が短すぎる | 中 | 品質 |
| FRQ_010 | 運行頻度が非常に高い（詰まりリスク） | 情報 | 分析 |
| FRQ_011 | frequencies 期間の重複 | 高 | 仕様 |
| FRQ_012 | exact_times=1 で end_time が headway の境界と一致 | 低 | 仕様 |

## TRF — 乗換（Transfers）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| TRF_001 | from_stop_idが不足 | 致命的 | 仕様 |
| TRF_002 | to_stop_idが不足 | 致命的 | 仕様 |
| TRF_003 | 指定のIDがstops.txtに存在しない | 致命的 | 仕様 |
| TRF_004 | transfer_typeが無効 | 高 | 仕様 |
| TRF_005 | min_transfer_timeが不足 | 致命的 | 仕様 |
| TRF_006 | from_trip_idがtrips.txtに存在しない | 致命的 | 仕様 |
| TRF_007 | to_trip_idがtrips.txtに存在しない | 致命的 | 仕様 |
| TRF_008 | from_route_idがroutes.txtに存在しない | 致命的 | 仕様 |
| TRF_009 | to_route_idがroutes.txtに存在しない | 致命的 | 仕様 |
| TRF_010 | min_transfer_timeが長すぎる | 中 | 分析 |
| TRF_011 | 停留所は定義されているが歩行距離が非常に長い | 情報 | 品質 |
| TRF_012 | 乗換レコードが重複 | 致命的 | 仕様 |
| TRF_013 | 乗換タイプがコンテキストと不一致 | 致命的 | 品質 |
| TRF_014 | 席内乗換に対応する便なし | 高 | 仕様 |
| TRF_015 | 席内乗換が無効 | 高 | 品質 |
| TRF_016 | 乗換条件が競合 | 致命的 | 仕様 |
| TRF_017 | 乗換が誤った路線を参照 | 高 | 仕様 |
| TRF_018 | from_trip_idとto_trip_idが同一の便 | 中 | 品質 |
| TRF_019 | 席内乗換で異なるroute_type | 中 | 相互運用 |
| TRF_020 | 乗継に必要な歩行速度が速すぎる | 中 | 品質 |
| TRF_021 | 乗換の端点が停留所でも駅でもない | 致命的 | 仕様 |
| TRF_022 | 1-to-n継続で運行カレンダーが矛盾 | 高 | 仕様 |
| TRF_023 | n-to-1継続で運行カレンダーが矛盾 | 高 | 仕様 |

## GGL — Googleトランジット互換性

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| GGL_001 | transfer_type=4/5はGoogleトランジット非対応 | 低 | 相互運用 |
| GGL_002 | ic_priceが無効な値 | 低 | 相互運用 |

## FAR — 運賃属性（Fare Attributes）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| FAR_001 | fare_idが重複 | 致命的 | 仕様 |
| FAR_002 | 運賃が不足または無効 | 致命的 | 仕様 |
| FAR_003 | currency_typeが不足 | 致命的 | 仕様 |
| FAR_004 | payment_methodが無効 | 致命的 | 仕様 |
| FAR_005 | transfersが無効 | 致命的 | 仕様 |
| FAR_006 | transfer_durationが無効 | 中 | 仕様 |
| FAR_008 | agency_idが存在しない | 致命的 | 仕様 |
| FAR_010 | 運賃ルールが重複 | 中 | 品質 |
| FAR_011 | payment_methodが不足 | 致命的 | 仕様 |
| FAR_013 | priceが通貨のISO 4217小数桁数と一致しません | 情報 | 品質 |
| FAR_012 | fare_idが不足 | 致命的 | 仕様 |

## FRL — 運賃ルール（Fare Rules）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| FRL_001 | fare_idがfares.txtに存在しない | 致命的 | 仕様 |
| FRL_002 | route_idがroutes.txtに存在しない | 致命的 | 仕様 |
| FRL_003 | origin_idが無効 | 致命的 | 仕様 |
| FRL_004 | destination_idが無効 | 致命的 | 仕様 |
| FRL_005 | contains_idが無効 | 致命的 | 仕様 |
| FRL_006 | 運賃ルールが定義されていない | 情報 | 品質 |
| FRL_007 | 運賃ルールの論理的不整合 | 中 | 品質 |
| FRL_008 | すべての路線をカバーする運賃が未定義 | 情報 | 品質 |
| FRL_009 | 発地・着地の運賃範囲が不完全 | 中 | 品質 |

## RCT — 乗客カテゴリー（Rider Categories, Fares v2）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| RCT_001 | rider_category_idが重複 | 致命的 | 仕様 |
| RCT_002 | rider_category_nameが不足 | 致命的 | 仕様 |
| RCT_003 | is_default_fare_categoryが無効 | 致命的 | 仕様 |
| RCT_004 | min_ageまたはmax_ageが無効（GTFS拡張フィールド — 公式仕様には存在しません） | 中 | 品質 |
| RCT_005 | max_ageがmin_ageより小さい | 中 | 品質 |
| RCT_006 | fare_productのデフォルトrider_category数が1件ではない | 中 | 仕様 |
| RCT_007 | eligibility_urlが無効 | 低 | 仕様 |
| RCT_008 | rider_category_idが空 | 致命的 | 仕様 |

## FMD — 運賃メディア（Fare Media, Fares v2）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| FMD_001 | fare_media_idが重複 | 致命的 | 仕様 |
| FMD_002 | fare_media_typeが不足または無効 | 致命的 | 仕様 |
| FMD_003 | TransitCard/MobileAppにfare_media_nameを推奨 | 低 | 品質 |
| FMD_004 | fare_media_idが空 | 致命的 | 仕様 |

## FPD — 運賃商品（Fare Products, Fares v2）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| FPD_001 | fare_productsの複合主キーが重複 | 致命的 | 仕様 |
| FPD_002 | 金額が不足または数値ではない | 致命的 | 仕様 |
| FPD_003 | currencyが有効なISO 4217コードでない | 致命的 | 仕様 |
| FPD_004 | fare_media_idが存在しない | 致命的 | 仕様 |
| FPD_005 | rider_category_idが存在しない | 致命的 | 仕様 |
| FPD_007 | amountが通貨のISO 4217小数桁数と一致しません | 低 | 仕様 |

## FLG — 運賃区間ルール（Fare Leg Rules, Fares v2）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| FLG_001 | fare_product_idが存在しない | 致命的 | 仕様 |
| FLG_002 | network_idが存在しない | 致命的 | 仕様 |
| FLG_003 | from_area_idが存在しない | 致命的 | 仕様 |
| FLG_004 | to_area_idが存在しない | 致命的 | 仕様 |
| FLG_005 | from_timeframe_group_idが存在しない | 致命的 | 仕様 |
| FLG_006 | to_timeframe_group_idが存在しない | 致命的 | 仕様 |
| FLG_007 | rule_priorityが無効 | 中 | 仕様 |
| FLG_008 | fare_product_idがありません | 致命的 | 仕様 |

## FLJ

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| FLJ_001 | from_network_idが未入力または不明 | 致命的 | 仕様 |
| FLJ_002 | to_network_idが未入力または不明 | 致命的 | 仕様 |
| FLJ_003 | from_stop_idが未入力または不明 | 致命的 | 仕様 |
| FLJ_004 | to_stop_idが未入力または不明 | 致命的 | 仕様 |

## FTR — 運賃乗換ルール（Fare Transfer Rules, Fares v2）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| FTR_001 | fare_transfer_typeが不足または無効 | 致命的 | 仕様 |
| FTR_002 | from_leg_group_idが存在しない | 致命的 | 仕様 |
| FTR_003 | to_leg_group_idが存在しない | 致命的 | 仕様 |
| FTR_004 | fare_product_idが存在しない | 致命的 | 仕様 |
| FTR_005 | duration_limit_typeが無効 | 致命的 | 仕様 |
| FTR_006 | duration_limitが無効 | 中 | 仕様 |
| FTR_007 | duration_limitなしでduration_limit_typeが設定されている | 中 | 仕様 |
| FTR_008 | transfer_countが無効 | 中 | 仕様 |
| FTR_009 | leg groupが同じ場合transfer_count必須 | 中 | 仕様 |
| FTR_010 | leg groupが異なる場合transfer_count禁止 | 中 | 仕様 |
| FTR_011 | duration_limit定義済みだがduration_limit_type欠如 | 中 | 仕様 |

## ARS — エリア（Areas, Fares v2）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| ARS_001 | area_idが重複 | 致命的 | 仕様 |
| ARS_002 | areas.txtのarea_idが空 | 致命的 | 仕様 |

## SAR — 停留所エリア（Stop Areas, Fares v2）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| SAR_001 | area_idが存在しない | 致命的 | 仕様 |
| SAR_002 | stop_idが存在しない | 致命的 | 仕様 |
| SAR_003 | stop_areasのarea_idが空 | 致命的 | 仕様 |
| SAR_004 | stop_areasのstop_idが空 | 致命的 | 仕様 |

## NET — ネットワーク（Networks, Fares v2）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| NET_001 | network_idが重複 | 致命的 | 仕様 |
| NET_002 | route_networks.network_idが未入力または不明 | 致命的 | 仕様 |
| NET_003 | route_networks.route_idが未入力または不明 | 致命的 | 仕様 |
| NET_004 | networks.txtのnetwork_idが空 | 致命的 | 仕様 |

## TFR — 時間帯（Timeframes, Fares v2）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| TFR_001 | timeframe_group_idが不足 | 致命的 | 仕様 |
| TFR_002 | service_idが存在しない | 致命的 | 仕様 |
| TFR_003 | start_timeまたはend_timeの形式が無効 | 高 | 仕様 |
| TFR_004 | end_timeがstart_timeより前 | 中 | 品質 |
| TFR_005 | 同一グループ・service_id内で時間範囲が重複 | 中 | 仕様 |
| TFR_006 | start_timeまたはend_timeが24:00:00超 | 致命的 | 仕様 |
| TFR_007 | start_timeとend_timeの一方のみ指定 | 致命的 | 仕様 |
| TFR_008 | timeframesのservice_idが空 | 致命的 | 仕様 |
