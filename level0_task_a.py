"""Task A, Level 0: TF-IDF features and logistic regression.

    python level0_task_a.py

The settings below are fixed, not tuned, so it is fine to evaluate the test set once here.
When you tune your own models, compare them on the validation set and run the test set once at the end.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from mustcite import evaluate_a, load_task_a, save_results

train, val, test = load_task_a()


def text(df):
    return df.title + ". " + df.abstract


config = {"features": "tfidf words+bigrams, min_df=3, sublinear_tf", "model": "logistic regression, C=5"}
vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=3, sublinear_tf=True, max_features=200_000)
X_train = vectorizer.fit_transform(text(train))
model = LogisticRegression(C=5, max_iter=2000).fit(X_train, train.label)

for name, df in (("val", val), ("test", test)):
    pred = model.predict(vectorizer.transform(text(df)))
    save_results(f"level0_task_a_{name}", evaluate_a(df.label, pred), config)
