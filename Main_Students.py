student_dict = {
    "student": ["Angela", "James", "lily"],
    "score": [56, 76, 98]
}
import pandas
# So the .datafram pandas function takes a dictonary or array and organizes it, it works well with key value
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#iter rows lets you loop trhough the rows rather than the columns
for (index, row) in student_data_frame.iterrows():
    print(row.score)