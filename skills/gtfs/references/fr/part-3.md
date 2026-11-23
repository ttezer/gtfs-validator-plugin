## SHP — Tracés

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| SHP_001 | shape_id manquant | CRITIQUE | Spec |
| SHP_002 | shape_pt_lat manquant ou invalide | CRITIQUE | Spec |
| SHP_003 | shape_pt_lon manquant ou invalide | CRITIQUE | Spec |
| SHP_004 | shape_pt_sequence manquant ou invalide | CRITIQUE | Spec |
| SHP_005 | shape_dist_traveled diminue | CRITIQUE | Spec |
| SHP_006 | Le tracé ne comporte qu’un seul point | FAIBLE | Quality |
| SHP_008 | shape_pt_sequence en double | CRITIQUE | Spec |
| SHP_009 | Le tracé s’auto-intersecte | INFO | Analytics |
| SHP_010 | Point de tracé répété (coordonnées identiques consécutives) | FAIBLE | Quality |
| SHP_012 | Tracé trop éloigné des arrêts de la course | ÉLEVÉE | Analytics |
| SHP_014 | Premier ou dernier arrêt éloigné de l’extrémité du tracé | INFO | Analytics |
| SHP_015 | Le tracé comporte statistiquement trop peu de points | MOYENNE | Quality |
| SHP_016 | Sens du tracé incohérent avec le sens de la course | ÉLEVÉE | Quality |
| SHP_017 | La séquence d’arrêts est en conflit avec le tracé | INFO | Analytics |
| SHP_018 | Tracé référencé par aucune course | FAIBLE | Quality |
| SHP_019 | Les courses de ce tracé n’ont aucun horaire d’arrêt | MOYENNE | Quality |
| SHP_020 | Point répété dans le tracé | INFO | Analytics |
| SHP_021 | shape_dist_traveled négatif ou non numérique | FAIBLE | Spec |
| SHP_022 | Position de l’arrêt ambiguë sur le tracé | ÉLEVÉE | Quality |
| SHP_023 | Points consécutifs de même shape_dist_traveled aux mêmes coordonnées | MOYENNE | Quality |
| SHP_024 | Distance arrêt–tracé incohérente avec shape_dist_traveled | MOYENNE | Quality |
| SHP_025 | La distance des stop_times de la course dépasse la distance totale du tracé | MOYENNE | Quality |
| SHP_026 | Le tracé a un nombre de points extrême (>5 000) | INFO | Analytics |
| SHP_028 | Même shape_dist_traveled avec des coordonnées différentes | ÉLEVÉE | Spec |
| SHP_029 | Même shape_dist_traveled, écart de coordonnées infime | INFO | Quality |
| SHP_030 | stop_times utilise shape_dist_traveled mais les distances du tracé sont absentes | MOYENNE | Quality |

## FRQ — Fréquences

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| FRQ_001 | trip_id introuvable | CRITIQUE | Spec |
| FRQ_002 | start_time invalide | CRITIQUE | Spec |
| FRQ_003 | end_time invalide | CRITIQUE | Spec |
| FRQ_004 | headway_secs manquant ou invalide | CRITIQUE | Spec |
| FRQ_005 | end_time antérieure à start_time | CRITIQUE | Quality |
| FRQ_006 | headway_secs trop long | MOYENNE | Analytics |
| FRQ_007 | exact_times invalide | MOYENNE | Spec |
| FRQ_008 | headway_secs nul (fréquence invalide) | CRITIQUE | Spec |
| FRQ_009 | Intervalle de fréquence trop court | MOYENNE | Quality |
| FRQ_010 | Fréquence très élevée (risque d’effet accordéon) | INFO | Analytics |
| FRQ_011 | Périodes de fréquence qui se chevauchent | ÉLEVÉE | Spec |
| FRQ_012 | exact_times=1 avec end_time sur une limite d’intervalle | FAIBLE | Spec |

