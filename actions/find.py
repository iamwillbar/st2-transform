from st2common.runners.base_action import Action

from objectpath import *
import json

class FindAction(Action):
  def run(self, data, path):
    tree = Tree(data)
    return list(tree.execute(path))
