
           Module 1: Introduction & Setup

Module 1: Introduction & Setup
1.1 Pandas Kya Hai aur Kyun Use Karte Hain?
Explanation: Pandas Python ki sabse popular Data Analysis library hai. Yeh tabular data (jaise Excel sheet) ko aasani se handle karti hai.
Data cleaning
Data manipulation
Data analysis
Data visualization ke liye base
Real life mein CSV, Excel, Database se data aata hai — Pandas usko jaldi process karne mein madad karti hai.
Pandas vs Excel:
Excel mein manual click karte ho → Pandas mein code se automate kar sakte ho
Lakhs-crores rows handle kar sakti hai (Excel nahi)
Bahut fast aur flexible
1.2 Installation
Terminal ya Command Prompt mein ek baar yeh command run kar do:
pip install pandas
(agar Jupyter Notebook use kar rahe ho toh !pip install pandas)
1.3 Importing Pandas
Har code file ke top pe yeh likhna zaroori hai:
import pandas as pd
import numpy as np          # aksar saath mein use hota hai

# Version check karna (important)
print("Pandas Version:", pd.__version__)
Output (jo abhi run kiya):
Pandas Version: 3.0.1
1.4 Pandas ke Do Main Data Structures
Structure	Dimension	Matlab	Example
Series	1D	Ek single column (jaise list)	Student ke marks
DataFrame	2D	Full table (rows + columns)	Student ka complete record
Simple Visual:
Series → Ek column
DataFrame → Multiple columns wala Excel sheet
1.5 Quick First Example
# Pehla DataFrame banate hain
data = {
    'Name': ['Jyoti', 'Rahul', 'Priya'],
    'Age': [22, 25, 23],
    'City': ['Lucknow', 'Kanpur', 'Varanasi']
}

df = pd.DataFrame(data)
print(df)
Output:
Name  Age       City
0   Jyoti   22    Lucknow
1   Rahul   25     Kanpur
2   Priya   23  Varanasi
Basic checks karna:
print("Shape (rows, columns):", df.shape)
print("\nColumns names:", df.columns.tolist())
print("\nData types:\n", df.dtypes)
print("\nFirst 2 rows:\n", df.head(2))
Output:
Shape (rows, columns): (3, 3)
Columns names: ['Name', 'Age', 'City']
Data types:
 Name    object
Age      int64
City    object
dtype: object

Module 1 ke Important Notes
Hamesha import pandas as pd likho (pd short form common hai)
NumPy ke saath kaam karta hai, isliye import numpy as np bhi common hai
Pandas data ko DataFrame mein store karke hi zyadatar kaam hota hai
Version 2.0 ke baad bahut improvements aaye hain (especially performance)
Common Mistakes Beginners karte hain:
1.pandas ki jagah Pandas likhna (case sensitive)
2.Installation ke baad kernel restart na karna (Jupyter mein)
3.Sirf pd import kiye bina direct pandas.DataFrame use karna

Ab bata:
Module 1 complete ho gaya! ✅
Agla kya padhein?
1.Module 2: Pandas Series (bahut important base)
2.Module 3: Pandas DataFrame (sabse zyada use hota hai)
Ya phir bol: "Module 2 padhao"
Tu bas number ya naam bol de, main turant next module detail mein padha dunga with lots of examples.
Bata kya padhna hai ab? 😊
Executed code
ha
Haan bhai, samajh gaya! 🔥
Ab Module 2: Pandas Series detail mein padhte hain. Yeh bahut important hai kyunki Series DataFrame ka basic building block hai.
Module 2: Pandas Series (1-Dimensional Data)
2.1 Series Kya Hai?
Explanation: Series ek labelled 1D array hai. Matlab:
Values + Index
Ek single column jaisa
List se powerful kyunki isme custom labels (index) daal sakte ho
Missing values (NaN) ko bhi easily handle karta hai
2.2 Series Kaise Banate Hain?
Example 1: List se Series
import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)
Output:
0    10
1    20
2    30
3    40
4    50
dtype: int64
Example 2: Custom Index ke saath
s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s2)
Output:
a    10
b    20
c    30
d    40
dtype: int64
Example 3: Dictionary se Series
s3 = pd.Series({'Math': 85, 'Science': 90, 'English': 78, 'Hindi': 92})
print(s3)
Output:
Math       85
Science    90
English    78
Hindi      92
dtype: int64
Example 4: Name aur dtype specify karke
s4 = pd.Series([1.5, 2.7, 3.8, 4.2], 
               index=['A', 'B', 'C', 'D'],
               name='Marks',
               dtype='float64')
print(s4)
Output:
A    1.5
B    2.7
C    3.8
D    4.2
Name: Marks, dtype: float64
2.3 Series ke Important Attributes
print("Index:", s3.index.tolist())
print("Values:", s3.values)
print("Data type:", s3.dtype)
print("Name:", s3.name)
print("Shape:", s3.shape)
print("Size:", s3.size)
Output:
Index: ['Math', 'Science', 'English', 'Hindi']
Values: [85 90 78 92]
Data type: int64
Name: None
Shape: (4,)
Size: 4
2.4 Data Access Karna (Indexing)
print("s2['b'] =", s2['b'])           # label se
print("s2.iloc[2] =", s2.iloc[2])     # position se (integer location)
print("s3['Science'] =", s3['Science'])
Output:
s2['b'] = 20
s2.iloc[2] = 30
s3['Science'] = 90
Slicing examples:
print("\nFirst 3 elements:\n", s2[:3])
print("\nLast 2 elements:\n", s2[-2:])
print("\nSpecific labels:\n", s3[['Math', 'Hindi']])
2.5 Arithmetic Operations (Broadcasting)
s5 = pd.Series([1, 2, 3, 4])
s6 = pd.Series([10, 20, 30, 40])

print("Addition:\n", s5 + s6)
print("\nMultiplication by 2:\n", s5 * 2)
print("\nPower:\n", s5 ** 2)
Output:
Addition:
 0    11
1    22
2    33
3    44
dtype: int64

Multiplication by 2:
 0     2
1     4
2     6
3     8
dtype: int64
Different index wale Series ka operation:
s7 = pd.Series([1, 2, 3], index=['a','b','c'])
s8 = pd.Series([10, 20], index=['a','b'])
print(s7 + s8)
Output (NaN aayega jahaan index match nahi karta):
a    11.0
b    22.0
c     NaN
dtype: float64
2.6 Statistical Methods
marks = pd.Series([75, 82, 90, 68, 95, 88])

print("Sum:", marks.sum())
print("Mean:", marks.mean())
print("Median:", marks.median())
print("Minimum:", marks.min())
print("Maximum:", marks.max())
print("Standard Deviation:", marks.std())
print("\nDescribe:\n", marks.describe())
Output:
Sum: 498
Mean: 83.0
Median: 85.0
Minimum: 68
Maximum: 95
Standard Deviation: 10.04987562112089

Describe:
 count     6.000000
mean     83.000000
std      10.049876
min      68.000000
25%      77.250000
50%      85.000000
75%      89.500000
max      95.000000
dtype: float64
2.7 Missing Values (NaN) in Series
s_miss = pd.Series([10, 20, None, 40, np.nan, 60])
print("Original:\n", s_miss)

print("\nIs null:\n", s_miss.isnull())
print("\nNumber of missing values:", s_miss.isnull().sum())
print("\nDrop NaN:\n", s_miss.dropna())
print("\nFill with 0:\n", s_miss.fillna(0))
print("\nForward fill:\n", s_miss.ffill())
Output:
Original:
 0    10.0
1    20.0
2     NaN
3    40.0
4     NaN
5    60.0
dtype: float64

Number of missing values: 2

Module 2: Important Notes & Tips
Series mein index unique hone chahiye (duplicate allowed lekin confusing hota hai)
.loc[] label-based hota hai, .iloc[] position-based
Arithmetic operations mein index align hota hai (NaN aa sakta hai)
describe() bahut useful hai quick summary ke liye
Hamesha vectorized operations use karo (loop mat chalaao)
Common Mistakes:
Index aur values ko confuse karna
None aur np.nan ko alag samajhna (dono missing value hain)
String index mein case-sensitive hota hai

Module 2 Complete! ✅
Ab bata:
Module 3: Pandas DataFrame padhna hai?
Bas likh de: "Module 3 padhao"
Ya koi doubt ho toh poochh pehle. Main wait kar raha hoon! 😊
ha
Haan bhai, bilkul! 🔥 Ab Module 3: Pandas DataFrame detail mein padhte hain. Yeh Pandas ka sabse important aur sabse zyada use hone wala part hai.
Module 3: Pandas DataFrame (2D Table)
3.1 DataFrame Kya Hai?
Explanation: DataFrame ek 2-dimensional labelled data structure hai.
Rows aur Columns dono ke naam hote hain
Excel sheet ya SQL table jaisa dikhta hai
Har column ek Series hota hai
Real-world data analysis ka main backbone
3.2 DataFrame Kaise Banate Hain? (Different Ways)
Example 1: Dictionary of Lists se (Sabse Common)
import pandas as pd

data = {
    'Name': ['Jyoti', 'Rahul', 'Priya', 'Aman'],
    'Age': [22, 25, 23, 24],
    'City': ['Lucknow', 'Kanpur', 'Varanasi', 'Agra'],
    'Marks': [85, 78, 92, 65]
}

df = pd.DataFrame(data)
print(df)
Output:
Name  Age       City  Marks
0   Jyoti   22    Lucknow     85
1   Rahul   25     Kanpur     78
2   Priya   23  Varanasi     92
3    Aman   24       Agra     65
Example 2: List of Dictionaries se
data2 = [
    {'Name': 'Jyoti', 'Age': 22, 'City': 'Lucknow'},
    {'Name': 'Rahul', 'Age': 25, 'City': 'Kanpur'},
    {'Name': 'Priya', 'Age': 23, 'City': 'Varanasi'}
]

df2 = pd.DataFrame(data2)
print(df2)
Output:
Name  Age       City
0   Jyoti   22    Lucknow
1   Rahul   25     Kanpur
2   Priya   23  Varanasi
Example 3: NumPy Array se
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

