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

``Martijn P.A. Starmans. LiverRadiomics. Zenodo (2021). Available from:  https://github.com/MStarmans91/LiverRadiomics, DOI: https://doi.org/10.5281/zenodo.5175705.``

``Martijn P.A. Starmans, Razvan L. Miclea, Valerie Vilgrain, Maxime Ronot, Yvonne Purcell, Jef Verbeek, Wiro J. Niessen, Jan N.M. Ijzermans, Rob A. de Man, Michail Doukas, Stefan Klein, Maarten G. Thomeer “Automated differentiation of malignant and benign primary solid liver lesions on MRI: an externally validated radiomics model” Submitted. Preprint available at medRxiv 2021.08.10.21261827; doi: https://doi.org/10.1101/2021.08.10.21261827``

## Installation
For both the feature extraction and model optimization, WORC, version 3.5.0,
is required:

    pip install "WORC==3.5.0"

## Usage: Dataset
The Liver dataset as used in the paper was publicly released as part of the following paper:

``Martijn P.A. Starmans et al. (2021). The WORC* database: MRI and CT scans, segmentations, and clinical labels for 932 patients from six radiomics studies, Submitted. Preprint available at medRxiv 2021.08.19.21262238; doi: https://doi.org/10.1101/2021.08.19.21262238``

The data can be found at https://xnat.bmia.nl/data/projects/worc; scripts to download the data can be found at https://github.com/MStarmans91/WORCDatabase, including a script to reproduce the internal validation experiment for the radiomics model of this Liver study.

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

## Usage: Model Optimization
The ModelOptimization.py script can be used for the model optimization. Again,
we provided you with the exact same configuration file that was used in the study.
The script can be easily modified to use your own data instead of the
provided example data and requires: see for more details the script itself.

Note that the script performs a dummy experiment: it supplies 10x the example
features to WORC, which will result in non-separable dataset, and thus no
sensible model. Usage of your own data is therefore highly recommended.

To reproduce the internal validation experiments, we refer to https://github.com/MStarmans91/WORCDatabase
as mentioned above.

## Known Issues
For some of the known issues, please visit the WORC FAQ:
https://worc.readthedocs.io/en/latest/static/faq.html.
