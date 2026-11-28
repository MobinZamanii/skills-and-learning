# Bioinformatics

**From Biological Data to Computational Discovery**

A comprehensive, Python-centered and research-oriented learning repository covering bioinformatics, biological data science, genomics, transcriptomics, proteomics, cancer research, and computational biology.

## Project goals

- Explain the biological and mathematical foundations behind computational methods.
- Teach practical analysis with Python and established bioinformatics tools.
- Work with public, documented biological datasets.
- Emphasize reproducibility, statistical rigor, and biological interpretation.
- Connect computational results to defensible research questions.

## Learning roadmap

| Module | Scope | Notebooks |
|---|---|---:|
| 01. Foundations of Bioinformatics | Molecular biology, genetics, biological data | 2 |
| 02. Python for Bioinformatics | Python, scientific computing, statistics, visualization | 3 |
| 03. Biological Databases | Biological resources and programmatic retrieval | 2 |
| 04. Sequence Analysis | Sequence processing, alignment, BLAST, motifs, phylogenetics | 3 |
| 05. Genomics | NGS, genome analysis, variants and annotation | 3 |
| 06. Transcriptomics & Single-Cell | Bulk RNA-seq, differential expression, single-cell analysis | 4 |
| 07. Proteomics & Systems Biology | Proteins, structures, pathways, biological networks | 3 |
| 08. Cancer Bioinformatics & AI | Cancer genomics, biomarkers, ML/DL, multi-omics | 4 |
| **Total** | **8 modules** | **24** |

## Repository structure

```text
Bioinformatics/
├── 01_Foundations_of_Bioinformatics/
├── 02_Python_for_Bioinformatics/
├── 03_Biological_Databases/
├── 04_Sequence_Analysis/
├── 05_Genomics/
├── 06_Transcriptomics_and_Single_Cell/
├── 07_Proteomics_and_Systems_Biology/
├── 08_Cancer_Bioinformatics_and_AI/
├── datasets/
├── resources/
├── environment/
├── assets/
├── .gitignore
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE
├── CHANGELOG.md
└── README.md
```

## How to use this repository

1. Start with Module 01 if you are new to bioinformatics.
2. Complete the Python foundations before moving to data-intensive modules.
3. Read each notebook sequentially; notebooks may rely on concepts introduced earlier.
4. Follow the dataset instructions in `datasets/README.md`.
5. Record software versions and keep a reproducible environment.
6. Interpret biological findings cautiously; computational association does not establish causation.

## Notebook design standard

Each full notebook is intended to include:

1. Introduction and learning objectives
2. Biological background
3. Theoretical and mathematical foundations
4. Computational methods and assumptions
5. Required libraries and environment notes
6. Dataset description and provenance
7. Step-by-step Python implementation
8. Visualization and quality assessment
9. Biological interpretation
10. Limitations and common pitfalls
11. Exercises and a research challenge
12. References and further reading

The notebooks currently contain structured authoring outlines. They are scaffolds, not completed lessons or validated analysis pipelines.

## Core tools

Python, Jupyter, NumPy, pandas, SciPy, Biopython, scikit-learn, PyTorch, Scanpy, AnnData, PyDESeq2, GSEApy, NetworkX, matplotlib, and seaborn.

Some specialist workflows also rely on external tools such as FastQC, STAR, BWA, samtools, GATK, and Ensembl VEP. These are not replaced by Python libraries; their use will be documented where appropriate.

## Data policy

Large datasets are not committed to this repository. Dataset documentation should include the source, accession, organism, data type, version or release, license/usage restrictions, download instructions, and expected directory layout. Never commit controlled-access data, personal data, credentials, or data whose terms prohibit redistribution.

## Reproducibility and scientific rigor

- Avoid patient-level leakage when splitting biomedical datasets.
- Document cohort definitions, inclusion criteria, and sample identifiers.
- Distinguish exploratory analysis from confirmatory analysis.
- Report missingness, batch effects, limitations, and negative results.
- Use external validation where the research question requires it.
- Do not interpret predictive performance as clinical utility without appropriate evidence.

## Citation

If you use this repository, cite it using the metadata in [`CITATION.cff`](CITATION.cff). Please also cite original datasets, software, and scientific methods.

## License

Code in this repository is released under the MIT License. This license does not override the licenses or terms of use of external datasets, images, software, or third-party materials.
