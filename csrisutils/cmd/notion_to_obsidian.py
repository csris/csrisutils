import logging
import os
import re
import shutil
import sys

from csrisutils.cmd import app
import csrisutils.fileutils as fu


logger = logging.getLogger(__name__)


def convert_export(src_directory, dst_directory):
    for root, dirs, files in os.walk(src_directory):
        new_root = re.sub(f'^{src_directory}', dst_directory, root)

        for dname in dirs:
            dst_path = os.path.join(new_root, dname)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)

            if not os.path.isdir(dst_path):
                app.panic(f'{dst_path} exists and is not a directory. Aborting.')

        for file in files:
            _convert_file(
                os.path.join(root, file), 
                os.path.join(new_root, file), 
            )


def _convert_file(src_file, dst_file):
    (_, ext) = os.path.splitext(src_file)
    if ext == '.md':
        _convert_md(src_file, dst_file)
    else:
        shutil.copy(src_file, dst_file, follow_symlinks=False)


def _convert_md(src_file, dst_file):
    with open(src_file) as infile, open(dst_file, 'w') as outfile:
        for line in infile:
            converted_line = re.sub('    ', '\t', line)
            outfile.write(converted_line)


def main():
    app.main(convert_export)
