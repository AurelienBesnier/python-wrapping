project(
  'wrapping.meson',
  'cpp',
  version: '0.0.1',
)

py = import('python').find_installation()
nanobind_dep = dependency('nanobind', static: true)
py.extension_module(
  'example',
  sources: ['src/cpp/ext_nano.cpp'],
  dependencies: [nanobind_dep],
  install: true,
  subdir: 'wrapping/meson',
  install_rpath: '$ORIGIN'
)

python_sources = [
  'src/wrapping/meson/__init__.py',
]

py.install_sources(
  python_sources,
  pure: false,   # Will be installed next to binaries
  subdir: 'wrapping/meson' # Folder relative to site-packages to install to
)
