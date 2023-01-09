## Install for dev

```
pip install -e .
```

## Undo install for dev

```
pip uninstall mycli
```

## Usage

```
mycli --help
```

## Change command

Edit mycli to desired from `setup.py`

``` python
# setup.py

setup(
    entry_points={
        'console_scripts': [
            'mycli = cli.main:entry_point'
        ]
    }
)
```

## Change package name and version

edit file `cli/__version__.py`

## Build

```
python setup.py bdist_wheel
```

output path is `dist/mycli-1.0.0-py3-none-any.whl`
