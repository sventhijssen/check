## Command line
Using command line, one can run the program using the following template:

```bash
python3 cli/main.py new_log LOG_NAME | read BENCHMARK_NAME | BDD_TYPE | write_bdd BDD_FILENAME | COMPACT 
```

#### Log file
It is best to record your experiments with a log. To set up a new log, use ```new_log LOG_FILENAME```. It is best practice to use the file extension ``.log``. Note that a log file will be overridden when the same log name is used.

#### BDD type
Two BDD types can be used: ```robdd``` and ```sbdd```. The BDD type ```robdd``` can be used with the flag ```-m``` to merge multiple single-output ROBDDs.

#### XBAR file
One can write a crossbar to file using the command ```write_xbar XBAR_FILENAME```. It is best practice to use the file extension ``.xbar``.
Further, one can read a crossbar from file using the command ```read_xbar XBAR_NAME XBAR_FILENAME```.

#### COMPACT
COMPACT can be called using optional arguments. See https://github.com/sventhijssen/compact/tree/compact2/examples for more information.

#### ENUM
For brute-force enumeration, the command ```enum SPECIFICATION``` must be used. 
A specification file is required and must be the first argument. 
Further, the specification file must be a Verilog file (see example.py).
```bash
python3 cli/main.py new_log t481.log | read benchmarks/t481.pla | robdd -m | compact | enum t481.v
```

Optionally, one can set a sampling size using the flag ```-s SAMPLING_SIZE``` where ```SAMPLING_SIZE``` is an integer.
```bash
python3 cli/main.py new_log t481.log | read benchmarks/t481.pla | robdd -m | compact | enum t481.v -s 100
```

#### CHECK
For the framework CHECK, the command ```check SPECIFICATION``` must be used. By default, dynamic graph extraction is used.
A specification file is required and must be the first argument. 
Further, the specification file must be a Verilog file (see example.py).
```bash
python3 cli/main.py new_log t481.log | read benchmarks/t481.pla | robdd -m | compact | check t481.v
```

Alternatively, if one wants to use static graph extraction, then the flag ```-static``` can be used.
```bash
python3 cli/main.py new_log t481.log | read benchmarks/t481.pla | robdd -m | compact | check t481.v -static
```

Optionally, one can run sampling in parallel using the flag ```-s SAMPLING_SIZE``` where ```SAMPLING_SIZE``` is an integer.
```bash
python3 cli/main.py new_log t481.log | read benchmarks/t481.pla | robdd -m | compact | enum t481.v -static -s 100
```

To record the statistics (i.e. number of paths, number of literals), one can use the flag ```-r```.
```bash
python3 cli/main.py new_log t481.log | read benchmarks/t481.pla | robdd -m | compact | enum t481.v -r -s 100
```

## Examples
#### Equivalence
In the file [_example_equivalence.py_](example_equivalence.py), an example is provided to check the equivalence of a crossbar design and its specification _without_ alterations.

#### Non-equivalence
In the file [_example_non_equivalence.py_](example_non_equivalence.py), an example is provided to check the equivalence of a crossbar design and its specification _with_ alterations.
