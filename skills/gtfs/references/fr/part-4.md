## PTH — Cheminements

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| PTH_001 | pathway_id en double | CRITIQUE | Spec |
| PTH_002 | from_stop_id introuvable | CRITIQUE | Spec |
| PTH_003 | to_stop_id introuvable | CRITIQUE | Spec |
| PTH_004 | pathway_mode manquant ou invalide | CRITIQUE | Spec |
| PTH_005 | is_bidirectional manquant | CRITIQUE | Spec |
| PTH_006 | length invalide | MOYENNE | Spec |
| PTH_007 | traversal_time invalide | MOYENNE | Spec |
| PTH_008 | stair_count manquant | FAIBLE | Quality |
| PTH_009 | max_slope manquant | FAIBLE | Quality |
| PTH_010 | min_width invalide | FAIBLE | Spec |
| PTH_011 | Le cheminement forme une boucle | ÉLEVÉE | Quality |
| PTH_012 | Aucun cheminement accessible vers la station | ÉLEVÉE | Spec |
| PTH_013 | Analyse des cheminements accessibles | INFO | Analytics |
| PTH_014 | Le cheminement franchit la limite de la station | CRITIQUE | Quality |
| PTH_015 | Le cheminement mène à un arrêt inatteignable | MOYENNE | Analytics |
| PTH_016 | Sortie définie comme bidirectionnelle | ÉLEVÉE | Spec |
| PTH_017 | max_slope n’est pas un nombre | MOYENNE | Spec |
| PTH_018 | signposted_as trop long | FAIBLE | Quality |
| PTH_019 | Nœud générique relié à un seul cheminement (impasse) | MOYENNE | Quality |
| PTH_020 | pathway_id manquant | CRITIQUE | Spec |
| PTH_021 | from_stop_id manquant | CRITIQUE | Spec |
| PTH_022 | to_stop_id manquant | CRITIQUE | Spec |
| PTH_023 | pathway_mode manquant | CRITIQUE | Spec |
| PTH_024 | is_bidirectional manquant | CRITIQUE | Spec |
| PTH_025 | Longueur de cheminement recommandée manquante | FAIBLE | Quality |
| PTH_030 | Cheminement affecté à un quai qui possède des zones d’embarquement | FAIBLE | Spec |
| PTH_029 | traversal_time de cheminement recommandé manquant | FAIBLE | Quality |
| PTH_026 | L’extrémité du cheminement est une station | CRITIQUE | Spec |
| PTH_031 | L’extrémité du cheminement est un arrêt accessible depuis la rue (stop_access=1) | CRITIQUE | Spec |
| PTH_027 | stair_count invalide (nul ou non entier) | MOYENNE | Spec |
| PTH_028 | max_slope utilisé en dehors d’un cheminement piéton | FAIBLE | Quality |

## LVL — Niveaux

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| LVL_001 | level_id en double | CRITIQUE | Spec |
| LVL_002 | level_index invalide | CRITIQUE | Spec |
| LVL_003 | level_name manquant | FAIBLE | Quality |
| LVL_004 | Niveau inutilisé | FAIBLE | Quality |
| LVL_005 | level_name trop long | MOYENNE | Quality |
| LVL_006 | level_id manquant sur un arrêt relié par ascenseur | MOYENNE | Quality |
| LVL_007 | level_index manquant | CRITIQUE | Spec |
| LVL_008 | level_id manquant | CRITIQUE | Spec |

## FIN — Informations du jeu de données

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| FIN_001 | feed_publisher_name manquant | CRITIQUE | Spec |
| FIN_002 | feed_publisher_url manquant ou invalide | CRITIQUE | Spec |
| FIN_003 | feed_lang manquant | CRITIQUE | Spec |
| FIN_004 | default_lang invalide | MOYENNE | Spec |
| FIN_005 | feed_start_date invalide | MOYENNE | Spec |
| FIN_006 | feed_end_date invalide ou passée | ÉLEVÉE | Spec |
| FIN_007 | feed_version manquant | FAIBLE | Quality |
| FIN_008 | feed_contact_email invalide | FAIBLE | Spec |
| FIN_009 | feed_contact_url invalide | FAIBLE | Spec |
| FIN_010 | Validité du jeu de données expirée | ÉLEVÉE | Analytics |
| FIN_012 | feed_start_date postérieure à feed_end_date | FAIBLE | Spec |
| FIN_013 | fare_attributes.agency_id recommandé mais manquant | INFO | Quality |
| FIN_014 | Dates de validité du jeu de données (feed_start_date/feed_end_date) manquantes | FAIBLE | Quality |
| FIN_015 | Plusieurs enregistrements feed_info | MOYENNE | Quality |
| FIN_016 | feed_start_date dans le futur (jeu de données pas encore actif) | FAIBLE | Quality |
| FIN_017 | Le jeu de données expire dans un futur très lointain | INFO | Quality |
| FIN_018 | feed_contact_email et feed_contact_url tous deux manquants | FAIBLE | Quality |
| FIN_019 | La validité du jeu de données expire sous 7 jours | FAIBLE | Quality |
| FIN_020 | Fenêtre de validité du jeu de données inférieure à 7 jours | INFO | Quality |

