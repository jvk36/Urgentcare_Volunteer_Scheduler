# Volunteer Scheduler
The aim of this project is to automate the scheduling process at a local urgent care. The current plan of action is for the coordinator to receive about 100 emails from the 100 volunteers signed up. The coordinator then sifts through these emails and makes a schedule on google sheets manually. While he gets plenty of credit for being able to do so for many months, it isn't the most accurate schedule nor is it the best use of time. Just taking into account - human error and physically being unable to remember 100 volunteers' worth of availability to optimize shift filled leaves us with a calendar that is ridden with errors or is not optimized to have most shifts filled. Our goal is to correct for this.

The urgent care has three locations and is open 12 hours every day. There are three shifts available for volunteers to sign up for. For each shift, there can be a maximum of 2 volunteers signed up. Most volunteers are high school or college students and their availability changes every week depending on their school and work schedule. There is also the fact that volunteers may be available for 15 shifts per week, but only want to volunteer for three shifts per week. As such, we are trying collect their availability and produce a schedule for a month that optimizes the number of shifts covered while providing volunteers with the desired number of shifts. Our final goal is to produce a google calendar listing the volunteers covering specific shifts and to set up a reminding system to alert volunteers of their commitment 2 days in advance. 


## CSV table properties
Each CSV file contains entries with the following properties in the exact order that is specified below.

#### schedule.csv
- name
- startTime
- endTime
- location
- email

#### locationMapping.csv
- location
- locationCalendar

