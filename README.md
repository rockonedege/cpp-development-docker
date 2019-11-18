# cpp-development-docker
Dockerfiles with some c++ tools pre-configured.

Based on conanio/gcc or conanio/clang, additional tools include:

- vcpkg
- cppcheck
- clang-tidy
- clang-format
- cmake-format
- dot

## Getting Started:

pre-built images are available on Docker Hub:
```sh
docker pull tomgee/cpp-dev-clang
``` 
or
```sh
docker pull tomgee/cpp-dev-gcc
```

## How To Build Images

For people who need to build it locally,

Run 
```python
python script/run.py
```
to generate Dockerfiles into `/release` folder.

## How To Create Containers

Run 
```python
python example/run-container.py
```
to generate ccontainers.