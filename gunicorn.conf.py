import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = "127.0.0.1:8000"
errorlog = '/home/ubuntu/logs/gunicorn-error.log'  # Make sure you have the log folder create
accesslog = '/home/ubuntu/logs/gunicorn-access.log'
loglevel = 'debug'