## TRN — Traductions

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| TRN_001 | Valeur table_name invalide | CRITIQUE | Spec |
| TRN_002 | field_name invalide pour cette table | CRITIQUE | Spec |
| TRN_003 | language invalide | MOYENNE | Spec |
| TRN_004 | record_id introuvable | ÉLEVÉE | Spec |
| TRN_005 | Traduction en double | CRITIQUE | Spec |
| TRN_006 | Enregistrement de traduction contradictoire | CRITIQUE | Spec |
| TRN_007 | Traduction dans la même langue que feed_lang | FAIBLE | Quality |
| TRN_008 | La valeur de traduction est vide | CRITIQUE | Spec |
| TRN_009 | record_id et field_value ne peuvent pas être utilisés ensemble | ÉLEVÉE | Spec |
| TRN_010 | record_sub_id invalide | ÉLEVÉE | Spec |
| TRN_011 | field_name n’est pas traduisible | ÉLEVÉE | Spec |
| TRN_013 | Un champ d’identité ne peut pas être utilisé dans une traduction de feed_info | ÉLEVÉE | Spec |
| TRN_014 | record_sub_id valide uniquement pour stop_times | ÉLEVÉE | Spec |
| TRN_017 | Traduction de stop_times sans record_sub_id — l’enregistrement est ambigu | MOYENNE | Spec |
| TRN_015 | record_id et field_value sont tous deux vides | ÉLEVÉE | Spec |
| TRN_016 | field_value ne correspond à aucun enregistrement — la traduction n’est jamais appliquée | MOYENNE | Spec |

## LIC — Licences

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| LIC_001 | Licence manquante | CRITIQUE | Spec |
| LIC_002 | Deux licences indiquées | CRITIQUE | Spec |
| LIC_003 | Table sous licence inconnue | MOYENNE | Interop |
| LIC_004 | Table sous licence en double | CRITIQUE | Spec |
| LIC_005 | Table sous licence absente | INFO | Quality |
| LIC_006 | Licence du flux absente | INFO | Quality |
| LIC_007 | Identifiant SPDX absent de la liste | INFO | Quality |
| LIC_008 | Noms de table en conflit | CRITIQUE | Interop |
| LIC_009 | URL de licence invalide | CRITIQUE | Spec |

## ATR — Attributions

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| ATR_001 | attribution_id manquant | ÉLEVÉE | Quality |
| ATR_002 | organization_name manquant | CRITIQUE | Spec |
| ATR_003 | Rôle d’attribution non défini | ÉLEVÉE | Spec |
| ATR_004 | is_producer invalide | CRITIQUE | Spec |
| ATR_005 | is_operator invalide | CRITIQUE | Spec |
| ATR_006 | is_authority invalide | CRITIQUE | Spec |
| ATR_007 | attribution_url invalide | CRITIQUE | Spec |
| ATR_008 | attribution_email invalide | FAIBLE | Spec |
| ATR_009 | Plusieurs champs de référence d’attribution renseignés | ÉLEVÉE | Spec |
| ATR_010 | agency_id introuvable | FAIBLE | Spec |
| ATR_011 | route_id introuvable | FAIBLE | Spec |
| ATR_012 | trip_id introuvable | FAIBLE | Spec |

