#!/bin/bash
set -euo pipefail
echo "meeting notes" > notes.txt
python3 -c "import zipfile; z = zipfile.ZipFile('docs.zip', 'w'); z.write('notes.txt'); z.close()"
rm notes.txt
