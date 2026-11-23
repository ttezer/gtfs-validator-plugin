## TRP — Courses

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| TRP_001 | trip_id manquant ou en double | CRITIQUE | Spec |
| TRP_002 | route_id introuvable | CRITIQUE | Spec |
| TRP_003 | service_id introuvable | CRITIQUE | Spec |
| TRP_004 | shape_id introuvable | ÉLEVÉE | Spec |
| TRP_005 | direction_id invalide | MOYENNE | Spec |
| TRP_006 | wheelchair_accessible invalide | FAIBLE | Spec |
| TRP_007 | bikes_allowed invalide | FAIBLE | Spec |
| TRP_032 | cars_allowed invalide | FAIBLE | Spec |
| TRP_011 | Girouette de course non renseignée | ÉLEVÉE | Quality |
| TRP_012 | direction_id manquant sur une ligne bidirectionnelle | FAIBLE | Quality |
| TRP_013 | La ligne ne comporte qu’une seule course | INFO | Analytics |
| TRP_014 | trip_short_name trop long | INFO | Quality |
| TRP_015 | block_id ne regroupe aucune course | FAIBLE | Quality |
| TRP_017 | Course basée sur la fréquence absente de stop_times | MOYENNE | Quality |
| TRP_019 | shape_id manquant alors que le service continu est actif | ÉLEVÉE | Spec |
| TRP_020 | trip_headsign correspond au nom d’un arrêt intermédiaire | INFO | Analytics |
| TRP_021 | Transport des vélos (bikes_allowed) non précisé | INFO | Quality |
| TRP_022 | Chevauchement des horaires de courses au sein d’un enchaînement | ÉLEVÉE | Interop |
| TRP_023 | Aucune course active dans les 7 prochains jours | FAIBLE | Quality |
| TRP_024 | Type de ligne incohérent au sein de l’enchaînement | FAIBLE | Quality |
| TRP_025 | Forte proportion de courses sans information d’accessibilité en fauteuil roulant | INFO | Quality |
| TRP_026 | Course dont l’ensemble des dates actives est vide | MOYENNE | Analytics |
| TRP_028 | Certaines courses n’indiquent pas l’accessibilité en fauteuil roulant | INFO | Quality |
| TRP_029 | Aucune course n’indique l’accessibilité en fauteuil roulant | INFO | Quality |
| TRP_031 | route_id manquant | CRITIQUE | Spec |
| TRP_034 | Le champ safe_duration n’est pas un nombre | MOYENNE | Spec |
| TRP_035 | trips.txt contient un service_id vide | CRITIQUE | Spec |