df3 = pd.DataFrame(arr, columns=['A', 'B', 'C'])
print(df3)
Output:
A  B  C
0  1  2  3
1  4  5  6
2  7  8  9
Example 4: Empty DataFrame + Columns
df_empty = pd.DataFrame(columns=['Name', 'Age', 'City'])
print(df_empty)
3.3 DataFrame ke Important Attributes & Methods
print("Shape (rows, columns):", df.shape)
print("Columns:", df.columns.tolist())
print("Index:", df.index.tolist())
print("Data Types:\n", df.dtypes)
print("\nMemory Usage:\n", df.memory_usage(deep=True))
Output:
Shape (rows, columns): (4, 4)
Columns: ['Name', 'Age', 'City', 'Marks']
Data Types:
 Name      object
Age        int64
City      object
Marks      int64
dtype: object
Quick Summary Methods:
print("First 2 rows:\n", df.head(2))
print("\nLast 2 rows:\n", df.tail(2))
print("\nRandom 1 row:\n", df.sample(1))
print("\nBasic Info:")
df.info()
print("\nStatistical Summary:\n", df.describe())
df.info() Output (important):
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Name    4 non-null      object
 1   Age     4 non-null      int64 
 2   City    4 non-null      object
 3   Marks   4 non-null      int64 
dtypes: int64(2), object(2)
memory usage: 260.0+ bytes
df.describe() Output:
Age      Marks
count   4.000000   4.000000
mean   23.500000  80.000000
std     1.290994  11.401754
min    22.000000  65.000000
25%    22.750000  74.250000
50%    23.500000  81.500000
75%    24.250000  86.750000
max    25.000000  92.000000
3.4 Column aur Row Selection
# Single Column
print("Single Column:\n", df['Name'])

# Multiple Columns
print("\nMultiple Columns:\n", df[['Name', 'Marks']])


# Single Row using iloc (position based)
print("\nRow 1 using iloc:\n", df.iloc[1])
Output Example:
Single Column:
0    Jyoti
1    Rahul
2    Priya
3     Aman
Name: Name, dtype: object
3.5 Basic Data Manipulation (Intro)
# New Column add karna
df['Grade'] = ['A', 'B', 'A', 'C']
print("After adding Grade column:\n", df)

# Column delete karna
df = df.drop('City', axis=1)   # axis=1 means column
print("\nAfter dropping City:\n", df)

# Rename Column
df = df.rename(columns={'Marks': 'Score'})
print("\nAfter renaming:\n", df)

Module 3: Important Notes
Har column ek Series hota hai
df.shape → (rows, columns) hota hai
df.info() → data quality check ke liye sabse best
df.describe() → sirf numerical columns pe kaam karta hai
Column names case-sensitive hote hain
Hamesha copy() use karo agar original data change nahi karna chahte
Common Mistakes:
df['new_col'] = value karte waqt length match nahi karna
drop() ke baad assignment bhool jaana (df = df.drop(...))
head() aur tail() ke bina badi file dekhna

Module 3 Complete! ✅
Ab bata bhai:
Module 4: Indexing & Selection padhna hai?
Bas likh: "Module 4 padhao"
Ya koi doubt ho Module 1, 2 ya 3 mein toh abhi poochh sakta hai.
Ready ho toh bol! 😊
ha
Haan bhai, bilkul! 🔥 Ab Module 4: Indexing & Selection detail mein padhte hain. Yeh module bahut important hai kyunki iske baad hi tum real data se sahi tareeke se cheezein nikaal paoge.
Module 4: Indexing & Selection
4.1 Pandas Mein Indexing Ke 3 Main Tarike
Method	Kaise Use Karte Hain	Kis Basis Pe Kaam Karta Hai	Best For
[]	df['col']	Column name	Simple column selection
.loc[]	df.loc[row, col]	Label (naam) based	Label se row/column
.iloc[]	df.iloc[row_pos, col_pos]	Position (index number) based	Position se row/column
4.2 Practical Examples (Same DataFrame use kar rahe hain)
Pehle ek clean DataFrame bana lete hain:
import pandas as pd

data = {
    'Name': ['Jyoti', 'Rahul', 'Priya', 'Aman', 'Sneha'],
    'Age': [22, 25, 23, 24, 21],
    'City': ['Lucknow', 'Kanpur', 'Varanasi', 'Agra', 'Delhi'],
    'Marks': [85, 78, 92, 65, 88],
    'Grade': ['A', 'B', 'A', 'C', 'A']
}

df = pd.DataFrame(data)
df.index = ['S1', 'S2', 'S3', 'S4', 'S5']   # Custom row labels
print(df)
Output:
Name  Age       City  Marks Grade
S1   Jyoti   22    Lucknow     85     A
S2   Rahul   25     Kanpur     78     B
S3   Priya   23  Varanasi     92     A
S4    Aman   24       Agra     65     C
S5   Sneha   21      Delhi     88     A
4.3 Column Selection
# 1. Single Column
print("Single Column:\n", df['Name'])

# 2. Multiple Columns
print("\nMultiple Columns:\n", df[['Name', 'Marks', 'Grade']])

# 3. Single Column as DataFrame (double brackets)
print("\nSingle Column as DataFrame:\n", df[['Marks']])
4.4 Row Selection using .loc[] (Label-based)
print("Single Row (S3):\n", df.loc['S3'])

print("\nMultiple Rows:\n", df.loc[['S1', 'S3', 'S5']])

print("\nRows S2 to S4 (inclusive):\n", df.loc['S2':'S4'])

# Row + Column combination
print("\nS3 ki Name aur Marks:\n", df.loc['S3', ['Name', 'Marks']])

# All rows but selected columns
print("\nAll rows, only Name & Grade:\n", df.loc[:, ['Name', 'Grade']])
4.5 Row Selection using .iloc[] (Position-based)
print("First Row (position 0):\n", df.iloc[0])

print("\nRows 1 to 3 (position):\n", df.iloc[1:4])   # 4 exclusive

print("\nLast 2 Rows:\n", df.iloc[-2:])

# Position se row + column
print("\nRow 2, Column 0 and 3:\n", df.iloc[2, [0, 3]])
4.6 Boolean Indexing (Filtering) – Sabse Powerful
# Condition 1: Age > 23
print("Age > 23:\n", df[df['Age'] > 23])

# Condition 2: Marks >= 85 aur Grade = 'A'
print("\nMarks >= 85 and Grade A:\n", 
      df[(df['Marks'] >= 85) & (df['Grade'] == 'A')])

# Condition 3: City in ['Lucknow', 'Delhi']
print("\nCity Lucknow or Delhi:\n", 
      df[df['City'].isin(['Lucknow', 'Delhi'])])
Output Example (ek filter ka):
Name  Age    City  Marks Grade
S1   Jyoti   22 Lucknow     85     A
S3   Priya   23 Varanasi     92     A
S5   Sneha   21    Delhi     88     A
4.7 Advanced Selection
# .at[] → Fast single value (label)
print("S3 ki Marks:", df.at['S3', 'Marks'])

# .iat[] → Fast single value (position)
print("Row 0, Column 3:", df.iat[0, 3])

# Query method (string based filtering)
print("\nUsing query:\n", df.query("Age > 22 and Marks > 70"))
4.8 Setting & Resetting Index
# Set column as index
df_set = df.set_index('Name')
print("After setting Name as index:\n", df_set.head(2))

# Reset indexv
df_reset = df_set.reset_index()
print("\nAfter reset_index:\n", df_reset.head(2))

Module 4: Important Notes & Best Practices
.loc[] → Labels (naam) use karta hai → inclusive slicing
.iloc[] → Positions (0,1,2...) use karta hai → exclusive slicing
Multiple conditions ke liye & (and), (or), ~ (not) use karo aur har condition ko () mein rakho
Boolean indexing mein & aur Python ke and/or se alag hain
.query() method bahut clean aur readable hota hai complex filters ke liye
Hamesha original DataFrame ko change karne se pehle .copy() bana lo
Common Mistakes Beginners Karte Hain:
df['Age' > 23] galat (bracket missing)
and / or use karna ki jagah & / use karna bhool jaana
.loc aur .iloc ko confuse karna
Slicing mein inclusive/exclusive bhool jaana

Module 4 Complete! ✅
Ab bata bhai:
Module 5: Data Manipulation padhna hai?
Bas likh de: "Module 5 padhao"
Ya koi doubt ho Module 4 mein toh abhi clear kar lo.
Main wait kar raha hoon! 😊
5.4s
ha
Haan bhai, bilkul! 🔥 Ab Module 5: Data Manipulation detail mein padhte hain. Yeh module bahut practical hai kyunki yahan hum DataFrame ko asli tarike se badalte, add karte, delete karte aur modify karte hain.
Module 5: Data Manipulation
5.1 Pehle Ek Clean DataFrame Le Lo (Practice Ke Liye)
import pandas as pd

data = {
    'Name': ['Jyoti', 'Rahul', 'Priya', 'Aman', 'Sneha'],
    'Age': [22, 25, 23, 24, 21],
    'City': ['Lucknow', 'Kanpur', 'Varanasi', 'Agra', 'Delhi'],
    'Marks': [85, 78, 92, 65, 88],
    'Grade': ['A', 'B', 'A', 'C', 'A']
}

df = pd.DataFrame(data)
print("Original DataFrame:\n")
print(df)
Output:
Name  Age       City  Marks Grade
0   Jyoti   22    Lucknow     85     A
1   Rahul   25     Kanpur     78     B
2   Priya   23  Varanasi     92     A
3    Aman   24       Agra     65     C
4   Sneha   21      Delhi     88     A
5.2 Adding New Column
# 1. Single value se (sab mein same value)
df['School'] = 'ABC Public School'
print("After adding School column:\n", df)

# 2. List se (har row ke liye alag value)
df['Passed'] = [True, True, True, False, True]
print("\nAfter adding Passed column:\n", df)

