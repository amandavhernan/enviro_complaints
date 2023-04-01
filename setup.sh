rm -f enviro_complaints.db
# install sqlite, datasette, datasette-vega
pip install sqlite-utils datasette datasette-vega
# install plugins for codespaces and full-text search
datasette install datasette-codespaces datasette-configure-fts
# add data, build db
sqlite-utils insert enviro_complaints.db complaints "complaints_data.csv" --csv
# enable full-text search for county
sqlite-utils enable-fts enviro_complaints.db county
# turn on db
datasette serve enviro_complaints.db