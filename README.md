# General
This auxiliary repository can be used to tune the mathematical pendulum environment used [here]().

The repository adapts [RL Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo)'s tuning procedure. RL Baselines3 Zoo uses [Optuna](https://optuna.org) for optimizing the hyperparameters.

Please have a look at the main repository and `RL Baselines3 Zoo/README.md` for more information.

# Adapted Project Structure
To modify or extend this work, note that the following files have been added or modified compared to RL Baselines3 Zoo (Sep. 2021). The modifications affect only A2C and PPO. A specific environment configuration is hard-coded.

```
RL Baselines3 Zoo/
├── hyperparams/ <- Untuned default hyperparameters mathematical pendulum
│   ├──a2c.yml
│   └──ppo.yml
├── utils/
│   ├── pendulum/ <- Mathematical pendulum environment
│   │   ├── assets/
│   │   │   ├── README.md
│   │   │   └── clockwise.png
│   │   ├── __init__.py
│   │   ├── math_pendulum_env.py
│   │   ├── pendulum_roa.py
│   │   └── safe_region.py
│   ├── hyperparams_opt.py <- Adapted hyperparameter samplers for A2C and PPO
└── └── import_envs.py <- Register mathematical pendulum environment

```
