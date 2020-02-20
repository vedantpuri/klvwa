# Weather App (Klaviyo)

## Requirements
- Python >= 3.6
- requests
- beautifulsoup >= 4
- lxml

## Credentials
```
Username: kvadmin
Email: vedantpuri13@gmail.com
PW: kvweatherapp
```

## Steps to Run
- pip install requirements
- Create and Load fixture
- Store necessary env variables (SCRIPT TO DO THAT)
- migrations
- runserver
- Run mailer

## Assumptions
- email validity
- api is correct
- api always returns given a correctly formatted location (had to assume because cant form body of email other wise)


## Scalability
- Caching weather API calls (O(100))
- Checks email validity before sending (no unneseccary queries)


## Security
- SMTP SSL reason
- no cookies(no pass)
- csrf token Django

## Design Choices
- Linking Models with Foreign Key. FIRSTLY VERY RARE THAT population list will change, only ones at bottom, secondly want to keep customers that we already have with their weather. ON delete Protect because want customer to stay UNLESS unsubscribe (because population change). Even in the worst case 350 cities. Send email that location has been removed (don’t think that is good from a customer perspective)

- Weather API code(sunny 800 etc) design choices: because want to cover wide range

- Environment variables(Repeated)

## Sources
- Abbreviations of states http://worldpopulationreview.com/states/state-abbreviations/
