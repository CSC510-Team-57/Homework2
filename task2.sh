grep -o -e "CSC510" -e "sample" dataset1/file*|
uniq -c|
cut -c7-|
grep -E "^[^12] .*:CSC510|^[1-9][0-9].*:CSC510|^[^0].*:sample"|
cut -d: -f1|
tac|
uniq -d -s 2|
sort -r|
cut -c3-|
sed -e 's|dataset1/file_|filtered_|g'