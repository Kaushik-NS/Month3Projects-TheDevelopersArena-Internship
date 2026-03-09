\# Pipeline Design



The system follows a standard ETL (Extract, Transform, Load) design.



\## Extract

Weather data is fetched from the OpenWeather API for a list of configured cities.



\## Transform

The data is validated and formatted to ensure:



\- Valid temperature values

\- Correct humidity ranges

\- Valid pressure values



Invalid records are skipped.



\## Load

Validated data is stored in the SQLite database.



Tables used:



\- cities

\- weather\_data

\- pipeline\_runs

\- pipeline\_logs



\## Scheduling



The scheduler runs the ETL pipeline at regular intervals using the schedule library.



Example schedule:



every 1 minute → fetch new weather data.

