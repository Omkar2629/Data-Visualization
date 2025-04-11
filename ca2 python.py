Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:\\Users\\omkar\\Desktop\\railway.csv")
print(df)
                Transaction ID Date of Purchase  ... Reason for Delay Refund Request
0      da8a6ba8-b3dc-4677-b176       08-12-2023  ...              NaN             No
1      b0cdd1b0-f214-4197-be53       16-12-2023  ...   Signal Failure             No
2      f3ba7a96-f713-40d9-9629       19-12-2023  ...              NaN             No
3      b2471f11-4fe7-4c87-8ab4       20-12-2023  ...              NaN             No
4      2be00b45-0762-485e-a7a3       27-12-2023  ...              NaN             No
...                        ...              ...  ...              ...            ...
31648                      NaN              NaN  ...              NaN            NaN
31649                      NaN              NaN  ...              NaN            NaN
31650                      NaN              NaN  ...              NaN            NaN
31651                      NaN              NaN  ...              NaN            NaN
31652                      NaN              NaN  ...              NaN            NaN

[31653 rows x 18 columns]
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
print(df)
                transaction_id date_of_purchase  ... reason_for_delay refund_request
0      da8a6ba8-b3dc-4677-b176       08-12-2023  ...              NaN             No
1      b0cdd1b0-f214-4197-be53       16-12-2023  ...   Signal Failure             No
2      f3ba7a96-f713-40d9-9629       19-12-2023  ...              NaN             No
3      b2471f11-4fe7-4c87-8ab4       20-12-2023  ...              NaN             No
4      2be00b45-0762-485e-a7a3       27-12-2023  ...              NaN             No
...                        ...              ...  ...              ...            ...
31648                      NaN              NaN  ...              NaN            NaN
31649                      NaN              NaN  ...              NaN            NaN
31650                      NaN              NaN  ...              NaN            NaN
31651                      NaN              NaN  ...              NaN            NaN
31652                      NaN              NaN  ...              NaN            NaN

[31653 rows x 18 columns]
df.drop_duplicates(inplace=True)
print(df)
               transaction_id date_of_purchase  ... reason_for_delay refund_request
0     da8a6ba8-b3dc-4677-b176       08-12-2023  ...              NaN             No
1     b0cdd1b0-f214-4197-be53       16-12-2023  ...   Signal Failure             No
2     f3ba7a96-f713-40d9-9629       19-12-2023  ...              NaN             No
3     b2471f11-4fe7-4c87-8ab4       20-12-2023  ...              NaN             No
4     2be00b45-0762-485e-a7a3       27-12-2023  ...              NaN             No
...                       ...              ...  ...              ...            ...
3291  56d9ec44-caa4-4dde-bc12       13-01-2024  ...              NaN             No
3292  12fb9b5c-d44c-474b-b767       13-01-2024  ...              NaN             No
3293  3dfaadac-68b2-4079-b544       13-01-2024  ...              NaN             No
3294  2d118801-5256-49de-a3b0       13-01-2024  ...              NaN             No
3295                      NaN              NaN  ...              NaN            NaN

[3296 rows x 18 columns]
df['reason for delay'] = df['reason_for_delay'].fillna('None')
print(df)
               transaction_id date_of_purchase  ... refund_request reason for delay
0     da8a6ba8-b3dc-4677-b176       08-12-2023  ...             No             None
1     b0cdd1b0-f214-4197-be53       16-12-2023  ...             No   Signal Failure
2     f3ba7a96-f713-40d9-9629       19-12-2023  ...             No             None
3     b2471f11-4fe7-4c87-8ab4       20-12-2023  ...             No             None
4     2be00b45-0762-485e-a7a3       27-12-2023  ...             No             None
...                       ...              ...  ...            ...              ...
3291  56d9ec44-caa4-4dde-bc12       13-01-2024  ...             No             None
3292  12fb9b5c-d44c-474b-b767       13-01-2024  ...             No             None
3293  3dfaadac-68b2-4079-b544       13-01-2024  ...             No             None
3294  2d118801-5256-49de-a3b0       13-01-2024  ...             No             None
3295                      NaN              NaN  ...            NaN             None

