import WORC
import os
import glob


def editconfig(config):
    # Normalize based on ROI
    config['Preprocessing']['Normalize'] = 'True'
    config['Preprocessing']['Normalize_ROI'] = 'True'

    # For naming of features
    config['ImageFeatures']['image_type'] = 'MR'

    # Turn this to True if you want to use the features from ExampleData\semantics.csv
    config['SelectFeatGroup']['semantic_features'] = 'False'

    # Label to predict
    config['Labels']['modus'] = 'singlelabel'
    config['Labels']['label_names'] = 'Malignant'

    # Turn this to True when using a fixed separate training and test set, i.e. external validation
    config['Bootstrap']['Use'] = 'False'

    return config


# Inputs
name = 'WORC_Liver_Malignant'
current_path = os.path.dirname(os.path.abspath(__file__))
label_file = os.path.join(current_path, 'ExampleData', 'pinfo.csv')
semantics_file = os.path.join(current_path, 'ExampleData', 'sem.csv')
config = os.path.join(current_path, 'ExampleData', 'config.ini')

# Altough you can also supply the raw image, we will supply the extracted
# features directly.
feature_files = glob.glob(os.path.join(current_path, 'ExampleData', 'example_features_predict_LiverRadiomics-*.hdf5'))
feature_files.sort()

# As we only have a single feature file, we will repeat it to mimick
# having multiple. We do this in a dictionary, in which the keys
# correspond to the "patient" names also used in the label and semantics files
patient_names = ['LiverRadiomics-' + str(i).zfill(3) for i in range(0, 10)]
features = {k: v for k, v in zip(patient_names, feature_files)}

# Create the WORC network
network = WORC.WORC(name)

# Instead of supplying the .ini file to the network, we will create
# the config object for you directly from WORC,
# so you can interact with it if you want.
# Altough it is a configparser object, it works similar as a dictionary
config = network.defaultconfig()

# The default config from the WORC 2.1.3 version we used, was a stripped
# version in order to get a quick result. The actual default used for normal
# experiments is created through the editconfig function.
config = editconfig(config)

# NOTE: Since we now only use 10 "patients" in this example, we do not use resampling.
# Do not do this for the full experiment.
config['Resampling']['Use'] = '0.0'

# Append the sources to be used. When using images and segmentations, use the
# images_train and segmentations_train instead of features_train object.
network.features_train.append(features)
network.labels_train.append(label_file)
network.semantics_train.append(semantics_file)
network.configs.append(config)

# Build, set, and execture the network
network.build()
network.set()
network.execute()

# NOTE: if you want extensive evaluation including ROC curves, statistical
# testing of features, add ``network.add_evaluation('Malignant')'' after
# network.build().
