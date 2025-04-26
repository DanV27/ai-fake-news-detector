from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os
from newspaper import Article
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Load your updated model
model_pipeline = joblib.load(os.path.join('model', 'fake_news_model.pkl'))

# Initialize database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///predictions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define Prediction model
class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    result = db.Column(db.String(10), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    news_text = data.get('text', '')
    news_url = data.get('url', '')
    scraped_text = ''

    if news_url:
        try:
            article = Article(news_url)
            article.download()
            article.parse()
            news_text = article.text
            scraped_text = news_text[:1000]
        except Exception as e:
            return jsonify({'error': 'Failed to extract text from URL.'}), 400

    if not news_text:
        return jsonify({'error': 'No text provided.'}), 400

    prediction = model_pipeline.predict([news_text])[0]
    probability = model_pipeline.predict_proba([news_text])[0].max()
    result_label = 'Fake' if prediction == 1 else 'Real'

    # Save to DB
    new_pred = Prediction(text=news_text[:500], result=result_label, confidence=round(probability * 100, 2))
    db.session.add(new_pred)
    db.session.commit()

    result = {
        'prediction': result_label,
        'confidence': round(probability * 100, 2),
        'preview': scraped_text
    }

    return jsonify(result)

@app.route('/history', methods=['GET'])
def history():
    predictions = Prediction.query.order_by(Prediction.date.desc()).limit(5).all()
    history_data = [{
        'text': p.text,
        'result': p.result,
        'confidence': p.confidence,
        'date': p.date.strftime('%Y-%m-%d %H:%M')
    } for p in predictions]

    return jsonify(history_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Only creates DB tables if they don't exist
    app.run(debug=True)
