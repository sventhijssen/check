import time
from datetime import datetime

from networkx import Graph

from aux import config
from synth.CrossbarMapping import CrossbarMapping
from aux.MappingMethod import MappingMethod
from synth.VHLabeling import VHLabeling


class COMPACT(MappingMethod):

    def __init__(self):
        """
        The class COMPACT initializes the framework.
        """
        super(COMPACT, self).__init__()
        self.labeling = None

    def map(self, graph: Graph, layers: int = 1):
        """
        Given a graph, and optionally a
        :param graph:
        :param layers:
        :return:
        """
        print("COMPACT started")
        print(datetime.now())
        self.start_time = time.time()
        self.log += 'COMPACT version: {}\n'
        self.log += 'Nodes: {}\n'.format(len(graph.nodes))
        self.log += 'Edges: {}\n'.format(len(graph.edges))

        config.log.add('COMPACT version: VH-labeling\n')
        config.log.add('Gamma: {}\n'.format(config.gamma))
        config.log.add('Nodes: {}\n'.format(len(graph.nodes)))
        config.log.add('Edges: {}\n'.format(len(graph.edges)))
        vh_labeling = VHLabeling(graph)
        self.labeling = vh_labeling.label()
        crossbar_mapping = CrossbarMapping(graph)

        self.crossbar = crossbar_mapping.map(self.labeling)
        self.end_time = time.time()

        config.log.add('COMPACT time (s): {}\n'.format(self.end_time - self.start_time))

        print("COMPACT stopped")
        
        return self.crossbar

    def get_log(self) -> str:
        v, h, vh = VHLabeling.get_labels(self.labeling)
        log = ''
        log += 'Label V: {}\n'.format(v)
        log += 'Label H: {}\n'.format(h)
        log += 'Label VH: {}\n'.format(vh)
        # log += self.labeling.get_log()
        log += 'COMPACT time (s): {}\n'.format(self.end_time - self.start_time)
        # config.log_file.content += log
        return log
