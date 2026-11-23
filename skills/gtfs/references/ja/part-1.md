## ARC — アーカイブ / ファイルレベル

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| ARC_001 | ZIPアーカイブを開けません | 致命的 | 仕様 |
| ARC_002 | ファイルをUTF-8で読み込めません | 致命的 | 品質 |
| ARC_003 | オプションファイルにUTF-8エンコードエラー | 中 | 品質 |
| ARC_004 | 必須ファイルが不足 | 致命的 | 仕様 |
| ARC_006 | オプションのGTFSファイルが存在 | 情報 | 分析 |
| ARC_007 | GTFS仕様外のファイル | 情報 | 品質 |
| ARC_008 | カレンダーファイルが不足（calendar.txt・calendar_dates.txtの両方） | 致命的 | 仕様 |
| ARC_031 | translations.txtがあるのにfeed_info.txtがない | 致命的 | 仕様 |
| ARC_009 | 任意ファイルにデータ行なし | 情報 | 品質 |
| ARC_010 | ファイルにUTF-8 BOMあり | 情報 | 品質 |
| ARC_011 | ファイルサイズ（情報） | 情報 | 分析 |
| ARC_012 | 行の列数がヘッダーと不一致 | 致命的 | 仕様 |
| ARC_013 | CSV解析エラー | 致命的 | 仕様 |
| ARC_014 | ヘッダーフィールドに前後の空白 | 中 | 品質 |
| ARC_015 | ヘッダー列が重複 | 致命的 | 相互運用 |
| ARC_025 | 必須列がヘッダーに存在しない | 致命的 | 仕様 |
| ARC_017 | GTFS仕様外の列名 | 情報 | 品質 |
| ARC_018 | 空データ行 | 中 | 品質 |
| ARC_019 | ヘッダーに空の列名 | 高 | 品質 |
| ARC_020 | 推奨ファイルが不足（shapes.txtまたはfeed_info.txt） | 低 | 品質 |
| ARC_021 | 非印刷可能または問題のある文字 | 低 | 品質 |
| ARC_022 | ファイルの行数が参考閾値（100万行）を超過 | 情報 | 分析 |
| ARC_023 | GTFSアーカイブ内のネストされたZIPファイル | 中 | 品質 |
| ARC_024 | サブディレクトリ内のGTFS .txtファイル（読み込み不可） | 中 | 仕様 |
| ARC_026 | 不正な改行文字 | 中 | 仕様 |
| ARC_027 | ZIPエントリにユーザー読み取り権限がない | 情報 | 品質 |
| ARC_028 | GTFS公開URLが.zipファイル名で終わっていない | 低 | 品質 |
| ARC_029 | Zip爆弾保護：アーカイブがzip爆弾の上限を超えました | 致命的 | 品質 |
| ARC_030 | フィールド値にタブまたは改行 | 高 | 仕様 |
| ARC_032 | フィールド値にHTMLマークアップまたは文字参照 | 高 | 仕様 |
| ARC_033 | フィールド値にエスケープされていない引用符（RFC 4180） | 高 | 仕様 |
| ARC_034 | ヘッダー行がデータ行として繰り返されている | 高 | 仕様 |
| ARC_035 | 必須ファイルが空 | 致命的 | 仕様 |
| ARC_036 | ZIPストリームヘッダーが中央ディレクトリと矛盾 | 低 | 品質 |
| ARC_037 | ID列にASCII以外の文字 | 低 | 品質 |

