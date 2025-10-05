# Clean Breathing ML

## Overview

FastAPI service that serves an air quality prediction model with a simple HTML form and JSON API.

## Local setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --reload
```

Open http://127.0.0.1:8000 in your browser to use the web UI.

## Deployment notes

- Heroku expects a `Procfile` at the project root. This project runs using:

	```
	web: uvicorn app:app --host=0.0.0.0 --port=${PORT}
	```

- Ensure environment variable `PORT` is provided by the platform (Heroku does this automatically).

