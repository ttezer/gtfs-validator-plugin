## GEO — Géographique / spatial

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| GEO_002 | Arrêt trop éloigné de la médiane du jeu de données | ÉLEVÉE | Analytics |
| GEO_006 | Saut important dans le tracé | ÉLEVÉE | Analytics |
| GEO_007 | Saut critique dans le tracé (3× le seuil) | ÉLEVÉE | Analytics |
| GEO_009 | Arrêt trop éloigné du tracé de la ligne | ÉLEVÉE | Quality |
| GEO_012 | Grappe d’arrêts (arrêts trop proches les uns des autres) | MOYENNE | Analytics |
| GEO_013 | Synthèse de la couverture géographique du jeu de données | INFO | Analytics |
| GEO_014 | Couverture géographique du jeu de données trop étendue | INFO | Analytics |
| GEO_015 | Coordonnées d’arrêt hors des limites du Japon (feed_lang : ja) | MOYENNE | Quality |
| GEO_016 | Arrêt situé à proximité de Null Island (\|lat\|<0,1 et \|lon\|<0,1) | ÉLEVÉE | Quality |
| GEO_017 | Point de tracé situé à proximité de Null Island | ÉLEVÉE | Quality |
| GEO_018 | Tous les arrêts du jeu de données dans un rayon de 200 m (données de test probables) | ÉLEVÉE | Analytics |
| GEO_019 | L’arrêt a des coordonnées entières (précision nulle) | MOYENNE | Quality |
| GEO_020 | Tracé dégénéré — tous les points au même endroit | ÉLEVÉE | Quality |
| GEO_021 | Plus de 30 % des arrêts partagent des coordonnées (problème systématique) | ÉLEVÉE | Analytics |
| GEO_022 | Latitude d’arrêt proche d’un pôle (\|lat\| > 89) | ÉLEVÉE | Quality |

## DQ — Qualité des données / expérience utilisateur

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| DQ_003 | Description de ligne manquante | INFO | Quality |
| DQ_004 | URL de ligne manquante | INFO | Quality |
| DQ_005 | Aucune période de service valide | ÉLEVÉE | Quality |
| DQ_005b | Aucune course n’a d’horaires d’arrêt | ÉLEVÉE | Quality |
| DQ_005c | Forte proportion d’arrêts sans coordonnées | ÉLEVÉE | Quality |
| DQ_006 | Forte proportion de courses sans tracé | ÉLEVÉE | Quality |
| DQ_009 | Aucun horaire d’arrêt dans les courses | INFO | Quality |
| DQ_010 | Agence utilisée par aucune ligne | INFO | Quality |
| DQ_011 | Un seul arrêt existe | FAIBLE | Quality |
| DQ_012 | Trop d’agences, agency_id non utilisé | FAIBLE | Quality |
| DQ_013 | Trop peu de courses | INFO | Analytics |
| DQ_016 | Espaces superflus dans la valeur d’un champ | MOYENNE | Quality |
| DQ_017 | Valeur de coordonnée suspecte | INFO | Quality |
| DQ_018 | Valeur tout en majuscules dans un champ recommandé | MOYENNE | Quality |
| DQ_019 | Valeur tout en minuscules dans un champ recommandé | MOYENNE | Quality |
| DQ_020 | Champ recommandé manquant ou vide | FAIBLE | Quality |
| DQ_021 | Clé primaire en double (duplicate_key) | ÉLEVÉE | Spec |
| DQ_022 | Plus de 80 % des arrêts partagent le même stop_name | ÉLEVÉE | Quality |

## VAT — Détection analytique d’entités

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| VAT_001 | Similarité de tracé entre lignes (doublon probable) | MOYENNE | Analytics |
| VAT_002 | Pôle de correspondance non défini — de nombreuses lignes y passent mais aucune correspondance n’est définie | INFO | Analytics |
| VAT_003 | Durée de course statistiquement aberrante | FAIBLE | Analytics |
| VAT_005 | Grappe d’arrêts isolée — arrêts déconnectés de la composante principale du réseau | MOYENNE | Analytics |
| VAT_006 | Déséquilibre de densité de service — une seule ligne représente une large part des courses du jeu de données | INFO | Analytics |
| VAT_007 | Correspondance au terminus manquante — une autre ligne dessert le terminus mais aucune correspondance n’est définie | INFO | Analytics |
| VAT_008 | Un même tracé est utilisé par plus de 30 % des lignes | INFO | Analytics |

