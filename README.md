# tensorboard_jhm
This extension fixes `%tensorboard` magics to work with [jupyter_tensorboard](https://github.com/InfuseAI/jupyter_tensorboard). It is useful on jupyerhub servers where you cannot open a distinct port for each tensorboard instance or when using DockerSpawner. 

## Installation
```
pip install git+https://github.com/poiug07/tensorboard_jhm.git
```

## Usage
Load extension:
```python
%load_ext tensorboard_jhm
```

To use:
```python
%tensorboard --logdir . --h 500
```

## Simple docs
`--logdir dir/to/logs` - Path to directory where tensorboard instance is running. Default: `Jupyter.notebook.base_url`

`--h 500` - Height of resulting iframe in pixels(px). Default: `640`

!Note:
* Requires running tensorboard instance. This magics does not spawn tensorboard instance.
* Overwrites default %tensorboard magics

## Acknowledgement
This extension was inspired by [mltooling](https://github.com/ml-tooling/ml-workspace/) patch for jupyter_tensorboard.