## XFL — Inter-fichiers / sémantique

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| XFL_002 | La course n’a aucun enregistrement stop_times | ÉLEVÉE | Interop |
| XFL_006 | service_id ne contient que des exceptions d’annulation (aucun jour actif) | MOYENNE | Analytics |
| XFL_012 | Ligne sans course exploitée | ÉLEVÉE | Quality |
| XFL_013 | shape_id utilisé dans plusieurs sens | ÉLEVÉE | Quality |
| XFL_014 | Référence de traduction invalide (enregistrement source introuvable) | MOYENNE | Quality |
| XFL_015 | Référence invalide dans une attribution | CRITIQUE | Spec |
| XFL_016 | La traduction référence feed_info mais feed_info.txt est absent | ÉLEVÉE | Spec |
| XFL_019 | Réseau défini dans deux fichiers distincts (routes.network_id + networks.txt ou route_networks.txt) | MOYENNE | Spec |
| XFL_020 | Couple (from_trip_id/to_trip_id, route_id) invalide dans transfers | CRITIQUE | Spec |
| XFL_021 | Couple (from_trip_id/to_trip_id, stop_id) invalide dans transfers | ÉLEVÉE | Interop |
| XFL_022 | location_group_id introuvable | CRITIQUE | Spec |
| XFL_023 | stop_id introuvable (location_group_stops) | CRITIQUE | Spec |
| XFL_024 | location_group_id introuvable (stop_times) | CRITIQUE | Spec |
| XFL_025 | location_id introuvable (locations.geojson) | CRITIQUE | Spec |
| XFL_031 | Collision d’identifiants : stop_id, id de locations.geojson et location_group_id partagent un même espace de noms | CRITIQUE | Spec |
| XFL_032 | location_groups.txt contient un location_group_id vide | CRITIQUE | Spec |
| XFL_033 | location_group_stops contient un location_group_id vide | CRITIQUE | Spec |
| XFL_034 | location_group_stops contient un stop_id vide | CRITIQUE | Spec |
| XFL_027 | Ligne avec cemv=2 mais produit sans contact applicable | INFO | Interop |
| XFL_028 | Agence avec cemv=1 mais aucun support sans contact | INFO | Quality |
| XFL_029 | Ligne avec cemv=1 mais aucun support sans contact | INFO | Quality |
| XFL_030 | Support sans contact présent mais aucun cemv=1 | INFO | Quality |

## OPR — Cohérence d’exploitation

| Règle | Titre | Gravité | Classe |
|---|---|---|---|
| OPR_001 | Intervalle de passage trop long sur la ligne | MOYENNE | Analytics |
| OPR_003 | Effet accordéon (intervalle minimal trop faible) | FAIBLE | Analytics |
| OPR_004 | Aucun service le week-end | INFO | Analytics |
| OPR_005 | Fréquence de service inhabituelle | INFO | Analytics |
| OPR_006 | La course compte trop peu d’arrêts (non fonctionnelle) | ÉLEVÉE | Analytics |
| OPR_007 | Séquence d’arrêts répétée au sein d’une course | INFO | Analytics |
| OPR_008 | Vitesse excessive sur plusieurs segments | INFO | Analytics |
| OPR_009 | Heure de départ de la course de nuit trop tardive | INFO | Analytics |
| OPR_010 | Conflits de politique d’accessibilité ou de transport des vélos sur la ligne | MOYENNE | Analytics |
| OPR_011 | Le service n’a aucun jour actif | ÉLEVÉE | Analytics |
| OPR_012 | Interruption de service | MOYENNE | Analytics |
| OPR_013 | La ligne n’est exploitée que dans un seul sens (pas de sens retour) | INFO | Analytics |
| OPR_014 | Temps de correspondance moyen trop long | MOYENNE | Analytics |
| OPR_015 | La ligne n’est exploitée qu’avec un seul tracé | INFO | Analytics |
| OPR_016 | Aucun service actif sur l’ensemble du jeu de données | INFO | Analytics |
| OPR_017 | Distance de course trop courte | MOYENNE | Analytics |
| OPR_019 | Chevauchement de calendriers sur la ligne (plusieurs services le même jour) | INFO | Analytics |
| OPR_020 | Chevauchement de jours d’exception sur la ligne | FAIBLE | Analytics |
| OPR_021 | Conflit de remplacement de calendrier : le remplacement et le service de base sont actifs simultanément | ÉLEVÉE | Analytics |
| OPR_022 | Remplacement de calendrier non appliqué : le service de base circule le jour du remplacement | ÉLEVÉE | Analytics |
| OPR_023 | Vide de remplacement de calendrier : aucun service actif dans la fenêtre | MOYENNE | Analytics |
| OPR_024 | La ligne a un nombre de courses extrême | INFO | Analytics |
| OPR_025 | Durée moyenne des courses du jeu de données inférieure à 60 secondes | ÉLEVÉE | Analytics |
