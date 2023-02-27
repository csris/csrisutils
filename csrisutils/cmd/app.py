import logging
import sys

import argh


LOG_FORMAT = '%(asctime)s.%(msecs)03d %(levelname)s %(name)s: %(message)s'
DATE_FORMAT = '%FT%T' 


logger = logging.getLogger(__name__)


def main(*commands):
    p = argh.ArghParser()

    if len(commands) == 1:
        p.set_default_command(commands[0])
    else:
        p.add_commands(commands)

    p.add_argument('--verbose', '-v', action='store_true')

    args = p.parse_args()

    logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT)

    log_level = logging.ERROR
    if args.verbose:
        log_level = logging.DEBUG

    package_logger = logging.getLogger(__name__.split('.')[0])
    package_logger.setLevel(log_level)

    logger.debug(f'Command: {sys.argv}')

    p.dispatch()


def panic(msg, *args, **kwargs):
    logger.critical(msg, *args, **kwargs)
    sys.exit(1)
