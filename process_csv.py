import pandas as pd
import numpy as np
import pprint

df = pd.read_csv("scheduling_data.csv")

cols = df.columns.tolist()

df = df.rename(columns={cols[0]: "time", cols[1]: "email",
               cols[2]: "name", cols[3]: "d_per_w", cols[4]: "loc"})


df = df.replace("10a-2p", "1")
df = df.replace("2p-6p", "2")
df = df.replace("6p-10p", "3")
df = df.replace("10a-2p, 6p-10p", "1, 3")
df = df.replace("10a-2p, 2p-6p", "1, 2")
df = df.replace("2p-6p, 6p-10p", "2, 3")
df = df.replace("10a-2p, 2p-6p, 6p-10p", "1, 2, 3")

days_in_jan = 31
rename_dict = {}

for x in range(1, days_in_jan+1):
    rename_dict[cols[x+4]] = "WV" + str(x)

for x in range(1, days_in_jan+1):
    rename_dict[cols[x+4+days_in_jan]] = "OP" + str(x)

for x in range(1, days_in_jan+1):
    rename_dict[cols[x+4+(days_in_jan*2)]] = "RO" + str(x)

for x in range(1, days_in_jan+1):
    rename_dict[cols[x+4+(days_in_jan*3)]] = "BOTH" + str(x)

df = df.rename(columns=rename_dict)
df['index_col'] = df.index

cols = df.columns.tolist()

# display(df)


def build_user_from_row(df_row):
    user_info = {}
    user_info["index"] = df_row["index_col"]
    user_info["name"] = df_row["name"]
    user_info["email"] = df_row["email"]
    user_info["d_per_w"] = df_row["d_per_w"]
    user_info["loc"] = df_row["loc"]
    user_info["time"] = df_row["time"]
    return user_info

# for now, I'm going to assume that no user is doing Rochester AND another location
# the fix for this is straightforward but I won't deal with it rn


def look_at_cols_for_loc_for_user(user_dict):
    if(user_dict["loc"] == "Williamsville"):
        # we're only going to be looking at the Rochester subset of the dataframe
        # after the first five indices of metadata (time, email, name, d_per_w, location,)
        wv_df = df[cols[5:5+days_in_jan]]
        users_monthly_availability = wv_df.loc[user_dict["index"]]
    elif(user_dict["loc"] == "Orchard Park"):
        op_df = df[cols[5+days_in_jan:5+(days_in_jan*2)]]
        users_monthly_availability = op_df.loc[user_dict["index"]]
    elif(user_dict["loc"] == "Rochester"):
        roch_df = df[cols[5+(days_in_jan*2):5+(days_in_jan*3)]]
        users_monthly_availability = roch_df.loc[user_dict["index"]]
    elif(user_dict["loc"] == "Both Williamsville and Orchard Park"):
        both_df = df[cols[5+(days_in_jan*3):5+5+(days_in_jan*4)]]
        users_monthly_availability = both_df.loc[user_dict["index"]]
    else:
        print("There was an error somewhere.")
    return dict(users_monthly_availability)


#display(df)

# for y in range(len(df.index)):
#     print(df.loc[y]["name"])
#     print(look_at_cols_for_loc(build_user_from_row(df.loc[y])))


df.to_csv("output.csv")