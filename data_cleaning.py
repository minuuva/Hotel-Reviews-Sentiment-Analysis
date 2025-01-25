import pandas as pd
import re

data = pd.read_csv('hotelreviews.csv')
columns = data.columns

# COLUMNS = 'Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date','Average_Score', 'Hotel_Name', 'Reviewer_Nationality',
# 'Negative_Review', 'Review_Total_Negative_Word_Counts', 'Total_Number_of_Reviews', 'Positive_Review', 'Review_Total_Positive_Word_Counts',
# 'Total_Number_of_Reviews_Reviewer_Has_Given', 'Reviewer_Score', 'Tags', 'days_since_review', 'lat', 'lng'

# Handling Incomplete Data
columns_to_drop = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Total_Number_of_Reviews_Reviewer_Has_Given', 'days_since_review', 'lat', 'lng']
data = data.drop(columns = columns_to_drop)
# Removed all rows with missing reviews
data = data[~((data['Negative_Review'] == 'No Negative') | (data['Positive_Review'] == 'No Positive'))]

# Counting the number of rows for each hotel and only keeping hotels with 1000+ rows of data / dropping duplicates, NAs
hotel_counts = data['Hotel_Name'].value_counts()
hotels_to_keep = hotel_counts[hotel_counts >= 1000].index
filtered_data = data[data['Hotel_Name'].isin(hotels_to_keep)]
filtered_data = filtered_data.dropna().drop_duplicates()


# Removing rows with irrelevant placeholders
placeholders = ["Nothing", "Other"]
filtered_data = filtered_data[~filtered_data['Negative_Review'].isin(placeholders)]
filtered_data = filtered_data[~filtered_data['Positive_Review'].isin(placeholders)]


# Function to remove excessive whitespace and special characters
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()

filtered_data[['Positive_Review', 'Negative_Review']] = filtered_data[['Positive_Review', 'Negative_Review']].applymap(clean_text)

# Changing all text to lowercase for consistency
filtered_data[['Positive_Review', 'Negative_Review']] = filtered_data[['Positive_Review', 'Negative_Review']].applymap(str.lower)

# Exporting cleaned dataset
filtered_data.to_csv('cleaned_hotelreviews.csv', index=False)
