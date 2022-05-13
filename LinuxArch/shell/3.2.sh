#!/bin/bash

cat <<EOF >>brightup.sh
#!/bin/sh
# Created on $(date) # : <<-- this will be evaluated before cat;
echo "\$HOME will not be evaluated because it is backslash-escaped"
EOF
