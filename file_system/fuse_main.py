
from fuse import FUSE
from fuse_operations import FuseOperations
import argparse
import logging
import subprocess


def umount(path):
    subprocess.run(['umount', path], capture_output=True)


def run_fuse(mount, source_dir):
    umount(mount)
    FUSE(FuseOperations(mount, source_dir), mount,  foreground=True, allow_other=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mount')
    parser.add_argument('--dir', dest='source_dir', default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    run_fuse(args.mount, args.source_dir)