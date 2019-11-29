FROM conanio/gcc9
LABEL author="Tom Tan <rockonedge@live.com>"
LABEL version="1.0"

USER root
RUN apt-get update -qq && apt-get install -qq --no-install-recommends \
    unzip \
    ncdu \
    clang-tidy \
    clang-format \
    graphviz \
    > /dev/null

# # cmake
# RUN wget --no-check-certificate --quiet -O cmake-linux.sh https://github.com/Kitware/CMake/releases/download/v3.15.4/cmake-3.15.4-Linux-x86_64.sh \
#     && sh cmake-linux.sh --skip-license --prefix=/usr/local \
#     && cmake --version

# cppcheck
USER root
RUN cd /tmp \
    && wget --no-check-certificate --quiet -O cppcheck.tar.gz https://github.com/danmar/cppcheck/archive/1.89.tar.gz \
    && tar xf cppcheck.tar.gz \
    && cd cppcheck-1.89 \
    && mkdir build \
    && cd build \
    && cmake .. >/dev/null \
    && make install >/dev/null \
    && cd ../.. && rm -rf cppcheck* \
    && cppcheck --version

# vcpkg installed to /vcpkg
RUN cd /tmp \
    && wget --no-check-certificate --quiet -O master.zip https://github.com/microsoft/vcpkg/archive/master.zip \
    && unzip -q master.zip \
    && rm master.zip   \
    && cd vcpkg-master \
    && ./bootstrap-vcpkg.sh -useSystemBinaries  \
    && rm -rf buildtrees && rm -rf downloads && rm -rf ./toolsrc/Release \
    && chmod -R 777 ./ \
    && mv /tmp/vcpkg-master /vcpkg \
    && cd /usr/bin && ln -s /vcpkg/vcpkg vcpkg \
    && vcpkg version 

# cmake-format
RUN pip install -qqq cmake_format


USER conan

COPY install-common.sh /scripts/install-common.sh
COPY manifest.sh /scripts/manifest.sh
CMD [ "sh", "-c", "/scripts/manifest.sh; bash"]

WORKDIR /workspace

