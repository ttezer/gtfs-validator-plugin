## DQ — データ品質 / ユーザー体験

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| DQ_003 | 路線の説明が不足 | 情報 | 品質 |
| DQ_004 | 路線URLが不足 | 情報 | 品質 |
| DQ_005 | 有効なサービス期間なし | 高 | 品質 |
| DQ_005b | stop_timesのある便なし | 高 | 品質 |
| DQ_005c | 座標なしの停留所の割合が高い | 高 | 品質 |
| DQ_006 | 形状なしの便の割合が高い | 高 | 品質 |
| DQ_009 | すべての便にstop_timesなし | 情報 | 品質 |
| DQ_010 | 事業者がどの路線にも使用されていない | 情報 | 品質 |
| DQ_011 | 停留所が1つしかない | 低 | 品質 |
| DQ_012 | 複数の事業者でagency_idが使用されていない | 低 | 品質 |
| DQ_013 | 便数が少なすぎる | 情報 | 分析 |
| DQ_016 | フィールド値に余分な空白 | 中 | 品質 |
| DQ_017 | 疑わしい座標値 | 情報 | 品質 |
| DQ_018 | 推奨フィールドが全大文字 | 中 | 品質 |
| DQ_019 | 推奨フィールドが全小文字 | 中 | 品質 |
| DQ_020 | 推奨フィールドが不足または空 | 低 | 品質 |
| DQ_021 | 主キーが重複 | 高 | 仕様 |
| DQ_022 | 停留所の80%以上が同じstop_name値を共有 | 高 | 品質 |

## VAT — エンティティ分析検出

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| VAT_001 | 路線の形状類似度が高い（重複路線の可能性） | 中 | 分析 |
| VAT_002 | 乗換ポイントが未定義（多くの路線が通過するが乗換なし） | 情報 | 分析 |
| VAT_003 | 便の所要時間が統計的な外れ値 | 低 | 分析 |
| VAT_005 | 孤立した停留所クラスター（ネットワークから切断） | 中 | 分析 |
| VAT_006 | サービス密度の偏り（1路線がフィードの大部分を占有） | 情報 | 分析 |
| VAT_007 | 終点の乗換不足（別路線が終点に来るが乗換未定義） | 情報 | 分析 |
| VAT_008 | 同じシェープがフィード路線の30%以上で使用 | 情報 | 分析 |

## JPN

| ルール | タイトル | 重要度 | クラス |
|---|---|---|---|
| JPN_001 | GTFS-JP：停留所名のかな（ja-Hrkt）読みが欠落 | 中 | 品質 |
| JPN_002 | GTFS-JP：jp_office_id が office_jp.txt に未定義 | 高 | 相互運用 |
| JPN_003 | GTFS-JP：agency_jp の agency_id が agency.txt に未定義 | 高 | 相互運用 |
| JPN_004 | GTFS-JP：translations.txt が欠如 | 高 | 相互運用 |
| JPN_005 | GTFS-JP：office_jp の office_name が空 | 高 | 相互運用 |
| JPN_006 | GTFS-JP：運賃ファイルが欠如 | 中 | 品質 |
| JPN_007 | GTFS-JP：feed_info.txt が欠如 | 中 | 品質 |
| JPN_008 | GTFS-JP：route_long_name のかな読みが欠如 | 中 | 品質 |
| JPN_009 | GTFS-JP：trip_headsign のかな読みが欠如 | 中 | 品質 |
| JPN_010 | GTFS-JP：agency_name のかな読みが欠如 | 中 | 品質 |
| JPN_011 | GTFS-JP：事業者が1つでもagency_idが必須 | 高 | 相互運用 |
| JPN_012 | GTFS-JP：agency_jp の agency_id が欠如 | 高 | 相互運用 |
| JPN_013 | GTFS-JP：agency_zip_number の形式が無効 | 中 | 品質 |
| JPN_014 | GTFS-JP：office_jp の office_id が欠如または重複 | 高 | 相互運用 |
| JPN_015 | GTFS-JP legacy：routes_jp の route_id が無効 | 高 | 相互運用 |
| JPN_016 | GTFS-JP：pattern_jp／旧版 routes_jp の route_update_date が無効 | 中 | 品質 |
| JPN_017 | GTFS-JP：jp_pattern_id が欠如または重複 | 高 | 相互運用 |
| JPN_018 | GTFS-JP：jp_pattern_id が未定義 | 高 | 相互運用 |
| JPN_019 | GTFS-JP：かな翻訳の参照が無効 | 中 | 相互運用 |
| JPN_020 | GTFS-JP：営業所連絡先の形式が不審 | 中 | 品質 |
| JPN_021 | GTFS-JP：かな翻訳が不整合 | 中 | 品質 |
| JPN_022 | GTFS-JP v4：必須コアフィールドが不足 | 中 | 相互運用 |
| JPN_023 | GTFS-JP：feed_langがjaではない | 高 | 相互運用 |
| JPN_024 | GTFS-JP：agency_langがjaではない | 高 | 相互運用 |
| JPN_025 | GTFS-JP：agency_timezoneがAsia/Tokyoではない | 高 | 相互運用 |
| JPN_026 | GTFS-JP：運賃通貨がJPYではない | 高 | 相互運用 |
| JPN_027 | GTFS-JP V3：route_type が 3 ではない | 高 | 相互運用 |
| JPN_028 | GTFS-JP v3：必須かな翻訳が不足 | 中 | 品質 |
| JPN_029 | GTFS-JP v4：推奨かな翻訳が不足 | 低 | 品質 |
| JPN_030 | GTFS-JP v3：必須日本語翻訳が不足 | 中 | 品質 |
| JPN_031 | GTFS-JP：ゾーン運賃の対象停留所に zone_id がない | 高 | 相互運用 |
| JPN_032 | GTFS-JP V3：agency_idが法人番号形式ではない | 中 | 相互運用 |
| JPN_033 | GTFS-JP：カスタムファイルまたはフィールドで予約済みjp名前空間を使用 | 中 | 相互運用 |
