def reading_csv_files(formatted_data, scheduling_data):
    with open(formatted_data) as file_obj_1:
        reader_obj_1 = csv.reader(file_obj_1)
    with open(scheduling_data) as file_obj_2:
        reader_obj_2 = csv.reader(file_obj_2)
    return formatted_data, scheduling_data


def desired_shifts(read_formatted_data, read_scheduling_data):
    final_formatted_data, final_scheduling_data = reading_csv_files(read_formatted_data, read_scheduling_data)
    volunteer_name_set1 = final_formatted_data["name"].tolist()
    volunteer_name_set2 = final_scheduling_data["name"].tolist()
    for name in volunteer_name_set1:
        shift_count = 0
        for row in final_scheduling_data:
            if row[2] == name:
                shift_count += 1
        volunteer_shift_number = 0
        for row in final_formatted_data:
            if row[2] == name:
                volunteer_shift_number = row[3]
        if shift_count > volunteer_shift_number:
            print(f'There are more number of shifts for {name}')


def daily_shifts(read_formatted_data, read_scheduling_data):
    final_formatted_data, final_scheduling_data = reading_csv_files(read_formatted_data, read_scheduling_data)
    volunteer_name_set1 = final_formatted_data["name"].tolist()
    volunteer_name_set2 = final_scheduling_data["name"].tolist()
    for name in volunteer_name_set1:
        shift_count = 0
        for row in final_scheduling_data:
            if row[2] == name:
                shift_count += 1
        volunteer_shift_number = 0
        for row in final_formatted_data:
            if row[2] == name:
                volunteer_shift_number = row[3]
        if shift_count <= volunteer_shift_number:
            print(f'There are less number of shifts for {name}')


def priority_shifts(read_formatted_data, read_scheduling_data):
    final_formatted_data, final_scheduling_data = reading_csv_files(read_formatted_data, read_scheduling_data)
    volunteer_name_set1 = final_formatted_data["name"].tolist()
    volunteer_name_set2 = final_scheduling_data["name:"].tolist()
    for name in volunteer_name_set1:
        shift_count = 0
        for row in final_scheduling_data:
            if row[2] == name:
                shift_count += 1
        volunteer_shift_number = 0
        for row in final_formatted_data:
            if row[2] == name:
                volunteer_shift_number = row[3]
        if shift_count <= volunteer_shift_number:
            print(f'There are less number of shifts for {name}')


def max_2_shifts(read_formatted_data, read_scheduling_data):
    final_formatted_data, final_scheduling_data = reading_csv_files(read_formatted_data, read_scheduling_data)
    volunteer_name_set1 = final_formatted_data["name"].tolist()
    volunteer_name_set2 = final_scheduling_data["name"].tolist()
    for name in volunteer_name_set1:
        shift_count = 0
        for row in final_scheduling_data:
            if row[2] == name:
                shift_count += 1
        volunteer_shift_number = 0
        for row in final_formatted_data:
            if row[2] == name:
                volunteer_shift_number = row[3]
        if shift_count <= volunteer_shift_number:
            print(f'There are less number of shifts for {name}')


def max_2_shifts(read_formatted_data, read_scheduling_data):
    final_formatted_data, final_scheduling_data = reading_csv_files(read_formatted_data, read_scheduling_data)
    volunteer_name_set1 = final_formatted_data["name"].tolist()
    volunteer_name_set2 = final_scheduling_data["name"].tolist()
    for name in volunteer_name_set1:
        shift_count = 0
        for row in final_scheduling_data:
            if row[2] == name:
                shift_count += 1
        volunteer_shift_number = 0
        for row in final_formatted_data:
            if row[2] == name:
                volunteer_shift_number = row[3]
        if shift_count <= volunteer_shift_number:
            print(f'There are less number of shifts for {name}')


