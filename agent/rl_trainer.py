import ray
from ray import tune
from ray.rllib.agents import ppo

class RLTrainer:
    def __init__(self, config):
        ray.init(ignore_reinit_error=True)
        self.config = config
        self.agent = ppo.PPOTrainer(config=self.config, env=self._create_env())

    def _create_env(self):
        from agent.env import TradingEnv
        return TradingEnv

    def train_one_iteration(self):
        result = self.agent.train()
        return result

    def save_checkpoint(self, path):
        return self.agent.save(path)
