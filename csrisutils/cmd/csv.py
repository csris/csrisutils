import csv
import logging
import sys

from csrisutils.cmd import app
import csrisutils.fileutils as fu


logger = logging.getLogger(__name__)


def difference(*files):
    sets = [set(_read_csv(file)) for file in files]
    common_rows = sets[0].difference(*sets[1:])

    writer = csv.writer(sys.stdout)
    writer.writerows(common_rows)


def intersection(*files):
    sets = [set(_read_csv(file)) for file in files]
    common_rows = set.intersection(*sets)

    writer = csv.writer(sys.stdout)
    writer.writerows(common_rows)


def union(*files):
    sets = [set(_read_csv(file)) for file in files]
    all_rows = set.union(*sets)

    writer = csv.writer(sys.stdout)
    writer.writerows(all_rows)


def markdown(file):
    rows = _read_csv(file)
    max_cols = max(len(row) for row in rows)

    header = [str(i) for i in range(max_cols)]
    header_underline = ['-' * len(col) for col in header]

    print(_format_markdown_row(header))
    print(_format_markdown_row(header_underline))

    for row in rows:
        row = row + ('',) * (max_cols - len(row))
        print(_format_markdown_row(row))


def _format_markdown_row(row):
    return ' | '.join(row).join(['| ', ' |'])


def _read_csv(file):
    with fu.open(file) as in_file:
        reader = csv.reader(in_file)
        return [tuple(row) for row in reader]


def main():
    app.main(
        markdown,
        union,
        intersection,
        difference
    )