## STM — Horaires d’arrêt

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| STM_001 | trip_id introuvable | CRITIQUE | Spec |
| STM_002 | stop_id introuvable | CRITIQUE | Spec |
| STM_003 | Format de arrival_time invalide | CRITIQUE | Spec |
| STM_004 | Format de departure_time invalide | CRITIQUE | Spec |
| STM_005 | stop_sequence manquant ou invalide | CRITIQUE | Spec |
| STM_006 | stop_id manquant (stop_times) | CRITIQUE | Spec |
| STM_007 | Heure de départ antérieure à l’heure d’arrivée | ÉLEVÉE | Interop |
| STM_008 | L’heure diminue entre deux arrêts | CRITIQUE | Interop |
| STM_009 | pickup_type invalide | ÉLEVÉE | Spec |
| STM_010 | drop_off_type invalide | ÉLEVÉE | Spec |
| STM_012 | Vitesse irréaliste entre deux arrêts | ÉLEVÉE | Interop |
| STM_014 | Vitesse excessive sur un segment | ÉLEVÉE | Analytics |
| STM_015 | arrival_time manquant au premier arrêt | CRITIQUE | Spec |
| STM_016 | arrival_time manquant au dernier arrêt | CRITIQUE | Spec |
| STM_017 | Distance de tracé manquante dans les horaires d’arrêt | MOYENNE | Quality |
| STM_018 | continuous_pickup invalide (stop_times) | MOYENNE | Spec |
| STM_019 | continuous_drop_off invalide (stop_times) | MOYENNE | Spec |
| STM_020 | Temps de parcours nul (distance > 200 m) | ÉLEVÉE | Quality |
| STM_021 | Distance entre arrêts nulle ou négative | INFO | Analytics |
| STM_022 | timepoint invalide | MOYENNE | Spec |
| STM_024 | Incohérence d’unité pour shape_dist_traveled | INFO | Quality |
| STM_025 | Durée de segment très courte | INFO | Analytics |
| STM_026 | Distance excessive entre deux arrêts | INFO | Analytics |
| STM_028 | Durée de course trop longue | ÉLEVÉE | Analytics |
| STM_029 | Durée de course trop courte | MOYENNE | Analytics |
| STM_030 | shape_dist_traveled négatif ou non numérique | FAIBLE | Spec |
| STM_032 | stop_sequence en double au sein d’une course | FAIBLE | Spec |
| STM_033 | Course à un seul arrêt (inutilisable) | ÉLEVÉE | Interop |
| STM_034 | Une seule des heures d’arrivée ou de départ est définie | MOYENNE | Interop |
| STM_035 | Même arrêt desservi deux fois consécutivement (terminus ou boucle) | INFO | Analytics |
| STM_036 | stop_times non trié par trip_id + stop_sequence (unsorted_stop_times) | INFO | Quality |
| STM_037 | arrival_time/departure_time interdits dans une fenêtre Flex | ÉLEVÉE | Spec |
| STM_038 | start_pickup_drop_off_window >= end_pickup_drop_off_window | ÉLEVÉE | Interop |
| STM_039 | Fenêtre de prise en charge ou de dépose manquante en contexte Flex | CRITIQUE | Spec |
| STM_040 | pickup/drop_off_booking_rule_id manquant dans des stop_times Flex (Optionnel dans la spécification) | MOYENNE | Quality |
| STM_060 | Zone, fenêtre et prise en charge/dépose se chevauchent simultanément au sein d’une course | ÉLEVÉE | Spec |
| STM_061 | Vitesse impossible entre des arrêts éloignés non consécutifs | ÉLEVÉE | Interop |
| STM_059 | booking_rule_id recommandé lorsque pickup_type/drop_off_type=2 | FAIBLE | Quality |
| STM_041 | stop_id et location_id/group_id ne peuvent pas être utilisés ensemble | ÉLEVÉE | Spec |
| STM_042 | stop_headsign contient des caractères non pris en charge par Google Transit | FAIBLE | Interop |
| STM_043 | Course au nombre d’arrêts extrême (>200) | INFO | Analytics |
| STM_044 | Le fichier stop_times dépasse 2 000 000 d’enregistrements (avertissement de performance WASM) | INFO | Analytics |
| STM_045 | L’heure de départ de la course dépasse la fenêtre de la journée de service | INFO | Analytics |
| STM_046 | trip_id manquant | CRITIQUE | Spec |
| STM_047 | timepoint=1 sans heure d’arrivée ni de départ | CRITIQUE | Spec |
| STM_048 | Heures de journée de service après minuit écrites en 00:xx (spécification GTFS) | ÉLEVÉE | Spec |
| STM_049 | Départ après minuit écrit en 00:xx sur le même enregistrement (spécification GTFS) | ÉLEVÉE | Spec |
| STM_050 | Colonne timepoint présente mais valeur vide | FAIBLE | Quality |
| STM_051 | pickup_type 0/3 interdit avec une fenêtre Flex | ÉLEVÉE | Spec |
| STM_052 | drop_off_type 0 interdit avec une fenêtre Flex | ÉLEVÉE | Spec |
| STM_053 | De nombreux arrêts consécutifs ont la même heure | INFO | Analytics |
| STM_054 | continuous_pickup interdit avec une fenêtre Flex | ÉLEVÉE | Spec |
| STM_055 | continuous_drop_off interdit avec une fenêtre Flex | ÉLEVÉE | Spec |
| STM_056 | shape_dist_traveled n’augmente pas | CRITIQUE | Spec |
| STM_058 | Heure de fenêtre Flex de prise en charge ou de dépose invalide | CRITIQUE | Spec |

## PDW — Fenêtre de prise en charge/dépose

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| PDW_006 | Chevauchement de fenêtres de prise en charge/dépose pour un même couple course+zone | MOYENNE | Analytics |

