# Sentiment Analysis and Insights Extraction

This repository contains a Python script for sentiment analysis and insights extraction from a list of reviews. The script uses the Hugging Face Transformers library for sentiment analysis, the YAKE keyword extraction library for extracting keywords, and includes logic for identifying positive aspects, negative aspects, and issues within the reviews.

## How to Use

### Dependencies

- Python 3.x
- Install required Python packages using the following command:

    ```bash
    pip install transformers yake
    ```

### Running the Code

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Open and run the `analyze_reviews.py` script:

    ```bash
    python analyze_reviews.py
    ```

3. View the results:

    The script will print the extracted positive aspects, negative aspects, and issues from the provided sample reviews.

## Code Explanation

The core functionality is provided by the `analyze_reviews.py` script. Here's a brief explanation:

- `analyze_sentiment(review)`: Uses the Hugging Face Transformers library to perform sentiment analysis on a given review.

- `extract_keywords(text, num_keywords=5)`: Utilizes the YAKE keyword extraction library to extract keywords from the text.

- `extract_issues(text)`: Identifies issues based on specific keywords in the provided text.

- `extract_insights(reviews)`: Iterates through a list of reviews, analyzes sentiment, and extracts positive aspects, negative aspects, and issues.

- Sample reviews and their results are provided in the script for testing.

## Customization

- You can customize the keyword extraction logic in the `extract_keywords` function by adjusting parameters or using a different library.
  
- Modify the issue extraction logic in the `extract_issues` function based on your specific requirements.

- Feel free to replace the sample reviews with your own dataset.

## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/)
- [YAKE Keyword Extraction](https://github.com/LIAAD/yake)