# 3. Existing columns se naya column (calculation)
df['Marks_Percent'] = (df['Marks'] / 100) * 100   # simple example
df['Age_Group'] = pd.cut(df['Age'], bins=[0, 22, 25, 30], labels=['Young', 'Adult', 'Senior'])
print("\nAfter adding calculated columns:\n", df[['Name', 'Marks', 'Marks_Percent', 'Age_Group']])
5.3 Deleting Columns aur Rows
# Column delete karna
df = df.drop('School', axis=1)                    # axis=1 = column
print("After dropping 'School' column:\n", df.columns.tolist())

# Multiple columns drop
df = df.drop(['Passed', 'Marks_Percent'], axis=1)
print("\nAfter dropping multiple columns:\n", df.columns.tolist())

# Row delete karna (index se)
df = df.drop([2, 4])          # Priya aur Sneha ko delete
print("\nAfter dropping rows 2 and 4:\n", df)
5.4 Renaming Columns aur Index
df = df.rename(columns={
    'Marks': 'Score',
    'City': 'Location'
})

df = df.rename(index={0: 'Student1', 1: 'Student2', 3: 'Student3'})
print("After renaming:\n", df)
5.5 Modifying Existing Data
# 1. Single value change
df.loc['Student1', 'Score'] = 90
print("After changing Jyoti's score:\n", df)

# 2. Multiple values using condition
df.loc[df['Score'] < 70, 'Grade'] = 'D'
print("\nAfter updating Grade for low scorers:\n", df)

# 3. Column ka pura data change
df['Location'] = df['Location'].str.upper()
print("\nAfter making city names uppercase:\n", df)
5.6 Adding New Rows
# Method 1: pd.concat() (Recommended)
new_student = pd.DataFrame({
    'Name': ['Rohan'],
    'Age': [26],
    'Location': ['NOIDA'],
    'Score': [87],
    'Grade': ['A']
})

df = pd.concat([df, new_student], ignore_index=True)
print("After adding new row:\n", df)
Note: ignore_index=True purane index ko reset kar deta hai.
5.7 Changing Data Types (astype)
print("Before:\n", df.dtypes)

df['Age'] = df['Age'].astype('int8')        # memory save ke liye
df['Score'] = df['Score'].astype('float64')

print("\nAfter changing dtypes:\n", df.dtypes)
5.8 Copy vs View (Important Concept)
# Safe tarika
df_copy = df.copy()          # Deep copy (original pe asar nahi padega)

# Galat tarika (View ban jata hai)
df_view = df                # Yeh sirf reference hai

df_copy.loc[0, 'Name'] = 'Jyoti Sharma'
print("Original df Name:", df.loc[0, 'Name'])        # change nahi hoga
print("Copy df Name:", df_copy.loc[0, 'Name'])       # change ho jayega

Module 5: Important Notes & Best Practices
Hamesha df = df.drop(...) ya df = df.rename(...) karo, warna change temporary rahega
axis=0 → rows, axis=1 → columns
pd.concat() rows add karne ke liye best hai
pd.cut() categorical columns banane ke liye bahut useful
Memory optimization ke liye astype('int8'), astype('category') use karo jab possible ho
String operations ke liye .str accessor use karo (jaise .str.upper())
Common Mistakes:
drop() karne ke baad df = likhna bhool jaana
Index reset na karna jab rows add/delete karte ho
Original DataFrame pe direct changes karna (copy banao)
Data type sahi se na set karna (object dtype zyada memory leta hai)

Module 5 Complete! ✅
Ab bata bhai:
Module 6: Handling Missing Data padhna hai?
Bas likh de: "Module 6 padhao"
Koi doubt ho Module 5 mein toh abhi bata do. Main ready hoon! 😊
3.7s
ha
Thought for 7s
Haan bhai, bilkul! 🔥 Ab Module 6: Handling Missing Data detail mein padhte hain. Yeh module bahut important hai kyunki real-world data mein 20-30% tak missing values (NaN) hote hain. Pandas isko bahut aasani se handle karta hai.
Module 6: Handling Missing Data (NaN Values)
6.1 Missing Data Kya Hai aur Kyun Problem Hai?
Explanation:
Pandas mein missing value ko NaN (Not a Number) kehte hain.
Yeh None, np.nan ya empty cell se aata hai.
Agar hum isko handle nahi karenge toh calculations (mean, sum) galat ho sakte hain.
Real projects mein missing data clean karna pehla step hota hai.
6.2 Pehle Ek DataFrame with Missing Values Bana Le
import pandas as pd
import numpy as np

data = {
    'Name': ['Jyoti', 'Rahul', 'Priya', 'Aman', 'Sneha', 'Rohan'],
    'Age': [22, np.nan, 23, 24, np.nan, 26],
    'City': ['Lucknow', 'Kanpur', np.nan, 'Agra', 'Delhi', np.nan],
    'Marks': [85, 78, np.nan, 65, 88, np.nan],
    'Grade': ['A', 'B', 'A', np.nan, 'A', 'B']
}

df = pd.DataFrame(data)
print("Original DataFrame with NaN:\n")
print(df)
Output:
Name   Age       City  Marks Grade
0   Jyoti  22.0    Lucknow   85.0     A
1   Rahul   NaN     Kanpur   78.0     B
2   Priya  23.0        NaN    NaN     A
3    Aman  24.0       Agra   65.0   NaN
4   Sneha   NaN      Delhi   88.0     A
5   Rohan  26.0        NaN    NaN     B
6.3 Detecting Missing Values
print("1. isnull() / isna():\n", df.isnull())

print("\n2. Column-wise missing count:\n", df.isnull().sum())

print("\n3. Total missing values in whole DataFrame:", df.isnull().sum().sum())

print("\n4. Percentage of missing values:\n", 
      (df.isnull().sum() / len(df) * 100).round(2))
Output (important parts):
Column-wise missing count:
Name     0
Age      2
City     2
Marks    2
Grade    1
dtype: int64

Total missing values: 7

Percentage:
Age     33.33
City    33.33
Marks   33.33
Grade   16.67
6.4 Dropping Missing Values (dropna)
# 1. Drop rows jisme koi bhi NaN ho
df_drop_row = df.dropna()
print("After dropna() (rows):\n", df_drop_row)

# 2. Drop columns jisme NaN ho
df_drop_col = df.dropna(axis=1)
print("\nAfter dropna(axis=1) (columns):\n", df_drop_col.columns.tolist())

# 3. Threshold (kam se kam 4 non-null values hone chahiye)
df_thresh = df.dropna(thresh=4)
print("\nAfter thresh=4:\n", df_thresh)
6.5 Filling Missing Values (fillna)
# 1. Fixed value se fill
df_fill = df.fillna(0)
print("Fill with 0:\n", df_fill[['Age', 'Marks']])

# 2. Column-wise different value
df_fill2 = df.fillna({'Age': 20, 'Marks': 70, 'City': 'Unknown'})
print("\nColumn-wise fill:\n", df_fill2)

# 3. Forward Fill (previous value se)
df_ffill = df.fillna(method='ffill')
print("\nForward Fill (ffill):\n", df_ffill)

# 4. Backward Fill (next value se)
df_bfill = df.fillna(method='bfill')
print("\nBackward Fill (bfill):\n", df_bfill)

# 5. Mean / Median se fill (numerical columns ke liye best)
df_mean = df.copy()
df_mean['Age'] = df_mean['Age'].fillna(df_mean['Age'].mean())
df_mean['Marks'] = df_mean['Marks'].fillna(df_mean['Marks'].mean())
print("\nMean Fill:\n", df_mean[['Age', 'Marks']])
6.6 Advanced Methods
# 1. Interpolate (linear method - values ke beech mein guess)
df_interp = df.copy()
df_interp['Age'] = df_interp['Age'].interpolate()
print("Interpolate on Age:\n", df_interp['Age'])

# 2. Replace specific value
df_replace = df.replace({'Grade': {np.nan: 'Missing'}})
print("\nReplace NaN in Grade:\n", df_replace['Grade'])
6.7 Best Practice Workflow (Real Projects Mein)
# Ek saath sab check aur clean
print("Missing before:\n", df.isnull().sum())

# Strategy:
# 1. Numerical → mean/median
# 2. Categorical → mode ya 'Unknown'
# 3. Agar bahut zyada missing ho toh drop

df_clean = df.copy()
df_clean['Age'] = df_clean['Age'].fillna(df_clean['Age'].median())
df_clean['Marks'] = df_clean['Marks'].fillna(df_clean['Marks'].mean())
df_clean['City'] = df_clean['City'].fillna('Unknown')
df_clean['Grade'] = df_clean['Grade'].fillna(df_clean['Grade'].mode()[0])

print("\nAfter cleaning:\n", df_clean)
print("\nMissing after cleaning:", df_clean.isnull().sum().sum())

Module 6: Important Notes & Best Practices
isnull() aur isna() dono same kaam karte hain
dropna() se pehle hamesha df.isnull().sum() check karo
Numerical columns ke liye mean/median, categorical ke liye mode ya 'Unknown' best
method='ffill' ya bfill time-series data ke liye bahut useful
interpolate() continuous data (jaise temperature, sales) ke liye accha hai
Hamesha .copy() bana ke clean karo, original data safe rakho
Common Mistakes:
dropna() karne ke baad df = likhna bhool jaana
Saare columns mein same value fill karna (galat hota hai)
fillna(0) ko har jagah use karna (kabhi-kabhi galat interpretation deta hai)
mode()[0] bhool jaana (mode series return karta hai)

Module 6 Complete! ✅
Ab bata bhai:
Module 7: Data Cleaning & Transformation padhna hai?
Bas likh de: "Module 7 padhao"
Koi doubt ho Module 6 mein (dropna, fillna, etc.) toh abhi poochh lo. Main ready hoon! 😊
6s
ha
Haan bhai, bilkul! 🔥 Ab Module 7: Data Cleaning & Transformation detail mein padhte hain. Yeh module real-life data ke liye sabse zyada important hai kyunki raw data hamesha messy hota hai (extra spaces, case issues, wrong format, duplicates etc.).
Module 7: Data Cleaning & Transformation
7.1 Pehle Messy DataFrame Le Lo (Real Example)
import pandas as pd
import numpy as np

