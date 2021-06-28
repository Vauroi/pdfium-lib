import os
import subprocess
from subprocess import check_call

import modules.config as c
import modules.functions as f


def run_task_build_depot_tools():
    f.debug("Building depot tools...")

    build_dir = os.path.join("build")
    f.create_dir(build_dir)

    tools_dir = os.path.join(build_dir, "depot-tools")
    f.remove_dir(tools_dir)

    cwd = build_dir
    command = " ".join(
        [
            "git",
            "clone",
            "https://chromium.googlesource.com/chromium/tools/depot_tools.git",
            "depot-tools",
        ]
    )
    check_call(command, cwd=cwd, shell=True)

    f.debug("Execute on your terminal: export PATH=$PATH:$PWD/build/depot-tools")


def run_task_build_emsdk():
    f.debug("Building Emscripten SDK...")

    build_dir = os.path.join("build")
    f.create_dir(build_dir)

    tools_dir = os.path.join(build_dir, "emsdk")
    f.remove_dir(tools_dir)

    cwd = build_dir
    command = " ".join(
        [
            "git",
            "clone",
            "https://github.com/emscripten-core/emsdk.git",
        ]
    )
    check_call(command, cwd=cwd, shell=True)

    cwd = tools_dir
    command = " ".join(["git", "checkout", "2.0.12"])
    check_call(command, cwd=cwd, shell=True)

    cwd = tools_dir
    command = " ".join(["./emsdk", "install", "2.0.12"])
    check_call(command, cwd=cwd, shell=True)

    cwd = tools_dir
    command = " ".join(["./emsdk", "activate", "2.0.12"])
    check_call(command, cwd=cwd, shell=True)

    cwd = tools_dir
    command = " ".join(["source", "emsdk_env.sh"])
    check_call(command, cwd=cwd, shell=True)


def run_task_format():
    # check
    try:
        subprocess.check_output(["black", "--version"])
    except OSError:
        f.error("Black is not installed, check: https://github.com/psf/black")

    # start
    f.debug("Formating...")

    # make.py
    command = " ".join(
        [
            "black",
            "make.py",
        ]
    )
    check_call(command, shell=True)

    # modules
    command = " ".join(
        [
            "black",
            "modules/",
        ]
    )
    check_call(command, shell=True)

    f.debug("Finished")
