# Steps to reproduce

``` python -m wps.server ```
``` python -m wps.test ```

This should yield an error message: 

``` 
    Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "C:\Users\lang_m13\AppData\Local\Continuum\miniconda3\envs\logic\lib\multiprocessing\spawn.py", line 105, in spawn_main
        exitcode = _main(fd)
    File "C:\Users\lang_m13\AppData\Local\Continuum\miniconda3\envs\logic\lib\multiprocessing\spawn.py", line 115, in _main
        self = reduction.pickle.load(from_parent)
    EOFError: Ran out of input
 ```