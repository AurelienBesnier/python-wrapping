cd wrapping
echo -e "\033[0;36mInstall wrapping.boost...\033[0m"
cd boost; pip install .; cd ..
echo -e "\033[0;36mDone !\033[0m"
echo -e "\033[0;36mInstall wrapping.cython...\033[0m"
cd cython; pip install .; cd ..
echo -e "\033[0;36mDone !\033[0m"
echo -e "\033[0;36mInstall wrapping.fortran...\033[0m"
cd fortran; pip install .; cd ..
echo -e "\033[0;36mDone !\033[0m"
echo -e "\033[0;36mInstall wrapping.nanobind...\033[0m"
cd nanobind; pip install .; cd ..
echo -e "\033[0;36mDone !\033[0m"
echo -e "\033[0;36mInstall wrapping.pybind...\033[0m"
cd pybind; pip install .; cd ../
echo -e "\033[0;36mDone !\033[0m"
echo -e "\033[0;36mInstall wrapping.shell...\033[0m"
cd shell; pip install .; cd ../..
echo -e "\033[0;36mDone !\033[0m"