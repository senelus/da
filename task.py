import pandas as pd

def is_match(first_fileds, second_fields):
    for word in first_fileds.lower().replace('-', ' ').split():
        if word in second_fields.lower():
            return True
    return False

data = pd.read_csv("works.csv").dropna()
not_matched = 0
for (frist_field, second_field) in zip(data["jobTitle"], data["qualification"]):
    if not is_match(frist_field, second_field) and not is_match(second_field, frist_field):
        not_matched += 1
print(data.shape[0], not_matched)
print(data[data["jobTitle"].str.lower().str.contains("менеджер"[:-2])]["qualification"].str.lower().value_counts().head(5))
print(data[data["qualification"].str.lower().str.contains("инженер"[:-2])]["jobTitle"].str.lower().value_counts().head(5))
