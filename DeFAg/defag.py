import requests
import re
from textblob import TextBlob

def get_repo_details(github_url):  # Extracting repo details
    pattern = r"https?://github\.com/(?P<owner>[\w-]+)/(?P<repo>[\w-]+)"
    match = re.match(pattern, github_url)
    if not match:
        raise ValueError(f"Invalid GitHub URL: {github_url}. Please provide a valid repository URL.")
    
    return match.group('owner'), match.group('repo')

def fetch_github_data(owner, repo, token=None):  # Using GitHub API to fetch details
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"token {token}"

    responses = {}
    urls = {
        "issues": f"https://api.github.com/repos/{owner}/{repo}/issues",
        "pulls": f"https://api.github.com/repos/{owner}/{repo}/pulls",
        "commits": f"https://api.github.com/repos/{owner}/{repo}/commits"
    }

    for key, url in urls.items():
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            responses[key] = response.json()
        else:
            print(f"Error fetching {key}: {response.status_code} - {response.text}")
            responses[key] = []

    return responses

def clean_text(text):  # Remove unwanted characters from the text
    if not text:
        return ""
    text = re.sub(r"<.*?>", "", text) 
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  
    return text.strip()

def preprocess_github_data(data):
    cleaned_data = {}
    for key, items in data.items():
        if isinstance(items, list):
            cleaned_data[key] = [clean_text(item.get("body", "")) for item in items if "body" in item]
    return cleaned_data

def basic_sentiment_analysis(data):  # Sentiment analysis
    sentiments = {
        "positive": [],
        "negative": [],
        "neutral": []
    }

    for key, items in data.items():
        if isinstance(items, list):
            for item in items:
                cleaned_item = clean_text(item)
                if cleaned_item:
                    polarity = TextBlob(cleaned_item).sentiment.polarity
                    if polarity > 0:
                        sentiments["positive"].append(item)
                    elif polarity < 0:
                        sentiments["negative"].append(item)
                    else:
                        sentiments["neutral"].append(item)

    return sentiments

def generate_sentiment_summary(sentiments):  # Generate sentiment summary
    positive_count = len(sentiments["positive"])
    negative_count = len(sentiments["negative"])
    neutral_count = len(sentiments["neutral"])
    total = positive_count + negative_count + neutral_count

    sentiment_summary = (
        f"Sentiment Analysis Summary:\n"
        f"Positive Sentiments: {positive_count} entries\n"
        f"Negative Sentiments: {negative_count} entries\n"
        f"Neutral Sentiments: {neutral_count} entries\n"
    )

    if total > 0:
        if positive_count >= 0.5 * total:
            sentiment_summary += "Insight: Users and contributors appreciate your work. Consider further enhancing the highly appreciated features or documentation.\n"
        elif negative_count >= 0.5 * total:
            sentiment_summary += "Insight: Many users and contributors are raising concerns. Prioritize addressing recurring issues to improve the user experience.\n"
        else:
            sentiment_summary += "Insight: The feedback is balanced. While some users are happy, some concerns have been raised. Focus on addressing the negative feedback while maintaining what users like about the project.\n"

    return sentiment_summary

if __name__ == "__main__":
    github_url = input("Enter the GitHub repository URL: ").strip()
    token = ""  # Add your GitHub token here if needed for authentication

    try:
        owner, repo = get_repo_details(github_url)
        print(f"Fetching data for repository: {owner}/{repo}...")
        raw_data = fetch_github_data(owner, repo, token)

        cleaned_data = preprocess_github_data(raw_data)

        if cleaned_data:
            print("Data successfully retrieved and cleaned. Performing sentiment analysis...")
            sentiment_data = basic_sentiment_analysis(cleaned_data)
            sentiment_summary = generate_sentiment_summary(sentiment_data)
            print(sentiment_summary)
        else:
            print("No valid cleaned data to analyze.")
        
    except Exception as e:
        print(f"Error: {e}")