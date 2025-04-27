# AI Fake News Detector

An AI-powered web app that detects whether a news article is **Fake** or **Real** using a machine learning model. Users can paste article text or a URL, view a confidence score, and track recent predictions.

---

## Live Demo
![Fake News Detector Demo](https://github.com/DanV27/ai-fake-news-detector/blob/main/Frontend/demo.gif)




---

## Tech Stack

- **Front-End**: HTML, CSS, JavaScript, Bootstrap
- **Back-End**: Python, Flask, Flask-CORS, Flask-SQLAlchemy
- **Machine Learning**: Scikit-learn (Naive Bayes, TF-IDF)
- **Scraping**: Newspaper3k
- **Database**: SQLite (for prediction history)

---

## Features

- **Fake News Detection** from either raw text or article URLs.
- **Confidence Score** on each prediction.
- **Preview** of the scraped article text.
- **Recent Predictions History** saved and displayed.
- **Responsive UI** with Bootstrap styling.
- **Clear/Reset** functionality for easy re-use.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-fake-news-detector.git
   cd ai-fake-news-detector
2. **Set up the virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies:

pip install -r requirements.txt

4. **Train the Model (Optional if model provided):

A script can be provided or model file included.

5. **Run Flask back-end:

cd Backend
python app.py

6. **Run the front-end:<br>
cd frontend<br>
python -m http.server 8000<br>
Visit: http://localhost:8000<br>
---
**Machine Learning Details**<br>
-Dataset: Fake and Real News Dataset<br>
-Model: Naive Bayes classifier with TF-IDF vectorization.<br>
-Accuracy: 93.24%<br>

**Future Improvements**<br>
-Deploy on Render/Netlify.<br>
-Add User Authentication for personalized history.<br>
-Experiment with more advanced models (Logistic Regression, BERT).<br>
-Add data visualizations or download history.<br>

**Acknowledgements**<br>
-Dataset provided by Kaggle.<br>
-UI styled with Bootstrap.<br>
-Text scraping powered by Newspaper3k.<br>

**Contact**<br>
Daniel Valenzuela – www.linkedin.com/in/daniel-valenzuela-9ab407359 – vdanny911@gmail.com<br>
GitHub: DanV27<br>
