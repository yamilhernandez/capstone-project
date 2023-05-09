apt-get update
apt-get install tk --yes
gunicorn --bind 0.0.0.0:8000 DEPO.asgi -w 4 -k uvicorn.workers.UvicornWorker