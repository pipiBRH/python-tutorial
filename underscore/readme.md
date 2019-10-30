# underscore of veriables

1. foo_
2. _foo
3. \_\_foo\_\_
4. __foo

## foo_

Avoid `built-in keywords` or `built-in functions`

## _foo

`pretend, simulate private functions or variables`

#### You don't want target
*  Access directly
* Import directly

[doc](https://docs.python.org/3/tutorial/classes.html#private-variables)
```
“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python. However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated as a non-public part of the API (whether it is a function, a method or a data member). It should be considered an implementation detail and subject to change without notice.
```

[PEP 257](https://pep257.readthedocs.io/en/latest/error_codes.html#grouping)
```
Unconstrained in D103: Missing docstring in public function
```

## __foo__

[PEP8](https://www.python.org/dev/peps/pep-0008/#naming-conventions)
```
__double_leading_and_trailing_underscore__ : "magic" objects or attributes that live in user-controlled namespaces. E.g. __init__ , __import__ or __file__ . Never invent such names; only use them as documented.
```

[stackoverflow](https://stackoverflow.com/questions/27965088/never-invent-such-names-only-use-them-as-documented-who/27965109#27965109)
```
So, if you are not a Python core developer or writing a PEP that may be one day become part of the Python standard library or core language definition, try to stay away from using dunder names in your API.
```

#### Are there any exceptions?
Look at [SQLAlchemy](https://github.com/zzzeek/sqlalchemy)

`__tablename__`, `__table__`, `__mapper__`

## __foo
[name mangling](https://en.wikipedia.org/wiki/Name_mangling#Python)

[PEP8](https://www.python.org/dev/peps/pep-0008/)
```
If your class is intended to be subclassed, and you have attributes that you do not want subclasses to use, consider naming them with double leading underscores and no trailing underscores. This invokes Python's name mangling algorithm, where the name of the class is mangled into the attribute name. This helps avoid attribute name collisions should subclasses inadvertently contain attributes with the same name.
```