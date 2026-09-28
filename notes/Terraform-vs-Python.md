* Terraform
  - Manages state of the infrastructure
  - It will know the current state and will determine the difference between current state and your configured/desired state
  - TF is idempotent (multiple executions of the same config file, will always be the same result)
  - Much easier to add/destroy infrastructure
  - More easier and high-level syntax

* Python
  - Does not manage state
  - not idempotent
  - need to explicity write code to destroy resources
  - low level syntax
  
* Why should I use Python Boto3 then?
- With Boto3 you can do more things, because of its low-level API
- More complex logic possible - Python is powerful language.
- It has lots of libraries
- Added Web interface in Python project to run manual tasks

