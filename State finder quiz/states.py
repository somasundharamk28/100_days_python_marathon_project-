import pandas as pd
data = pd.read_csv("50_states.csv")

for i in data["state"]:
    if answer_text == i:
        answer_text.goto