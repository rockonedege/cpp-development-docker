echo 'start initiating the docker environment'
echo '======================================='
echo "ninja " &&  ninja --version 
cppcheck --version
cmake --version  | grep -i -A 1 'version'
vcpkg version    | grep -i -A 1 'version'
cc --version  | grep -i -A 1 'version'
clang-format --version
clang-tidy --version
dot -V
echo '======================================='

vcpkg install \
        boost-date-time \
        boost-log \
        boost-thread \
        boost-system \
        boost-filesystem \
        boost-exception \
        boost-timer \
        boost-chrono \
        boost-program-options \
        boost-iostreams \
        boost-uuid \
        boost-test \
        fmt \
        pybind11

/bin/bash 