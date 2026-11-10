
import pandas as pd

students = pd.DataFrame({
    "Name": ["Max", "Kirill", "Ilya", "Eugene", "Aleksandra"],
    "Age": [21, 22, 24, 32, 19],
    "mark": [6, 5, 4, 8, 7],
})
print(students)
print(students["mark"])
print(students[students["mark"] > 4])
print(students["Age"].mean())


##
import pandas as pd

students = pd.DataFrame({
    "Name": ["Max", "Kirill", "Ilya", "Eugene", "Aleksandra"],
    "Age": [21, 22, 24, 32, 19],
    "mark": [6, 5, 4, 8, 7],
})

students["passed"] = students["mark"] >= 5
print(students)
print(students.sort_values("mark", ascending=False))
good_rslt = students[students["mark"] > 4 ]
print(good_rslt[["Name", "mark"]])