# Meson Build

To install, you need to make sure that you have meson install in your environment.

Then, run the following commands:

### Install
Install the subprojects
```bash
mkdir -p subprojects
meson wrap install robin-map
meson wrap install nanobind
```

Then install like a regular python project with pip:
```bash
pip install .
```