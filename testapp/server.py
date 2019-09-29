from flask import Flask, request
from testapp.task import run_task, save, find

import os
import re
app = Flask(__name__)

storagedir = os.path.dirname(os.getcwd())


@app.route("/", methods=['GET', 'POST'])
def list_or_create():
    """
    List all completed tasks or create a new one
    When listing it should return a list of full paths starting from root
    """

    if request.method == 'POST':
        try:
            finished, task = run_task(request.get_data().decode())
        except TimeoutError as err:
            finished,task=err.args
            return "Error, Task taking long time to complete. Please try again later"
        finally:
            save(storagedir, (finished, task))
        return task
    else:
        return "%s\n" % (format_tasks(find(storagedir)),)
@app.route("/<date>/<time>")
def show_task_details(date,time):
    print(date)
    dirpath=os.path.join(storagedir,date)
    filepath=os.path.join(storagedir,date,time)
    
    try:
        if( os.path.exists(filepath) and os.path.exists(dirpath)):
            with open (filepath)as file:
                data=file.read()
            file.close()
            return data
        else:
            return "Invalid Task Details. Please check"
    except:
        return "Invalid Task Details. Please check"
    # print(time)
    return "hello"

def format_tasks(item, path=[]): 
    path=list(filter(lambda x: storagedir != x, path))
    if str == type(item):
        return [os.path.join(*(path + [item]))]
    else:
        root,children = item        
        resp = []
        for e in children:
            resp += format_tasks(e, path+[root])
        return resp