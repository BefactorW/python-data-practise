
#
import pandas as pd

books = pd.DataFrame({
    "title": ["Dune", "Emma", "Ulysses"],
    "pages": [412, 474, 730],
    "read": [True, False, True],
})

print(books)
print(books["pages"])
print(books[books["pages"] > 450])



