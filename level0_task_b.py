"""Task B, Level 0: TF-IDF features and logistic regression on the citation contexts.

    python level0_task_b.py

The settings below are fixed, not tuned, so it is fine to evaluate the test set once here.
When you tune your own models (including the threshold), use the validation set and run the test set once at the end.
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from mustcite import evaluate_b, load_task_b, save_results

train, val, test = load_task_b()


def text(df):
    return df.sections + " :: " + df.contexts


config = {"features": "tfidf words+bigrams of section and contexts", "model": "logistic regression, C=2, balanced",
          "threshold": 0.5}
vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=3, sublinear_tf=True, max_features=200_000)
X_train = vectorizer.fit_transform(text(train))
model = LogisticRegression(C=2, max_iter=2000, class_weight="balanced").fit(X_train, train.label)

for name, df in (("val", val), ("test", test)):
    score = model.predict_proba(vectorizer.transform(text(df)))[:, 1]
    save_results(f"level0_task_b_{name}", evaluate_b(df.label, score, threshold=0.5), config)
