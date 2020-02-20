# Weather App (Klaviyo)

## Requirements
- Python >= 3.6
- requests
- beautifulsoup >= 4
- lxml

## Admin Credentials
If you would like to inspect deeper under the hood, I have provided with the admin credentials of the website
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
During this project I made some small assumptions, which I thought I would mention. Due to heavy semester load it was hard for me to implement/check some of these.
- Email Existence: For the purposes of this assignment I assumed that the emails being enter will exist. Ofcourse, while filling the form, there is a Django regex check to validate format, but currently there is no check for whether the email is actually a real one or not.
- weatherbit.io returns weather correctly
- The requests to weatherbit.io never fail. Ideally, there should be a check for this but due to the free subscription there is a cap on the number of calls I can make (so I cannot poll till I succeed) and the assignment asks us to set the content of the body of the email with the weather and description of the location, which is a hard field to have a default value and wouldn't suit the app.
wise)


## Scalability
- Caching weather API calls (O(100))
- No recomputation of what kind to email to send, going by locations and storing the email

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
