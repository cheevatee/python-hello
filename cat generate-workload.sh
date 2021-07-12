
url=python-hello-python-hello.apps.cluster-sktxn.sktxn.sandbox419.opentlc.com

random_list() {
        array[0]="/"
        array[1]="/one"
        array[2]="/two"
        array[3]="/three"
        array[4]="/four"
        array[5]="/error"
        size=${#array[@]}
        index=$(($RANDOM % $size))
        rand_url=${array[$index]}
}

generate_load() {
        siege -c 50 -t 30S $url$rand_url
}

while true
do
        random_list
        generate_load
        rand_url=""
        sleep 3
done
