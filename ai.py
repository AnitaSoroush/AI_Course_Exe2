# code at: shorturl.at/uACQT
#                     u A QT

import random
import time
from copy import deepcopy


# ******
from sqlite3 import Time

"DFS"
"BFS"
"IDFS"
# ******

"RBFS"
"ASTAR"
#
"MINMAX"
"Q-LEARNING"


class Agent:
    def __init__(self, perceive_func=None, agent_id=None):
        self.perceive_func = perceive_func
        self.my_id = agent_id

        ######### EDITABLE SECTION #########

        self.predicted_actions = []

        ######### END OF EDITABLE SECTION #########

    def act(self):
        sensor_data = self.perceive_func(self)

        ######### EDITABLE SECTION #########

        if self.predicted_actions==[]: self.predicted_actions=self.bfs(sensor_data['Current_Env'])
        action=self.predicted_actions.pop()
        time.sleep(1)

        ######### END OF EDITABLE SECTION #########

        return action
    
    # idfs--------------------------------------------------------------------------------------------------------------

    ######### VV EDITABLE SECTION VV #########
    def idfs(self, root_env):
        depth = 1
        while True:
            result = self.dls(root_env, depth)
            if result[0]:
                return result[1]
            # snake=root_env.state.agent_list[self.my_id]
            # depth += snake.shekam + len(snake.body)
            depth += 1


    def dls(self, game, limit):  # returns [success, action]
        if game.goal_test(): return [True, "found the goal"]
        elif limit == 0: return [False, "reached limit"]

        actions_list = ["right", "left", "up", "down"]
        random.shuffle(actions_list)
        for action in actions_list:
            child_game = deepcopy(game)
            game_result = child_game.take_action(action, self.my_id)
            if 'has died' not in game_result:

                dls_result=self.dls(child_game, limit - 1)
                actions_taken = deepcopy(dls_result[1]) if type(dls_result[1]) is list else []
                actions_taken.append(action)
                if dls_result[0]:
                    return [True, actions_taken]

        return [False, "no good action found"]

    # bfs---------------------------------------------------------------------------------------------------------------

    def bfs(self, root_env):
        bfs_tree_leaves = []
        bfs_tree_leaves.append({
            "game": root_env,
            "predicted_actions": []
        })
        while True:
            bfs_node = bfs_tree_leaves.pop()
            if bfs_node["game"].goal_test():
                return bfs_node["predicted_actions"]

            actions_list = ["right", "left", "up", "down"]
            random.shuffle(actions_list)
            for action in actions_list:
                child_game = deepcopy(bfs_node["game"])
                game_result = child_game.take_action(action, self.my_id)
                if 'has died' not in game_result:
                    # a = bfs_node["predicted_actions"].copy().append(action)
                    bfs_tree_leaves.append({
                        "game": child_game,
                        "predicted_actions": bfs_node["predicted_actions"] + [action]
                    })

    # dfs---------------------------------------------------------------------------------------------------------------

    def dfs_starter(self, root_env):
        result = self.dfs(root_env)
        if result[0]:
            return result[1]

    def dfs(self, game):  # returns [success, action]
        if game.goal_test(): return [True, "found the goal"]

        actions_list = ["right", "left", "up", "down"]
        random.shuffle(actions_list)
        for action in actions_list:
            child_game = deepcopy(game)
            game_result = child_game.take_action(action, self.my_id)
            if 'has died' not in game_result:
                dfs_result = self.dfs(child_game)
                actions_taken = deepcopy(dfs_result[1]) if type(dfs_result[1]) is list else []
                actions_taken.append(action)
                if dfs_result[0]:
                    return [True, actions_taken]

        return [False, "no good action found"]

    # Sample-----------------------------------------------------------------------------------------------------------

    # def idfs(self, root_env):
    #     depth = 1
    #     while True:
    #         result = self.dls(root_env, depth)
    #         if result[0]:
    #             return result[1]
    #         snake = root_env.state.agent_list[self.my_id]
    #         depth += snake.shekam + len(snake.body)
    #
    # def dls(self, game, limit):  # returns [success, action]
    #     if game.goal_test():
    #         return [True, "found the goal"]
    #     elif limit == 0:
    #         return [False, "reached limit"]
    #
    #     actions_list = ["right", "left", "up", "down"]
    #     random.shuffle(actions_list)
    #
    #
    #     for action in actions_list:
    #         child_game = deepcopy(game)
    #         game_result = child_game.take_action(action, self.my_id)
    #         if 'has died' not in game_result:
    #
    #
    #             dls_result = self.dls(child_game, limit - 1)
    #             actions_taken = deepcopy(dls_result[1]) if type(dls_result[1]) is list else []
    #             actions_taken.append(action)
    #             if dls_result[0]:
    #                 return [True, actions_taken]
    #
    #     return [False, "no good action found"]
    #

