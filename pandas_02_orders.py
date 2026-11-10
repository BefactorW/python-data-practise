import pandas as pd
orders_pd = pd.read_csv("orders.csv")
print(orders_pd)
orders_pd["revenue"] = orders_pd["price"] * orders_pd["quantity"]
print(orders_pd["revenue"])
print(orders_pd.groupby("category")["revenue"].sum())
print(orders_pd.sort_values("revenue", ascending=False))