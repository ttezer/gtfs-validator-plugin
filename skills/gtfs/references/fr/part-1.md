## ARC — Archive / niveau fichier

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| ARC_001 | Impossible d’ouvrir l’archive ZIP | CRITIQUE | Spec |
| ARC_002 | Fichier illisible en UTF-8 | CRITIQUE | Quality |
| ARC_003 | Erreur d’encodage UTF-8 dans un fichier optionnel | MOYENNE | Quality |
| ARC_004 | Fichier obligatoire manquant | CRITIQUE | Spec |
| ARC_006 | Fichier GTFS optionnel présent | INFO | Analytics |
| ARC_007 | Fichier non GTFS non reconnu | INFO | Quality |
| ARC_008 | Fichier de calendrier manquant (calendar.txt et calendar_dates.txt) | CRITIQUE | Spec |
| ARC_031 | feed_info.txt manquant alors que translations.txt est présent | CRITIQUE | Spec |
| ARC_009 | Le fichier facultatif ne contient aucun enregistrement de données | INFO | Quality |
| ARC_010 | Le fichier contient une BOM UTF-8 | INFO | Quality |
| ARC_011 | Taille du fichier (info) | INFO | Analytics |
| ARC_012 | Le nombre de colonnes ne correspond pas à l’en-tête | CRITIQUE | Spec |
| ARC_013 | Erreur d’analyse CSV | CRITIQUE | Spec |
| ARC_014 | Espaces en début ou en fin dans l’en-tête | MOYENNE | Quality |
| ARC_015 | Colonne d’en-tête en double | CRITIQUE | Interop |
| ARC_025 | Colonne obligatoire absente de l’en-tête | CRITIQUE | Spec |
| ARC_017 | Colonne inconnue (non définie dans la spécification GTFS) | INFO | Quality |
| ARC_018 | Enregistrement de données vide | MOYENNE | Quality |
| ARC_019 | Nom de colonne vide dans l’en-tête | ÉLEVÉE | Quality |
| ARC_020 | Fichier GTFS recommandé manquant (shapes.txt ou feed_info.txt) | FAIBLE | Quality |
| ARC_021 | Caractère non imprimable ou problématique dans un champ | FAIBLE | Quality |
| ARC_022 | Le nombre d’enregistrements dépasse le seuil indicatif de 1 000 000 | INFO | Analytics |
| ARC_023 | Fichier ZIP imbriqué dans l’archive GTFS | MOYENNE | Quality |
| ARC_024 | Fichier GTFS .txt dans un sous-répertoire (il ne sera pas analysé) | MOYENNE | Spec |
| ARC_026 | Caractères de fin de ligne mal formés | MOYENNE | Spec |
| ARC_027 | L’entrée ZIP n’a pas de droit de lecture utilisateur | INFO | Quality |
| ARC_028 | L’URL de publication GTFS ne se termine pas par un fichier .zip | FAIBLE | Quality |
| ARC_029 | Protection anti-bombe zip déclenchée | CRITIQUE | Quality |
| ARC_030 | Tabulation ou saut de ligne dans la valeur d’un champ | ÉLEVÉE | Spec |
| ARC_032 | Balise HTML ou séquence d’échappement dans la valeur d’un champ | ÉLEVÉE | Spec |
| ARC_033 | Guillemet non échappé dans la valeur d’un champ (RFC 4180) | ÉLEVÉE | Spec |
| ARC_034 | Ligne d’en-tête répétée comme enregistrement de données | ÉLEVÉE | Spec |
| ARC_035 | Fichier obligatoire vide | CRITIQUE | Spec |
| ARC_036 | En-tête de flux ZIP en contradiction avec le répertoire central | FAIBLE | Quality |
| ARC_037 | Caractère non ASCII dans un champ d’identifiant | FAIBLE | Quality |

