[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5175705.svg)](https://doi.org/10.5281/zenodo.5175705)

# LiverRadiomics
Scripts to compute the radiomics features and fit the machine learning models as presented in the paper "Automated differentiation of malignant and benign primary solid liver lesions on MRI: an externally validated radiomics model" by M. P. A. Starmans et al. Submitted. Preprint available at medRxiv 2021.08.10.21261827; doi: https://doi.org/10.1101/2021.08.10.21261827

Before trying out the code in this repository, we advice you to get
familiar with the WORC package through the WORC tutorial:
https://github.com/MStarmans91/WORCTutorial.

## License
This package is covered by the open source [APACHE 2.0 License](APACHE-LICENSE-2.0).

When using this code, please cite this repository and the corresponding paper
as following:

```bibtex
@article{starmans2023liverradiomics,
   title            = {Automated differentiation of malignant and benign primary solid liver lesions on MRI: an externally validated radiomics model}, 
   author           = {Martijn P.A. Starmans and Razvan L. Miclea and Valerie Vilgrain and Maxime Ronot and Yvonne Purcell and Jef Verbeek and Wiro J. Niessen and Jan N.M. Ijzermans and Rob A. de Man and Michail Doukas and Stefan Klein and Maarten G. Thomeer},
   year             = {2021},
   eprint           = {2021.08.10.21261827},
   archivePrefix    = {medRxiv},
   primaryClass     = {eess.IV},
   doi              = {10.1101/2021.08.10.21261827}
}

@software{starmans2023liverradiomicscode,
  author       = {Martijn P. A. Starmans},
  title        = {LiverRadiomics},
  year         = {2023},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.5175705},
  url          = {https://github.com/MStarmans91/LiverRadiomics}
}
```


## Installation
For both the feature extraction and model optimization, WORC, version 3.6.1,
is required:

    pip install "WORC==3.6.1"

## Usage: Dataset
The Liver dataset as used in the paper was publicly released as part of the following paper:

```bibtex
@article {Starmans2021WORCDatabase,
	title           = {The WORC database: MRI and CT scans, segmentations, and clinical labels for 930 patients from six radiomics studies},
	author          = {Starmans, Martijn P.A. and Timbergen, Milea J.M. and Vos, Melissa and Padmos, Guillaume A. and Gr{\"u}nhagen, Dirk J. and Verhoef, Cornelis and Sleijfer, Stefan and van Leenders,   Geert J.L.H. and Buisman, Florian E. and Willemssen, Francois E.J.A. and Koerkamp, Bas Groot and Angus, Lindsay and van der Veldt, Astrid A.M. and Rajicic, Ana and Odink, Arlette E. and Renckens, Michel and Doukas, Michail and de Man, Rob A. and IJzermans, Jan N.M. and Miclea, Razvan L. and Vermeulen, Peter B. and Thomeer, Maarten G. and Visser, Jacob J. and Niessen, Wiro J. and Klein, Stefan},
	year            = {2021},
    eprint          = {2021.08.19.21262238},
    archivePrefix   = {medRxiv},
    primaryClass    = {eess.IV},
	doi             = {10.1101/2021.08.19.21262238},
}
```

The data can be found at https://xnat.bmia.nl/data/projects/worc; scripts 
to download the data can be found at https://github.com/MStarmans91/WORCDatabase,
including a script to reproduce the internal validation experiment for the radiomics model of this Liver study.

## Usage: Feature Extraction
The ExtractFeatures.py script can be used to extract all features. We provided
you with the exact same configuration file that was used in the study. The
script can be easily modified to use your own data instead of the
provided example data and requires:

1. An image in ITK Image format, e.g. .nii, .nii.gz, .tiff, .nrrd, .raw
2. A segmentation in ITK Image format.
3. Optionally, metadata in DCM format

Extracting the features from the example data should take less than 10 seconds.
Using a larger image and/or mask may result in a longer computation time.

## Usage: model training and optimization
To reproduce the experiments on the internal validation, we refer
to https://github.com/MStarmans91/WORCDatabase as mentioned above.
The WORC database contains this internal validation dataset; the associated
Github repo contains the scripts to reproduce our radiomics results.

## Known Issues
For some of the known issues, please visit the WORC FAQ:
https://worc.readthedocs.io/en/latest/static/faq.html.
