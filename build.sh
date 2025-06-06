#!/usr/bin/env bash
# Exit on error
set -o errexit

# Mostrar cada comando ejecutado
set -x

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Apply any outstanding database migrations
python manage.py migrate

# Convert static asset files
python manage.py collectstatic --no-input