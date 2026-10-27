"""Task C, Level 0: rank the candidates by TF-IDF similarity to the query's title and abstract.

    python level0_task_c.py

This baseline reads text only; it ignores the citation graph. Nothing is tuned, so it is fine to
evaluate the test set once here.
"""
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from mustcite import evaluate_c, load_task_c, save_results

TOP = 100
config = {"features": "tfidf words, english stop words, min_df=3, sublinear_tf", "score": "cosine similarity"}

for split in ("val", "test"):
    data = load_task_c(split)
    queries, candidates = data["queries"], data["candidates"]
    vectorizer = TfidfVectorizer(min_df=3, sublinear_tf=True, stop_words="english")
    C = vectorizer.fit_transform(candidates.title + ". " + candidates.abstract)
    Q = vectorizer.transform(queries.title + ". " + queries.abstract)

    ranking = {}
    for start in range(0, Q.shape[0], 500):                      # 500 queries at a time to save memory
        scores = (Q[start:start + 500] @ C.T).toarray()          # rows are L2-normalized: dot = cosine
        top = np.argsort(-scores, axis=1)[:, :TOP]
        for i, row in enumerate(top):
            ranking[queries.paper_id[start + i]] = candidates.paper_id.values[row].tolist()

    save_results(f"level0_task_c_{split}", evaluate_c(split, ranking, k=10), config)
