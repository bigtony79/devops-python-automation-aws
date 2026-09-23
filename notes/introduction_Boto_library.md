* Automation of maintenance repetitive tasks on AWS such as
  * Doing regular backups
  * Doing regular clean-ups
  * Configuration of existing servers
  * Doing health-checks/monitoring
 
* Boto3 is AWS SDK for Python. There are equivalent libraries in Azure and Googe Cloud.

* Python can also be used for provisioning of infrastructure.

* To install boto3, you can use **pip** package manager and install the package under a virtual environment called **venv**
```
 # Create a virtual environment called .venv
 python -m venv .venv

 # Activate the virtual environment .ven
 source .venv/bin/activate

 # Install boto3 using pip
 pip install boto3
```

* Make sure you have configured AWS CLI to allow boto3 to communicate with AWS by saving the AWS Credentials in the **credentials file** under the .aws folder in your home directory
  ```
    mkidr ~/.aws
    vim ~/.aws/credentials
  ```

* To connect python boto3 project to a non-default region without modifying AWS configuration file, you can pass in the region name as shown below:
```
 ec2_client = boto3.client('ec2, region_name="eu-west-3")
```
This is an example of a named parameter. This tells Python which value is assigned to the parameter. With the use of named parameters, ordering of parameters is not required.

* Difference between boto3.client and boto3.resource
  - client = more low-level API
  - client - provides one to one mapping to underlying HTTP API operations
  - resource = provides resources objects to access attributes and perform actions
  - resource = high-level and object oriented


