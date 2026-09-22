# OIM 3641 — AI Driven App Development

This is my classwork repo for OIM 3641 at Babson. Everything I build for this
course, in-class activities, homework, and project work, lives here.

## About Me

I'm an undergrad at Babson taking OIM 3641, where I'm learning Python and using
it to work through business problems. I'm newer to programming, so a lot of
what's in this repo is me practicing the fundamentals: variables and data
structures, writing functions, calling APIs, and getting comfortable with the
tools developers actually use. I keep everything here so I can look back at how
my code has changed over the semester.

## Skills & Tools

**Languages**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=flat&logo=postgresql&logoColor=white)
![Markdown](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white)

**Libraries**

![pandas](https://img.shields.io/badge/pandas-150458?style=flat&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikitlearn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)

**Tools**

![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000?style=flat&logo=pycharm&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5FE9?style=flat&logo=uv&logoColor=white)

Some of these I'm still learning — the badges are where I'm headed this
semester, not a claim that I've mastered all of them.

## Directory Structure

The repo is one `uv` project at the root. Activities are numbered in the order
we do them, so the files read chronologically.

```
OIM3641/
├── README.md                  # you are here
├── pyproject.toml             # project dependencies, managed by uv
├── uv.lock                    # locked versions, so the env is reproducible
├── .gitignore                 # keeps .env and notebook checkpoints out of git
├── main.py                    # starter file
├── 01-llm-call.py             # In-Class Activity 1: calling the Gemini API
└── 02-python-concepts.ipynb   # In-Class Activity 2: Python fundamentals
```

As the semester goes on I'll keep adding numbered scripts and notebooks here,
and I'll break out a folder for the term project once that starts. Anything with
secrets — like a `.env` holding an API key — is gitignored and never committed.

## Install Instructions

You'll need [Git](https://git-scm.com/downloads) and
[uv](https://docs.astral.sh/uv/getting-started/installation/) installed.

Clone the repo and set up the environment:

```bash
git clone https://github.com/davina-li-01/OIM3641.git
cd OIM3641
uv sync
```

`uv sync` reads `pyproject.toml` and `uv.lock` and builds a matching virtual
environment, so you don't have to install anything by hand.

Run a script:

```bash
uv run 01-llm-call.py
```

Open the notebook:

```bash
uv run jupyter lab
```

### A note on API keys

The scripts that call an API expect a `.env` file in the project root. Create
your own — it's gitignored, so mine isn't in the repo:

```bash
# .env
GOOGLE_API_KEY=your-key-here
```

You can get a Gemini key from [Google AI Studio](https://aistudio.google.com/apikey).

## Contact / Connect

- **Email:** dli4@babson.edu
- **LinkedIn:** [linkedin.com/in/davina-li](https://www.linkedin.com/in/davina-li)
- **GitHub:** [@davina-li-01](https://github.com/davina-li-01)
