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

## Build

```
python setup.py bdist_wheel
```