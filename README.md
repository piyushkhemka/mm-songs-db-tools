# mm-songs-db-tools
Million Songs DB Tools

Tools based on the Million Songs DB: [http://labrosa.ee.columbia.edu/millionsong/](http://labrosa.ee.columbia.edu/millionsong/)

## Usage:

### MMSongsDbToCsvConverter

Helper object for reading hdf5 files and writing the results to a csv

Sample usage:

    from mmsongsdbtools.mmsongsdbtocsvconverter import MMSongsDbToCsvConverter
    converter = MMSongsDbToCsvConverter('mmsongsdb.csv', ['artist_name', 'tempo'])
    converter.convert_directory('.')

The second parameter for the constructor of `MMSongsDbToCsvConverter` is an optional list of attributes to fetch for your csv. Available options are listed here:

[http://labrosa.ee.columbia.edu/millionsong/pages/example-track-description](http://labrosa.ee.columbia.edu/millionsong/pages/example-track-description)

Helper command line script: `mmsongsdb_to_csv.py`.

Sample usage:

    ./mmsongsdb_to_csv.py <csv_filename> <directory> [<attr_to_save> <attr_to_save> ...]

parameters:

- `<csv_filename>` the filename of the output csv file
- `<directory>` the name of the directory that has the `.h5` files in it
- `<attr_to_save>` optional attributes to save in the csv file (if not specified, all attributes will be used)


## Requirements:

- [pytables](http://pytables.github.io/)


## Resources:

- http://labrosa.ee.columbia.edu/millionsong/
- https://github.com/tbertinmahieux/MSongsDB/tree/master/PythonSrc
    - hdf5\_getters.py is a direct copy straight from [https://github.com/tbertinmahieux/MSongsDB/blob/408393766dfa449da90faaf8a65aed9cc420849a/PythonSrc/hdf5_getters.py](https://github.com/tbertinmahieux/MSongsDB/blob/408393766dfa449da90faaf8a65aed9cc420849a/PythonSrc/hdf5_getters.py)