## TRF — Correspondances

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| TRF_001 | from_stop_id manquant | CRITIQUE | Spec |
| TRF_002 | to_stop_id manquant | CRITIQUE | Spec |
| TRF_003 | from_stop_id ou to_stop_id introuvable | CRITIQUE | Spec |
| TRF_004 | transfer_type invalide | ÉLEVÉE | Spec |
| TRF_005 | min_transfer_time manquant | CRITIQUE | Spec |
| TRF_006 | from_trip_id introuvable | CRITIQUE | Spec |
| TRF_007 | to_trip_id introuvable | CRITIQUE | Spec |
| TRF_008 | from_route_id introuvable | CRITIQUE | Spec |
| TRF_009 | to_route_id introuvable | CRITIQUE | Spec |
| TRF_010 | Temps de correspondance trop long | MOYENNE | Analytics |
| TRF_011 | Correspondance définie mais distance importante | INFO | Quality |
| TRF_012 | Enregistrement de correspondance en double | CRITIQUE | Spec |
| TRF_013 | Type de correspondance incohérent avec le contexte | CRITIQUE | Quality |
| TRF_014 | Aucune course pour une correspondance sans changement de véhicule | ÉLEVÉE | Spec |
| TRF_015 | Correspondance sans changement de véhicule invalide | ÉLEVÉE | Quality |
| TRF_016 | Conditions de correspondance contradictoires | CRITIQUE | Spec |
| TRF_017 | Correspondance de course sur la mauvaise ligne | ÉLEVÉE | Spec |
| TRF_018 | La correspondance de course référence la même course | MOYENNE | Quality |
| TRF_019 | route_type différent dans une correspondance sans changement de véhicule | MOYENNE | Interop |
| TRF_020 | Vitesse de marche trop élevée pour la correspondance | MOYENNE | Quality |
| TRF_021 | L’extrémité de la correspondance n’est ni un arrêt ni une station | CRITIQUE | Spec |
| TRF_022 | Calendriers contradictoires dans une continuation de course 1 vers n | ÉLEVÉE | Spec |
| TRF_023 | Calendriers contradictoires dans une continuation de course n vers 1 | ÉLEVÉE | Spec |

## GGL — Compatibilité Google Transit

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| GGL_001 | transfer_type=4/5 non pris en charge par Google Transit | FAIBLE | Interop |
| GGL_002 | Valeur ic_price invalide (spécifique à Google) | FAIBLE | Interop |

## FAR — Attributs tarifaires

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| FAR_001 | fare_id en double | CRITIQUE | Spec |
| FAR_002 | price manquant ou invalide | CRITIQUE | Spec |
| FAR_003 | currency_type manquant | CRITIQUE | Spec |
| FAR_004 | payment_method invalide | CRITIQUE | Spec |
| FAR_005 | transfers invalide | CRITIQUE | Spec |
| FAR_006 | transfer_duration invalide | MOYENNE | Spec |
| FAR_008 | agency_id introuvable | CRITIQUE | Spec |
| FAR_010 | Règles tarifaires qui se chevauchent | MOYENNE | Quality |
| FAR_011 | payment_method manquant | CRITIQUE | Spec |
| FAR_013 | price ne respecte pas le nombre de décimales ISO 4217 de la devise | INFO | Quality |
| FAR_012 | fare_id manquant | CRITIQUE | Spec |

## FRL — Règles tarifaires

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| FRL_001 | fare_id introuvable | CRITIQUE | Spec |
| FRL_002 | route_id introuvable | CRITIQUE | Spec |
| FRL_003 | origin_id invalide | CRITIQUE | Spec |
| FRL_004 | destination_id invalide | CRITIQUE | Spec |
| FRL_005 | contains_id invalide | CRITIQUE | Spec |
| FRL_006 | Aucune règle tarifaire définie | INFO | Quality |
| FRL_007 | Incohérence logique dans une règle tarifaire | MOYENNE | Quality |
| FRL_008 | Aucun tarif défini pour l’ensemble des lignes | INFO | Quality |
| FRL_009 | Couverture tarifaire origine/destination incomplète | MOYENNE | Quality |

## RCT — Catégories de voyageurs (Tarifs v2)

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| RCT_001 | rider_category_id en double | CRITIQUE | Spec |
| RCT_002 | rider_category_name manquant | CRITIQUE | Spec |
| RCT_003 | is_default_fare_category invalide | CRITIQUE | Spec |
| RCT_004 | min_age ou max_age invalide (champ d’extension GTFS — absent de la spécification officielle) | MOYENNE | Quality |
| RCT_005 | max_age inférieur à min_age | MOYENNE | Quality |
| RCT_006 | fare_product n’a pas exactement une catégorie de voyageur par défaut | MOYENNE | Spec |
| RCT_007 | eligibility_url invalide | FAIBLE | Spec |
| RCT_008 | rider_category_id vide | CRITIQUE | Spec |

## FMD — Supports tarifaires (Tarifs v2)

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| FMD_001 | fare_media_id en double | CRITIQUE | Spec |
| FMD_002 | fare_media_type manquant ou invalide | CRITIQUE | Spec |
| FMD_003 | fare_media_name recommandé pour TransitCard/MobileApp | FAIBLE | Quality |
| FMD_004 | fare_media_id vide | CRITIQUE | Spec |