data = {
    'Name': [' jyoti ', 'Rahul', 'Priya ', 'Aman', 'sneha', 'Rohan', 'Jyoti'],
    'Age': [22, 25, 23, 24, 21, 26, 22],
    'City': ['Lucknow', 'kanpur', 'Varanasi', 'Agra', 'delhi', 'Noida', 'Lucknow'],
    'Marks': [85, 78, 92, 65, 88, 87, 85],
    'Grade': ['A', 'B', 'A', 'C', 'A', 'B', 'A'],
    'Join_Date': ['2023-01-15', '2023-02-20', None, '2023-03-10', '2023/04/05', '2023-05-12', '2023-01-15']
}

df = pd.DataFrame(data)
print("Original Messy DataFrame:\n")
print(df)
Output:
Name  Age      City  Marks Grade   Join_Date
0   jyoti    22   Lucknow     85     A  2023-01-15
1    Rahul   25    kanpur     78     B  2023-02-20
2   Priya    23  Varanasi     92     A         NaN
3     Aman   24      Agra     65     C  2023-03-10
4    sneha   21     delhi     88     A  2023/04/05
5    Rohan   26     Noida     87     B  2023-05-12
6    Jyoti   22   Lucknow     85     A  2023-01-15
7.2 String Cleaning (.str Accessor)
# 1. Remove extra spaces
df['Name'] = df['Name'].str.strip()

# 2. Convert to Title Case (First letter capital)
df['Name'] = df['Name'].str.title()

# 3. City ko consistent case mein
df['City'] = df['City'].str.title()

print("After String Cleaning:\n")
print(df[['Name', 'City']])
Output:
Name       City
0    Jyoti    Lucknow
1    Rahul     Kanpur
2    Priya  Varanasi
3     Aman       Agra
4    Sneha      Delhi
5    Rohan      Noida
6    Jyoti    Lucknow
7.3 Removing Duplicates (drop_duplicates)
print("Before removing duplicates, shape:", df.shape)

# Remove duplicate rows (based on all columns)
df = df.drop_duplicates()

# Agar specific columns pe duplicate check karna ho
# df = df.drop_duplicates(subset=['Name', 'City'])

print("After removing duplicates, shape:", df.shape)
print("\nData after duplicate removal:\n", df)
7.4 Handling Date Column (Very Important)
# Convert string to proper datetime
df['Join_Date'] = pd.to_datetime(df['Join_Date'], errors='coerce')

print("After converting to datetime:\n")
print(df[['Name', 'Join_Date']])
print("\nData Types after conversion:\n", df.dtypes)
Output:
Name  Join_Date
0       Jyoti 2023-01-15
1       Rahul 2023-02-20
...
Data Types:
Join_Date    datetime64[ns]
7.5 Value Counts & Unique Values
print("Unique Cities:", df['City'].unique())
print("\nValue Counts of Grade:\n", df['Grade'].value_counts())
print("\nValue Counts of City:\n", df['City'].value_counts())
7.6 Sorting Data
# Sort by Marks (descending)
df_sorted = df.sort_values(by='Marks', ascending=False)
print("Top 3 students by Marks:\n", df_sorted.head(3))

# Sort by multiple columns
df_sorted2 = df.sort_values(by=['City', 'Marks'], ascending=[True, False])
print("\nSorted by City then Marks:\n", df_sorted2[['Name', 'City', 'Marks']])
7.7 Ranking
df['Rank'] = df['Marks'].rank(ascending=False, method='min')
print("With Rank column:\n", df[['Name', 'Marks', 'Rank']])
7.8 Categorical Data Handling
# Grade ko category type mein convert (memory efficient)
df['Grade'] = df['Grade'].astype('category')

print("Grade as category:\n", df['Grade'])
print("\nCategories:", df['Grade'].cat.categories)
7.9 Replacing Specific Values
# Example: City name change
df['City'] = df['City'].replace({'Kanpur': 'Kanpur Nagar'})

# Multiple replacements
df['Grade'] = df['Grade'].replace({'A': 'Excellent', 'B': 'Good'})

Module 7: Important Notes & Best Practices
Hamesha .str accessor use karo string operations ke liye (strip(), title(), upper(), lower(), contains() etc.)
pd.to_datetime() mein errors='coerce' rakho taaki galat date NaN ban jaye
drop_duplicates() karne se pehle subset parameter check karo
sort_values() mein inplace=True mat use karo (future versions mein remove ho sakta hai). Hamesha df = df.sort_values(...) karo
value_counts() analysis ke liye bahut powerful hai
astype('category') categorical columns (jaise Grade, Gender, City) ke liye memory bachata hai
Cleaning steps ka order important hai:
1.Strip spaces
2.Case correction
3.Duplicates remove
4.Data type conversion
5.Date handling
Common Mistakes:
.str bhool jaana aur direct string methods use karna
pd.to_datetime() ke baad format na specify karna (mixed formats mein)
Duplicates remove karte waqt subset na dena
Original data pe direct cleaning karna (copy banao)

Module 7 Complete! ✅
Ab bata bhai:
Module 8: Grouping & Aggregation (GroupBy) padhna hai? (Yeh bahut powerful module hai – jaise SQL GROUP BY)
Bas likh de: "Module 8 padhao"
Koi doubt ho Module 7 mein (string cleaning, datetime, duplicates etc.) toh abhi poochh lo.
Main ready hoon! 😊
4.2s
Executed code
ha
Haan bhai, bilkul! 🔥 Ab Module 8: Grouping & Aggregation (GroupBy) detail mein padhte hain. Yeh Pandas ka sabse powerful aur real-world mein sabse jyada use hone wala module hai. Jaise SQL ka GROUP BY hota hai, waise hi yeh hai.
Module 8: Grouping & Aggregation (GroupBy)
8.1 GroupBy Kya Hai?
Explanation: GroupBy data ko kisi category ke hisaab se group karta hai aur phir har group pe calculation (sum, mean, count etc.) karta hai. Example: Department-wise average salary, City-wise total marks, Grade-wise student count.
8.2 Pehle Ek Realistic Dataset Bana Le
import pandas as pd
import numpy as np

data = {
    'Student': ['Jyoti', 'Rahul', 'Priya', 'Aman', 'Sneha', 'Rohan', 'Neha', 'Vikas'],
    'Department': ['IT', 'HR', 'IT', 'Marketing', 'IT', 'HR', 'Marketing', 'IT'],
    'City': ['Lucknow', 'Kanpur', 'Lucknow', 'Agra', 'Delhi', 'Kanpur', 'Agra', 'Lucknow'],
    'Salary': [65000, 48000, 72000, 55000, 68000, 52000, 60000, 75000],
    'Experience': [3, 5, 4, 2, 6, 7, 3, 5],
    'Bonus': [5000, 3000, 6000, 4000, 5500, 3500, 4500, 7000]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n")
print(df)
Output:
Student Department      City  Salary  Experience  Bonus
0    Jyoti         IT   Lucknow   65000           3   5000
1    Rahul         HR    Kanpur   48000           5   3000
2    Priya         IT   Lucknow   72000           4   6000
3     Aman  Marketing      Agra   55000           2   4000
4    Sneha         IT     Delhi   68000           6   5500
5    Rohan         HR    Kanpur   52000           7   3500
6     Neha  Marketing      Agra   60000           3   4500
7    Vikas         IT   Lucknow   75000           5   7000
8.3 Basic GroupBy
# 1. Simple GroupBy + mean
print("Department wise Average Salary:\n")
print(df.groupby('Department')['Salary'].mean())

# 2. GroupBy + sum
print("\nDepartment wise Total Bonus:\n")
print(df.groupby('Department')['Bonus'].sum())
Output:
Department wise Average Salary:
Department
HR           50000.0
IT           70000.0
Marketing    57500.0
Name: Salary, dtype: float64

Department wise Total Bonus:
Department
HR           6500
IT          23500
Marketing    8500
Name: Bonus, dtype: int64
8.4 Multiple Aggregations (agg)
# Multiple functions ek saath
result = df.groupby('Department').agg({
    'Salary': ['mean', 'sum', 'max', 'min'],
    'Experience': ['mean', 'count'],
    'Bonus': 'sum'
})

print("Multiple Aggregations:\n")
print(result)
Output (clear aur powerful):
Salary                    Experience       Bonus
                    mean      sum    max    min       mean count   sum
Department                                                             
HR              50000.0    100000  52000  48000       6.0     2  6500
IT              70000.0   280000  75000  65000       4.5     4 23500
Marketing       57500.0   115000  60000  55000       2.5     2  8500
8.5 GroupBy with Multiple Columns
# Department + City wise analysis
multi_group = df.groupby(['Department', 'City']).agg({
    'Salary': 'mean',
    'Bonus': 'sum',
    'Student': 'count'
}).round(0)

print("Department & City wise Analysis:\n")
print(multi_group)
8.6 Important GroupBy Methods
# 1. size() - har group mein kitne records hain
print("Group Size:\n", df.groupby('Department').size())

# 2. count() - non-null values
print("\nCount of non-null values:\n", df.groupby('Department').count())

# 3. first() / last()
print("\nFirst row of each group:\n", df.groupby('Department').first())

# 4. nth() - nth row of each group
print("\nSecond highest salary in each department:\n", 
      df.groupby('Department')['Salary'].nth(1))
8.7 transform() vs agg() vs apply()
# agg() → group level summary (result chhota hota hai)
# transform() → har row ko group ka result deta hai (size same rahta hai)

df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
df['Salary_Diff'] = df['Salary'] - df['Dept_Avg_Salary']

print("After transform():\n")
print(df[['Student', 'Department', 'Salary', 'Dept_Avg_Salary', 'Salary_Diff']])
8.8 Filtering Groups
# Sirf un departments ko dikhao jinka average salary 60000 se zyada ho
filtered = df.groupby('Department').filter(lambda x: x['Salary'].mean() > 60000)
print("Departments with avg salary > 60000:\n", filtered)
8.9 Custom Function with apply()
def performance(x):
    return pd.Series({
        'Avg_Salary': x['Salary'].mean(),
        'Total_Employees': x['Student'].count(),
        'High_Earners': (x['Salary'] > 70000).sum()
    })

print("Custom Performance Analysis:\n")
print(df.groupby('Department').apply(performance))

Module 8: Important Notes & Best Practices
groupby() ke baad hamesha aggregation function lagao (mean, sum, count, agg etc.)
agg() sabse flexible hai – multiple columns + multiple functions
transform() tab use karo jab har row mein group ka result chahiye
Multiple columns group karne ke liye list pass karo: groupby(['col1', 'col2'])
filter() groups ko condition ke hisaab se rakhta hai
Large data mein groupby bahut fast hota hai
Common Mistakes:
groupby ke baad direct print karna (aggregation bhool jaana)
mean() ke jagah avg() likhna (galat hai)
transform() aur agg() ko confuse karna
Numerical columns pe string functions lagana

Module 8 Complete! ✅
Ab bata bhai:
Module 9: Merging, Joining & Concatenation padhna hai?
Bas likh de: "Module 9 padhao"
Koi doubt ho GroupBy mein (agg, transform, filter etc.) toh abhi poochh lo. Main yahin hoon! 😊
Chalo, next module ready kar raha hoon...
6.5s
ha
Haan bhai, bilkul! 🔥 Ab Module 9: Merging, Joining & Concatenation detail mein padhte hain. Yeh module bahut powerful hai kyunki real projects mein data aksar alag-alag files ya tables se aata hai. Isme hum do ya zyada DataFrames ko jodte hain (jaise Excel mein VLOOKUP + multiple sheets).
Module 9: Merging, Joining & Concatenation
9.1 Pehle Do Datasets Bana Le (Real Scenario)
import pandas as pd

# Employee Details Table (Left Table)
employee = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Jyoti', 'Rahul', 'Priya', 'Aman', 'Sneha', 'Rohan'],
    'Department': ['IT', 'HR', 'IT', 'Marketing', 'IT', 'Finance'],
    'Salary': [65000, 48000, 72000, 55000, 68000, 52000]
})

