# python-hello

New project name python-hello
~~~
oc new-project python-hello
~~~

Deploy python-hello
~~~
oc new-app python~https://github.com/cheevatee/python-hello -e APP_FILE=hello.py
oc expose svc python-hello
oc get route
~~~

Create script for re-deploy python-hello
~~~
cat <<EOF >> deploy-python-hello.sh
oc project python-hello
oc delete all --all -n python-hello
oc new-app python~https://github.com/cheevatee/python-hello -e APP_FILE=hello.py -n python-hello
sleep 10
oc logs -f python-hello-1-build -n python-hello
oc expose svc python-hello -n python-hello
sleep 5
oc get po -o wide -n python-hello
oc get route -n python-hello
EOF
chmod 755 deploy-python-hello.sh
~~~

Re-deploy python-hello

~~~
./deploy-python-hello.sh
~~~

