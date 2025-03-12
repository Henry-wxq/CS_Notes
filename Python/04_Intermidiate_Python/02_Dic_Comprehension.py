"""
Dictionary Comprehension
new_dict = {new_key:new_value for item in list}
new_dict = {new_key:new_value for (key, value) in dict.items()}
new_dict = {new_key:new_value for (key, value) in dict.items() if test}

loop though a dataframe is similar to work with a dictionary
new_df = {new_index:new_value for (index, row) in df.iterrows()}
"""
import random
import pandas as pd

if __name__ == "__main__":
    names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
    student_scores = {student: random.randint(1, 100) for student in names}
    print(student_scores)

    weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22,
                 "Sunday": 24}
    weather_f = {key: ((value * 9 / 5) + 32) for (key, value) in weather_c.items()}
    print(weather_f)

    # loop though pandas df
    student_dict = {"student": ["Angela", "James", "Lily"],
                    "score": [56, 76, 98]}
    student_df = pd.DataFrame(student_dict)
    print(student_df)

    # not meaningful
    # for (key, value) in student_df.items():
    #     # key is the column name
    #     print(key)
    #     # value is the column values
    #     print(value)

    # Loop through rows of a data frame
    for (index, row) in student_df.iterrows():
        # print(index)
        # # pandas series object
        # print(row)
        print(row.student)

