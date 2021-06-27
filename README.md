# ng-lgas

A Python Library that offers a list of local government areas in Nigeria as well as their coordinates (latitudes and longitudes).


## Installation

`ng-lgas` is available on [PYPI](https://pypi.python.org/pypi/ng-lgas/) <https://pypi.python.org/pypi/ng-lgas/>.
Install with ``pip`` i.e.



    pip install ng-lgas


### Usage

```python
from ng_lgas import NG_LGA

ng_lgas = NG_LGA()
print(ng_lgas.get_state_codes())
print(ng_lgas.get_by_state_code('KW'))
```

### Running Tests

```shell
python -m unittest
```

