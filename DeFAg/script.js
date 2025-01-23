function fetchData() {
    const repoUrl = document.getElementById("repo-url").value.trim();
    const resultElement = document.getElementById("sentiment-summary");

    if (!repoUrl) {
        alert("Please enter a GitHub repository URL.");
        return;
    }

    async function fetchSentimentSummary() {
        try {
           
            const response = await fetch(`http://localhost:5000/sentiment-summary?repo-url=${encodeURIComponent(repoUrl)}`);
            if (response.ok) {
                const data = await response.json();
                resultElement.textContent = data.sentiment_summary;
            } else {
                resultElement.textContent = "Error fetching sentiment summary.";
            }
        } catch (error) {
            resultElement.textContent = "An error occurred while fetching the sentiment summary.";
        }
    }
    
    fetchSentimentSummary();
}
