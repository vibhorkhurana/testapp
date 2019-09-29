import time
import random
from datetime import datetime
import os

fllist=[]
def run_task(args, timeout=5, runtime=None,async=False):
    """
    Perform a potentialy slow operation. Returns data
    or throws a TimeoutError if operation takes longer than `timeout`
    """
    success=True
    started = datetime.utcnow()

    if runtime is None:
        runtime = random.uniform(0, timeout * 2)

    if runtime > timeout:
        if async:
            time.sleep(timeout)
        success=False
        # raise TimeoutError("work was not completed in time")
    else:
        success=True
        if async:
            time.sleep(runtime)

    finished = datetime.utcnow()
    duration = (finished - started).total_seconds()

    results = """
    {
        "started": %d,
        "duration": %d,
        "results": %d,
        "args": "%s",
        "success":%s
    }
    """ % (started.timestamp(), duration, runtime, args,success)

    if(success==False):
        raise TimeoutError(finished,results)
    else:
        return (finished, results)



def save(basedir, task):
    """
    Save the results of a task to `basedir`
    """

    finished, results = task


    targetdir = os.path.join(basedir, finished.strftime("%Y-%m-%d"))

    try:
        os.mkdir(targetdir)
    except FileExistsError:
        pass

    target = os.path.join(targetdir, finished.strftime("%H:%M:%S"))
    with open(target, "w") as fd:
        fd.write(results)

    return target


def find(path, depth=-1):
    fllist=[]
    """
    Recursively find all directories and files under `path`.

    Returns a tuple containing the file path and a list of children.
    A child element can represent a file (string) or a sub-director (tuple).

    Given the following directory structure:

    ./root
    ./root/file
    ./root/sub-directory
    ./root/sub-directory/deep-file
    ./root/empty-directory

    and called with a the argument `path="./root"` the return value should be:

    ("./root", [
        "file",
        ("sub-directory", ["deep-file"]),
        "empty-directory"
    ])
    """
    for x in filter( lambda f: not f.startswith('.'), os.listdir(path)):
        if(os.path.isdir(os.path.join(path,x))==True):
            for root,dir,files in os.walk(os.path.join(path,x)): 
                fllist.append((os.path.basename(root),files))
        else:
            fllist.append(x)

    return(path,fllist)
    # return ('', fllist)