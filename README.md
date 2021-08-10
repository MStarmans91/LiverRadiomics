# LiverRadiomics
Scripts to compute the radiomics features and fit the machine learning models as presented in the paper "Automated differentiation of malignant and benign primary solid liver lesions in non-cirrhotic livers on MRI: an externally validated radiomics model." by M. P. A. Starmans et al. 2021.

Before trying out the code in this repository, we advice you to get
familiar with the WORC package through the WORC tutorial:
https://github.com/MStarmans91/WORCTutorial.

## License
This package is covered by the open source [APACHE 2.0 License](APACHE-LICENSE-2.0).

When using this code, please cite this repository and the corresponding paper
as following:

``Martijn P.A. Starmans. LiverRadiomics. Zenodo (2021). Available from:  https://github.com/MStarmans91/LiverRadiomics.``

## Installation
For both the feature extraction and model optimization, WORC, version 3.4.2,
is required:

    pip install "WORC==3.4.2"

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

## Known Issues
For some of the known issues, please visit the WORC FAQ:
https://worc.readthedocs.io/en/latest/static/faq.html.
