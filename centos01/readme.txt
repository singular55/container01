eclipse.ini changes

jee version made memory options match parallel version
from:
-Xms256m
-Xmx1024m
to:
-Xms512m
-Xmx2048m

Both versions have added -vm option prior to -vmargs in file:
-vm
/opt/java/jdk1.8.0_152/bin/java

Matches our HPC setup for java
