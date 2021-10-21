# General
This auxiliary repository can be used to tune the mathematical pendulum environment used [here](https://github.com/MarlonMueller/stable-baselines3-contrib/tree/feat/safety-wrappers).

The repository adapts [RL Baselines3 Zoo](https://github.com/DLR-RM/rl-baselines3-zoo)'s tuning procedure.<br />
RL Baselines3 Zoo uses [Optuna](https://optuna.org) for optimizing the hyperparameters.<br />
Please have a look at the main repository and `RL Baselines3 Zoo/README.md` for more information.<br />

## Example

```
taskset --cpu-list 0 python3.8 -m train --env MathPendulum-v0 -optimize --n-trials 500 --n-jobs 1 --sampler skopt --pruner none --n-startup-trials 10 --n-evaluations 1 --algo a2c  -n 75000 --eval-episodes 25 --no-optim-plots
```

```
taskset --cpu-list 0 python3.8 -m train --env MathPendulum-v0 -optimize --n-trials 500 --n-jobs 1 --sampler skopt --pruner none --n-startup-trials 10 --n-evaluations 1 --algo ppo  -n 75000 --eval-episodes 25 --no-optim-plots
```

Note that these examples only optimize final reward performance since --n-evaluations 1.<br />
Please have a look at `RL Baselines3 Zoo/train.py` for more information.

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
