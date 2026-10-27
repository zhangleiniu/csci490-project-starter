# MustCite-Mini

A subset of the MustCite corpus (https://mustcite.com), a collection of papers from top AI/ML venues with
their matched references, prepared for CSCI 490-B9 Deep Learning, Fall 2026.

## Papers: `papers.csv.gz` (18,000 rows)

Six venues, six years (2020–2025), 500 papers sampled at random for each venue and year.

| Column | Meaning |
|---|---|
| `paper_id` | unique id, also used in the other two files |
| `title`, `abstract` | as published |
| `venue` | `aaai`, `acl`, `cvpr`, `iclr`, `icml` or `neurips` |
| `year` | 2020 to 2025 |
| `split` | `train` (2020–2023, 12,000), `val` (2024, 3,000) or `test` (2025, 3,000) |

Authors are left out on purpose: a model could learn the authors instead of the content.

## Citations: `citations.csv.gz` (56,033 rows)

One row per citation where both papers are in `papers.csv.gz`: `citing_id` cites `cited_id`.
16,048 papers have at least one citation edge; the median is 5 edges per paper.

## Citation contexts: `contexts.csv.gz` (52,072 rows)

Sentences from the full text of a paper around one of its citations, for at most 3 cited papers per citing paper.

| Column | Meaning |
|---|---|
| `citing_id` | the paper that cites (in `papers.csv.gz`) |
| `cited_id`, `cited_title`, `cited_venue`, `cited_year` | the paper that is cited (often not in `papers.csv.gz`) |
| `sections` | the section of each mention, separated by ` \| ` |
| `contexts` | up to 3 mentions, separated by ` \|\|\| `; the cited paper is `[CITATION]`, other citations `[REF]` |
| `num_mentions` | how often the paper cites it in total (only the first 3 are in `contexts`) |
| `label` | 1 = core, 0 = background (see below) |
| `split` | the split of the citing paper |

**How the label was made.** An LLM read each context and answered whether the cited work is a baseline or a
direct comparison in the citing paper, or the source of its main dataset, benchmark, task or method (1), or
only background or related work (0). The labels are machine-made and some are wrong. 18% are 1.

The contexts were extracted from PDFs automatically, so some sentences are cut or contain broken symbols.

## Split

By year, the same for all tasks: train on 2020–2023, choose on 2024, test once on 2025.
A paper and all of its citation contexts are in the same split.
