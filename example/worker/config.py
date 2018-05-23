"""Configuration file for Celery."""

import os


# Set broker url.
broker_url = os.environ["BROKER_URL"]

# Register tasks module.
imports = ("worker.tasks",)

# Ignore results of all tasks.
task_ignore_result = True

# Global time limit (in seconds) for tasks. If this is reached, the worker
# processing the task will be killed and replaced.
task_time_limit = 240

# Kill workers and start a new one after this many tasks to prevent memory
# leaks.
worker_max_tasks_per_child = 50
