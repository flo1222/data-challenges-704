## Objective

Understand how test works and implement your first test

Install the code coverage package `pip install coverage`.

## Run tests

Inspect `mlproject/lib.py`  and `tests/lib_test.py`
Inspect Makefile and run:
```bash
make test
```

You just run all tests under `test/`

## Create your own test

You'll now test `haversine()` function:

- Create a `tools.py` file under `mlproject/` here you'll implement the `haversine()` function taking 4 coordinates as input and returning haversine distance
- Create `tool_test.py` file under `tests/` testing your `haversine()`

Run `make test` again and check that your test passes
