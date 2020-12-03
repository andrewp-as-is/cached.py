<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/cached.svg?maxAge=3600)](https://pypi.org/project/cached/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/cached.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/cached.py/actions)

### Installation
```bash
$ [sudo] pip install cached
```

#### Examples
`@cached` decorator

```python
>>> from cached import cached

>>> @cached
    def func(*args, **kwags):
```

`cached(function)` function
```python
>>> from cached import cached

>>> def func(*args, **kwags):
        ...
>>> cached(func)()
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