# Department Details Table (Right Table)
department = pd.DataFrame({
    'Dept_ID': ['IT', 'HR', 'Marketing', 'Finance', 'Operations'],
    'Dept_Name': ['Information Technology', 'Human Resources', 'Marketing', 'Finance', 'Operations'],
    'Manager': ['Vikas', 'Neha', 'Suresh', 'Pooja', 'Ramesh'],
    'Location': ['Lucknow', 'Kanpur', 'Agra', 'Delhi', 'Noida']
})

print("Employee Table:\n", employee)
print("\nDepartment Table:\n", department)
Output (short):
Employee Table:
   Emp_ID    Name Department  Salary
0     101   Jyoti         IT   65000
1     102   Rahul         HR   48000
...
9.2 pd.concat() – Simple Stacking (Rows ya Columns jodna)
# 1. Rows mein jodna (Vertical Concat)
df1 = employee.iloc[:3]   # first 3 rows
df2 = employee.iloc[3:]   # remaining rows

concat_rows = pd.concat([df1, df2], ignore_index=True)
print("After concat rows:\n", concat_rows)

# 2. Columns mein jodna (Horizontal Concat) - Axis=1
concat_cols = pd.concat([employee[['Emp_ID', 'Name']], 
                         employee[['Department', 'Salary']]], axis=1)
print("\nAfter concat columns:\n", concat_cols)
Note: ignore_index=True purane index ko reset kar deta hai.
9.3 pd.merge() – Sabse Important (SQL JOIN jaisa)
# Basic Inner Merge (common column pe)
merged = pd.merge(employee, department, 
                  left_on='Department', 
                  right_on='Dept_ID', 
                  how='inner')

print("Inner Merge Result:\n")
print(merged)
Output:
Emp_ID   Name Department  Salary Dept_ID              Dept_Name Manager Location
0     101  Jyoti         IT   65000      IT  Information Technology   Vikas  Lucknow
1     103  Priya         IT   72000      IT  Information Technology   Vikas  Lucknow
...
9.4 Different Types of Joins (how parameter)
print("1. INNER JOIN (default):", len(pd.merge(employee, department, left_on='Department', right_on='Dept_ID', how='inner')))

print("\n2. LEFT JOIN (saari employees, matching departments):")
left_join = pd.merge(employee, department, left_on='Department', right_on='Dept_ID', how='left')
print(left_join[['Name', 'Department', 'Dept_Name', 'Manager']])

print("\n3. RIGHT JOIN:")
right_join = pd.merge(employee, department, left_on='Department', right_on='Dept_ID', how='right')

print("\n4. OUTER JOIN (saari rows dono taraf se):")
outer_join = pd.merge(employee, department, left_on='Department', right_on='Dept_ID', how='outer')
Summary of Joins:
Join Type	Matlab	Kitni rows aayengi
inner	Sirf common records	Kam
left	Saari left table + matching right	Employee jitni
right	Saari right table + matching left	Department jitni
outer	Saari records dono tables se (NaN bhi)	Sabse zyada
9.5 Additional Useful Parameters in merge()
# 1. Suffixes for duplicate column names
merged_suffix = pd.merge(employee, department, 
                         left_on='Department', 
                         right_on='Dept_ID', 
                         how='left',
                         suffixes=('_emp', '_dept'))

# 2. Merge on Index
employee.set_index('Department', inplace=True)
department.set_index('Dept_ID', inplace=True)

merged_index = employee.join(department, how='left')
print("\nUsing .join() on index:\n", merged_index.head())
9.6 Real-World Example (Multiple Merges)
# Agar teen tables hon toh step-by-step merge karo
# employees → departments → another table (projects etc.)

# Bonus: Indicator column (kaunsi rows kahan se aayi)
merged_with_indicator = pd.merge(employee, department, 
                                 left_on='Department', 
                                 right_on='Dept_ID', 
                                 how='outer',
                                 indicator=True)

print(merged_with_indicator['_merge'].value_counts())

Module 9: Important Notes & Best Practices
pd.merge() → SQL style join (sabse zyada use hota hai)
df.join() → mainly index pe join ke liye
pd.concat() → simple stacking (rows/columns) ke liye
Hamesha left_on aur right_on clearly specify karo jab column names alag hon
how='left' sabse common hai real projects mein (master table left rakho)
Duplicate columns se bachne ke liye suffixes=('_x', '_y') use karo
Merge ke baad NaN check zaroor karo (isnull().sum())
Common Mistakes:
Column names match na karna (left_on galat likhna)
how parameter bhool jaana (default inner hota hai)
Index reset na karna concat ke baad
Bahut bade data pe merge karte waqt memory issue (dhyan rakho)

Module 9 Complete! ✅
Ab bata bhai:
Module 10: Pivot Tables & Cross Tabulation padhna hai?
Bas likh de: "Module 10 padhao"
Koi doubt ho Module 9 mein (merge, join, concat, how='left' etc.) toh abhi poochh lo. Main yahin hoon!
Chalo, agla module bhi ready hai jab tu bolega... 😊
5.1s
ha
Haan bhai, bilkul! 🔥 Ab Module 10: Pivot Tables & Cross Tabulation detail mein padhte hain. Yeh module data analysis mein bahut powerful hai – jaise Excel ka Pivot Table hota hai, waise hi Pandas mein bhi hai, lekin code se aur zyada flexible.
Module 10: Pivot Tables & Cross Tabulation
10.1 Pehle Ek Realistic Sales Dataset Bana Le
import pandas as pd
import numpy as np

data = {
    'Date': pd.date_range('2025-01-01', periods=12),
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 
               'North', 'South', 'East', 'West'],
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile', 'Tablet', 
                'Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile', 'Tablet'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics',
                 'Electronics', 'Electronics', 'Electronics', 'Electronics',
                 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'Sales': [45000, 32000, 18000, 52000, 41000, 25000, 48000, 38000, 
              22000, 55000, 29000, 31000],
    'Units': [15, 40, 25, 18, 35, 30, 20, 28, 22, 16, 38, 27],
    'Discount': [5, 10, 8, 12, 7, 15, 6, 9, 11, 4, 13, 10]
}

df = pd.DataFrame(data)
print("Original Sales Data:\n")
print(df)
10.2 pivot_table() – Sabse Powerful Function
# 1. Basic Pivot Table: Region-wise Total Sales
pivot1 = pd.pivot_table(df, 
                        values='Sales', 
                        index='Region', 
                        aggfunc='sum')

print("Region-wise Total Sales:\n", pivot1)

# 2. Region aur Product wise analysis
pivot2 = pd.pivot_table(df, 
                        values='Sales', 
                        index='Region', 
                        columns='Product', 
                        aggfunc='sum',
                        fill_value=0)   # NaN ko 0 se replace

print("\nRegion x Product wise Sales:\n", pivot2)
Output Example:
Region x Product wise Sales:
Product   Laptop  Mobile  Tablet
Region                         
East       48000   29000   22000
North      45000   41000   22000
South      55000   32000   25000
West       52000   38000   31000
10.3 Multiple Aggregations aur Values
# Multiple values + multiple functions
pivot_multi = pd.pivot_table(df, 
                             values=['Sales', 'Units'], 
                             index='Region', 
                             columns='Product',
                             aggfunc={
                                 'Sales': ['sum', 'mean'],
                                 'Units': 'sum'
                             },
                             fill_value=0)

print("Advanced Pivot Table:\n")
print(pivot_multi.round(0))
10.4 Margins (Grand Total) Add Karna
pivot_margin = pd.pivot_table(df, 
                              values='Sales', 
                              index='Region', 
                              columns='Product',
                              aggfunc='sum',
                              margins=True,           # Grand Total
                              margins_name='Total')

print("Pivot with Grand Total:\n", pivot_margin)
10.5 pivot() vs pivot_table()
# pivot() → sirf reshaping (no aggregation)
# pivot_table() → reshaping + aggregation (recommended)

# Example of pivot (jab har combination unique ho)
try:
    simple_pivot = df.pivot(index='Date', columns='Product', values='Sales')
    print("Simple pivot:\n", simple_pivot.head())
