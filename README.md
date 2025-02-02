**🏨 Hotel Review Sentiment Analysis 📊**

**📌 Project Overview**
This project analyzes hotel reviews using sentiment analysis to determine hotel rankings. By leveraging TextBlob for sentiment scoring, we compare calculated sentiment-based hotel scores with actual user ratings to uncover discrepancies and insights.

**🎯 Objectives**
📝 Process and clean hotel reviews to remove noise.
🔍 Perform sentiment analysis on positive and negative reviews.
📊 Compare sentiment-based hotel scores with actual user ratings.
📈 Visualize trends to understand customer satisfaction.

**🛠️ Technologies Used**
Python 🐍
Pandas & NumPy 📊
Matplotlib & Seaborn 📉
TextBlob 📝
Jupyter Notebook 📒

**🏗️ Data Processing Steps**
Cleaning the dataset 🧹

Removed missing and irrelevant data.
Standardized text formatting.

**Sentiment Analysis 💬**

Used TextBlob to assign polarity scores to reviews.
Calculated a Hotel Score (0-100 scale) based on sentiment.

**Data Visualization 📊**

Word clouds for positive & negative reviews.
Scatter plots comparing review scores vs. sentiment scores.
Correlation heatmaps to analyze rating consistency.

**📉 Key Findings**
🔹 Sentiment-based scores correlate (0.70) with actual review scores but have discrepancies due to sarcasm and nuanced language.
🔹 Customers sometimes leave negative reviews but rate hotels highly, affecting score accuracy.
🔹 More advanced NLP models (e.g., deep learning) could improve sentiment precision.

**🔥 Future Improvements**
🤖 Use advanced sentiment models like BERT or Vader for better accuracy.
🏷️ Topic modeling to categorize common review themes.
⏳ Analyze sentiment trends over time to detect service improvements or declines.

**📂 Project Structure**
📁 Hotel_Review_Sentiment_Analysis  
 ├── 📜 data/hotelreviews.csv (Original set)  
 ├── 📜 notebooks/data_cleaning.ipynb  
 ├── 📜 notebooks/sentiment_analysis.ipynb  
 ├── 📜 notebooks/visualization.ipynb  
 ├── 📜 reports/hotel_sentiment_results.csv  
 ├── 📜 README.md  


**🚀 How to Run**

1. Clone the repository:
```
git clone https://github.com/yourusername/hotel-sentiment-analysis.git
cd hotel-sentiment-analysis
```

3. Install dependencies:
```
pip install -r requirements.txt
```

5. Run the Jupyter notebooks to explore the data! 📊

📜 License
This project is open-source and free to use under the MIT License.

