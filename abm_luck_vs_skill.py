"""
abm_luck_vs_skill.py
Two agents. Different rules. Rare big wins possible.

Agent K+2 (careful): acts only when recent evidence suggests positive expectation.
Agent K+0 (reckless): acts often without forecasting.

Run: python abm_luck_vs_skill.py
Outputs: shows a plot and saves 'example_result.png' in the repo root.
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Reproducibility
RNG = np.random.default_rng(42)


def pareto_payoff(alpha: float = 1.4, xm: float = 1.0) -> float:
    """
    Heavy-tailed positive payoff.
    Many small/zero gains. Rare large gains.
    """
    return xm * (1.0 + RNG.pareto(alpha))


def try_idea(q: float = 0.05, cost: float = 1.0) -> float:
    """
    Try an idea once.
    Success with prob q → Pareto payoff; else 0.
    Net = payoff - cost.
    """
    success = RNG.random() < q
    payoff = pareto_payoff() if success else 0.0
    return payoff - cost


def simulate(
    T: int = 500,
    cost: float = 1.0,
    q: float = 0.05,
    p_agent2: float = 0.6,
    N_hist: int = 50,
):
    """
    Simulate T steps.

    Agent 1 (K+2): acts only if mean of last N_hist net results > 0.
    Agent 2 (K+0): acts each step with probability p_agent2.

    Returns:
        w1, w2: np.ndarray cumulative wealth paths (length T+1).
    """
    w1 = [0.0]
    w2 = [0.0]
    history = []  # observed net results used by K+2

    for _ in range(T):
        # K+2 decision: needs positive recent average
        act1 = len(history) >= N_hist and (np.mean(history[-N_hist:]) > 0.0)
        # K+0 decision: random attempt with fixed probability
        act2 = RNG.random() < p_agent2

        r1 = try_idea(q=q, cost=cost) if act1 else 0.0
        r2 = try_idea(q=q, cost=cost) if act2 else 0.0

        if act1:
            history.append(r1)
        if act2:
            history.append(r2)

        w1.append(w1[-1] + r1)
        w2.append(w2[-1] + r2)

    return np.array(w1), np.array(w2)


def main():
    # Feel free to tweak these for your runs.
    T = 600
    cost = 1.0
    q = 0.06
    p_agent2 = 0.6
    N_hist = 50

    w1, w2 = simulate(T=T, cost=cost, q=q, p_agent2=p_agent2, N_hist=N_hist)

    plt.figure()
    plt.plot(w1, label="K+2 (careful)")
    plt.plot(w2, label="K+0 (reckless)")
    plt.xlabel("Time")
    plt.ylabel("Wealth")
    plt.title("Luck vs Skill: K+2 vs K+0")
    plt.legend()
    plt.tight_layout()

    out_path = Path("example_result.png")
    plt.savefig(out_path, dpi=200)
    print(f"Saved plot to: {out_path.resolve()}")

    # Also show interactively if running locally
    try:
        plt.show()
    except Exception:
        pass


if __name__ == "__main__":
    main()
