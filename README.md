# MOTHER-DB
This repository contains code for the MOTHER-DB.org. MOTHER-DB is a database, meta-data archive and set of programs for annotating and storing ovary histology images from a wide range of species.

The Multispecies Ovary Tissue Histology Electronic Repository (MOTHER) provides public access to digitized microscopic images of ovary tissues along with information that ensures image integrity and quality. Currently, there is no electronic repository of ovary histology slides that preserves these valuable research collections for future generations. MOTHER is a web-accessible, open resource for scientists, educators, and the public to stimulate collaboration and scientific research. Educators may use the slide images in a range of courses from reproductive biology to teaching computerized image analysis.

This repository contains programs to help annotate ovary histology slides. For example, identifying follicles and their developmental stage.
In addition, this repository will include AI/ML code for the automated annotation of ovary histology slides as well as sample data.

Major Code projects include:

1. CompareTwoAnnotators: This Jupyter-Python notebook compares annotations created by two human annotators. These manual annotations are created using QuPath (https://github.com/qupath/qupath) and a table of annotations is exported. The exported annotation files form the two annotators are input to the notebook. The notebook identifies agreements and disagreements in the two annotators files and creates tables and output images showing agreements and disagreements. For example, see 
[CompareTwo_single_slide_writeup.pdf](https://github.com/user-attachments/files/17318330/CompareTwo_single_slide_writeup.pdf)

2. Automated annotation Jupyter-Python notebooks that are trained using human-annotated ovary histology images that attempts to identify follicles (across 7 or more known follicle stages) as well as other ovary features such as the corpus luetem or cortex.


Funding: MOTHER DB is funded by grant “CIBR Multispecies Ovary Tissue Histology Electronic Repository (MOTHER)” from the National Science Foundation (NSF DBI-2054061, 2021–2025).

Disclaimer: Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation.
