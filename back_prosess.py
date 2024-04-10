from celery import Celery

# Celeryインスタンスの設定
app = Celery('tasks', broker='redis://localhost:6379/0')

# タスクの定義
@app.task
def add(x, y):
    return x + y
