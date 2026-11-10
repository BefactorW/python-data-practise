
##
# import pandas as pd

# books = pd.DataFrame({
#     "title": ["Dune", "Emma", "Ulysses"],
#     "pages": [412, 474, 730],
#     "read": [True, False, True],
# })

# print(books)
# print(books["pages"])
# print(books[books["pages"] > 450])


##
# import pandas as pd

# students = pd.DataFrame({
#     "Name": ["Max", "Kirill", "Ilya", "Eugene", "Aleksandra"],
#     "Age": [21, 22, 24, 32, 19],
#     "mark": [6, 5, 4, 8, 7],
# })
# print(students)
# print(students["mark"])
# print(students[students["mark"] > 4])
# print(students["Age"].mean())


##
# import pandas as pd

# students = pd.DataFrame({
#     "Name": ["Max", "Kirill", "Ilya", "Eugene", "Aleksandra"],
#     "Age": [21, 22, 24, 32, 19],
#     "mark": [6, 5, 4, 8, 7],
# })

# students["passed"] = students["mark"] >= 5
# print(students)
# print(students.sort_values("mark", ascending=False))
# good_rslt = students[students["mark"] > 4 ]
# print(good_rslt[["Name", "mark"]])


##
# import pandas as pd

# df = pd.read_csv("fruits.csv")
# print(df)
# print(df.groupby("type")["kg"].sum())


import pandas as pd
orders_pd = pd.read_csv("orders.csv")
print(orders_pd)
orders_pd["revenue"] = orders_pd["price"] * orders_pd["quantity"]
print(orders_pd["revenue"])
print(orders_pd.groupby("category")["revenue"].sum())
print(orders_pd.sort_values("revenue", ascending=False))

