
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask,jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/")
@app.route("/monitor")
def main():
    print (str(datetime.now())+": Processing /monitor or / functionality")
    return jsonify({"result":"True"}),200

@app.route("/pause")
def pause_jobs():
    print (str(datetime.now())+": Pausing Jobs")
    sched.pause()
    return jsonify({"result":"True"}),200

@app.route("/resume")
def resume_jobs():
    print (str(datetime.now())+": Resuming Jobs")
    sched.resume()
    return jsonify({"result":"True"}),200


def job_function_1():
    print (str(datetime.now())+": job_function_1: Executing")

def job_function_2():
    print (str(datetime.now())+": job_function_2: Executing")

sched = BackgroundScheduler(daemon=True)
sched.add_job(job_function_1,'interval',seconds=10)
sched.add_job(job_function_2,'interval',seconds=5)
sched.start()



if __name__ == '__main__':
    app.run()