## BKR — Règles de réservation

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| BKR_001 | Champ de réservation en jour antérieur défini dans un contexte interdit | ÉLEVÉE | Spec |
| BKR_003 | prior_notice_start_time valide uniquement avec prior_notice_start_day | ÉLEVÉE | Spec |
| BKR_004 | Champs prior_notice interdits pour la réservation en temps réel | ÉLEVÉE | Spec |
| BKR_005 | prior_notice_duration_max valide uniquement avec booking_type=1 | MOYENNE | Spec |
| BKR_006 | prior_notice_duration_min invalide (≤ 0 ou non numérique) | ÉLEVÉE | Spec |
| BKR_007 | prior_notice_duration_min obligatoire pour booking_type=1 | CRITIQUE | Spec |
| BKR_008 | prior_notice_last_day obligatoire pour booking_type=2 | CRITIQUE | Spec |
| BKR_009 | prior_notice_last_time obligatoire pour booking_type=2 | CRITIQUE | Spec |
| BKR_010 | prior_notice_start_time obligatoire lorsque prior_notice_start_day est défini | ÉLEVÉE | Spec |
| BKR_011 | prior_notice_last_day > prior_notice_start_day : fenêtre de réservation invalide | ÉLEVÉE | Interop |
| BKR_012 | prior_notice_duration_min interdit avec booking_type=2 | MOYENNE | Spec |
| BKR_013 | prior_notice_last_time valide uniquement avec prior_notice_last_day | ÉLEVÉE | Spec |
| BKR_014 | prior_notice_service_id valide uniquement avec booking_type=2 | ÉLEVÉE | Spec |
| BKR_015 | prior_notice_service_id introuvable (calendar/calendar_dates) | CRITIQUE | Spec |
| BKR_016 | booking_type manquant ou invalide | CRITIQUE | Spec |
| BKR_017 | pickup_booking_rule_id introuvable (booking_rules) | CRITIQUE | Spec |
| BKR_018 | drop_off_booking_rule_id introuvable (booking_rules) | CRITIQUE | Spec |
| BKR_019 | booking_rule_id manquant ou en double | CRITIQUE | Spec |
| BKR_024 | prior_notice_start_day interdit avec booking_type=1 et duration_max | MOYENNE | Spec |
| BKR_020 | booking_url invalide | MOYENNE | Spec |
| BKR_021 | info_url invalide | FAIBLE | Spec |
| BKR_022 | phone_number invalide | FAIBLE | Quality |
| BKR_023 | Le champ numérique prior_notice n’est pas un entier | MOYENNE | Spec |
| BKR_025 | Le champ horaire prior_notice n’est pas une heure valide | MOYENNE | Spec |

## AGN — Agence

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| AGN_002 | agency_name manquant | CRITIQUE | Spec |
| AGN_003 | agency_url manquant ou invalide | CRITIQUE | Spec |
| AGN_004 | agency_timezone manquant ou invalide | CRITIQUE | Spec |
| AGN_005 | Incohérence de fuseau horaire entre agences | MOYENNE | Spec |
| AGN_006 | agency_lang invalide | FAIBLE | Spec |
| AGN_007 | agency_phone invalide | FAIBLE | Quality |
| AGN_008 | agency_fare_url invalide | FAIBLE | Spec |
| AGN_009 | agency_email invalide | FAIBLE | Spec |
| AGN_010 | agency_id en double | CRITIQUE | Spec |
| AGN_011 | Plusieurs agences sans agency_id | CRITIQUE | Spec |
| AGN_012 | cemv_support invalide (agence) | FAIBLE | Spec |
| AGN_013 | Discordance entre la langue du jeu de données et celle de l’agence | FAIBLE | Interop |
| AGN_014 | Plusieurs agences mais agency_id manquant dans agency.txt | CRITIQUE | Spec |
| AGN_015 | agency_url utilise http non sécurisé | INFO | Quality |
| AGN_016 | agency_phone suspect ou factice | INFO | Quality |
| AGN_017 | agency_lang incohérent entre agences | FAIBLE | Interop |
| AGN_018 | agency_id vide dans un flux à agence unique | INFO | Quality |

