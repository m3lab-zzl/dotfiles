#!/usr/bin/env python3
import os

HOME = os.environ.get("HOME")


def run(cmd: str):
    print("--> ", cmd)
    os.system(cmd)


if __name__ == "__main__":
    condaexe = os.environ.get("CONDA_EXE")
    if condaexe:
        condabinpath = os.path.dirname(condaexe)
        run(f"source {condabinpath}/activate && python3 update_tools.py all")
    else:
        import platform

        ost = platform.system()
        if ost == "Linux":
            run(
                "wget https://mirror.nju.edu.cn/github-release/conda-forge/miniforge/LatestRelease/Miniforge3-Linux-x86_64.sh"
            )
            run(f"sh Miniforge3-Linux-x86_64.sh -b -p {HOME}/mamba3")
        elif ost == "Darwin":
            run(
                "curl -L -o Miniforge3-Darwin-arm64.sh https://mirror.nju.edu.cn/github-release/conda-forge/miniforge/LatestRelease/Miniforge3-Darwin-arm64.sh"
            )
            run(f"sh Miniforge3-Darwin-arm64.sh -b -p {HOME}/mamba3")
        else:
            raise NotImplementedError(f"Unknown OS, {ost}")
        run(
            f"{HOME}/mamba3/bin/mamba run -p {HOME}/mamba3 --no-capture-output python3 update_tools.py all"
        )

    run('git config --global user.name "$(whoami)"')
    run('git config --global user.email "$(whoami)@$(hostname)"')
