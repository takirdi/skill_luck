# Why the Reckless Win More Often Than the Careful

Two entrepreneurs meet in a café.

One has spreadsheets, forecasts, and market analyses. She acts only when the data says the odds are good.

The other buys a domain on a whim. No plan. No research. He just starts.

Ten years later… guess who hits a unicorn?

---

## The intuition

In some fields, skill rules.  
In others, **fat-tailed payoffs** dominate. A few rare wins beat many small losses.

- **K+2 (careful)** waits for clear positive expectation.
- **K+0 (reckless)** tries often. Fails often. Sometimes lands a jackpot.

When big wins are rare and unpredictable, volume can beat precision.

---

## The simulation

This repo includes a tiny model with two agents.

- **Agent 1 (K+2)**: data-driven. Acts only if recent outcomes imply positive expectation.
- **Agent 2 (K+0)**: acts without forecasting.

Each attempt has a cost. Payoffs follow a **Pareto** (heavy-tailed) distribution: many zeros, few huge wins.

Full code: [`abm_luck_vs_skill.py`](./abm_luck_vs_skill.py)

Run:
```bash
python abm_luck_vs_skill.py
```

---

## Example result

Below is a sample output showing both agents’ wealth over time.

![Simulation Result](./example_result.png)

**What it shows**
- **K+2**: smoother path. Fewer losses. Misses rare jackpots.
- **K+0**: volatile path. Many failures. Occasional massive wins.

---

## Real-world parallels

- **Startups**: most fail; a few repay the portfolio.
- **Creative work**: many flops; some change culture.
- **Moonshot investing**: many zeros; a few 100×.

---

## Closing thought

This is not a call to be reckless.  
It’s a reminder to match strategy to the world you’re in.

When outcomes are heavy-tailed i.e. follow the kind of pattern where **most attempts fail or pay little, but a few rare ones pay huge** — like startup investments, where 1 in 50 may become a billion-dollar company — **more tries** can beat **better forecasts**.  

Sometimes, in such an environment, being wrong often is the only way to be right big.