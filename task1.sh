ps a | grep infinite.sh
kill $(ps a | grep infinite.sh | grep -v grep | awk '{print $1}')
