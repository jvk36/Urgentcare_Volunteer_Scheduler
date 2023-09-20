# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 20:14:26 2022

@author: UBHacking2022
"""

from process_csv import build_user_from_row, look_at_cols_for_loc_for_user
import pandas as pd
import pprint

#this is a variable that was intended to be used so we can change the num_days later
#but right now the num of days is pretty hardcoded, I dont think we can change it
num_of_jan_days = 31

#this is the csv from the file we read in
df = pd.read_csv("output.csv")
df = df.fillna("0")


#im just displaying it here
# display(df)

#this gets us the number of rows, I think
print(len(df.index))


#this function takes in a user_dictionary and counts up the number of shifts
#this is pivotal for sorting later (this is how we sort users)
def compute_number_of_shifts(user_dict):
    shift_counter = 0
    monthly_schedule = user_dict["monthly_schedule"]
    for x in monthly_schedule.keys():
        shifts_per_day = (str(monthly_schedule[x]).split())
        for y in shifts_per_day:
            shift_counter += 1
        user_dict["num_shifts"] = shift_counter


#ann wanted to add this function to take an input list of strings and change it to a list of ints
def change_list_elements_to_int(input_list):
    my_list = []
    for x in input_list:
        my_list.append(int(x))
    return my_list

#this is creating an empty list so that we can put the user dicts in it
all_user_info = []

#this is the part of the script where we run a few of the previous functions
for row in range(len(df.index)):
    user_dict = (build_user_from_row(df.loc[row]))
    user_dict["monthly_schedule"] = look_at_cols_for_loc_for_user(
        build_user_from_row(df.loc[row]))
    compute_number_of_shifts(user_dict)
    all_user_info.append(user_dict)

output_dataframe = pd.DataFrame(
    columns=["name", "startTime", "endTime", "location", "email"])
# display(output_dataframe)
# print(len(all_user_info))

#sort the user dicts based on the num_shifts element in the dict
all_user_info = sorted(all_user_info, key=lambda d: d['num_shifts'])
pprint.pprint(all_user_info)


#here I make structures that are basically calendars of shifts
list_of_day_integers = list(range(1, num_of_jan_days+1))



RO_cal = {key: [None, None, None] for key in list_of_day_integers}
WV_cal = {key: [None, None, None] for key in list_of_day_integers}
OP_cal = {key: [None, None, None] for key in list_of_day_integers}

#pprint.pprint(RO_cal)

#start to fill the rochester scrape



def fill_calendar(location, calendar):
    processed_volunteers = []
    for volunteer in all_user_info:
        if volunteer["loc"] == location:
            volunteer_metadata = []
            volunteer_metadata.append(volunteer["name"])
            volunteer_metadata.append(volunteer["index"])
            volunteer_metadata.append(volunteer["time"])
            
            for previous_volunteer in processed_volunteers:
                if volunteer["name"] == previous_volunteer[0]:
                   if volunteer["time"] < previous_volunteer[2]:
                       #if the current volunteers time precedes the previous one,
                       #we need to go through the entire calendar and zero out entries with
                       #the volunteers name
                       for x in range(1, 32):
                           for y in range(0, 3):
                               if calendar[x][y] == volunteer["name"]:
                                   calendar[x][y] = None
            processed_volunteers.append(volunteer_metadata)
            
            
            shift = ""
            for day in list(volunteer["monthly_schedule"].keys()):
                shift_counter = 0
                #print(day)
                #print(volunteer["monthly_schedule"])
                real_day = int(day[2:])
                shift = volunteer["monthly_schedule"][day]
                if(type(shift) is str):
                    print(shift)
                    split_shifts = shift.split(", ")
                    split_shifts = change_list_elements_to_int(split_shifts)
                    shift = split_shifts
                    if(len(shift) == 1 and int(shift[0]) !=0):
                        if (calendar[real_day][shift[0]-1] == None):
                            shift_counter += 1
                            if shift_counter == 1:
                                calendar[real_day][shift[0]-1] = volunteer["name"]
                    elif(len(shift)>1):
                        for x in shift:
                            if (calendar[real_day][x-1] == None):
                                shift_counter += 1
                                if shift_counter == 1:
                                    calendar[real_day][x-1] = volunteer["name"]
                if shift != 0 and shift == shift:
                    if type(shift) is float:
                        shift = int(shift)
                    if(type(shift) is int):
                        if (calendar[real_day][shift-1] == None):
                            shift_counter += 1
                            if shift_counter == 1:
                                calendar[real_day][shift-1] = volunteer["name"]
    return calendar





# for volunteer in all_user_info:
#     shift = ""
#     if volunteer["loc"] == "Williamsville":
#         for day in list(volunteer["monthly_schedule"].keys()):
#             #print(day)
#             #print(volunteer["monthly_schedule"])
#             real_day = int(day[2:])
#             shift = volunteer["monthly_schedule"][day]
#             if(type(shift) is str):
#                 print(shift)
#                 split_shifts = shift.split(", ")
#                 split_shifts = change_list_elements_to_int(split_shifts)
#                 shift = split_shifts
#                 if(len(shift) == 1 and int(shift[0]) !=0):
#                     if (WV_cal[real_day][shift[0]-1] == None):
#                         WV_cal[real_day][shift[0]-1] = volunteer["name"]
#                 elif(len(shift)>1):
#                     for x in shift:
#                         if (WV_cal[real_day][x-1] == None):
#                             WV_cal[real_day][x-1] = volunteer["name"]
#             if shift != 0 and shift == shift:
#                 if type(shift) is float:
#                     shift = int(shift)
#                 if(type(shift) is int):
#                     if (WV_cal[real_day][shift-1] == None):
#                         WV_cal[real_day][shift-1] = volunteer["name"]



# for volunteer in all_user_info:
#     shift = ""
#     if volunteer["loc"] == "Orchard Park":
#         for day in list(volunteer["monthly_schedule"].keys()):
#             #print(day)
#             #print(volunteer["monthly_schedule"])
#             real_day = int(day[2:])
#             shift = volunteer["monthly_schedule"][day]
#             if(type(shift) is str):
#                 print(shift)
#                 split_shifts = shift.split(", ")
#                 split_shifts = change_list_elements_to_int(split_shifts)
#                 shift = split_shifts
#                 if(len(shift) == 1 and int(shift[0]) !=0):
#                     if (OP_cal[real_day][shift[0]-1] == None):
#                         OP_cal[real_day][shift[0]-1] = volunteer["name"]
#                 elif(len(shift)>1):
#                     for x in shift:
#                         if (OP_cal[real_day][x-1] == None):
#                             OP_cal[real_day][x-1] = volunteer["name"]
#             if shift != 0 and shift == shift:
#                 if type(shift) is float:
#                     shift = int(shift)
#                 if(type(shift) is int):
#                     if (OP_cal[real_day][shift-1] == None):
#                         OP_cal[real_day][shift-1] = volunteer["name"]       

        # if(len(shift)==1):
        #     if (RO_cal[real_day][shift[0]-1] == None):
        #         RO_cal[real_day][shift[0]-1] = volunteer["name"]
        # else:   
        #     for x in shift:
        #            if (RO_cal[real_day][x-1] == None):
        #                RO_cal[real_day][x-1] = volunteer["name"] 
    # print(volunteer["name"])
    #     for (day, shift) in zip(volunteer["monthly_schedule"].keys(), volunteer["monthly_schedule"].values()):
    #         #print(day, shift)
    #         if(type(shift) is str):
    #             split_shifts = shift.split(", ")
    #             split_shifts = change_list_elements_to_int(split_shifts)
    #             volunteer["monthly_schedule"][day] = split_shifts
    #         elif(not pd.isna(shift)):
    #             volunteer["monthly_schedule"][day] = int(shift)
    #         #print(volunteer["monthly_schedule"][day])
        # for day in volunteer["monthly_schedule"].keys():
        #     if(type(volunteer["monthly_schedule"][day]) == list):
        #         if len(volunteer["monthly_schedule"][day]) == 1 and volunteer["monthly_schedule"][day][0] != 0:
        #             shift = volunteer["monthly_schedule"][day][0]
            #         if(RO_cal[int(day[2:])][shift-1] is None):
            #             print("Adding " + str(volunteer["name"]) + " day " + str(day) +  " into the calendar!")
            #             RO_cal[int(day[2:])][shift-1] = volunteer["name"]
            #             print(RO_cal[int(day[2:])][shift-1])
            #             print(day)
            #     else:
            #         for element in volunteer["monthly_schedule"][day]:
            #             if(RO_cal[int(day[2:])][element-1] is None):
            #                 print("Adding " + str(volunteer["name"]) + " day " + str(day) +  " into the calendar!")
            #                 RO_cal[int(day[2:])][element-1] = volunteer["name"]
            # elif(type(volunteer["monthly_schedule"][day]) == int):
            #     shift = volunteer["monthly_schedule"][day]
            #     if(RO_cal[int(day[2:])][shift-1] is None):
            #         print("Adding " + str(volunteer["name"]) + " day " + str(day) +  " into the calendar!")
            #         RO_cal[int(day[2:])][shift-1] = volunteer["name"]

print("Rochester Cal")
RO_cal = fill_calendar("Rochester", RO_cal)
pprint.pprint(RO_cal) 
print("Williamsville Cal") 
WV_cal = fill_calendar("Williamsville", WV_cal)              
pprint.pprint(WV_cal)
OP_cal = fill_calendar("Orchard Park", OP_cal)              
pprint.pprint(OP_cal)                


#now we're gonna pass in the completed calendars above into what misha wants
def convert_calendar_into_what_misha_wants(cal, location:str, all_user_info):
    #this outputs a list of lists that will encode everything in the calendar:
        #each list has the NAME, the LOCATION, the START DATE, the END DATE, the EMAIL
        #   in that order
    cal_list = []
    for day in range (1,32):
            for shift in range(0,3):
                
                if cal[day][shift] == None:
                    continue
                
                shift_list = []
                
                name = cal[day][shift]
                
                shift_list.append(name)
                shift_list.append(location)
                start_date = "2023-01-"
                end_date = "2023-01-"
                
                #if day single digit then the "day" needs a 0 before it
                if day < 10:
                    start_date = start_date + "0"
                    end_date = end_date + "0"
                
                start_date = start_date + str(day)
                end_date = end_date + str(day)
                
                #i think these start and end dates get 0s after the T if they're single digit like ex. 2:00, is that right?
                
                if shift+1 == 1:
                    start_date = start_date + "T10:00:00"
                elif shift+1 == 2:
                    start_date = start_date + "T14:00:00"
                elif shift+1 == 3:
                    start_date = start_date + "T18:00:00"
                    
                if shift+1 == 1:
                    end_date = end_date + "T14:00:00"
                elif shift+1 == 2:
                    end_date = end_date + "T18:00:00"
                elif shift+1 == 3:
                    end_date = end_date + "T22:00:00"
                

                for x in all_user_info:
                    if x["name"] == name:
                        email = x["email"]

                # print(day, shift, name)
                # print(start_date)
                # print(end_date)
                shift_list.append(start_date)
                shift_list.append(end_date)
                shift_list.append(str(email))
                
                cal_list.append(shift_list)
                
    return cal_list       
            

#print(convert_calendar_into_what_misha_wants(OP_cal, "Orchard Park", all_user_info))

RO_df = pd.DataFrame(convert_calendar_into_what_misha_wants(RO_cal, "Rochester", all_user_info)) 
WV_df = pd.DataFrame(convert_calendar_into_what_misha_wants(WV_cal, "Williamsville", all_user_info))
OP_df = pd.DataFrame(convert_calendar_into_what_misha_wants(OP_cal, "Orchard Park", all_user_info))

# saving the dataframe 
RO_df.to_csv('rochester_calendar.csv') 
WV_df.to_csv('williamsville_calendar.csv') 
OP_df.to_csv('orchard_park_calendar.csv') 
