# Test application

## Running

The application depends on flask, after installing the dependencies you can
run the application by executing the `bin/testapp` file.


## Tasks


### 1. List available data when calling `GET /`

The `find` function only returns dummy data.

Search through the given path and return all files and directories that are
not hidden.



### 2. Remove top directory from `GET /`

When calling `GET /` we're currently getting the whole path. The root directory
should be removed from the path.

Current functionality returns the following:

```
["./tasks/2019-09-23/..."]
```

After this fix the correct return should be:

```
["2019-09-23/..."]
```


### 3. Return appropriate response for timeout

When executing a task by calling `POST /` the `run_task` function may timeout
and throw a `TimeoutError`. Instead of crashing the request should return an
error message and appropriate error code.



### 4. Add endpoint to retrieve a finished task

Tasks are stored in a directory structure. The ID of a task is in the format
`<date>/<time>`. Add a endpoint that accepts a call to `GET /<date>/<time>`.
The request should lookup to see if a task exists with that given date/time
and return the data or an error.



### 5. Store tasks that crashed

Only tasks that was successfully completed tasks are stored. Store all the results
but add a flag in the results that tells the caller if request was successfull or
not. 


### 6. Make it async

Currently the task is blocking the entire request. Allow caller to give a flag
which controlls whetever `run_task` should run in backgournd
