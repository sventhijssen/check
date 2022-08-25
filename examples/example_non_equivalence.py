import os
import random
from itertools import product
from pathlib import Path

from aux.CrossbarReader import CrossbarReader
from aux.CrossbarWriter import CrossbarWriter
from cli.Program import Program
from core.Literal import Literal

directory = Path(os.getcwd())
benchmark_name = "misex1"  # Change your benchmark (make sure to have its Verilog which can be obtained using ABC).

log_filename = benchmark_name + ".log"
log_filepath = directory.joinpath(log_filename)

original_xbar_filename = benchmark_name + ".xbar"
original_xbar_filepath = directory.joinpath(original_xbar_filename)

altered_xbar_filename = benchmark_name + "_altered.xbar"
altered_xbar_filepath = directory.joinpath(altered_xbar_filename)

# The benchmark's specification in Verilog
specification_filename = benchmark_name + ".v"
specification_filepath = directory.joinpath("benchmarks").joinpath(specification_filename)


def alter_xbar(seed: int = 0, nr_alters: int = 1):

    random.seed(seed)

    xbar_reader = CrossbarReader(original_xbar_filename)
    xbar = xbar_reader.read()

    for i in range(nr_alters):
        # We pick a random element from the crossbar and change its literal
        positions = list(product(range(xbar.rows), range(xbar.columns)))

        (r, c) = random.choice(positions)
        memristor = xbar.get_memristor(r, c)

        possibilities = [Literal('True', True), Literal('False', False)]

        new_literal = random.choice(possibilities)

        while memristor.literal == new_literal:
            new_literal = random.choice(possibilities)
        memristor.literal = new_literal

    xbar_writer = CrossbarWriter(xbar, altered_xbar_filename)
    xbar_writer.write()


try:
    program = Program()
    program.execute("new_log {} | read {} | robdd -m | compact | write_xbar {}".format(log_filepath, specification_filepath, original_xbar_filepath))

    # There is no command to alter a crossbar.
    # Further, if we want to compare an altered crossbar using different verification techniques
    # (enumeration, static/dynamic graph extraction), we must use the same crossbar for fair comparison.
    # Hence, we write the crossbar to file such that it can be read for these different verification techniques.
    alter_xbar()

    program.execute("read_xbar {} {} | check {} -s 10 -r -static".format(benchmark_name, altered_xbar_filepath, specification_filepath))

except Exception as e:
    print(e)
