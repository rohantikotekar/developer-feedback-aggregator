# Overview
1. The Developer Feedback Aggregator is a Flask web application designed to help developers analyze feedback from GitHub repositories. 
2. By using the GitHub API, this application fetches issues, pull requests, and commits from a specified repository, 
3. It cleans the data, and performs sentiment analysis on the feedback provided by users and contributors. 
4.  The insights generated can help developers understand user sentiment, prioritize improvements, and enhance overall productivity.
5.  The deployed application can be found here:  https://defag-app-final-3f5e97a27639.herokuapp.com/

# Feature
1. Input GitHub Repository URL: Users provide the URL of the GitHub repository they want to analyze.
2. Fetch Data: The application extracts the repository owner and name from the URL and fetches relevant data using the GitHub API.
3. Clean Data: The fetched data is processed to remove unnecessary content, making it suitable for analysis.
4. Perform Sentiment Analysis: The cleaned data undergoes sentiment analysis to categorize feedback into positive, negative, and neutral sentiments.
5. Generate Summary: The application generates a summary of the sentiment analysis, providing insights into user feedback.


# Installation 
1. git clone https://github.com/rohantikotekar/developer-feedback-aggregator.git
2. cd developer-feedback-aggregator
3. python -m venv venv
4. source venv/bin/activate
5. pip install Flask requests textblob
6. python app.py


# Benefits for Developers
#### - Enhanced Understanding: <br> Gain insights into user sentiment regarding your project, helping you understand what users appreciate and what issues they face.
#### - Prioritization of Improvements: <br> Identify areas that require immediate attention based on user feedback, allowing you to prioritize development efforts effectively.
#### - Informed Decision-Making: <br> Use the generated insights to make data-driven decisions about feature enhancements, bug fixes, and overall project direction.

# Contributions
#### - Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.


