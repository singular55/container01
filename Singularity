Bootstrap:docker
From:centos:7

%labels
MAINTAINER singular55

%environment
	LANG=C.UTF-8
	# couldn't change LC_ALL on target
	#LC_ALL=C.UTF-8
	PATH=/bin_override:$PATH
	LIBRARY_PATH=/lib_override:$LIBRARY_PATH
	LD_LIBRARY_PATH=/lib_override:$LD_LIBRARY_PATH
	#WORKDIR=/work
	WRITEABLE=~/Container_Writeable
	#export LC_ALL LANG PATH LIBRARY_PATH LD_LIBRARY_PATH WORKDIR
	export LANG PATH LIBRARY_PATH LD_LIBRARY_PATH WRITEABLE

%setup
	mkdir -p $SINGULARITY_ROOTFS/lib_override
	mkdir -p $SINGULARITY_ROOTFS/bin_override
	#mkdir -p $SINGULARITY_ROOTFS/work




	## mysql - full install
	# https://dev.mysql.com/downloads/file/?id=495278 - login
	# https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.20-linux-glibc2.12-x86_64.tar.xz
	#wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.20-linux-glibc2.12-x86_64.tar.xz -O /tmp/mysql.tar.xz
	#tar -xf /tmp/mysql.tar.xz -C $SINGULARITY_ROOTFS/bin_override
	#rm /tmp/mysql.tar.xz




%post
	
	#yum --enablerepo=extras install -y epel-release
	yum -y install epel-release	
	
	#setup intel repos
	#yum-config-manager --add-repo https://yum.repos.intel.com/setup/intelproducts.repo
	yum-config-manager --add-repo https://yum.repos.intel.com/intelpython/setup/intelpython.repo
	
	# key fails to authenticate repo?
	#rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
	# new key
	rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2023.PUB
	
	yum repolist
	#yum install -y wget python3 
	yum install intelpython3 intel-mpi



	#fix some X / DBus issues?
	#dbus-uuidgen > /var/lib/dbus/machine-id



%files
	#eclipse.ini eclipse.ini
	#eclipse-parallel.ini eclipse-parallel.ini

%runscript
	#exec /bin/echo "Hi there, container runscript!"
	#exec /usr/bin/meld

	mkdir -p ${WRITEABLE}
	touch ${WRITEABLE}/HiThere

	/bin/echo "Config files should go in ${WRITEABLE}."


#%apprun meld
	#exec meld "$@"


#%apprun eclipse
	#exec /bin_override/eclipse/eclipse "$@"

