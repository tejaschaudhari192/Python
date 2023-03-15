import pandas as pd

data = [
    {
        "Age": "Youth",
        "Income": "High",
        "Student": "No",
        "Credit_Rating": "Fair",
        "Buys_book": "No"
    },
    {
        "Age": "Youth",
        "Income": "High",
        "Student": "No",
        "Credit_Rating": "Excellent",
        "Buys_book": "No"
    },
    {
        "Age": "Youth",
        "Income": "High",
        "Student": "No",
        "Credit_Rating": "Excellent",
        "Buys_book": "No"
    },
    {
        "Age": "Middle_aged",
        "Income": "High",
        "Student": "No",
        "Credit_Rating": "Fair",
        "Buys_book": "Yes"
    },
    {
        "Age": "Senior",
        "Income": "Medium",
        "Student": "No",
        "Credit_Rating": "Fair",
        "Buys_book": "Yes"
    },
    {
        "Age": "Senior",
        "Income": "Low",
        "Student": "Yes",
        "Credit_Rating": "Fair",
        "Buys_book": "Yes"
    },
    {
        "Age": "Senior",
        "Income": "Low",
        "Student": "Yes",
        "Credit_Rating": "Excellent",
        "Buys_book": "No"
    },
    {
        "Age": "Middle_aged",
        "Income": "Low",
        "Student": "Yes",
        "Credit_Rating": "Excellent",
        "Buys_book": "Yes"
    },
    {
        "Age": "Youth",
        "Income": "Low",
        "Student": "Yes",
        "Credit_Rating": "Fair",
        "Buys_book": "Yes"
    },
]

x = pd.DataFrame(data)
print(x)
x.to_csv("x.csv")