## BKR — 予約ルール（Booking Rules）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| BKR_001 | 予約ルール: prior_notice_start_dayが禁止コンテキスト | 高 | 仕様 |
| BKR_003 | prior_notice_start_timeにprior_notice_start_dayが必要 | 高 | 仕様 |
| BKR_004 | リアルタイム予約でprior_noticeフィールドが禁止 | 高 | 仕様 |
| BKR_005 | prior_notice_duration_maxはbooking_type=1のみ有効 | 中 | 仕様 |
| BKR_006 | prior_notice_duration_minが無効 | 高 | 仕様 |
| BKR_007 | booking_type=1でprior_notice_duration_minが必須 | 致命的 | 仕様 |
| BKR_008 | booking_type=2でprior_notice_last_dayが必須 | 致命的 | 仕様 |
| BKR_009 | booking_type=2でprior_notice_last_timeが必須 | 致命的 | 仕様 |
| BKR_010 | prior_notice_start_day設定時にprior_notice_start_timeが必須 | 高 | 仕様 |
| BKR_011 | prior_notice_start_day > prior_notice_last_day（無効な予約ウィンドウ） | 高 | 相互運用 |
| BKR_012 | booking_type=2でprior_notice_duration_min禁止 | 中 | 仕様 |
| BKR_013 | prior_notice_last_timeにprior_notice_last_dayが必要 | 高 | 仕様 |
| BKR_014 | prior_notice_service_idはbooking_type=2のみ有効 | 高 | 仕様 |
| BKR_015 | prior_notice_service_idが見つかりません（calendar/calendar_dates） | 致命的 | 仕様 |
| BKR_016 | booking_typeが未設定または無効 | 致命的 | 仕様 |
| BKR_017 | pickup_booking_rule_idが見つかりません（booking_rules） | 致命的 | 仕様 |
| BKR_018 | drop_off_booking_rule_idが見つかりません（booking_rules） | 致命的 | 仕様 |
| BKR_019 | booking_rule_idが未設定または重複 | 致命的 | 仕様 |
| BKR_024 | booking_type=1 かつ duration_max がある場合 prior_notice_start_day は禁止 | 中 | 仕様 |
| BKR_020 | booking_urlが無効 | 中 | 仕様 |
| BKR_021 | info_urlが無効 | 低 | 仕様 |
| BKR_022 | phone_numberが無効 | 低 | 品質 |
| BKR_023 | prior_notice数値項目が整数でない | 中 | 仕様 |
| BKR_025 | prior_notice時刻項目が有効な時刻でない | 中 | 仕様 |

## AGN — 事業者（Agency）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| AGN_002 | agency_nameが不足 | 致命的 | 仕様 |
| AGN_003 | agency_urlが不足または無効 | 致命的 | 仕様 |
| AGN_004 | agency_timezoneが不足または無効 | 致命的 | 仕様 |
| AGN_005 | 事業者間でタイムゾーンが不一致 | 中 | 仕様 |
| AGN_006 | agency_langが無効 | 低 | 仕様 |
| AGN_007 | agency_phoneが無効 | 低 | 品質 |
| AGN_008 | agency_fare_urlが無効 | 低 | 仕様 |
| AGN_009 | agency_emailが無効 | 低 | 仕様 |
| AGN_010 | agency_idが重複 | 致命的 | 仕様 |
| AGN_011 | 複数事業者でagency_idなし | 致命的 | 仕様 |
| AGN_012 | cemv_supportが無効（事業者） | 低 | 仕様 |
| AGN_013 | フィード言語と事業者言語が不一致 | 低 | 相互運用 |
| AGN_014 | 複数事業者だがagency.txtにagency_idなし | 致命的 | 仕様 |
| AGN_015 | agency_urlが安全でないhttp | 情報 | 品質 |
| AGN_016 | agency_phoneが疑わしい/プレースホルダー | 情報 | 品質 |
| AGN_017 | 事業者間で agency_lang が不一致 | 低 | 相互運用 |
| AGN_018 | 単一事業者でagency_idが空 | 情報 | 品質 |

