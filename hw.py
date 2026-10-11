import pandas as pd

print("Panda Series ")

student_marks= pd.Series([98, 70, 63, 100, 85, 79, 52], index=["Ethan", "Sofi", "Julie", "Emily", "Evan", "Emma","Hayden"])
print(student_marks)


print("Data Frame")

data={
    "Student":["Ethan", "Sofi", "Julie", "Emily", "Evan", "Emma","Hayden"],
    "Total Grade /100":[98, 70, 63, 100, 85, 79, 52],
    "Math /50":[48, 25, 13, 50, 45, 39, 12],
    "English /50":[50, 45, 50, 50, 40, 40, 40]
}

df=pd.DataFrame(data)
print(df)

print("Reading data from a CSV file")

df.to_csv("student_marks.csv", index=False)
student_data=pd.read_csv("student_marks.csv")

print("CSV file read successfully!")
print(student_data)

print("View Data")
print("First 3 rows")
print(student_data.head(3))

print("Last 2 rows")
print(student_data.tail(2))

print("Data info")
print(student_data.info())

print("Cleaning Data")

messy_data={
    "Student":["Ethan", "Sofi", "Julie", "Emily", "Evan", "Emma","Hayden"],
    "Total Grade":[50, 70, 13, 100, 85, 79, 40],
    "Math":[None, 25, 13, 50, 45, 39, None],
    "English":[50, 45, None, 50, 40, 40, 40]
}

messy_df=pd.DataFrame(messy_data)


print("Data with Missing Values:")
print(messy_df)
 
cleaned_df = messy_df.fillna(0)
 
print("Cleaned Data:")
print(cleaned_df)
 
 
print("Student Total and Average Marks")
 
cleaned_df["Total"] = cleaned_df["Math"] + cleaned_df["English"] 
cleaned_df["Average"] = cleaned_df["Total"] / 2
 
print(cleaned_df)
 