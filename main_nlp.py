from transformers import pipeline
import yake

def analyze_sentiment(review):
    sentiment_analyzer = pipeline("sentiment-analysis")
    result = sentiment_analyzer(review)
    return result[0]

def extract_keywords(text, num_keywords=5):
    
    custom_kw_extractor = yake.KeywordExtractor(lan="en", n=num_keywords, dedupLim=0.9, top=5, features=None)
    keywords = [kw for kw, score in custom_kw_extractor.extract_keywords(text)]
    return keywords

def extract_issues(text):
    
    issues = []
    if "bug" in text.lower():
        issues.append("bug")
    if "problem" in text.lower():
        issues.append("problem")
    if "issue" in text.lower():
        issues.append("issue")
    return issues

def extract_insights(reviews):
    positive_aspects = set()
    negative_aspects = set()
    issues = set()

    for review in reviews:
        sentiment_result = analyze_sentiment(review)
        sentiment = sentiment_result['label']
        score = sentiment_result['score']

        if sentiment == 'POSITIVE':
            
            positive_aspects.update(extract_keywords(review))
        elif sentiment == 'NEGATIVE':
            
            negative_aspects.update(extract_keywords(review))
            issues.update(extract_issues(review))

    return list(positive_aspects), list(negative_aspects), list(issues)


reviews = [
    "I love this product! It's amazing!",
    "The quality is top-notch, but the price is too high.",
    "The instructions are unclear and confusing.",
    "Great features, but it crashes frequently.",
    "Not satisfied with the customer service.",
    "Excellent product, worth every penny!",
    "The design is sleek and modern, but the battery life is disappointing.",
    "Easy to use and setup, but lacks some advanced features.",
    "Disappointed with the shipping time. It took longer than expected.",
    "This product exceeded my expectations. Highly recommended!",
    "The customer support team was helpful and resolved my issue promptly.",
    "The user interface is intuitive, making it user-friendly.",
    "Received a damaged product. Poor packaging.",
    "The price is reasonable considering the features it offers.",
    "I encountered a software bug that needs immediate attention.",
    "The sound quality is excellent, but the device heats up quickly.",
    "The product is durable and built to last. Impressed with the build quality.",
    "Terrible experience with the return process. It was a hassle.",
    "Average product. Nothing extraordinary, but it gets the job done.",
    "The user manual is comprehensive and easy to follow.",
    "Not recommended. Numerous issues with functionality.",
    "The product arrived earlier than expected. Pleasant surprise!",
    "The interface is outdated and could use a modern redesign.",
    "Fantastic customer service. They went above and beyond to assist me.",
    "The product is versatile and can be used for various applications.",
    "Not happy with the performance. Laggy and slow.",
    "Great value for the money. Affordable and high-quality.",
    "The product is a game-changer. I can't imagine life without it.",
    "The packaging was eco-friendly, which is a plus for me.",
    "Too many unnecessary features. It complicates the user experience.",
    "Responsive touchscreen, but the battery drains quickly.",
]


positive_aspects, negative_aspects, issues = extract_insights(reviews)


print("Positive Aspects:", positive_aspects)
print("Negative Aspects:", negative_aspects)
print("Issues:", issues)
