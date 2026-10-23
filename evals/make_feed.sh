#!/bin/bash
# Writes the demo GTFS feed as feed.zip in the current directory.
# Usage: make_feed.sh [file-to-leave-out]
set -euo pipefail
skip="${1:-}"
dir="$(mktemp -d)"
cat > "$dir/agency.txt" <<'EOF'
agency_id,agency_name,agency_url,agency_timezone
A1,Demo Transit,https://example.com,Europe/Istanbul
EOF
cat > "$dir/stops.txt" <<'EOF'
stop_id,stop_name,stop_lat,stop_lon
S1,Merkez,37.2150,28.3630
S2,Hastane,37.2200,28.3700
S3,Otogar,37.2250,28.3800
S4,Kopya Durak,37.2250,28.3800
EOF
cat > "$dir/routes.txt" <<'EOF'
route_id,agency_id,route_short_name,route_long_name,route_type
R1,A1,1,Merkez - Otogar,3
EOF
cat > "$dir/trips.txt" <<'EOF'
route_id,service_id,trip_id
R1,WK,T1
R1,WK,T2
EOF
cat > "$dir/stop_times.txt" <<'EOF'
trip_id,arrival_time,departure_time,stop_id,stop_sequence
T1,08:00:00,08:00:00,S1,1
T1,08:10:00,08:10:00,S2,2
T1,08:05:00,08:05:00,S3,3
T2,09:00:00,09:00:00,S1,1
T2,09:10:00,09:10:00,S2,2
T2,09:20:00,09:20:00,S3,3
EOF
cat > "$dir/calendar.txt" <<'EOF'
service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date
WK,1,1,1,1,1,0,0,20261001,20261231
EOF
[ -n "$skip" ] && rm "$dir/$skip"
out="$PWD/feed.zip"
(cd "$dir" && python3 -c "import sys, zipfile, glob; z = zipfile.ZipFile(sys.argv[1], 'w'); [z.write(f) for f in sorted(glob.glob('*.txt'))]; z.close()" "$out")
rm -r "$dir"
