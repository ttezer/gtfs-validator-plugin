## PTH — 経路（Pathways）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| PTH_001 | pathway_idが重複 | 致命的 | 仕様 |
| PTH_002 | from_stop_idが存在しない | 致命的 | 仕様 |
| PTH_003 | to_stop_idが存在しない | 致命的 | 仕様 |
| PTH_004 | pathway_modeが不足または無効 | 致命的 | 仕様 |
| PTH_005 | is_bidirectionalが不足 | 致命的 | 仕様 |
| PTH_006 | lengthが無効 | 中 | 仕様 |
| PTH_007 | traversal_timeが無効 | 中 | 仕様 |
| PTH_008 | stair_countが不足 | 低 | 品質 |
| PTH_009 | max_slopeが不足 | 低 | 品質 |
| PTH_010 | min_widthが無効 | 低 | 仕様 |
| PTH_011 | 経路がループを形成 | 高 | 品質 |
| PTH_012 | 駅にアクセシブルな経路なし | 高 | 仕様 |
| PTH_013 | アクセシブル経路の分析 | 情報 | 分析 |
| PTH_014 | 経路が駅の境界を越えている | 致命的 | 品質 |
| PTH_015 | 経路が到達不能な停留所につながる | 中 | 分析 |
| PTH_016 | 出口が双方向として定義されている | 高 | 仕様 |
| PTH_017 | max_slopeが数値でない | 中 | 仕様 |
| PTH_018 | signposted_asが長すぎる | 低 | 品質 |
| PTH_019 | 汎用ノードが1経路にのみ接続（行き止まり） | 中 | 品質 |
| PTH_020 | pathway_idが不足 | 致命的 | 仕様 |
| PTH_021 | from_stop_idが不足 | 致命的 | 仕様 |
| PTH_022 | to_stop_idが不足 | 致命的 | 仕様 |
| PTH_023 | pathway_modeが不足 | 致命的 | 仕様 |
| PTH_024 | is_bidirectionalが不足 | 致命的 | 仕様 |
| PTH_025 | 推奨されるpathway lengthが不足 | 低 | 品質 |
| PTH_030 | 乗降場を持つプラットフォームに通路が割り当てられています | 低 | 仕様 |
| PTH_029 | 推奨されるpathway traversal_timeが不足 | 低 | 品質 |
| PTH_026 | 経路の端点が駅 | 致命的 | 仕様 |
| PTH_031 | 経路の端点が街路から直接アクセスされる停留所(stop_access=1) | 致命的 | 仕様 |
| PTH_027 | stair_countが無効（0または整数でない） | 中 | 仕様 |
| PTH_028 | max_slopeが歩道以外で使用 | 低 | 品質 |

## LVL — 階層（Levels）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| LVL_001 | level_idが重複 | 致命的 | 仕様 |
| LVL_002 | level_indexが無効 | 致命的 | 仕様 |
| LVL_003 | level_nameが不足 | 低 | 品質 |
| LVL_004 | 未使用の階層 | 低 | 品質 |
| LVL_005 | level_nameが長すぎる | 中 | 品質 |
| LVL_006 | エレベーター接続停留所にlevel_idなし | 中 | 品質 |
| LVL_007 | level_indexが不足 | 致命的 | 仕様 |
| LVL_008 | level_idが不足 | 致命的 | 仕様 |

## FIN — フィード情報（Feed Info）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| FIN_001 | feed_publisher_nameが不足 | 致命的 | 仕様 |
| FIN_002 | feed_publisher_urlが不足または無効 | 致命的 | 仕様 |
| FIN_003 | feed_langが不足 | 致命的 | 仕様 |
| FIN_004 | default_langが無効 | 中 | 仕様 |
| FIN_005 | feed_start_dateが無効 | 中 | 仕様 |
| FIN_006 | feed_end_dateが無効または過去の日付 | 高 | 仕様 |
| FIN_007 | feed_versionが不足 | 低 | 品質 |
| FIN_008 | feed_contact_emailが無効 | 低 | 仕様 |
| FIN_009 | feed_contact_urlが無効 | 低 | 仕様 |
| FIN_010 | フィードの有効期限が切れている | 高 | 分析 |
| FIN_012 | feed_start_dateがfeed_end_dateより後 | 低 | 仕様 |
| FIN_013 | fare_attributes.agency_idを推奨するが不足 | 情報 | 品質 |
| FIN_014 | feed_start_date・feed_end_dateの両方が不足 | 低 | 品質 |
| FIN_015 | feed_info.txtのレコードが複数 | 中 | 品質 |
| FIN_016 | feed_start_dateが将来（フィードがまだ有効でない） | 低 | 品質 |
| FIN_017 | フィードが非常に遠い将来に期限切れ | 情報 | 品質 |
| FIN_018 | feed_contact_emailとfeed_contact_urlの両方が不足 | 低 | 品質 |
| FIN_019 | フィードの有効期限まで7日以内 | 低 | 品質 |
| FIN_020 | フィード有効期間が7日未満 | 情報 | 品質 |

