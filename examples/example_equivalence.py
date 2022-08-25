import os
from pathlib import Path

from cli.Program import Program


directory = Path(os.getcwd())
benchmark_name = "misex1"

log_filename = benchmark_name + ".log"
log_filepath = directory.joinpath(log_filename)

# The benchmark's specification in Verilog
specification_filename = benchmark_name + ".v"
specification_filepath = directory.joinpath("benchmarks").joinpath(specification_filename)

try:
    program = Program()
    program.execute("new_log {} | read {} | robdd -m | compact | check {} -s 20 -r".format(log_filepath, specification_filepath, specification_filepath))
except Exception as e:
    print(e)
