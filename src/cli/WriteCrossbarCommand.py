from typing import List

from aux import config
from aux.CrossbarWriter import CrossbarWriter
from cli.Command import Command


class WriteCrossbarCommand(Command):

    def __init__(self, args: List[str]):
        super(WriteCrossbarCommand).__init__()
        if len(args) < 1:
            raise Exception("No filename defined.")
        self.file_name = args[0]

    def execute(self) -> bool:
        context = config.context_manager.get_context()
        cw = CrossbarWriter(context.crossbars[0], self.file_name)
        cw.write()
        return False
