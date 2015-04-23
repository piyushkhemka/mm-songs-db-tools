# mm-songs-db-tools
Million Songs DB Tools

Tools based on the Million Songs DB: [http://labrosa.ee.columbia.edu/millionsong/](http://labrosa.ee.columbia.edu/millionsong/)

## Usage:

### MMSongsDbToCsvConverter

Helper object for reading hdf5 files and writing the results to a csv

Sample usage:

    converter = MMSongsDbToCsvConverter('mmsongsdb.csv', ['artist_name', 'tempo'])
    converter.convert_directory('.')


## Requirements:

- pytables


## Resources:

- http://labrosa.ee.columbia.edu/millionsong/
- https://github.com/tbertinmahieux/MSongsDB/tree/master/PythonSrc
    - hdf5_getters.py is a direct copy straight from [https://github.com/tbertinmahieux/MSongsDB/blob/408393766dfa449da90faaf8a65aed9cc420849a/PythonSrc/hdf5_getters.py](https://github.com/tbertinmahieux/MSongsDB/blob/408393766dfa449da90faaf8a65aed9cc420849a/PythonSrc/hdf5_getters.py)
