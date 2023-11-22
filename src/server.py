import os
from fastapi import FastAPI

from Method import get_timestamp


app = FastAPI()

@app.get('/')
def index() -> dict[str, str]:
    return {
        'ENV': os.environ.get('ENV') or '',
        'timestamp': get_timestamp()
	}
