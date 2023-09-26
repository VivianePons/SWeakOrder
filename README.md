# s-Weak Order and s-Permutahedron

You will find here some raw research code and a demo related to the following series of papers:

[1] C. Ceballos and V. Pons. The s-weak order and s-permutahedra I: Combinatorics and Lattice Structure [arXiv:2212.11556](https://arxiv.org/abs/2212.11556), 2022

[2] C. Ceballos and V. Pons. The s-weak order and s-permutahedra II: The combinatorial complex of pure intervals [arXiv:2309.14261](https://arxiv.org/abs/2309.14261), 2023

[3] C. Ceballos and V. Pons. The s-weak order and s-permutahedra . In *31st International Conference on "Formal Power Series and Algebraic Combinatorics" (FPSAC 2019)*, volume 82B, Art. 76. Hanover, United States, 2019. Séminaire Lotharingien de Combinatoire. 


## Install

These files worksheets need the software [SageMath](https://www.sagemath.org/) (v 9.1). For most of the code, this is all that is needed. 

For printing the lattices as nice pdf pictures, we use [ImageMagick](https://imagemagick.org/index.php) and [dot2Tex](https://dot2tex.readthedocs.io/en/latest/) (through sage). On Linux, this can be installed this way:

```console
$ sudo apt-get -qy install imagemagick
$ sage -pip install dot2tex
```

The default configuration of ImageMagick does not convert pdf into png by default, which is necessary for printing laTeX created images directly in the notebook. This can be changed through the `policy.xml` file of the application. You can use the file [policy.xml](app/.magic/policy.xml) provided here.