## TRN — 翻訳（Translations）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| TRN_001 | table_nameが無効な値 | 致命的 | 仕様 |
| TRN_002 | field_nameがこのテーブルで無効 | 致命的 | 仕様 |
| TRN_003 | languageが無効 | 中 | 仕様 |
| TRN_004 | record_idが存在しない | 高 | 仕様 |
| TRN_005 | 翻訳が重複 | 致命的 | 仕様 |
| TRN_006 | 翻訳レコードが競合 | 致命的 | 仕様 |
| TRN_007 | 翻訳がfeed_langと同一言語 | 低 | 品質 |
| TRN_008 | translationの値が空 | 致命的 | 仕様 |
| TRN_009 | record_idとfield_valueを同時使用不可 | 高 | 仕様 |
| TRN_010 | record_sub_idが無効 | 高 | 仕様 |
| TRN_011 | field_nameが翻訳不可 | 高 | 仕様 |
| TRN_013 | feed_info翻訳でIDフィールドを使用不可 | 高 | 仕様 |
| TRN_014 | record_sub_idはstop_timesのみ有効 | 高 | 仕様 |
| TRN_017 | stop_times翻訳にrecord_sub_idがありません（対象行が特定できません） | 中 | 仕様 |
| TRN_015 | record_idとfield_valueが両方空 | 高 | 仕様 |
| TRN_016 | field_valueがどのレコードとも一致しません（翻訳が適用されません） | 中 | 仕様 |

## LIC — ライセンス

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| LIC_001 | ライセンス情報がありません | 致命的 | 仕様 |
| LIC_002 | ライセンス情報が重複 | 致命的 | 仕様 |
| LIC_003 | 不明な対象ファイル | 中 | 相互運用 |
| LIC_004 | 対象ファイルが重複 | 致命的 | 仕様 |
| LIC_005 | 対象ファイルがありません | 情報 | 品質 |
| LIC_006 | フィード全体のライセンスがありません | 情報 | 品質 |
| LIC_007 | SPDXライセンスIDが一覧にありません | 情報 | 品質 |
| LIC_008 | 対象ファイル名が衝突 | 致命的 | 相互運用 |
| LIC_009 | 独自ライセンスURLが無効 | 致命的 | 仕様 |

## ATR — 帰属（Attributions）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| ATR_001 | attribution_idが不足 | 高 | 品質 |
| ATR_002 | organization_nameが不足 | 致命的 | 仕様 |
| ATR_003 | ロールが未定義（is_producer・is_operator・is_authority） | 高 | 仕様 |
| ATR_004 | is_producerが無効 | 致命的 | 仕様 |
| ATR_005 | is_operatorが無効 | 致命的 | 仕様 |
| ATR_006 | is_authorityが無効 | 致命的 | 仕様 |
| ATR_007 | attribution_urlが無効 | 致命的 | 仕様 |
| ATR_008 | attribution_emailが無効 | 低 | 仕様 |
| ATR_009 | 帰属参照フィールドが複数設定 | 高 | 仕様 |
| ATR_010 | agency_idが存在しない | 低 | 仕様 |
| ATR_011 | route_idが存在しない | 低 | 仕様 |
| ATR_012 | trip_idが存在しない | 低 | 仕様 |

