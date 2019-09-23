from flask import Flask, request
from testapp.task import run_task, save, find

import os

app = Flask(__name__)

storagedir = "./tasks"


@app.route("/", methods=['GET', 'POST'])
def list_or_create():
    """
    List all completed tasks or create a new one

    When listing it should return a list of full paths starting from root
    """

    if request.method == 'POST':
        finished, task = run_task(request.get_data().decode())
        save(storagedir, (finished, task))
        
        return task
    else:
        
        return "%s\n" % (format_tasks(find(storagedir)),)


def format_tasks(item, path=[]):
    if str == type(item):
        path += [item]
        return [os.path.join(*(path + [item]))]
    else:
        root, children = item
        resp = []

        for e in children:
            resp += format_tasks(e, path + [root])

        return resp
        
