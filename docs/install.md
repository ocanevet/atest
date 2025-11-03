# Installation

## In a conda environment

```
(base) $ conda create -y -n ztest python=3.11 pip uv
(base) $ conda activate ztest
(ztest) $ uv pip install --extra-index-url https://test.pypi.org/simple/ ztest
```
