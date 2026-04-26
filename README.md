# Decorators Example

This module demonstrates basic Python decorators in `deocrators.py`.

## What is included

- `my_decorator(func)`  
  A simple decorator that prints:
  - `"before"` before calling the function
  - `"after"` after calling the function

- `calc_runtime(func)`  
  A decorator that measures function execution time and prints:
  - `"Start decorator"`
  - elapsed time using `time.time()`
  - `"end decorator"`
  It also returns the wrapped function result.

## Imports

- `time` is used by `calc_runtime` to calculate runtime.
- `stat` is currently imported but not used.

## Example usage

### 1) Basic decorator

```python
@my_decorator
def hello():
    print("Hello, World!")

hello()
```

Expected console output:

```text
before
Hello, World!
after
```

### 2) Runtime decorator

```python
@calc_runtime
def delay_by(t):
    time.sleep(t)
    print("testing test func")
    time.sleep(1)
    print("Ended test function")
    return "finished delay function"

print(delay_by(t=4))
```

Expected console output format:

```text
Start decorator
testing test func
Ended test function
Time execution: <seconds> Secs.
end decorator
finished delay function
```

`<seconds>` will vary by machine and workload (about 5 seconds in this example).

## Notes

- The filename is `deocrators.py` (spelling as currently used in the project).
- Consider removing unused imports (like `stat`) when cleaning up the module.
