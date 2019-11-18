echo '======================================================='
echo '    Additional C++ tools in this docker environment'
echo
echo ninja $(ninja --version) 
echo $(cppcheck     --version)
echo $(cmake        --version | grep -i -C 0 'version')
echo $(clang-format --version | grep -i -C 0 'version')
echo $(clang-tidy   --version | grep -i -C 0 'version')
dot          -V | grep -i -C 0 'version'
cc           --version  | grep -i -C 0 'version'
vcpkg        version 

# vcpkg list 
echo '======================================================='
