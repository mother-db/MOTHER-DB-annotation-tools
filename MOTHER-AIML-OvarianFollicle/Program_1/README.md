# MOTHER-DB project

Image segmentation of ovarian follicles, part of https://mother-db.org/

## Program 1, Train Image Generation.ipynb, Version 5_3, March 7, 2025:
Creation of sub-images from a set of annotated histology images and files of annotations.

This project developed uses AI/ML techniques to segment histology images from the ovaries of nonhuman primates. Specifically, this suite of programs attempts to identify the following six follicle types:

1.    Primordial
1.    Transitional Primordial
1.    Primary
1.    Transitional Primary
1.    Secondary
1.    Multilayer

The follicle type definitions are based on the recommendations of the NICHD-Sponsored Ovarian Nomenclature Workshop committee for primates.

Yano Maher JC, Zelinski MB, Oktay KH, Duncan FE, Segars JH, Lujan ME, Lou H, Yun B, Hanfling SN, Schwartz LE, Laronda MM, Halvorson LM, O'Neill KE, Gomez-Lobo V. Fertil Steril. 2024 Nov 14:S0015-0282(24)02394-X. doi: 10.1016/j.fertnstert.2024.11.016. PMID: 39549739.  PMCID: PMC12045743. DOI: 10.1016/j.fertnstert.2024.11.016
https://pubmed.ncbi.nlm.nih.gov/39549739/

## About this program module

This program takes as input a set of ovarian histology slides along with annotation files and creates sub-images of each annotation. In addition, the program creates "augmentations" of the images by rotating, flipping and offsetting the images. The output is a set of folders, one for each follicle type, containing the sub-images.

In addition, this program creates a set of "negative" sub-images, which are random samples of the original image but not too near an existing annotation. The minimal allowed distance between a randomly selected negative image and an existing image is set to be 1/4 of the sub-image width (50 pixels for sub-images that are 200 pixels wide). The number of negatives generated is based on the number of actual annotations, as defined by the parameter negatives_per_annot. A "blank" image is defined as any sub-image that has a standard deviation of the pixels in the sub-image that is less than a threshold. Depending on the amount of non-tissue area in the original slide, this process can generate an excessive number of blank images. To counter this, the number of blank negatives is reduced.

The output sub-images filenames include information necessity to trace a particular sub-image back to the original annotation and histology slide.

## About the data

The data consists of paired images and annotation files. For example, the image file 14736_UN_050a.ome.tif and its paired annotations file 14736_UN_050a.annotations.txt. Note that all the image/annotation file pairs are in the same directory.

The path to the paired images, along with other information such as image resolution, is described in the parameters.py file.