## STP — 停留所（Stops）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| STP_001 | stop_idが重複 | 致命的 | 仕様 |
| STP_002 | stop_idが空 | 致命的 | 仕様 |
| STP_003 | stop_nameが不足またはstop_latが範囲外 | 致命的 | 仕様 |
| STP_004 | stop_latが数値でない | 致命的 | 仕様 |
| STP_005 | stop_lonが無効または範囲外 | 致命的 | 仕様 |
| STP_006 | stop_latが不足 | 致命的 | 仕様 |
| STP_007 | stop_lonが不足 | 致命的 | 仕様 |
| STP_008 | location_typeが無効 | 高 | 仕様 |
| STP_009 | parent_stationがstops.txtに存在しない | 致命的 | 仕様 |
| STP_010 | parent_stationのlocation_typeが1でない | 高 | 仕様 |
| STP_011 | このlocation_typeにはparent_stationが必須 | 致命的 | 仕様 |
| STP_012 | stop_timesで使用される停留所のlocation_typeが不適切 | 致命的 | 仕様 |
| STP_013 | wheelchair_boardingが無効 | 低 | 仕様 |
| STP_014 | stop_timezoneが無効 | 中 | 仕様 |
| STP_015 | level_idがlevels.txtに存在しない | 致命的 | 仕様 |
| STP_016 | 同座標の停留所が別に存在 | 中 | 品質 |
| STP_017 | 停留所間が近すぎる | 低 | 品質 |
| STP_018 | 停留所が存在しない | 致命的 | 仕様 |
| STP_019 | stop_nameが長すぎる | 情報 | 品質 |
| STP_020 | どの便にも使用されていない停留所 | 中 | 分析 |
| STP_021 | 乗車エリアの親がプラットフォームでない | 高 | 品質 |
| STP_022 | stop_codeが不足 | 中 | 品質 |
| STP_023 | tts_stop_nameが無効 | 低 | 品質 |
| STP_024 | stop_accessがK2互換範囲外 | 情報 | 品質 |
| STP_026 | stop_accessが有効な列挙値でない | 低 | 仕様 |
| STP_028 | stop_codeが長すぎる | 情報 | 品質 |
| STP_029 | 停留所が親駅から遠い | 中 | 品質 |
| STP_030 | 子停留所のない駅 | 中 | 品質 |
| STP_031 | stop_nameとstop_descが同一 | 情報 | 品質 |
| STP_032 | 経路接続停留所にparent_stationなし | 中 | 品質 |
| STP_033 | zone_idが不足（運賃計算に必要） | 情報 | 品質 |
| STP_034 | stop_urlが事業者URLと同一 | 低 | 品質 |
| STP_035 | stop_urlが路線URLと同一 | 低 | 品質 |
| STP_036 | 駅（location_type=1）にparent_stationが設定されている | 低 | 仕様 |
| STP_037 | 一部の停留所で車椅子対応情報が未設定 | 情報 | 品質 |
| STP_038 | いずれの停留所も車椅子対応情報を報告していない | 情報 | 品質 |
| STP_039 | stop_codeが重複している | 低 | 品質 |
| STP_040 | 停留所名に冗長なstop/station語が含まれる | 低 | 品質 |
| STP_044 | platform_codeに冗長なplatform/track語が含まれる | 低 | 品質 |
| STP_045 | platform_codeがあるがparent_stationが空 | 情報 | 品質 |
| STP_046 | parent_stationのない停留所が駅のすぐ隣にある | 低 | 品質 |
| STP_047 | 同じ場所に2つの駅レコード | 低 | 品質 |
| STP_041 | 子停留所名に親駅名が含まれていない | 低 | 品質 |
| STP_042 | stop_urlが無効 | 低 | 仕様 |
| STP_043 | stop_accessが禁止された文脈で使用 | 中 | 仕様 |

## RTS — 路線（Routes）

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| RTS_001 | route_idが重複 | 致命的 | 仕様 |
| RTS_002 | agency_idがagency.txtに存在しない | 致命的 | 仕様 |
| RTS_003 | route_short_nameとroute_long_nameの両方が不足 | 致命的 | 仕様 |
| RTS_004 | route_typeが不足または無効 | 致命的 | 仕様 |
| RTS_005 | route_urlが無効 | 中 | 仕様 |
| RTS_006 | route_colorが有効な16進カラーでない | 中 | 仕様 |
| RTS_007 | route_text_colorが有効な16進カラーでない | 中 | 仕様 |
| RTS_008 | route_colorとroute_text_colorのコントラストが不十分 | 中 | 品質 |
| RTS_010 | route_short_nameが長すぎる | 低 | 品質 |
| RTS_011 | route_long_nameが長すぎる | 情報 | 品質 |
| RTS_012 | 便のない路線 | 中 | 品質 |
| RTS_013 | continuous_pickupが無効 | 低 | 仕様 |
| RTS_016 | アクティブなサービス日がない路線 | 低 | 品質 |
| RTS_017 | 形状が定義されていない路線 | 情報 | 品質 |
| RTS_018 | continuous_drop_offが無効 | 低 | 仕様 |
| RTS_019 | 路線名が重複 | 中 | 品質 |
| RTS_020 | 路線URLと事業者URLが同一 | 情報 | 品質 |
| RTS_021 | route_short_nameがGoogleトランジットの上限（6文字）を超過 | 低 | 品質 |
| RTS_022 | route_long_nameにroute_short_nameが含まれている | 低 | 品質 |
| RTS_023 | route_descが路線名の繰り返し | 情報 | 品質 |
| RTS_024 | cemv_supportが無効（路線） | 低 | 仕様 |
| RTS_025 | routes.txtのagency_idが空（推奨） | 情報 | 品質 |
| RTS_026 | 短い路線名の重複 | 情報 | 品質 |
| RTS_027 | 長い路線名の重複 | 情報 | 品質 |
| RTS_028 | Flex路線でcontinuous_pickup/drop_off禁止 | 高 | 仕様 |
| RTS_029 | route_sort_orderが無効 | 低 | 仕様 |
| RTS_030 | route_typeがコア列挙型外の拡張値 | 低 | 相互運用 |
| RTS_031 | route_idがありません | 致命的 | 仕様 |