## STP — Arrêts

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| STP_001 | stop_id en double | CRITIQUE | Spec |
| STP_002 | stop_id vide | CRITIQUE | Spec |
| STP_003 | stop_name manquant ou stop_lat hors plage | CRITIQUE | Spec |
| STP_004 | stop_lat non numérique | CRITIQUE | Spec |
| STP_005 | stop_lon invalide ou hors plage | CRITIQUE | Spec |
| STP_006 | stop_lat manquant | CRITIQUE | Spec |
| STP_007 | stop_lon manquant | CRITIQUE | Spec |
| STP_008 | location_type invalide | ÉLEVÉE | Spec |
| STP_009 | parent_station introuvable | CRITIQUE | Spec |
| STP_010 | parent_station n’est pas de location_type=1 | ÉLEVÉE | Spec |
| STP_011 | parent_station obligatoire pour une entrée, une sortie ou une zone d’embarquement | CRITIQUE | Spec |
| STP_012 | Station ou entrée utilisée dans stop_times | CRITIQUE | Spec |
| STP_013 | wheelchair_boarding invalide | FAIBLE | Spec |
| STP_014 | stop_timezone invalide | MOYENNE | Spec |
| STP_015 | level_id introuvable | CRITIQUE | Spec |
| STP_016 | Deux arrêts aux coordonnées identiques | MOYENNE | Quality |
| STP_017 | Deux arrêts trop proches l’un de l’autre | FAIBLE | Quality |
| STP_018 | Aucun arrêt trouvé | CRITIQUE | Spec |
| STP_019 | stop_name trop long | INFO | Quality |
| STP_020 | Arrêt sans aucune course | MOYENNE | Analytics |
| STP_021 | Le parent de la zone d’embarquement n’est pas un quai | ÉLEVÉE | Quality |
| STP_022 | stop_code manquant | MOYENNE | Quality |
| STP_023 | tts_stop_name invalide | FAIBLE | Quality |
| STP_024 | stop_access hors de la plage de compatibilité K2 | INFO | Quality |
| STP_026 | Valeur stop_access invalide | FAIBLE | Spec |
| STP_028 | stop_code trop long | INFO | Quality |
| STP_029 | Arrêt situé dans une station mais coordonnée trop éloignée | MOYENNE | Quality |
| STP_030 | La station parente n’a aucun arrêt enfant | MOYENNE | Quality |
| STP_031 | Le nom et la description de l’arrêt sont identiques | INFO | Quality |
| STP_032 | parent_station manquant pour un quai relié par cheminement | MOYENNE | Quality |
| STP_033 | zone_id de l’arrêt manquant (nécessaire au calcul tarifaire) | INFO | Quality |
| STP_034 | stop_url identique à l’URL de l’agence | FAIBLE | Quality |
| STP_035 | stop_url identique à l’URL de la ligne | FAIBLE | Quality |
| STP_036 | La station possède un parent_station (invalide) | FAIBLE | Spec |
| STP_037 | Certains arrêts n’indiquent pas l’accessibilité en fauteuil roulant | INFO | Quality |
| STP_038 | Aucun arrêt n’indique l’accessibilité en fauteuil roulant | INFO | Quality |
| STP_039 | stop_code en double | FAIBLE | Quality |
| STP_040 | Le nom de l’arrêt contient un mot redondant (arrêt ou station) | FAIBLE | Quality |
| STP_044 | platform_code contient un mot redondant (quai ou voie) | FAIBLE | Quality |
| STP_045 | platform_code sans parent_station | INFO | Quality |
| STP_046 | Arrêt sans parent_station juste à côté d’une station | FAIBLE | Quality |
| STP_047 | Deux enregistrements de station pour le même lieu | FAIBLE | Quality |
| STP_041 | Le nom de l’arrêt enfant ne reprend pas celui de la station parente | FAIBLE | Quality |
| STP_042 | stop_url invalide | FAIBLE | Spec |
| STP_043 | stop_access utilisé dans un contexte interdit | MOYENNE | Spec |

## RTS — Lignes

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| RTS_001 | route_id en double | CRITIQUE | Spec |
| RTS_002 | agency_id introuvable | CRITIQUE | Spec |
| RTS_003 | route_short_name et route_long_name tous deux manquants | CRITIQUE | Spec |
| RTS_004 | route_type manquant ou invalide | CRITIQUE | Spec |
| RTS_005 | route_url invalide | MOYENNE | Spec |
| RTS_006 | route_color n’est pas une couleur hexadécimale valide | MOYENNE | Spec |
| RTS_007 | route_text_color n’est pas une couleur hexadécimale valide | MOYENNE | Spec |
| RTS_008 | Contraste insuffisant entre la couleur de la ligne et celle du texte | MOYENNE | Quality |
| RTS_010 | route_short_name trop long | FAIBLE | Quality |
| RTS_011 | route_long_name trop long | INFO | Quality |
| RTS_012 | Ligne sans aucune course | MOYENNE | Quality |
| RTS_013 | continuous_pickup invalide | FAIBLE | Spec |
| RTS_016 | Ligne sans aucun jour de service actif | FAIBLE | Quality |
| RTS_017 | Ligne sans tracé défini | INFO | Quality |
| RTS_018 | continuous_drop_off invalide | FAIBLE | Spec |
| RTS_019 | Nom de ligne en double | MOYENNE | Quality |
| RTS_020 | La ligne et l’agence partagent la même URL | INFO | Quality |
| RTS_021 | route_short_name dépasse la limite Google Transit (6 caractères) | FAIBLE | Quality |
| RTS_022 | route_long_name contient route_short_name | FAIBLE | Quality |
| RTS_023 | route_desc reprend un nom de ligne | INFO | Quality |
| RTS_024 | cemv_support invalide (ligne) | FAIBLE | Spec |
| RTS_025 | agency_id vide dans routes.txt (recommandé) | INFO | Quality |
| RTS_026 | Nom court de ligne en double | INFO | Quality |
| RTS_027 | Nom long de ligne en double | INFO | Quality |
| RTS_028 | continuous_pickup/drop_off interdits sur une ligne Flex | ÉLEVÉE | Spec |
| RTS_029 | route_sort_order invalide | FAIBLE | Spec |
| RTS_030 | route_type utilise une valeur étendue hors de l’énumération principale | FAIBLE | Interop |
| RTS_031 | route_id manquant | CRITIQUE | Spec |
