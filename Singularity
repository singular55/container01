Bootstrap:docker
From:conda/miniconda3-centos7

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

#%setup
	#mkdir -p $SINGULARITY_ROOTFS/lib_override
	#mkdir -p $SINGULARITY_ROOTFS/bin_override
	#mkdir -p $SINGULARITY_ROOTFS/work




	## mysql - full install
	# https://dev.mysql.com/downloads/file/?id=495278 - login
	# https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.20-linux-glibc2.12-x86_64.tar.xz
	#wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.20-linux-glibc2.12-x86_64.tar.xz -O /tmp/mysql.tar.xz
	#tar -xf /tmp/mysql.tar.xz -C $SINGULARITY_ROOTFS/bin_override
	#rm /tmp/mysql.tar.xz




%post
	mkdir -p /lib_override
	mkdir -p /bin_override
	
	#yum --enablerepo=extras install -y epel-release
	yum -y install epel-release	
	
	
	
	yum repolist
	#yum install -y wget 
	
	# even with gpgcheck=0, still fails to install?
	#yum install intelpython3 intel-mpi


	#wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
	#sh Miniconda3-latest-Linux-x86_64.sh

	#sh bashrc
	
	# no prompt, no progress bars (-q)
	conda update -y -q conda
	
	conda config --add channels intel
	#conda create -y -n idp intelpython3_full python=3
	conda create -y -n idp intelpython3_core python=3
	
	conda -V

	conda config --set pip_interop_enabled True
	
	## setup conda / pip interop
	#echo $SHELL
	#conda init bash
	#source .bashrc
	#conda activate idp
	##grab the one package we need from pip
	#pip install cpe
	#conda deactivate
	
	conda install -y -n idp -c franzinc agraph-python
	# auto cpe errors because it is python 2.7 only
	#conda install -y -n idp -c auto cpe
	conda install -y -n idp -c anaconda keyring
	conda install -y -n idp -c conda-forge plotly
	conda install -y -n idp -c conda-forge pylint
	conda install -y -n idp -c conda-forge rdflib


	# says bash - but not interactive?
	#echo $SHELL
	## Doesn't work on HPC
	#conda init bash
	#source .bashrc
	. /usr/local/etc/profile.d/conda.sh
	conda activate idp
	#conda config --set pip_interop_enabled True
	#grab the one package we need from pip
	pip install cpe
	conda deactivate
	
	
	#fix some X / DBus issues?
	#dbus-uuidgen > /var/lib/dbus/machine-id


#%setup
#	echo $SHELL
#	conda init bash
#	source .bashrc
#	conda activate idp
#	#conda config --set pip_interop_enabled True
#	#grab the one package we need from pip
#	pip install cpe
#	conda deactivate


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

