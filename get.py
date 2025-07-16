#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "platformdirs",
# ]
# ///

import argparse
import glob
import logging
import os
from pathlib import Path
import shutil
from typing import Iterable, Iterator

import platformdirs

class VsNatVis(object):
    def __init__(self):
        pass
    
    def get(self):
        chromium_src = VsNatVis.chromium_src_dir()
        src_dirs = [
            chromium_src / "tools" / "win" / "DebugVisualizers",
            chromium_src / "build" / "config" / "c++"
        ]
        for src_dir in src_dirs:
            VsNatVis.copy(src_dir, list(VsNatVis.user_dirs()))
    
    @staticmethod
    def copy(src_dir: Path, dst_dirs: Iterable[Path]):
        for file in src_dir.iterdir():
            name = file.name
            if name.endswith(".natvis") or name.endswith(".natstepfilter"):
                logging.info(f"Copying {file.name} in {file.parent}")
                for dst_dir in dst_dirs:
                    logging.info(f"Copying -> {dst_dir}")
                    shutil.copy(file, dst_dir)

    @staticmethod
    def chromium_src_dir() -> Path:
        return Path(os.environ["CHROMIUM_SRC"])

    @staticmethod
    def user_dirs() -> Iterator[Path]:
        doc_dir = Path(platformdirs.user_documents_dir())
        user_vs_dirs = glob.glob(str(doc_dir / "Visual Studio *"))
        user_dirs = map(lambda dir: Path(dir) / "Visualizers", user_vs_dirs)
        return user_dirs

def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("args", nargs="*")
    args = parser.parse_args()
    natvis = VsNatVis()
    if len(args.args) == 0:
        natvis.get()
        return
    for arg in args.args:
        if "get".startswith(arg):
            natvis.get()

if __name__ == "__main__":
    main()
