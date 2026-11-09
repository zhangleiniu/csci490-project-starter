# Which Conference Is This Paper From?

<!-- Example proposal for CSCI 490-B9, Task A. It shows what a full-marks README can look like at the
proposal stage. Your own README should be in your own words, with your own observation and plan. -->

**Author:** (example) · CSCI 490-B9 Deep Learning, NIU, Fall 2026

**AI tool use:** opencode (free model) wrote the first version of `data_check.py`, which I read and changed
to sample across years. ChatGPT explained the difference between accuracy and macro-F1. I wrote this README.

## 1. Task

The input is the title and abstract of an AI/ML paper; the output is one of six venues: AAAI, ACL, CVPR,
ICLR, ICML or NeurIPS.

> **Title:** Strategies for Pre-training Graph Neural Networks
> **Abstract (first sentence):** Many applications of machine learning require a model to make accurate
> predictions on test examples that are distributionally different from training ones, while task-specific
> labels are scarce during training. …
> **Label:** ICLR

## 2. Motivation

A digital library or a reviewer-matching system needs to know which community a paper belongs to, and
preprints do not say where they will be published. ACL (language) and CVPR (vision) are easy to recognize
from the topic. NeurIPS, ICML and ICLR publish the same kind of machine learning paper, and AAAI publishes a
bit of everything, so the model has to pick up weaker signals than the topic. The split by year adds a second
difficulty: the test papers are from 2025, and topics move fast.

## 3. Data

MustCite-Mini (`data/README.md`): 18,000 papers, 500 per venue and year, 2020–2025. The split is fixed by
year: train on 2020–2023, validation on 2024, test on 2025. A model must work on papers newer than any it was
trained on, which is how it would be used.

| Venue | Train | Validation | Test |
|---|---:|---:|---:|
| AAAI | 2,000 | 500 | 500 |
| ACL | 2,000 | 500 | 500 |
| CVPR | 2,000 | 500 | 500 |
| ICLR | 2,000 | 500 | 500 |
| ICML | 2,000 | 500 | 500 |
| NeurIPS | 2,000 | 500 | 500 |
| **Total** | **12,000** | **3,000** | **3,000** |

[samples.md](samples.md) has three papers per venue, drawn from different years (seed 0), not the first
three rows, which are all from 2020.

**What I noticed.** The topics drift within a venue. In ACL, the share of abstracts that mention
"language model" goes from 14% in 2020 to 37% in 2023 and 67% in 2024 (validation); in CVPR, "diffusion"
goes from 0% to 7% to 21%. A model trained on 2020–2023 sees these words much less often than it will
meet them at test time.

## 4. Method

**Level 0** (from `results/level0_task_a_val.json` and `results/level0_task_a_test.json`):

| Model | Val accuracy | Val macro-F1 | Test accuracy | Test macro-F1 |
|---|---:|---:|---:|---:|
| Level 0: TF-IDF + logistic regression | 42.4% | 0.411 | 39.2% | 0.379 |

The Level 0 confusion matrix on validation shows where it fails: ACL (72% recall) and CVPR (69%) are
easy; only 80 of the 500 ICLR papers are right, and 148 of them are predicted as NeurIPS.

**Plan for the next levels**, each with the number I expect:

| Level | Model | Expected val accuracy |
|---|---|---:|
| 1 | Embedding bag (mean of word vectors + linear layer), then a 1D CNN | 44% |
| 2 | DistilBERT, fine-tuned on title + abstract | 50% |
| 3 | Title only vs. title + abstract (question below) | – |

I expect Level 1 to be close to Level 0, since both mostly count words; Level 2 should help most on
ICLR/ICML/NeurIPS, where single words are not enough.

**Level 3 question:** How much of the accuracy comes from the title alone? I will train the Level 1 model and
the Level 2 model twice, on the title only and on title + abstract, and compare accuracy and per-venue recall
on validation. My guess is that the abstract helps DistilBERT more than the embedding bag, because the bag
already gets the topic words from the title.

## 5. Evaluation

The classes are balanced, so accuracy is meaningful; I also report macro-F1, which weights each venue
equally, and the confusion matrix, which shows which venues are mixed up. All choices (model, learning rate,
epochs) are made on validation (2024). Each final model is run on test (2025) once. Success: beat Level 0 on
validation by more than the spread across 3 seeds, and say for which venues.

## 6. Plan

| Week | What I will do |
|---|---|
| 11/2 – 11/8 | Data check, Level 0, this proposal |
| 11/9 – 11/15 | Level 1: embedding bag on Colab; choose epochs on validation; 3 seeds |
| 11/16 – 11/22 | Level 1: 1D CNN for comparison; progress report (11/19) |
| 11/23 – 11/29 | Level 2: fine-tune DistilBERT; title-only runs for Level 3 |
| 11/30 – 12/3 | Test once for each final model; presentation |

## Results

| Level | Model | Validation acc. | Test acc. | Results file |
|---|---|---:|---:|---|
| 0 | TF-IDF + logistic regression | 42.4% | 39.2% | `results/level0_task_a_val.json`, `results/level0_task_a_test.json` |

## How to run

```
pip install -r requirements.txt
python data_check.py       # writes samples.md and prints the table above
python level0_task_a.py    # writes the two Level 0 results files
```

## Data source

MustCite-Mini is a subset of the MustCite corpus of AI/ML papers (https://mustcite.com), prepared for this
course. See `data/README.md`.