## JPN

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| JPN_001 | GTFS-JP : lecture kana (ja-Hrkt) manquante pour le nom d’arrêt | MOYENNE | Quality |
| JPN_002 | GTFS-JP : jp_office_id non défini dans office_jp.txt | ÉLEVÉE | Interop |
| JPN_003 | GTFS-JP : agency_id de agency_jp non défini dans agency.txt | ÉLEVÉE | Interop |
| JPN_004 | GTFS-JP : translations.txt manquant | ÉLEVÉE | Interop |
| JPN_005 | GTFS-JP : office_name vide dans office_jp | ÉLEVÉE | Interop |
| JPN_006 | GTFS-JP : fichiers tarifaires manquants | MOYENNE | Quality |
| JPN_007 | GTFS-JP : feed_info.txt manquant | MOYENNE | Quality |
| JPN_008 | GTFS-JP : lecture kana manquante pour route_long_name | MOYENNE | Quality |
| JPN_009 | GTFS-JP : lecture kana manquante pour trip_headsign | MOYENNE | Quality |
| JPN_010 | GTFS-JP : lecture kana manquante pour agency_name | MOYENNE | Quality |
| JPN_011 | GTFS-JP : agency_id obligatoire même avec une seule agence | ÉLEVÉE | Interop |
| JPN_012 | GTFS-JP : agency_id manquant dans agency_jp | ÉLEVÉE | Interop |
| JPN_013 | GTFS-JP : format de agency_zip_number invalide | MOYENNE | Quality |
| JPN_014 | GTFS-JP : office_id manquant ou en double dans office_jp | ÉLEVÉE | Interop |
| JPN_015 | GTFS-JP hérité : route_id invalide dans routes_jp | ÉLEVÉE | Interop |
| JPN_016 | GTFS-JP : route_update_date invalide dans pattern_jp ou routes_jp hérité | MOYENNE | Quality |
| JPN_017 | GTFS-JP : jp_pattern_id manquant ou en double | ÉLEVÉE | Interop |
| JPN_018 | GTFS-JP : jp_pattern_id non défini | ÉLEVÉE | Interop |
| JPN_019 | GTFS-JP : référence de traduction kana invalide | MOYENNE | Interop |
| JPN_020 | GTFS-JP : format de contact du bureau suspect | MOYENNE | Quality |
| JPN_021 | GTFS-JP : traduction kana incohérente | MOYENNE | Quality |
| JPN_022 | GTFS-JP v4 : champ principal obligatoire manquant | MOYENNE | Interop |
| JPN_023 | GTFS-JP : feed_lang n’est pas ja | ÉLEVÉE | Interop |
| JPN_024 | GTFS-JP : agency_lang n’est pas ja | ÉLEVÉE | Interop |
| JPN_025 | GTFS-JP : agency_timezone n’est pas Asia/Tokyo | ÉLEVÉE | Interop |
| JPN_026 | GTFS-JP : la devise tarifaire n’est pas JPY | ÉLEVÉE | Interop |
| JPN_027 | GTFS-JP V3 : route_type différent de 3 | ÉLEVÉE | Interop |
| JPN_028 | GTFS-JP v3 : traduction kana obligatoire manquante | MOYENNE | Quality |
| JPN_029 | GTFS-JP v4 : traduction kana recommandée manquante | FAIBLE | Quality |
| JPN_030 | GTFS-JP v3 : traduction japonaise obligatoire manquante | MOYENNE | Quality |
| JPN_031 | GTFS-JP : zone_id absent à un arrêt desservi par une tarification zonale | ÉLEVÉE | Interop |
| JPN_032 | GTFS-JP V3 : agency_id n’a pas le format du numéro d’entreprise | MOYENNE | Interop |
| JPN_033 | GTFS-JP : espace de noms jp réservé utilisé par un fichier ou champ personnalisé | MOYENNE | Interop |
