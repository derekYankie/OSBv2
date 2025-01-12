FROM jupyter/base-notebook:hub-1.4.2
USER root


RUN apt-get update
RUN apt-get install graphviz -y
RUN apt-get install openjdk-11-jre-headless -y

RUN apt-get install git vim htop -y      # git and general utilities
RUN apt-get install make cmake libncurses-dev g++ -y  # make etc. to allow NEURON`s nrnivmodl

################################################################################

####  NeuroML etc.

RUN pip install pyneuroml pyelectro --no-cache-dir
RUN pip install git+https://github.com/NeuralEnsemble/neurotune.git --no-cache-dir


####  NEURON & NetPyNE

RUN pip install neuron --no-cache-dir
ENV NEURON_HOME=/opt/conda

# Install specific version of NetPyNE
ENV NETPYNE_CORE_REPO=https://github.com/Neurosim-lab/netpyne
ENV NETPYNE_CORE_BRANCH_TAG=osbv2
RUN git clone --depth=1 $NETPYNE_CORE_REPO -b $NETPYNE_CORE_BRANCH_TAG
RUN cd netpyne ; python setup.py install; cd -


####  Other simulators

# Brian
RUN pip install brian2 brian2tools --no-cache-dir

# Arbor
RUN pip install arbor --no-cache-dir


####  NWB

RUN pip install pynwb ipywidgets --no-cache-dir # nwbwidgets seaborn # v big increase in size...


####  Machine learning libs

RUN pip install torch==1.8.0 --no-cache-dir
RUN pip install git+https://github.com/SheffieldML/GPy.git@devel # for MDF

# For MDF
RUN pip install dask==2.30.0 distributed==2.30.1 protobuf==3.17.0
RUN pip install git+https://github.com/SheffieldML/GPy.git@devel
#RUN pip install modeci_mdf==0.3.3 # big jump in size of image...


####  Octave etc.

#RUN apt-get install octave -y
#RUN pip install octave_kernel --no-cache-dir


################################################################################

COPY hub/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py

RUN chown jovyan /opt
RUN chown -R jovyan /opt/conda  # give user permission to update existing packages


USER jovyan
# sym link workspace pvc to $FOLDER
RUN mkdir -p /opt/workspace
RUN mkdir -p /opt/home
RUN ln -s /opt/workspace workspace

RUN mkdir -p .jupyter/lab
RUN ln -s /opt/workspace .jupyter/lab/workspaces

COPY conf/ .jupyter/lab/user-settings/@jupyterlab

WORKDIR /opt/workspace