except Exception as e:
    print("Error in pivot:", e)
10.6 crosstab() – Frequency Table (Cross Tabulation)
# Region vs Product kitni baar aaya
cross1 = pd.crosstab(df['Region'], df['Product'])
print("Cross Tabulation (Count):\n", cross1)

# With normalization (percentage)
cross2 = pd.crosstab(df['Region'], df['Product'], normalize='index') * 100
print("\nPercentage Cross Tab:\n", cross2.round(1))
Output:
Cross Tabulation (Count):
Product  Laptop  Mobile  Tablet
Region                        
East          1       1       1
North         1       1       1
...
10.7 melt() – Wide to Long Format (Unpivot)
# Pivot table ko wapas long format mein laana
long_format = pd.melt(pivot2.reset_index(), 
                      id_vars=['Region'], 
                      var_name='Product', 
                      value_name='Sales')

print("Melted Data (Long Format):\n", long_format)
10.8 stack() aur unstack()
# Multi-level pivot ko stack/unstack karna
stacked = pivot2.stack()
print("\nStacked:\n", stacked)

unstacked = stacked.unstack()
print("\nUnstacked back:\n", unstacked)

Module 10: Important Notes & Best Practices
pivot_table() sabse zyada use hota hai kyunki yeh aggregation support karta hai
aggfunc mein 'sum', 'mean', 'count', 'max', 'min', len etc. use kar sakte ho
fill_value=0 NaN ko 0 se replace karta hai (bahut useful)
margins=True grand total add karta hai
crosstab() frequency/count ke liye best hai (jaise contingency table)
melt() wide format se long format mein convert karta hai (plotting ke liye accha)
Complex analysis ke liye index aur columns dono mein multiple levels daal sakte ho
Common Mistakes:
pivot() aur pivot_table() confuse karna
NaN values ko handle na karna (fill_value bhool jaana)
Aggregation function galat choose karna
melt() ke parameters (id_vars, var_name, value_name) bhool jaana

Module 10 Complete! ✅
Ab bata bhai:
Module 11: Time Series Analysis padhna hai?
Bas likh de: "Module 11 padhao"
Koi doubt ho Module 10 mein (pivot_table, crosstab, melt etc.) toh abhi clear kar lo.
Main wait kar raha hoon! 😊 Next module bhi bahut interesting hai (dates, resampling, rolling windows).
6.1s
ha
Thought for 8s
Haan bhai, bilkul! 🔥 Ab Module 11: Time Series Analysis detail mein padhte hain. Yeh module stock price, sales data, weather, sensor data wagairah ke liye bahut important hai. Pandas time series ko bahut aasani se handle karta hai.
Module 11: Time Series Analysis
11.1 Pehle Ek Realistic Time Series Dataset Bana Le
import pandas as pd
import numpy as np

# Daily sales data for 1 month
dates = pd.date_range(start='2025-01-01', periods=31, freq='D')

data = {
    'Date': dates,
    'Sales': [45000, 48000, 52000, 41000, 39000, 55000, 62000, 47000, 51000, 58000,
              43000, 49000, 53000, 46000, 42000, 60000, 65000, 48000, 52000, 57000,
              44000, 50000, 54000, 47000, 45000, 61000, 63000, 49000, 53000, 59000, 46000],
    'Units_Sold': [120, 135, 140, 110, 105, 155, 170, 130, 145, 160,
                   115, 130, 150, 125, 115, 165, 180, 135, 145, 155,
                   120, 140, 150, 130, 125, 170, 175, 135, 148, 162, 128],
    'Discount': [5, 8, 10, 6, 7, 12, 15, 9, 11, 13, 4, 8, 10, 7, 5, 14, 16, 8, 9, 12,
                 6, 10, 11, 7, 8, 13, 14, 9, 10, 12, 5]
}

df = pd.DataFrame(data)
print("Original Time Series Data (first 5 rows):\n")
print(df.head())
Output:
Date  Sales  Units_Sold  Discount
0 2025-01-01  45000         120         5
1 2025-01-02  48000         135         8
2 2025-01-03  52000         140        10
3 2025-01-04  41000         110         6
4 2025-01-05  39000         105         7
11.2 DateTime Index Set Karna (Zaroori Step)
df = df.set_index('Date')          # Date ko index bana do
print("After setting Date as Index:\n")
print(df.head())

print("\nIndex type:", df.index.dtype)   # datetime64[ns]
11.3 pd.date_range() – Dates Generate Karna
# Daily, weekly, monthly, hourly dates
daily   = pd.date_range('2025-01-01', periods=10, freq='D')
weekly  = pd.date_range('2025-01-01', periods=5,  freq='W')
monthly = pd.date_range('2025-01-01', periods=6,  freq='ME')   # Month End
hourly  = pd.date_range('2025-01-01', periods=5,  freq='H')

print("Monthly dates:\n", monthly)
11.4 Resampling (Daily → Weekly/Monthly)
# Weekly total sales
weekly_sales = df['Sales'].resample('W').sum()
print("Weekly Total Sales:\n", weekly_sales)

# Monthly average sales
monthly_avg = df['Sales'].resample('ME').mean().round(0)
print("\nMonthly Average Sales:\n", monthly_avg)

# Custom aggregation
resampled = df.resample('W').agg({
    'Sales': 'sum',
    'Units_Sold': 'sum',
    'Discount': 'mean'
})
print("\nWeekly aggregated:\n", resampled)
11.5 Shifting & Lagging (Pichhle din ka data)
df['Prev_Day_Sales'] = df['Sales'].shift(1)          # 1 day pehle
df['Next_Day_Sales'] = df['Sales'].shift(-1)         # 1 din aage
df['7_Day_Lag']      = df['Sales'].shift(7)

print("After shifting:\n")
print(df[['Sales', 'Prev_Day_Sales', '7_Day_Lag']].head(10))
11.6 Rolling Window Operations (Moving Average)
# 7-day moving average
df['7_Day_MA'] = df['Sales'].rolling(window=7).mean().round(0)

# 7-day rolling sum
df['7_Day_Total'] = df['Sales'].rolling(window=7).sum()

# Rolling with min_periods
df['3_Day_MA_min3'] = df['Sales'].rolling(window=3, min_periods=3).mean()

print("Rolling Window Example (first 10 rows):\n")
print(df[['Sales', '7_Day_MA', '7_Day_Total']].head(10))
11.7 Time Zone Handling
# Add timezone
df_tz = df.copy()
df_tz.index = df_tz.index.tz_localize('Asia/Kolkata')
print("With India timezone:\n", df_tz.index)

# Convert to another timezone
df_tz_ny = df_tz.index.tz_convert('America/New_York')
11.8 Advanced: Resample + Rolling Combo
# Monthly average then 3-month rolling mean
monthly = df['Sales'].resample('ME').mean()
monthly_rolling = monthly.rolling(window=3).mean().round(0)

print("Monthly Sales + 3-month Rolling Average:\n", monthly_rolling)

Module 11: Important Notes & Best Practices
Hamesha Date ko index banao (set_index('Date')) – tabhi resample, shift, rolling kaam karega
freq options: 'D' (daily), 'W' (weekly), 'ME' (month end), 'H' (hourly), 'M' (month start) etc.
resample() aggregation ke liye hai (sum, mean, max etc.)
shift() lagging/leading ke liye best (forecasting mein bahut use hota hai)
rolling(window=7) moving average ke liye sabse common
min_periods use karo agar starting mein data kam ho
Timezone ke liye tz_localize() aur tz_convert() use karo
Large time series data mein freq='D' ya 'H' carefully choose karo
Common Mistakes:
Date column ko index na banana (resample nahi chalega)
shift(1) ke baad NaN values ko handle na karna
rolling() ke baad min_periods na dena (starting rows mein NaN)
Wrong frequency dena ('M' vs 'ME')

Module 11 Complete! ✅
Ab bata bhai:
Module 12: Applying Functions padhna hai?
Bas likh de: "Module 12 padhao"
Koi doubt ho Time Series mein (resample, rolling, shift etc.) toh abhi poochh lo.
Main ready hoon next module ke liye! 😊
6.5s
ha
Haan bhai, bilkul! 🔥 Ab Module 12: Applying Functions detail mein padhte hain. Yeh module bahut powerful hai kyunki isme hum apne custom logic ko har row, har column, ya poore DataFrame pe laga sakte hain.
Module 12: Applying Functions
12.1 Pehle Ek Dataset Le Lo
import pandas as pd
import numpy as np

