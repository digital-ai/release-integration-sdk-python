# Digital.ai Release SDK

The Digital.ai Release Python SDK (digitalai-release-sdk) is a set of tools that developers can use to create container-based tasks.  

Developers can use the `BaseTask` abstract class as a starting point to define their custom tasks and take advantage of the other methods and attributes provided by the SDK to interact with the task execution environment.

## 📦 Installation

```shell script
pip install digitalai-release-sdk
```
##  🚀 Task Example: hello.py

```python
from digitalai.release.integration import BaseTask

class Hello(BaseTask):
    
    def execute(self) -> None:

        # Get the name from the input
        name = self.input_properties['yourName']
        if not name:
            raise ValueError("The 'yourName' field cannot be empty")

        # Create greeting
        greeting = f"Hello {name}"

        # Add greeting to the task's comment section in the UI
        self.add_comment(greeting)

        # Put greeting in the output of the task
        self.set_output_property('greeting', greeting)

 ```
## 🔁 Upgrading from `digitalai-release-sdk` 24.1.0 or 23.3.0 to 25.1.0

With the release of **digitalai-release-sdk 25.1.0**, the API stubs have been separated into a standalone package. 

👉 [`digitalai-release-api-stubs`](https://pypi.org/project/digitalai-release-api-stubs/)

To upgrade your project, follow these steps:

### Step 1: Install the API Stubs Package

You must explicitly install the new API stubs package:

```bash
pip install digitalai-release-api-stubs==25.1.0
```

Or, add it to your `requirements.txt` as needed.

---

### Step 2: Update Your Code

In previous versions, API clients were created like this:

```python
# Old code (pre-25.1.0)
configuration_api = ConfigurationApi(self.get_default_api_client())
```

In version **25.1.0**, use the following approach:

```python
# New code (25.1.0)

# Create a configuration object
configuration = Configuration(
    host=self.get_release_server_url(),
    username=self.get_task_user().username,
    password=self.get_task_user().password
)

# Instantiate the API client using the configuration
apiclient = ApiClient(configuration)

# Create the Configuration API client
configuration_api = ConfigurationApi(apiclient)
```

This pattern should be used for all API clients, such as `TemplateApi`, `TaskApi`, etc.

---

## Documentation
Read more about Digital.ai Release Python SDK [here](https://digital.ai/)