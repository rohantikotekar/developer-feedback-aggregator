# Overview
#### - The Developer Feedback Aggregator is a Flask web application designed to help developers analyze feedback from GitHub repositories. 
#### - By leveraging the GitHub API, this application fetches issues, pull requests, and commits from a specified repository, 
#### - It Cleans the data, and performs sentiment analysis on the feedback provided by users and contributors. 
#### - The insights generated can help developers understand user sentiment, prioritize improvements, and enhance overall productivity.

# Features
#### - Input GitHub Repository URL: Users provide the URL of the GitHub repository they want to analyze.
#### - Fetch Data: The application extracts the repository owner and name from the URL and fetches relevant data using the GitHub API.
#### - Clean Data: The fetched data is processed to remove unnecessary content, making it suitable for analysis.
#### - Perform Sentiment Analysis: The cleaned data undergoes sentiment analysis to categorize feedback into positive, negative, and neutral sentiments.
#### - Generate Summary: The application generates a summary of the sentiment analysis, providing insights into user feedback.

# Installation 
#### - git clone https://github.com/yourusername/developer-feedback-aggregator.git
#### - cd developer-feedback-aggregator
#### - python -m venv venv
#### - source venv/bin/activate  # On Windows use `venv\Scripts\activate`
#### - pip install Flask requests textblob
#### - pip install Flask requests textblob
#### - python app.py

# Benefits for Developers
#### - Enhanced Understanding: Gain insights into user sentiment regarding your project, helping you understand what users appreciate and what issues they face.
#### - Prioritization of Improvements: Identify areas that require immediate attention based on user feedback, allowing you to prioritize development efforts effectively.
#### - Informed Decision-Making: Use the generated insights to make data-driven decisions about feature enhancements, bug fixes, and overall project direction.

# Contributions
#### - Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.