data = {
    'Name': ['Jyoti', 'Rahul', 'Priya', 'Aman', 'Sneha', 'Rohan'],
    'Age': [22, 25, 23, 24, 21, 26],
    'Salary': [65000, 48000, 72000, 55000, 68000, 52000],
    'Department': ['IT', 'HR', 'IT', 'Marketing', 'IT', 'Finance'],
    'Marks': [85, 78, 92, 65, 88, 76]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n")
print(df)
12.2 apply() – Sabse Important
apply() axis ke hisaab se kaam karta hai:
axis=0 → Column-wise (default)
axis=1 → Row-wise
# 1. Column-wise apply (default)
print("Max of each column:\n", df.apply(max))

# 2. Row-wise apply
def total_income(row):
    return row['Salary'] + (row['Salary'] * 0.10)   # 10% bonus

df['Total_Income'] = df.apply(total_income, axis=1)
print("\nAfter row-wise apply:\n", df[['Name', 'Salary', 'Total_Income']])
12.3 Lambda Functions ke saath apply()
# Simple lambda
df['Age_Group'] = df['Age'].apply(lambda x: 'Young' if x <= 23 else 'Adult')

# Complex lambda
df['Performance'] = df.apply(lambda row: 
    'Excellent' if row['Marks'] >= 85 else 
    'Good' if row['Marks'] >= 75 else 'Average', axis=1)

print("\nAfter lambda apply:\n")
print(df[['Name', 'Age', 'Age_Group', 'Marks', 'Performance']])
12.4 map() – Sirf Series pe (Single Column)
# Dictionary mapping
grade_map = {85:'A', 78:'B', 92:'A+', 65:'C', 88:'A', 76:'B'}
df['Grade'] = df['Marks'].map(grade_map)

print("After map():\n", df[['Name', 'Marks', 'Grade']])
12.5 applymap() (purana) / map() on DataFrame (Naya tareeka)
# Saare DataFrame pe function (sirf numerical ya object pe)
df_numeric = df.select_dtypes(include='number')

# Example: har value ko 10% badhao
df_numeric = df_numeric.map(lambda x: x * 1.10)
print("After map on numeric columns:\n", df_numeric.round(0))
Note: Pandas 2.1+ mein applymap() ko map() se replace kar diya gaya hai DataFrame ke liye.
12.6 Custom Function Examples
# 1. Tax calculation
def calculate_tax(salary):
    if salary > 60000:
        return salary * 0.20
    elif salary > 40000:
        return salary * 0.15
    else:
        return salary * 0.10

df['Tax'] = df['Salary'].apply(calculate_tax)
df['Net_Salary'] = df['Salary'] - df['Tax']

print("\nTax & Net Salary:\n")
print(df[['Name', 'Salary', 'Tax', 'Net_Salary']].round(0))
# 2. Multiple columns pe custom logic
def performance_score(row):
    score = row['Marks'] * 0.6 + (row['Salary'] / 1000) * 0.4
    return round(score, 1)

df['Performance_Score'] = df.apply(performance_score, axis=1)
print("\nPerformance Score:\n", df[['Name', 'Marks', 'Salary', 'Performance_Score']])
12.7 Vectorized Operations (Sabse Fast)
# Best Practice: apply/map se pehle vectorized try karo

# Vectorized (bahut fast)
df['Bonus'] = df['Salary'] * 0.12
df['Age_Squared'] = df['Age'] ** 2

# apply se slow hota hai isliye avoid karo jab possible ho
12.8 When to Use What?
Function	Use Case	Speed	Axis Support
apply()	Row ya Column pe custom function	Medium	Yes
map()	Single Series (column) pe mapping	Fast	No
map() on DF	Poore DataFrame pe element-wise	Medium	No
Vectorized	Simple arithmetic / conditions	Fastest	Yes
Rule of Thumb: Pehle vectorized try karo → phir map() → last mein apply()

Module 12: Important Notes & Best Practices
apply(axis=1) row-wise hota hai – slow ho sakta hai badi files mein
Lambda functions simple cases ke liye best
map() dictionary ya function ke saath single column pe bahut fast hai
Complex logic ke liye custom function + apply() use karo
Hamesha vectorized operations (df['col'] * 2, df['col'] > 50) ko priority do – yeh sabse fast hai
apply() ko loop ki jagah mat samjho – yeh bhi internally loop chalaata hai
Common Mistakes:
Har jagah apply() use karna (vectorized bhool jaana)
axis=0 aur axis=1 confuse karna
map() ko DataFrame pe directly use karna (sirf Series pe kaam karta hai)
Lambda mein complex if-else likhte waqt syntax galat karna

Module 12 Complete! ✅
Ab bata bhai:
Module 13: File I/O Operations (Reading & Writing Files) padhna hai?
Yeh module bahut practical hai – CSV, Excel, JSON etc. padhna aur save karna sikhayega.
Bas likh de: "Module 13 padhao"
Koi doubt ho Module 12 mein (apply, map, lambda, vectorized) toh abhi poochh lo.
Main ready hoon! 😊
7.7s
ha
Thought for 14s
Haan bhai, bilkul! 🔥 Ab Module 13: File I/O Operations detail mein padhte hain. Yeh module bahut practical hai kyunki real projects mein data almost hamesha CSV, Excel, JSON, SQL ya database se aata hai. Is module mein hum seekhenge data padhna aur likhna dono.
Module 13: File I/O Operations
13.1 Reading Files (read_ functions)
Most Important: pd.read_csv() (sabse zyada use hota hai)
import pandas as pd

# 1. Basic CSV read
# df = pd.read_csv('data.csv')

# 2. Important Parameters (real projects mein zaroor use karo)
df = pd.read_csv('sales_data.csv', 
                 delimiter=',',           # ya '\t' for tab separated
                 header=0,                # pehli row header hai
                 names=None,              # agar custom column names dena ho
                 index_col=0,             # pehla column ko index bana do
                 usecols=['Date', 'Sales', 'Region'],  # sirf kuch columns padho
                 dtype={'Sales': 'float64', 'Region': 'category'},
                 parse_dates=['Date'],    # date columns ko datetime bana do
                 na_values=['NA', 'N/A', 'null'],  # custom missing values
                 skiprows=2,              # pehle 2 rows ignore karo
                 nrows=10000,             # sirf pehle 10000 rows padho
                 encoding='utf-8',        # Chinese/ Hindi data ke liye
                 chunksize=1000)          # badi file ke liye (loop mein padho)

# Example with real output simulation
print("After reading CSV with important params:")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Date dtype:", df['Date'].dtype)
Other Important Read Functions
# Excel file
# df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1', skiprows=1)

# JSON
# df_json = pd.read_json('data.json')

# HTML table (website se)
# df_html = pd.read_html('https://example.com/table')[0]

# SQL (database se)
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///mydb.db')
# df_sql = pd.read_sql('SELECT * FROM sales', engine)
13.2 Writing Files (to_ functions)
# 1. CSV mein save karna
df.to_csv('output_sales.csv', 
          index=False,           # index mat save karo
          header=True, 
          encoding='utf-8',
          mode='w',              # 'a' for append
          float_format='%.2f')   # decimal places

# 2. Excel mein save (multiple sheets bhi possible)
with pd.ExcelWriter('final_report.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sales_Data', index=False)
    df.describe().to_excel(writer, sheet_name='Summary')

# 3. JSON
df.to_json('output.json', orient='records')

# 4. Parquet (bahut fast aur compressed - big data ke liye best)
df.to_parquet('data.parquet', compression='snappy')
13.3 Handling Large Files (Chunksize)
# Agar file 10GB ki hai toh chunks mein padho
chunk_list = []
for chunk in pd.read_csv('huge_file.csv', chunksize=100000):
    # har chunk pe thoda processing
    chunk['New_Col'] = chunk['Sales'] * 1.1
    chunk_list.append(chunk)

# Saare chunks ko combine karo
df_large = pd.concat(chunk_list, ignore_index=True)
print("Large file processed successfully! Shape:", df_large.shape)
13.4 Common Real-World Examples
# 1. Clean CSV read (recommended template)
df = pd.read_csv('sales.csv',
                 parse_dates=['Order_Date'],
                 dtype={'Customer_ID': 'string', 'Quantity': 'int32'},
                 na_values=['?', 'N/A'])

# 2. Save with date format
df.to_csv('cleaned_sales.csv', index=False, date_format='%Y-%m-%d')

# 3. Read only specific sheet from Excel
# df = pd.read_excel('report.xlsx', sheet_name='Q1_Sales', usecols='A:D')
13.5 Quick Tips for Different Formats
CSV → sabse common, fast
Excel → read_excel / to_excel (multiple sheets ke liye ExcelWriter)
Parquet → big data ke liye best (size 10x chhota, speed 10x fast)
JSON → API data ke liye
SQL → database se direct connect

Module 13: Important Notes & Best Practices
Hamesha index=False rakho jab to_csv/to_excel karo (extra column nahi aayega)
Large files ke liye chunksize ya nrows use karo
parse_dates aur dtype specify karo → memory bach jaati hai aur speed badh jaati hai
Encoding 'utf-8' rakhna safe hai (Hindi/ special characters ke liye)
pd.read_csv ke 50+ parameters hain – important wale hi yaad rakho
Parquet/Feather format use karo jab data 100MB+ ho
to_csv karte waqt compression='gzip' laga sakte ho space bachane ke liye
Common Mistakes:
index=True chhod dena (extra unnamed column aa jaata hai)
Date columns ko string mein chhod dena (parse_dates bhool jaana)
Badi file ko ek baar mein padhna (memory error)
Sheet name galat dena Excel mein
Encoding galat hone se Hindi/ special characters garbage ban jaate hain

Module 13 Complete! ✅
Ab bata bhai:
Module 14: Advanced Topics padhna hai? (Issme MultiIndex, Memory Optimization, Styling, Big Data tips etc. aayenge)
Bas likh de: "Module 14 padhao"
Koi doubt ho Module 13 mein (read_csv parameters, chunksize, ExcelWriter etc.) toh abhi poochh lo.
Main ready hoon! 😊
7.5s
Executed code
ha
Haan bhai, bilkul! 🔥 Ab Module 14: Advanced Topics detail mein padhte hain. Yeh last technical module hai – yahan hum Pandas ko aur powerful aur efficient banayenge.
Module 14: Advanced Topics
14.1 MultiIndex / Hierarchical Indexing
import pandas as pd
import numpy as np

# MultiIndex DataFrame create karna
arrays = [
    ['IT', 'IT', 'HR', 'HR', 'Marketing', 'Marketing'],
    ['Senior', 'Junior', 'Senior', 'Junior', 'Senior', 'Junior']
]

index = pd.MultiIndex.from_arrays(arrays, names=['Department', 'Level'])

df_multi = pd.DataFrame({
    'Salary': [85000, 62000, 72000, 48000, 65000, 52000],
    'Bonus': [12000, 6000, 9000, 4000, 8000, 5000],
    'Experience': [7, 3, 5, 2, 4, 1]
}, index=index)

print("MultiIndex DataFrame:\n")
print(df_multi)
Output:
Salary  Bonus  Experience
Department  Level                                 
IT          Senior      85000  12000           7
            Junior      62000   6000           3
HR          Senior      72000   9000           5
            Junior      48000   4000           2
Marketing   Senior      65000   8000           4
            Junior      52000   5000           1
MultiIndex pe operations:
# 1. Specific level se access
print("\nIT Department only:\n", df_multi.loc['IT'])

# 2. Cross-section (xs)
print("\nAll Senior employees:\n", df_multi.xs('Senior', level='Level'))

# 3. Unstack (MultiIndex ko columns mein)
print("\nUnstacked:\n", df_multi.unstack())

# 4. Swap levels
print("\nSwap levels:\n", df_multi.swaplevel())
14.2 Memory Optimization (Bahut Important)
# Pehle memory check karo
print("Before optimization memory usage:")
print(df_multi.memory_usage(deep=True))

# Optimization techniques
df_opt = df_multi.copy()

# 1. Downcast numeric types
df_opt['Salary'] = pd.to_numeric(df_opt['Salary'], downcast='integer')
df_opt['Bonus'] = pd.to_numeric(df_opt['Bonus'], downcast='integer')

# 2. Categorical dtype (memory saver)
df_opt['Department'] = df_opt.index.get_level_values('Department').astype('category')
df_opt['Level'] = df_opt.index.get_level_values('Level').astype('category')

print("\nAfter optimization:")
print(df_opt.memory_usage(deep=True))
print("\nMemory saved significantly!")
14.3 Styling DataFrames (style)
# Beautiful output ke liye
styled = df_multi.style\
    .background_gradient(cmap='Blues', subset=['Salary'])\
    .format({'Salary': '₹{:,.0f}', 'Bonus': '₹{:,.0f}'})\
    .set_caption("Employee Salary Report")\
    .set_table_styles([{'selector': 'caption', 'props': [('font-size', '16px')]}])

# Jupyter mein yeh beautifully dikhega
# styled
14.4 Performance Tips (Speed Optimization)
# Galat tareeka (slow)
# for i in range(len(df)):
#     df.loc[i, 'New_Col'] = df.loc[i, 'Salary'] * 1.1

# Sahi tareeka (Vectorized - bahut fast)
df_multi['Total_Comp'] = df_multi['Salary'] + df_multi['Bonus']

# Apply ko minimize karo
# .map() aur vectorized operations ko priority do
14.5 Integration with Other Libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Pandas se direct plotting
df_multi['Salary'].plot(kind='bar', figsize=(10,6), title='Salary by Department & Level')
plt.show()

# Seaborn ke saath
sns.boxplot(data=df_multi.reset_index(), x='Department', y='Salary')
plt.title('Salary Distribution by Department')
plt.show()
14.6 Working with Big Data (Pandas Limitations)
Pandas Limitations: 1-2 GB RAM tak comfortably kaam karta hai
Solutions:
Dask (parallel Pandas)
Polars (bahut fast alternative)
Vaex
Modin
Quick Tip: Jab data 5GB+ ho toh Pandas ke bajaye Polars ya Dask consider karo.
14.7 Other Advanced Features
# 1. explode() - list wale columns ko rows mein convert
df_explode = pd.DataFrame({
    'Name': ['Jyoti', 'Rahul'],
    'Skills': [['Python', 'SQL', 'Pandas'], ['Java', 'Spring']]
})
print(df_explode.explode('Skills'))

# 2. query() method (SQL style filtering)
result = df_multi.query("Salary > 60000 and Experience >= 5")
print(result)

# 3. eval() for fast computation
df_multi.eval('Net_Salary = Salary + Bonus - (Salary * 0.1)', inplace=True)

Module 14: Important Notes & Summary
MultiIndex jab multiple grouping levels hon tab use karo
Memory Optimization real projects mein bahut jaruri hai (downcast + category dtype)
Styling reports banane ke liye accha hai
Vectorized operations hamesha apply() se better hain (speed ke liye)
Large data ke liye Pandas akela kaafi nahi – Dask/Polars seekh lo
query() aur eval() code ko clean aur fast banate hain
Common Mistakes:
Badi DataFrame pe apply() + loop chalaana
Memory usage check na karna
MultiIndex ko samajh na aane pe confuse hona
Styling ko production code mein daalna (sirf reporting ke liye)

Module 14 Complete! ✅
Ab hum Module 15 pe pahunch gaye hain – Real-World Projects & Best Practices
Bata bhai:
"Module 15 padhao"
Isme hum ek mini End-to-End Project karenge (EDA + Cleaning + Analysis + Insights) aur saare best practices cover karenge.
Ya phir agar tu kisi specific topic ko dubara detail mein dekhna chahta hai (jaise GroupBy, Merge, Time Series etc.) toh bata sakta hai.
Bol kya chahta hai ab? Module 15 shuru karein?
Main ready hoon! 😊
5.1s
ha
Haan bhai, bilkul! 🔥 Ab final module aa gaya!
Module 15: Real-World Projects & Best Practices
(End-to-End Pandas Workflow)
Yeh module sabse important hai kyunki yahan hum sirf theory nahi, balki real project karenge. Isme hum ek complete Sales Analysis Project step-by-step karenge.

Real-World Project: SuperStore Sales Analysis
Step 1: Project Overview
Hum ek e-commerce company ka sales data analyze karenge aur ye insights nikaalenge:
Total revenue, profit
Best performing region, category, product
Monthly/Yearly trends
Customer segmentation
Loss-making areas
Step 2: Loading the Data (Best Practice)
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Best way to read data
df = pd.read_csv('superstore_sales.csv', 
                 parse_dates=['Order_Date', 'Ship_Date'],
                 dtype={
                     'Order_ID': 'string',
                     'Customer_ID': 'string',
                     'Product_ID': 'string'
                 })

print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 3 rows preview:")
print(df.head(3))
Step 3: Initial Data Exploration (EDA)
# Basic info
print("=== Basic Information ===")
print("Shape:", df.shape)
print("\nInfo:")
df.info()

print("\nMissing Values (%):")
print((df.isnull().sum() / len(df) * 100).round(2))

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nNumerical Summary:")
print(df.describe().round(2))
Step 4: Data Cleaning (Complete Pipeline)
# 1. Copy bana lo (original safe rahe)
df_clean = df.copy()

# 2. Column names clean karo (spaces aur capital letters)
df_clean.columns = [col.strip().replace(' ', '_').lower() for col in df_clean.columns]

# 3. Handle missing values
df_clean['postal_code'] = df_clean['postal_code'].fillna('Unknown')
df_clean['ship_mode'] = df_clean['ship_mode'].fillna(df_clean['ship_mode'].mode()[0])

# 4. Create new useful columns
df_clean['year'] = df_clean['order_date'].dt.year
df_clean['month'] = df_clean['order_date'].dt.month_name()
df_clean['profit_margin'] = (df_clean['profit'] / df_clean['sales']) * 100
df_clean['order_month_year'] = df_clean['order_date'].dt.to_period('M')

print("Data Cleaning Completed!")
print("New Columns Added: year, month, profit_margin, order_month_year")
Step 5: Advanced Analysis using GroupBy + Pivot
# 1. Overall Business Metrics
total_sales = df_clean['sales'].sum()
total_profit = df_clean['profit'].sum()
profit_margin = (total_profit / total_sales) * 100

print(f"Total Sales     : ₹{total_sales:,.2f}")
print(f"Total Profit    : ₹{total_profit:,.2f}")
print(f"Overall Margin  : {profit_margin:.2f}%")

# 2. Top 5 Products by Sales
top_products = df_clean.groupby('product_name')['sales'].sum().nlargest(5)
print("\nTop 5 Products by Sales:\n", top_products)

# 3. Region-wise Performance
region_analysis = df_clean.groupby('region').agg({
    'sales': 'sum',
    'profit': 'sum',
    'profit_margin': 'mean',
    'order_id': 'nunique'
}).round(2)

print("\nRegion-wise Performance:\n", region_analysis)
Step 6: Time Series Analysis
# Monthly Sales Trend
monthly_trend = df_clean.groupby('order_month_year').agg({
    'sales': 'sum',
    'profit': 'sum'
}).reset_index()

monthly_trend['order_month_year'] = monthly_trend['order_month_year'].astype(str)

print("Monthly Sales Trend (first 6 months):")
print(monthly_trend.head(6))
Step 7: Pivot Table (Executive Report Style)
# Category vs Region vs Sales + Profit
report = pd.pivot_table(df_clean, 
                        values=['sales', 'profit'], 
                        index='category', 
                        columns='region',
                        aggfunc='sum',
                        margins=True)

print("Category vs Region Performance (Pivot Table):\n")
print(report.round(0))
Step 8: Final Insights & Recommendations (Real Output)
print("=== KEY BUSINESS INSIGHTS ===\n")

print("1. Highest Sales Region     :", region_analysis['sales'].idxmax())
print("2. Highest Profit Region    :", region_analysis['profit'].idxmax())
print("3. Most Profitable Category :", 
      df_clean.groupby('category')['profit'].sum().idxmax())

print("\n4. Loss Making Areas:")
loss_areas = df_clean[df_clean['profit'] < 0].groupby('sub_category')['profit'].sum().nsmallest(3)
print(loss_areas)

print("\n5. Recommendation:")
print("- Focus more on", df_clean.groupby('region')['profit_margin'].mean().idxmax(), "region")
print("- Improve", loss_areas.index[0], "sub-category")
Step 9: Best Practices Summary (Yaad rakhne wali baatein)
1.Hamesha .copy() banao pehle
2.Column names clean karo (lower(), strip())
3.Memory optimization karo (astype('category'), downcast)
4.Vectorized operations use karo (apply last option)
5.Date columns ko parse_dates se padho
6.Chaining use karo (readable code):
7.result = (df_clean
8.          .groupby('region')
9.          .agg({'sales':'sum'})
          .sort_values('sales', ascending=False))
10.Jupyter Notebook mein %timeit se performance check karo
11.Documentation add karo har step pe

Module 15 Complete! ✅
Pandas Complete Course Summary
Ab tumne pura syllabus cover kar liya hai:
Module 1 → Introduction & Setup
Module 2 → Series
Module 3 → DataFrame
Module 4 → Indexing & Selection
Module 5 → Data Manipulation
Module 6 → Missing Data
Module 7 → Data Cleaning
Module 8 → GroupBy & Aggregation
Module 9 → Merge, Join, Concat
Module 10 → Pivot & Crosstab
Module 11 → Time Series
Module 12 → Applying Functions
Module 13 → File I/O
Module 14 → Advanced Topics
Module 15 → Real Project & Best Practices
