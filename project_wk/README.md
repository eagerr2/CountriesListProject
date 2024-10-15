# Technical Challenge
---
# Overview
This project made using Django is a web application used to filter through countries using a case in-sensitive search bar. When a search term is inputted, the application checks the database for existing countries and displays the results. Each result includes the name of the country, its continent, and its population. If a country doesn't exist an error message is displayed instead. New countries can be added via the Django admin interface.
# Technology used
Python, Django, Bootstrap

## Data Initialisation

After forking this repository, if the data is not populated, you will need to load the country data from the `countries.json` file to ensure the application functions properly. This file contains the data related to country names, continents, and populations.

To load the data, depending on your environment, you can use one of the following commands within the root directory of the project to load the data and populate the database: 
python manage.py loaddata countries.json or python3 manage.py loaddata countries.json.
