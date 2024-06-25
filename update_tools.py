"""Automatically install software to reduce work on other computers @zzl"""

import os
import platform
import sys
from shutil import which

args = sys.argv

if args[1].startswith("m"):
    update_mamba = True
    update_cargo = False
    update_pip = False
elif args[1].startswith("c"):
    update_mamba = False
    update_cargo = True
    update_pip = False
elif args[1].startswith("p"):
    update_mamba = False
    update_cargo = False
    update_pip = True
else:
    update_mamba = True
    update_cargo = True
    update_pip = True


def run(cmd: str):
    print("--> ", cmd)
    os.system(cmd)


if update_mamba:
    # -> mamba install packages
    mic = "mamba install -c conda-forge -y"
    bin_package = {
        # python packages
        "pip-autoremove": "pip-autoremove",
        "pipdeptree": "pipdeptree",
        # rust package can be installed by mamba to reduce build time
        "typos": "typos",
        "ripgrep": "ripgrep",  # live grep
        "bat": "bat",  # improved cat
        "zoxide": "zoxide",  # autojump + preview
        "exa": "exa",  # better ls
        "tokei": "tokei",  # code statistics
        "fd": "fd-find",  # improved find
        # cli json / yaml file viewer written in rust
        # requires libxcb etc, easier to install with mamba
        "jless": "jless",
        # general packages
        "pre-commit": "pre-commit",
        "asciinema": "asciinema",  # terminal recording
        "magick": "imagemagick",  # image processing
        "ffmpeg": "ffmpeg",
        "bpytop": "bpytop",  # beautiful top
        "unzip": "unzip",  # unzip for nvim package
        "nvim": "nvim",  # neovim
        "node": "nodejs",
        "tmux": "tmux",
        "tldr": "tldr",  # too long dont read
        "make": "make",
        "dos2unix": "dos2unix",
        "cargo": "rust",  # enable installation of rust packages
        "ruff-lsp": "ruff-lsp",  # ruff language server, nvim
        "fish": "fish",  # fish shell
        "starship": "starship",  # prompt
        "h5glance": "h5glance",
        # h5dump is built-in from ubuntu20
    }
    # lazygit and gcc not supported by osx
    to_ins = ["git", "fzf", "prompt-toolkit"]
    for b, p in bin_package.items():
        if not which(b):
            to_ins.append(p)

    os_name = platform.system()
    if os_name == "Linux":
        to_ins.append("gcc")
    elif os_name == "Darwin":
        pass

    run(f"{mic} {' '.join(to_ins)}")
    run("mamba create -n lab jupyterlab_vim -y")

if update_cargo:
    # can only be installed by cargo
    bin_package = {
        "ruplacer": "ruplacer",  # replace file content
        "dust": "du-dust",  # disk usage
        "procs": "procs",  # improved ps
        "navi": "navi",
    }
    to_ins = []
    for b, p in bin_package.items():
        if not which(b):
            to_ins.append(p)

    if to_ins != []:
        run(f"cargo install {' '.join(to_ins)}")
    run("cargo install --git https://github.com/asciinema/agg")

if update_pip:
    bin_package = {
        "pyproject-fmt": "pyproject-fmt",  # improved ps
        "blind_watermark": "blind-watermark",
    }
    to_ins = []
    for b, p in bin_package.items():
        if not which(b):
            to_ins.append(p)

    if to_ins != []:
        run(f"pip install {' '.join(to_ins)}")
