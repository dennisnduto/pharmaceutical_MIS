# Gunicorn configuration for Render.com deployment
import os
import multiprocessing

# Create logs directory if it doesn't exist
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Server socket
bind = "0.0.0.0:8000"  # Using TCP socket for Render.com

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000

# Restart workers after this many requests to prevent memory leaks
max_requests = 1000
max_requests_jitter = 50

# Timeout for handling requests
timeout = 30
keepalive = 2

# Logging
loglevel = "info"
accesslog = os.path.join(log_dir, 'access.log')
errorlog = os.path.join(log_dir, 'error.log')
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = 'pharma_mis'

# Server mechanics
preload_app = True
pidfile = os.path.join(log_dir, 'gunicorn.pid')

# Environment
raw_env = ['ENVIRONMENT=production']
