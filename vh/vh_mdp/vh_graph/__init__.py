from gym.envs.registration import register
from gym.error import Error

try:
    register(
        id='vh_graph-v0',
        entry_point='vh_graph.envs:VhGraphEnv',
    )
except Error:
    # This repository imports the same package through both ``vh.vh_mdp`` and
    # ``vh_mdp``.  Gym only permits one registration for a given id.
    pass
