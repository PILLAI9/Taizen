import pandas as  pd

data_demo = {'Club':['Real Madrid','Barcalona','Manchester United','lili','Inter Milan'],
             'Champios League':[15,2,5,2,12]}
df = pd.DataFrame(data_demo)
# print(df.describe)

# print(df[df['Club']) == 'Real Madrid'])

# print(df['Club'] == 'Real Madrid')
# print(df['Club'])
df['Country']=['Spain','Spain','England','Italy','Italy']

# print(df['Country'])
# print(df)
new_data = {'Club':['Kerala Blasters'],'Champios League':[3],'Country':['India']}
new_data = pd.DataFrame(new_data)
df = pd.concat([df,new_data])
# print(df)

# for clubs in df['Club']:
#     # print(clubs)

# if 'Kerala Blasters' in df['Club'].values:
#     print("CLUB Found")

# for club in df['Club']:
#     if club == 'Real Madrid':
#         print("LETS GOOO")

count = df['Club'].value_counts()['lili']
# print(f"Club Found {count} times")

# groupby  = df.groupby('Champios League')['Club'].sum()
# print(groupby)


top_clubs = df[df['Champios League'] < 3]
# print(top_clubs)

sorted = df.sort_values(by = 'Champios League',ascending=True)
# # print(sorted)

# # for club in df['Club']:
# #     print(club)

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1

# for club in df['Club']:
#                print(club)
#                if 'Real Madrid' in club:
#                        print("Lets GOO")


index = 0
count  = 0

while index < len(df):
    if df['Champios League'][index]>5:
        count = count + 1
        print(df['Club'][index])

# print(df)

# print(len(df))










    











