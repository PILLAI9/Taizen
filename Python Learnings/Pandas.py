import pandas as pd

# data = {'Name':['Avina','Shan','Pradeee'],
#             'Age':[22,43,65] }

# df = pd.DataFrame(data)
# print(df)

# df.to_csv('C:\Users\VarunPillai\Taizen\Python Learnings\mascots.csv',index=True)
# df = df.read_csv('C:\Users\VarunPillai\Taizen\Python Learnings\mascots.csv')
# df = pd.read_csv('C:\\Users\\VarunPillai\\Taizen\\Python Learnings\mascots.csv')
# print(df.to_string)

# for i in range(1, 3):
#     if i == 5:
#         print(i)
#     else:
#         print("NOT FOUND")

# df = pd.read_csv('C:\\Users\\VarunPillai\\Taizen\Python Learnings\mascots.csv')
# print(df.head())

# print(df.info())
# print(df.describe)
# print(df.isnull().sum())
# print(df['mascot_common_name'].count())
# print(df.nunique())
# print(df['mascot'].value_counts())

df_data = pd.read_excel('c:\\Users\\VarunPillai\\Taizen\\Python Learnings\gas_data.xlsx')
# df = pd.DataFrame(df_data)
df = pd.DataFrame(df_data,columns =['X','Y'])
# print(df.tail())
print(df.sample(2))

