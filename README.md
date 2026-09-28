# Configuration Lab

Keeping API keys out of source code using `.env` and `python-dotenv`.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env      # Windows: copy .env.example .env
```

Open `.env` and replace `your_key_here` with your real API key, then run:

```bash
python main.py
```

`.env` is listed in `.gitignore`, so the real key is never pushed to GitHub.
