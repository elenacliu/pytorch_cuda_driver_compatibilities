# Compute Capabilities of each PyTorch Package

The project is a utility tool for PyTorch installation on Linux64 machine.

Checks the compute capabalities of each pytorch package in the [PyTorch conda channel](https://anaconda.org/pytorch) by running `cuobjdump` from the [CUDA Toolkit](https://docs.nvidia.com/cuda/) on the included `*.so` files.

For results see [table.md](table.md).


# References

Here are some great resources that provide insight into compatibility of cuda:

[https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#major-components](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#major-components)

[https://jia.je/software/2021/12/26/nvidia-cuda/](https://jia.je/software/2021/12/26/nvidia-cuda/)

[https://jia.je/software/2022/07/06/install-nvidia-cuda/](https://jia.je/software/2022/07/06/install-nvidia-cuda/)

[https://github.com/moi90/pytorch_compute_capabilities](https://github.com/moi90/pytorch_compute_capabilities)
