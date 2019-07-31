# pandas -- to read datasets 
# dataframe -- a table -- with n freatures & m training examples
import pandas as pd

# pd.read_csv('file_name.csv') -- to read a csv file
# csv file -- comma seperated values
df=pd.read_csv('weather_data.csv')
print(df)
# it automatically provides the serial no.(0 indexed) col as first col -- but that doesn't count

# df['col_name']  or  df.col_name-- to access a particular col 
print(df['temperature'])
print(df.temperature)
print(df['temperature'].max())
# df[['c1' , 'c2']] -- to access multiple col
print(df[['day','temperature']])
# we can't access a row in dataFrames


print(df['day'][df['event']=='Rain']) # it will day on that event = Rain


# csv file -- first stage -- a list containing tuples -- each tuples = a row of file
wheather=[('1/1/2017',32,6,'Rain'),
          ('1/2/2017',35,7,'Sunny'),
          ('1/3/2017',28,2,'Snow'),
          ('1/4/2017',24,7,'Snow'),
          ('1/5/2017',32,4,'Rain'),
          ('1/6/2017',31,2,'Sunny')
         ]
# pd.DataFrame(list,columns=['c1_name', 'c2_name' ... ]) -- to add col-name 
df=pd.DataFrame(wheather,columns=['day','temperature','windspeed','event'])
print(df)

# df.columns -- to get all the col-names
print(df.columns) 

# to rename col_names 
# 1. df.columns=['new1','new2'] -- we've to provide new names for all columns -- all will change at once
df.columns=['date','temperature','wind','event']
print(df.columns)

# 2. df = df.rename(columns={'old1':'new1','old2':'new2'}) -- this will returns a new df so store it 
# sequence of columns isn't neccessary  
df=df.rename(columns={'wind':'windo','event':'evento'})
print(df.columns)

# 3. df = df.rename({'old1':'new1','old2':'new2'},axis=1)
df=df.rename({'windo':'wind','evento':'event'},axis=1)
print(df.columns)

# 4. df.rename({'old1':'new1','old2':'new2'},axis=1,inplace=True) -- for direct -- no need to store
df.rename({'date':'day'},axis=1,inplace=True)
print(df.columns)


# df['col'].describe() -- returns count,max,min,mean,std(25,50,75)
print(df['temperature'].describe())

# df[df.col == df.col.max()] -- to select a row which has max temp
print(df[df.temperature==df.temperature.max()])

# df.c2[df.c1==df.c1.max()] -- returns that c2 which has max c1 value
print(df.day[df.temperature==df.temperature.max()])

# pd.read_excel('file_name.xlsx')
df=pd.read_excel('weather_data.xlsx')
print(df)

# df.to_csv('newFileName.csv') -- to convert df containing file into csv
df.to_csv('newfile.csv') # it will automatically add the serial no index
# df.to_csv('newFileName.csv',index=False) -- for not to add serial no index
df.to_csv('newfile.csv',index=False)

# df.to_excel('file_name.xlsx',sheet_name='sheet_name') -- to convert into excel file -- sheet name must be given
df.to_excel('newExcel.xlsx',sheet_name='weather_data')


# df.groupby('col') -- it will group whole df into groups present in col
# one group will contain one type of col
df=pd.read_csv('weather_data_cities.csv')
print(df)
g=df.groupby('city')
# g contains two things -- one is group_name & for other it will create df of that group
for group,group_df in g:
    print(group)
    print(group_df)

# g.get_group('group_name') -- returns df of that group
print(g.get_group('new york'))

# g.describe() -- returns count & etc. of all integer type cols of all groups
print(g.describe()) # there is two col (temp. & windspeed) -- so describe will work for both of them
# for each -- total describe = total groups


# creating df using dict
india=pd.DataFrame({'city' : ['mumbai','delhi','jaipur'],
                        'temp': [32,45,13],
                        'hum' : [80,60,120]
                        })
print(india)

# pd.concat([df1,df2])
us=pd.DataFrame({'city' : ['newyork','la','california'],
                        'temp': [22,45,63],
                        'hum' : [10,40,20]
                        })
print(pd.concat([india,us])) # serial index of both will be distinct -- they will have their own serial index
# to make single serial index
print(pd.concat([india,us],ignore_index=True))

# axis = 1 -- for col wise concat
print(pd.concat([india,us],axis=1))


# pd.merge(x,y,on='col_name') -- merging of two dfs
temp=pd.DataFrame({
                    'city':['mum','del','jai','aagra'],
                    'temp':[20,10,30,50]
                 })
humi=pd.DataFrame({
                    'city':['mum','del','jai'],
                    'humi':[20,10,30]
                 })
df=pd.merge(temp,humi,on='city')
print(df)
df=pd.merge(temp,humi,on='city',how='outer')
print(df)
# if there's a col_name(or col) which is both dfs -- then both col gonna be add -- but as a diff col name
# col of x = temp_x
# col of y = temp_y
humi['temp']=[30,40,200]
print(humi)
df=pd.merge(temp,humi,on='city')
print(df)


# add a col in existing df -- bcoz df is mostly similar to dict(bcoz it's genereated from it) -- so treat df like dict
# 1. df['new_col_name'] = [col_values]
humi['temp']=[30,40,200]
print(humi)

# 2. df.insert(n,'new_col_name',[col_values],True) -- this will add the col at nth index(0 indexed) 
humi.insert(1,'temp',[20,30,400],True)
print(humi)
# it will add this col anyway if there's True-- no matter this col is already present or not -- name of all same col will also be same
# if there's False instead of True -- then it won't add the col if it's already present & gives ERROR

# 3. df.assign(col_name = [col_values]) 
# if this col is already there -- it will replace that by this
humi=humi.assign(temp=[1,30,80])
print(humi)
print(humi.loc[2])

df=pd.DataFrame({'no':[1,2,3,4,5,6,7,8,9,19]},index=[49,48,47,46,45,1,2,3,4,5])
print(df)
# index_no -- given indices
# row_no -- rth row (0 indexed)

# df.loc[index_no] -- to access row of that index_no
print(df.loc[47])
# df.loc[:index_no] -- all rows upto that index_no -- inclusive
print(df.loc[:47])

# df.iloc[row_no] -- row of that row_no -- inclusive
print(df.iloc[4])
# df.iloc[:row_no] -- all rows till that row -- inclusive
print(df.iloc[:4])