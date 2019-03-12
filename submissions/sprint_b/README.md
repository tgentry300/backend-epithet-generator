# Epithet Generator
- This API was created using Shakesperian language to throw insults in JSON format back at the requester.

### API

Endpoint: `/`

-This endpoint will return 1 single epithet

Endpoint: `/vocabulary`

-This endpoint will return JSON object containing the vocabulary used to create the Insult.

Endpoint: `/epithets/<quantity>`

-This endpoint will return JSON object containing the amount of epithets as specified in the URL.

#### Developers

This program was built and tested using pytest and Flask-Testing packages.  To appropriately run these tests, be sure you are in the proper directory (sprint_b) and run `pytest` in the command line.  Happy Insulting!