[3296 rows x 19 columns]
plt.figure(figsize=(8,5))
<Figure size 800x500 with 0 Axes>
sns.countplot(x="purhcase_type", data=df)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    sns.countplot(x="purhcase_type", data=df)
  File "C:\Users\omkar\AppData\Local\Programs\Python\Python313\Lib\site-packages\seaborn\categorical.py", line 2631, in countplot
    p = _CategoricalAggPlotter(
  File "C:\Users\omkar\AppData\Local\Programs\Python\Python313\Lib\site-packages\seaborn\categorical.py", line 67, in __init__
    super().__init__(data=data, variables=variables)
  File "C:\Users\omkar\AppData\Local\Programs\Python\Python313\Lib\site-packages\seaborn\_base.py", line 634, in __init__
    self.assign_variables(data, variables)
  File "C:\Users\omkar\AppData\Local\Programs\Python\Python313\Lib\site-packages\seaborn\_base.py", line 679, in assign_variables
    plot_data = PlotData(data, variables)
  File "C:\Users\omkar\AppData\Local\Programs\Python\Python313\Lib\site-packages\seaborn\_core\data.py", line 58, in __init__
    frame, names, ids = self._assign_variables(data, variables)
  File "C:\Users\omkar\AppData\Local\Programs\Python\Python313\Lib\site-packages\seaborn\_core\data.py", line 232, in _assign_variables
    raise ValueError(err)
ValueError: Could not interpret value `purhcase_type` for `x`. An entry with this name does not appear in `data`.
sns.countplot(x="purchase_type", data=df)
<Axes: xlabel='purchase_type', ylabel='count'>
plt.title("Ticket Purchase Type distribution")
Text(0.5, 1.0, 'Ticket Purchase Type distribution')
plt.xlabel("Purchase Type")
Text(0.5, 0, 'Purchase Type')
plt.ylabel("Count")
Text(0, 0.5, 'Count')
plt.show()
plt.figure(figsize=(8,5))
<Figure size 800x500 with 0 Axes>
sns.countplot(x="ticket_class", data=df)
<Axes: xlabel='ticket_class', ylabel='count'>
plt.title("Ticket Class Distribution")
Text(0.5, 1.0, 'Ticket Class Distribution')
plt.xlabel("Ticket Class")
Text(0.5, 0, 'Ticket Class')
plt.ylabel("Count")
Text(0, 0.5, 'Count')
plt.show()
plt.figure(figsize=(8,5))
<Figure size 800x500 with 0 Axes>
sns.histplot(df['price'], bins=30, kde=True)
<Axes: xlabel='price', ylabel='Count'>
plt.title("Price distribution")
Text(0.5, 1.0, 'Price distribution')
plt.xlabel("Price")
Text(0.5, 0, 'Price')
plt.ylabel("Frequency")
Text(0, 0.5, 'Frequency')
plt.show()
plt.figure(figsize=(10,5))
<Figure size 1000x500 with 0 Axes>
sns.boxplot(x="ticket_type", y="price", data=df)
<Axes: xlabel='ticket_type', ylabel='price'>
plt.title("Ticket price by ticket type")
Text(0.5, 1.0, 'Ticket price by ticket type')
plt.xlabel("Ticket type")
Text(0.5, 0, 'Ticket type')
plt.ylabel("Price")
Text(0, 0.5, 'Price')
plt.show()
plt.figure(figsize=(8,5))
<Figure size 800x500 with 0 Axes>
avg_price = df.groupby('purchase_type')['price'].mean().sort_values()
sns.barplot(x=avg_price.index, y=avg_price.values)
<Axes: xlabel='purchase_type'>
>>> plt.title("Average ticket price by purchase type")
Text(0.5, 1.0, 'Average ticket price by purchase type')
>>> plt.xlabel("Purchase type")
Text(0.5, 0, 'Purchase type')
>>> plt.ylabel("Average Price")
Text(0, 0.5, 'Average Price')
>>> plt.show()
>>> plt.figure(figsize=(10,6))
<Figure size 1000x600 with 0 Axes>
>>> sns.scatterplot(x="time_of_purchase", y="price", hue="purchase_type", data=df)
<Axes: xlabel='time_of_purchase', ylabel='price'>
>>> plt.title("Ticket price // time of purchase")
Text(0.5, 1.0, 'Ticket price // time of purchase')
>>> plt.xlabel("Time of purchase")
Text(0.5, 0, 'Time of purchase')
>>> plt.ylabel("Price")
Text(0, 0.5, 'Price')
>>> plt.legend(title="Pruchase type")
<matplotlib.legend.Legend object at 0x000001C9C80139D0>
>>> plt.show()
>>> plt.figure(figsize=(8,6))
<Figure size 800x600 with 0 Axes>
>>> numeric_df = df.select_dtypes(include=['float64', 'int64'])
>>> correlation = numeric_df.corr()
>>> sns.heatmap(correlation, annot=True, cmap='coolwarm', linewidths=0.5)
<Axes: >
>>> plt.title("Correlation Heatmap")
Text(0.5, 1.0, 'Correlation Heatmap')
>>> plt.show()
>>> plt.figure(figsize=(10,8))
<Figure size 1000x800 with 0 Axes>
>>> sns.heatmap(correlation, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5, square=True)
<Axes: >
>>> plt.title("Correlation Heatmap")
Text(0.5, 1.0, 'Correlation Heatmap')
>>> plt.show()
>>> df['date_of_journey'] = pd.to_datetime(df['date_of_journey'], errors='coerce')
>>> avg_price_daily = df.groupby('date_of_journey')['price'].mean()
>>> plt.figure(figsize=(10,6))
<Figure size 1000x600 with 0 Axes>
>>> avg_price_daily.plot(kind='line', marker='o', linestyle='-')
<Axes: xlabel='date_of_journey'>
>>> plt.title("Average ticket price over time")
Text(0.5, 1.0, 'Average ticket price over time')
>>> plt.slabel("Date of journey")
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    plt.slabel("Date of journey")
AttributeError: module 'matplotlib.pyplot' has no attribute 'slabel'. Did you mean: 'clabel'?
>>> plt.xlabel("Date of journey")
Text(0.5, 0, 'Date of journey')
>>> plt.ylabel("Average Price")
Text(0, 0.5, 'Average Price')
>>> plt.show()
