## Inspiration: 
Having volunteered at the local pediatric urgent care, I have seen the results of an inefficient scheduling plan. As such, we are working on a project to rectify this discrepancy.

## What it does: 
We have created a web application that takes volunteer availability from a google form and establishes a google calendar with filled shifts. 

## How I built it: 
We have made a google form for volunteers to input their availability.  This data automatically goes into a google sheet.  We used the Google Sheets API to pull down this data and use it to create appointments for each facility that would like to have volunteers.  This list is optimized based on facility requirements such as prioritizing shifts on the weekends vs weekdays, preferring one volunteer in every time slot before taking on a second volunteer at any time, and to ensure that as many people as possible who volunteered get at least one appointment per week.

## Challenges I ran into: 
We decided to split the execution into the sub-tasks of requesting the data from the Google Sheets API, pre-processing the data, optimizing the schedule, and publishing the data out to Google Calendar so that we could work on all modules concurrently.  There were some challenges in defining the data structure that would need to be published by one stage and ingested by the following stage.  We worked this out by beginning at the Google Endpoints of what data the volunteers submit to the google form and what data google calendar needs to generate the necessary events.  From here, we worked out what data would need to be processed, generated, and provided to teach stage of the pipeline.

## Accomplishments that I'm proud of: 
I am a Biomedical Sciences major with no background in Computer Science and in the past 24 hours, working with a team of three coders, we have been able to make immense progress on an issue that has loomed over the urgent care I work at. 

## What I learned: 


## What's next for Bypass Scheduling: 
Add an option to schedule more than one volunteer for facilities that want multiple volunteers at any given time block, optimize for the amount of shifts that each volunteer wants, and hand over control of the google platform and code to the Urgent Care centers that will be using this application.