## FPD — Produits tarifaires (Tarifs v2)

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| FPD_001 | Clé composite fare_products en double | CRITIQUE | Spec |
| FPD_002 | amount manquant ou non numérique | CRITIQUE | Spec |
| FPD_003 | currency n’est pas un code ISO 4217 valide | CRITIQUE | Spec |
| FPD_004 | fare_media_id introuvable | CRITIQUE | Spec |
| FPD_005 | rider_category_id introuvable | CRITIQUE | Spec |
| FPD_007 | amount ne respecte pas le nombre de décimales ISO 4217 de la devise | FAIBLE | Spec |

## FLG — Règles de trajet tarifaire (Tarifs v2)

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| FLG_001 | fare_product_id introuvable | CRITIQUE | Spec |
| FLG_002 | network_id introuvable | CRITIQUE | Spec |
| FLG_003 | from_area_id introuvable | CRITIQUE | Spec |
| FLG_004 | to_area_id introuvable | CRITIQUE | Spec |
| FLG_005 | from_timeframe_group_id introuvable | CRITIQUE | Spec |
| FLG_006 | to_timeframe_group_id introuvable | CRITIQUE | Spec |
| FLG_007 | rule_priority invalide | MOYENNE | Spec |
| FLG_008 | fare_product_id manquant | CRITIQUE | Spec |

## FLJ

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| FLJ_001 | from_network_id manquant ou introuvable | CRITIQUE | Spec |
| FLJ_002 | to_network_id manquant ou introuvable | CRITIQUE | Spec |
| FLJ_003 | from_stop_id manquant ou introuvable | CRITIQUE | Spec |
| FLJ_004 | to_stop_id manquant ou introuvable | CRITIQUE | Spec |

## FTR — Règles de correspondance tarifaire (Tarifs v2)

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| FTR_001 | fare_transfer_type manquant ou invalide | CRITIQUE | Spec |
| FTR_002 | from_leg_group_id introuvable | CRITIQUE | Spec |
| FTR_003 | to_leg_group_id introuvable | CRITIQUE | Spec |
| FTR_004 | fare_product_id introuvable | CRITIQUE | Spec |
| FTR_005 | duration_limit_type invalide | CRITIQUE | Spec |
| FTR_006 | duration_limit invalide | MOYENNE | Spec |
| FTR_007 | duration_limit_type défini sans duration_limit | MOYENNE | Spec |
| FTR_008 | transfer_count invalide | MOYENNE | Spec |
| FTR_009 | transfer_count obligatoire lorsque les groupes de trajets sont identiques | MOYENNE | Spec |
| FTR_010 | transfer_count interdit lorsque les groupes de trajets diffèrent | MOYENNE | Spec |
| FTR_011 | duration_limit défini mais duration_limit_type manquant | MOYENNE | Spec |

## ARS — Zones (Tarifs v2)

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| ARS_001 | area_id en double | CRITIQUE | Spec |
| ARS_002 | areas.txt contient un area_id vide | CRITIQUE | Spec |

## SAR — Zones d’arrêt (Tarifs v2)

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| SAR_001 | area_id introuvable | CRITIQUE | Spec |
| SAR_002 | stop_id introuvable | CRITIQUE | Spec |
| SAR_003 | stop_areas contient un area_id vide | CRITIQUE | Spec |
| SAR_004 | stop_areas contient un stop_id vide | CRITIQUE | Spec |

## NET — Réseaux (Tarifs v2)

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| NET_001 | network_id en double | CRITIQUE | Spec |
| NET_002 | route_networks.network_id manquant ou introuvable | CRITIQUE | Spec |
| NET_003 | route_networks.route_id manquant ou introuvable | CRITIQUE | Spec |
| NET_004 | networks.txt contient un network_id vide | CRITIQUE | Spec |

## TFR — Plages horaires (Tarifs v2)

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| TFR_001 | timeframe_group_id manquant | CRITIQUE | Spec |
| TFR_002 | service_id introuvable | CRITIQUE | Spec |
| TFR_003 | Erreur de format sur start_time ou end_time | ÉLEVÉE | Spec |
| TFR_004 | end_time inférieure à start_time | MOYENNE | Quality |
| TFR_005 | Plages horaires qui se chevauchent au sein d’un même groupe et service_id | MOYENNE | Spec |
| TFR_006 | start_time ou end_time supérieure à 24:00:00 | CRITIQUE | Spec |
| TFR_007 | Une seule des valeurs start_time et end_time est renseignée | CRITIQUE | Spec |
| TFR_008 | timeframes contient un service_id vide | CRITIQUE | Spec |
