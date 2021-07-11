# python-hello

Deploy via OpenShift
~~~
oc new-app python~https://github.com/cheevatee/python-hello -e APP_FILE=hello.py
oc expose svc python-hello
oc get route
~~~
