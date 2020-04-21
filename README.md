# OSBv2
An updated version of the Open Source Brain platform


## Deploy

### Prerequisites

The OSB deployment is built on top of [CloudHarness](https://github.com/MetaCell/cloud-harness).
The deployment process is based on Python 3.7+ scripts. It is recommended to setup a virtual 
environment first.

With conda: 
```bash
conda create --name osb python=3.7
conda activate osb
```

To install CloudHarness:

```
git clone https://github.com/MetaCell/cloud-harness.git
cd cloud-harness
pip install -r requirements.txt
```

### Create deployment

CloudHarness scripts script automate the deployment process.

To update the Codefresh deployment, run:

```
harness-codefresh .
```

To manually create the helm chart to use on any Kubernetes deployment, run:

```
harness-deployment .
```
(Run `harness-deployment --help` to know more about parameters)


## Code generation facilities
To refresh your REST applications code with openapi-generate, run

```
harness-generate
```

To create a new application, run 

```
harness-application [APP_NAME]
```


