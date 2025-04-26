import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Sample dataset (replace with full dataset from CSV if needed)
data = {
    'text': [
        'The economy is doing great according to experts.',
        'Breaking: Celebrity found dead in their apartment!',
        'NASA confirms moon landing was faked.',
        'Local team wins championship after a thrilling game.',
        'Aliens have landed in New York City.'
    ],
    'label': [0, 0, 1, 0, 1]  # 0 = Real, 1 = Fake
}

df = pd.DataFrame(data)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Create TF-IDF + Naive Bayes pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('nb', MultinomialNB())
])

# Train the model
pipeline.fit(X_train, y_train)

# Evaluate (optional)
accuracy = pipeline.score(X_test, y_test)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Save the model
joblib.dump(pipeline, 'model/fake_news_model.pkl')

print("Model saved successfully.")
