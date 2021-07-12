oc project python-hello
oc delete all --all -n python-hello
oc new-app python~https://github.com/cheevatee/python-hello -e APP_FILE=hello.py -l app=monitor-app-metrics -n python-hello
sleep 10
oc logs -f python-hello-1-build -n python-hello
oc expose svc python-hello -l app=monitor-app-metrics -n python-hello
sleep 5
oc get po -o wide -n python-hello
oc get route -n python-hello
