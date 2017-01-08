# UPSILoN Extract
UPSILoN Extract is a Python script for extracting information from (time, magnitude, error) light curve data. It was created from the functionality built into the [UPSILoN](https://github.com/dwkim78/py3-UPSILoN) periodic variable star classifier ([Kim & Bailer-Jones 2015](https://arxiv.org/abs/1512.01611)).

All of the extraction functionality is directly from the UPSILoN classifier. UPSILoN Extract includes only the needed modules so that users do not have to download the Random Forest classifier included in the UPSILoN library. Additionally, UPSILoN Extract gives a command line tool `upsilon-extract` for batch processing light curve data files.

## Licensing
All of the code in the `extract_features` folder is from the UPSILoN library, licensed under the MIT License by Dae-Won Kim. See the [UPSILoN library history](https://github.com/dwkim78/py3-upsilon/commits/2c3e1da134014bf75fd672044f03f3b650045b10) for more attribution information.

The remainer of UPSILoN is also licensed under the MIT License.
