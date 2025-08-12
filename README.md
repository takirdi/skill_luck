# Luck_Skill

## Getting started

This Python simulation compares two agents in a world where rare big wins dominate outcomes.

- **K+2**: cautious, acts only with positive expected value.
- **K+0**: impulsive, acts without forecasting.

Most attempts fail or pay little; a few pay huge. In such settings, volume of tries can beat precision.

## Add your files

- `abm_luck_vs_skill.py` — simulation script.  
- `requirements.txt` — dependencies.  
- `blog_post.md` — article explaining the model.  
- `example_result.png` — sample output.

## Installation

```bash
git clone git@git.wur.nl:jada001/luck_skill.git
cd luck_skill

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
python abm_luck_vs_skill.py
```
## Run in Google Colab

You can run this project directly in Google Colab without installing anything locally:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/takirdi/skill_luck/blob/main/run_simulation.ipynb)


Generates a plot and saves `example_result.png`.

## Visuals

![Simulation Result](./example_result.png)

## Roadmap

- Multi-run statistics.  
- Compare Pareto vs lognormal payoffs.  
- Add adaptive decision rules.

## Authors and acknowledgment

Author: *Kaleb, J*  
Inspired by Pluchino et al. (2018) and level-k reasoning.

## License

MIT License.
