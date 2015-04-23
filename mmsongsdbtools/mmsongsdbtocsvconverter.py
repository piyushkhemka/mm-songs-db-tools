#!/usr/bin/env python

import csv
import json
import logging
import os

import hdf5_getters


logger = logging.getLogger(__name__)


class MMSongsDbToCsvConverter(object):
    """Helper object for reading hdf5 files and writing the results to a csv

    Sample usage:

        converter = MMSongsDbToCsvConverter('mmsongsdb.csv', ['artist_name', 'tempo'])
        converter.convert_directory('.')
    """
    def __init__(self, csv_filename, attrs_to_save=None):
        logger.info("Setting up MMSongsDbToCsvConverter to save to %s",
                    csv_filename)
        self.attrs_to_save = attrs_to_save
        self.getters = None
        self.fp = open(csv_filename, 'w')
        self.writer = csv.writer(self.fp)

    def _get_getters(self, h5):
        getters = filter(lambda key: key[:4] == 'get_' and key != 'get_num_songs',
                         hdf5_getters.__dict__.keys())
        if self.attrs_to_save:
            getters = filter(lambda key: key[4:] in self.attrs_to_save, getters)
            for attr in self.attrs_to_save:
                # Sanity
                if 'get_%s' % attr not in getters:
                    logger.error("Missing attr %s!", attr)
        return sorted(getters)

    def _handle_h5_file(self, filename):
        h5 = hdf5_getters.open_h5_file_read(filename)
        num_songs = hdf5_getters.get_num_songs(h5)
        if not self.getters:
            self.getters = self._get_getters(h5)
            getter_row = [getter[4:] for getter in self.getters]
            self.writer.writerow(getter_row)
        for i in xrange(num_songs):
            result = []
            for getter in self.getters:
                hdf5_getter = getattr(hdf5_getters, getter)
                value = hdf5_getter(h5, i)
                if value.__class__.__name__ == 'ndarray':
                    # Special case for ndarray types
                    value = json.dumps(value.tolist())
                result.append(value)
            self.writer.writerow(result)
        h5.close()

    def convert_directory(self, directory):
        for root, dirnames, filenames in os.walk(directory):
            filenames = filter(lambda filename: filename.endswith('.h5'),
                               filenames)
            logger.info("convert_directory() for dir %s with %s h5 files...",
                        root,
                        len(filenames))
            for filename in sorted(filenames):
                self._handle_h5_file(os.path.join(root, filename))
            for dirname in sorted(dirnames):
                self.convert_directory(os.path.join(root, dirname))
