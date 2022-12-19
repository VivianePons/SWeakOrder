# s-Weak Order and s-Permutahedron

[![Binder](https://beta.mybinder.org/badge.svg)](https://mybinder.org/v2/gh/VivianePons/SWeakOrder/main)


You will find here some raw research code and a demo related to the following series of papers:

[1] C. Ceballos and V. Pons. The s-weak order and s-permutahedra I: Combinatorics and Lattice Structure
[2] C. Ceballos and V. Pons. The s-weak order and s-permutahedra . In *31st International Conference on "Formal Power Series and Algebraic Combinatorics" (FPSAC 2019)*, volume 82B, Art. 76. Hanover, United States, 2019. Séminaire Lotharingien de Combinatoire. 


They present examples and implementations of the computations and algorithms described in the papers. You can run them yourself and experiment by [clicking on this binder link](https://mybinder.org/v2/gh/VivianePons/SWeakOrder/main). (Expect to wait a few minutes for the server to load).

## Install

These files worksheets need the software [SageMath](https://www.sagemath.org/) (v 9.1). For most of the code, this is all that is needed. 

For printing the lattices as nice pdf pictures, we use [ImageMagick](https://imagemagick.org/index.php) and [dot2Tex](https://dot2tex.readthedocs.io/en/latest/) (through sage). On Linux, this can be installed this way:

```console
$ sudo apt-get -qy install imagemagick
$ sage -pip install dot2tex
```

The file [policy.xml](app/.magic/policy.xml) is an ImageMagick policy file which allows for converting pdf into png (not default), which makes it possible to show some of the latex created images directly in the notebook.