## LOC — locations.geojson

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| LOC_001 | Type de géométrie inconnu ou invalide dans locations.geojson | ÉLEVÉE | Spec |
| LOC_012 | locations.geojson n’est pas une FeatureCollection GeoJSON valide | ÉLEVÉE | Spec |
| LOC_002 | L’objet Feature a une géométrie nulle ou absente | CRITIQUE | Spec |
| LOC_003 | L’objet Feature n’a pas la propriété obligatoire « id » | CRITIQUE | Spec |
| LOC_004 | L’anneau du polygone n’est pas fermé | MOYENNE | Spec |
| LOC_005 | La FeatureCollection ne contient aucun objet Feature | FAIBLE | Quality |
| LOC_006 | La superficie du polygone dépasse 500 km² | INFO | Quality |
| LOC_007 | Identifiant « id » d’objet Feature en double dans la FeatureCollection | MOYENNE | Spec |
| LOC_008 | Membre « type » absent ou différent de « Feature » | MOYENNE | Spec |
| LOC_009 | Objet « properties » manquant dans l’objet Feature | MOYENNE | Spec |
| LOC_011 | Polygone invalide : un anneau s’auto-intersecte ou un trou se situe à l’extérieur | ÉLEVÉE | Spec |
| LOC_010 | Le membre « coordinates » de la géométrie est absent ou n’est pas un tableau — la géométrie de la zone ne peut pas être résolue | CRITIQUE | Spec |

## CAL — Calendrier

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| CAL_001 | service_id en double | CRITIQUE | Spec |
| CAL_002 | Valeur invalide dans un champ de jour du calendrier | CRITIQUE | Spec |
| CAL_003 | start_date invalide | CRITIQUE | Spec |
| CAL_004 | end_date invalide | CRITIQUE | Spec |
| CAL_005 | start_date postérieure à end_date | CRITIQUE | Interop |
| CAL_006 | Tous les jours de la grille hebdomadaire sont désactivés | INFO | Quality |
| CAL_007 | Interruption dans la période de service | INFO | Analytics |
| CAL_008 | Le service expire prochainement | INFO | Analytics |
| CAL_009 | Tous les services du jeu de données ont expiré | INFO | Analytics |
| CAL_010 | Le service compte trop peu de jours actifs | MOYENNE | Analytics |
| CAL_011 | Service inutilisé | FAIBLE | Quality |
| CAL_012 | Interruption de service dans un futur proche | INFO | Analytics |
| CAL_013 | Période de service expirée | INFO | Analytics |
| CAL_014 | Dates de service hors de la plage de validité de feed_info | INFO | Interop |
| CAL_015 | Toutes les dates du calendrier sont futures (aucune course active aujourd’hui) | INFO | Analytics |
| CAL_016 | Le service s’étend jusqu’à une date très lointaine | INFO | Quality |
| CAL_017 | Le calendrier n’a pas encore commencé (toutes les dates actives sont futures) | INFO | Analytics |
| CAL_018 | Le service n’a aucun jour de semaine actif (tous les jours à 0, aucun remplacé par calendar_dates) | INFO | Quality |
| CAL_020 | La fenêtre de validité du jeu de données dépasse 5 ans | INFO | Quality |
| CAL_021 | Actif aujourd’hui mais aucun service dans les jours à venir | INFO | Analytics |
| CAL_022 | service_id manquant | CRITIQUE | Spec |
| CAL_023 | end_date du calendrier très lointaine (suspect) | MOYENNE | Quality |
| CAL_024 | Calendrier inactif dans les 7 prochains jours | INFO | Analytics |
| CAL_025 | Champ de jour du calendrier vide | CRITIQUE | Spec |

## CLD — Dates de calendrier

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| CLD_001 | service_id manquant | CRITIQUE | Spec |
| CLD_002 | Format de date invalide | CRITIQUE | Spec |
| CLD_003 | exception_type manquant ou invalide | CRITIQUE | Spec |
| CLD_004 | Un service défini uniquement par calendar_dates n’a aucune date active | ÉLEVÉE | Quality |
| CLD_005 | Date hors plage | INFO | Quality |
| CLD_006 | Trop de jours d’exception | INFO | Analytics |
| CLD_007 | Nombre excessif d’exceptions de calendrier | INFO | Analytics |
