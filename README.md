# cpp-development-docker
Dockerfiles with some c++ tools pre-configued.

Based on conanio/gcc or conanio/clang, additional tools includes:

- vcpkg
- cppcheck
- clang-tidy
- clang-format
- cmake-format
- dot

Run 
```python
python script/run.py
```
to generate Dockerfiles into `/release` folder.