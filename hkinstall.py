from hkpilot.utils.cmake import CMake

import inspect
import os


class libzmq(CMake):

    def __init__(self, path):
        super().__init__(path)

        self._package_name = "libzmq"
        self._package_version = "1.1.0"

        self._git_url = "git@github.com:zeromq/libzmq.git"
        self._git_branch = "master"
        self._git_clone_dir = "src"
        self._cmakelist_path = "src"

        self._cmake_options = {
            "WITH_TLS": "OFF"
        }
