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

# df_data = pd.read_excel('c:\\Users\\VarunPillai\\Taizen\\Python Learnings\gas_data.xlsx')
# df = pd.DataFrame(df_data)
# df = pd.DataFrame(df_data,columns =['X','Y'])
# df = pd.DataFrame(df_data)
# print(df)
# print(df.tail())
# print(df.sample(2))
# print(df['X'].tail())
# print(df['X'] == 142.103577)

# print(df[['Product','Well Type','Production forecast next month']])
# print(df.columns)

data_demo = {'Club':['Real Madrid','Barcalona','Manchester United'],'Champios League':[15,2,5]}
adf = pd.DataFrame(data_demo)
# print(adf)

# if "Real Madrid" in adf['Club'].values:
#     print("CHAMPOIIN TEAM")
# else:
#     print("Team is BAD")

# print(adf['Club'].values == "Real Madrid")

new_team = {'Club':'Liverpool','Champios League':1}
# print(adf[['Club','Champios League']]) == "Real Madrid"

print(adf['Club','Champios League']>10)

