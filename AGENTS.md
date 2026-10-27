# Rules for coding agents in this repository

This is a student course project (CSCI 490-B9 Deep Learning, NIU, Fall 2026). Read this file at the start
of every session and follow it. If a request conflicts with these rules, say so and do not do it.

## The project

- Task: <!-- write A, B or C and one sentence, e.g. "Task A: predict the venue of a paper from its title and abstract" -->
- Data: MustCite-Mini in `data/`. Load it only through the `load_*` functions in `mustcite.py`.

## Data and split

- The split is fixed by year: train = 2020-2023, validation = 2024, test = 2025.
- Never re-split, shuffle across splits, or move rows between splits. Never train on validation or test rows.
- Do not edit `mustcite.py` or the files in `data/`.

## Metrics

- Score every model with the matching function in `mustcite.py`: `evaluate_a`, `evaluate_b` or `evaluate_c`.
- Task A: accuracy, macro-F1 and the confusion matrix. Task B: precision, recall and F1 of the core class,
  and ROC-AUC (never accuracy alone). Task C: recall@10 and MRR.

## The test set is used once

- Choose models, hyperparameters, epochs and thresholds on the validation set only.
- Evaluate a model on the test set once, after all choices are made. Never use a test number to change anything.

## Every number comes from a file

- Save the metrics of every run with `save_results(name, metrics, config)`; it writes `results/<name>.json`.
- Every number in `README.md` must come from a file in `results/`. Never type a number that is not in a file.

## Code

- Small, readable scripts, one per model or experiment, named like `level1_lstm.py`. Comment what is not obvious.
- One training run must take less than 30 minutes on a free Colab T4 GPU.
- Fix random seeds, and save the settings of each run in the `config` of `save_results`.
- Do not commit model weights or other large files (see `.gitignore`).
- After each working step, suggest a commit with a message that says what changed.

## The student is the author

- The student must be able to explain every line. Explain what you wrote and why, briefly.
- Do not write the README's analysis or conclusions; the student writes those from the results.
