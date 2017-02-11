# this script runs async/bg on the A8 node(s)
# output in shared dir A8/script_out.txt

sleep 3.$[RANDOM %100]
date +%F >> A8/script_out.txt
