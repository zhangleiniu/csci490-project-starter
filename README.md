# Project title

<!--
This README is your proposal (due Thu 11/5) and, later, the front page of your project.
Replace every part in <angle brackets> and delete these comments. Keep the headings.
-->

**Author:** <your name> · CSCI 490-B9 Deep Learning, NIU, Fall 2026

**AI tool use:** <which tools you used (for example opencode with model X, ChatGPT), and for what>

## 1. Task

<What goes into the model, and what comes out? One or two sentences, then one example input and its label.>

## 2. Motivation

<Who would use this, and what makes it hard? Three to five sentences.>

## 3. Data

<Where the data comes from, and how it is split, and why. For MustCite-Mini, see `data/README.md`.>

<The output of your `data_check.py`: a table of the number of examples per class (or per year, for Task C)
and per split.>

| Class | Train | Validation | Test |
|---|---:|---:|---:|
| <class> | <n> | <n> | <n> |

<Three examples of each class are in [samples.md](samples.md). What did you notice when you read them?>

## 4. Method

**Level 0 result** (from `results/level0_<task>_val.json` and `..._test.json`):

| Model | Validation <metric> | Test <metric> |
|---|---:|---:|
| Level 0: <model> | <number> | <number> |

**Plan for the next levels.** For each, the number you expect:

| Level | Model | Expected <metric> on validation |
|---|---|---:|
| 1 | <a neural model you train> | <number> |
| 2 | <a pretrained Transformer, fine-tuned> | <number> |
| 3 | <your question, below> | – |

**Level 3 question:** <one question with no fixed answer, and how you will answer it with evidence>

## 5. Evaluation

<Which metric, which split, and what counts as success? Say why the metric fits your task.>

## 6. Plan

| Week | What I will do |
|---|---|
| 11/2 – 11/8 | <...> |
| 11/9 – 11/15 | <...> |
| 11/16 – 11/22 | <...> (progress report 11/19: Level 1) |
| 11/23 – 11/29 | <...> |
| 11/30 – 12/3 | <...> (presentation: Level 2) |

## Results

<Fill in as you go. One row per model, numbers from `results/`.>

| Level | Model | Validation | Test | Results file |
|---|---|---:|---:|---|
| 0 | <model> | <number> | <number> | `results/<file>.json` |

## How to run

```
pip install -r requirements.txt
python level0_task_a.py        # or your own scripts
```

## Data source

MustCite-Mini is a subset of the MustCite corpus of AI/ML papers (https://mustcite.com), prepared for this course.
See `data/README.md`.
