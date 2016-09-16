import pandas as pd

csv_data = pd.read_csv('/home/davis68/teaching/cs101-fa16/admin/rpt_all_students.csv')

print('c.NbGrader.db_students = [')
for idx,entry in csv_data.iterrows():
    print('dict(id="%s", first_name="%s", last_name="%s"),'%(entry['Net ID'], entry['First Name'], entry['Last Name']))
print(']')