## XFL — クロスファイル / 意味的整合性

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| XFL_002 | 便にstop_timesレコードなし | 高 | 相互運用 |
| XFL_006 | サービスにキャンセル例外のみ（アクティブ日なし） | 中 | 分析 |
| XFL_012 | 運行可能な便のない路線 | 高 | 品質 |
| XFL_013 | shape_idが複数の方向で使用されている | 高 | 品質 |
| XFL_014 | 翻訳のソースレコードが存在しない | 中 | 品質 |
| XFL_015 | 帰属の参照が無効 | 致命的 | 仕様 |
| XFL_016 | 翻訳でfeed_infoを参照しているがfeed_info.txtなし | 高 | 仕様 |
| XFL_019 | ネットワーク割り当てが2か所に定義されている | 中 | 仕様 |
| XFL_020 | （from_trip_id/to_trip_id, route_id）の組み合わせが無効 | 致命的 | 仕様 |
| XFL_021 | （from_trip_id/to_trip_id, stop_id）の組み合わせが無効 | 高 | 相互運用 |
| XFL_022 | location_group_idが存在しない | 致命的 | 仕様 |
| XFL_023 | stop_idが存在しない（location_group_stops） | 致命的 | 仕様 |
| XFL_024 | location_group_idが存在しない（stop_times） | 致命的 | 仕様 |
| XFL_025 | location_idが存在しない（locations.geojson） | 致命的 | 仕様 |
| XFL_031 | ID衝突：stop_id・locations.geojson id・location_group_idは共通の名前空間を持ちます | 致命的 | 仕様 |
| XFL_032 | location_groups.txtのlocation_group_idが空 | 致命的 | 仕様 |
| XFL_033 | location_group_stopsのlocation_group_idが空 | 致命的 | 仕様 |
| XFL_034 | location_group_stopsのstop_idが空 | 致命的 | 仕様 |
| XFL_027 | 路線cemv=2だが適用可能なcontactless productあり | 情報 | 相互運用 |
| XFL_028 | agency cemv=1だがcontactless mediaなし | 情報 | 品質 |
| XFL_029 | route cemv=1だがcontactless mediaなし | 情報 | 品質 |
| XFL_030 | contactless mediaありだがcemv=1なし | 情報 | 品質 |

## OPR — 運行整合性（Operational Consistency）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| OPR_001 | 路線の運行頻度が低い | 中 | 分析 |
| OPR_003 | 便の詰まり（最小間隔が短すぎる） | 低 | 分析 |
| OPR_004 | 週末運行なし | 情報 | 分析 |
| OPR_005 | 異常な運行頻度 | 情報 | 分析 |
| OPR_006 | 便の停留所数が少なすぎる | 高 | 分析 |
| OPR_007 | 便内の停留所再訪パターン | 情報 | 分析 |
| OPR_008 | 複数セグメントで速度超過 | 情報 | 分析 |
| OPR_009 | 深夜出発時刻が遅すぎる | 情報 | 分析 |
| OPR_010 | 路線でアクセシビリティまたは自転車ポリシーが競合 | 中 | 分析 |
| OPR_011 | サービスにアクティブな日なし | 高 | 分析 |
| OPR_012 | サービスの空白 | 中 | 分析 |
| OPR_013 | 路線が一方向のみ運行 | 情報 | 分析 |
| OPR_014 | フィード全体の平均乗換時間が長すぎる | 中 | 分析 |
| OPR_015 | 路線が1つの形状のみで運行 | 情報 | 分析 |
| OPR_016 | フィード全体でアクティブなサービスなし | 情報 | 分析 |
| OPR_017 | 便の距離が非常に短い | 中 | 分析 |
| OPR_019 | 路線で同日に複数のサービスが重複 | 情報 | 分析 |
| OPR_020 | 路線の例外日の重複 | 低 | 分析 |
| OPR_021 | カレンダー上書き競合: 上書きとベースが同時アクティブ | 高 | 分析 |
| OPR_022 | カレンダー上書き未適用: 上書き日にベースサービスが動いている | 高 | 分析 |
| OPR_023 | カレンダー上書き空白: ウィンドウ内にアクティブなサービスなし | 中 | 分析 |
| OPR_024 | 路線の便数が極端に多い | 情報 | 分析 |
| OPR_025 | フィード全体の平均便所要時間が60秒未満 | 高 | 分析 |
