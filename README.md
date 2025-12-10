# Azure Functions Python Template

This is a Python-based Azure Functions project template configured for local development and deployment to Azure.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+** - [Download Python](https://www.python.org/downloads/)
- **Azure Functions Core Tools v4** - [Installation Guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local)
- **Visual Studio Code** - [Download VS Code](https://code.visualstudio.com/)
- **Azure Functions Extension for VS Code** - [Install Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurefunctions)
- **Python Extension for VS Code** - [Install Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### Installing Azure Functions Core Tools

**Windows (using npm):**
```powershell
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

**Windows (using Chocolatey):**
```powershell
choco install azure-functions-core-tools
```

**macOS (using Homebrew):**
```bash
brew tap azure/functions
brew install azure-functions-core-tools@4
```

## 🚀 Getting Started

### 1. Clone or Download the Project

Navigate to the project directory:
```powershell
cd "c:\Users\CharlesLehong.AzureAD\Downloads\AZ FUNC TEMPLATE"
```

### 2. Create a Python Virtual Environment

Create a virtual environment named `.venv`:

**Windows:**
```powershell
python -m venv .venv
```

**macOS/Linux:**
```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

> **Note:** You should see `(.venv)` prefix in your terminal prompt when the virtual environment is activated.

### 4. Install Dependencies

With the virtual environment activated, install the required packages:

```powershell
pip install -r requirements.txt
```

This will install all dependencies including:
- `azure-functions` - Azure Functions runtime
- `pandas` - Data manipulation
- `prophet` - Time series forecasting
- `numpy` - Numerical computing
- `requests` - HTTP library
- `scikit-learn` - Machine learning
- And many more (see `requirements.txt` for full list)

### 5. Configure Local Settings (Optional)

The `local.settings.json` file contains local configuration. You can add environment variables here:

```json
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "",
    "YOUR_CUSTOM_SETTING": "your_value"
  }
}
```

> **Important:** `local.settings.json` is typically not committed to source control as it may contain secrets.

## 🏃 Running the Project

### Method 1: Using VS Code (Recommended)

#### Using the Debug Panel

1. Open the project in VS Code
2. Press `F5` or click **Run > Start Debugging**
3. The Azure Functions runtime will start automatically
4. VS Code will:
   - Install dependencies (if needed)
   - Start the Functions host
   - Attach the debugger

#### Using VS Code Tasks

You can also run tasks manually:

1. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (macOS)
2. Type "Tasks: Run Task"
3. Select one of:
   - **func: host start** - Start the Functions host
   - **pip install (functions)** - Install dependencies

### Method 2: Using Command Line

1. Ensure your virtual environment is activated
2. Run the Functions host:

```powershell
func start
```

### Accessing Your Function

Once running, you'll see output like:

```
Azure Functions Core Tools
Core Tools Version:       4.x.xxxx
Function Runtime Version: 4.x.x.xxxxx

Functions:
        TEST_FUNC: [POST,GET] http://localhost:7071/api/TEST_FUNC
```

You can test the function using:

**Using curl:**
```powershell
curl -X POST http://localhost:7071/api/TEST_FUNC -H "Content-Type: application/json" -d "{\"key\":\"value\"}"
```

**Using PowerShell:**
```powershell
Invoke-RestMethod -Uri "http://localhost:7071/api/TEST_FUNC" -Method POST -Body '{"key":"value"}' -ContentType "application/json"
```

**Using a browser:** Navigate to `http://localhost:7071/api/TEST_FUNC` for GET requests

## 🔧 VS Code Configuration

The `.vscode` folder contains all the configuration needed to run and debug your Azure Functions project in VS Code. Below are the complete contents of each configuration file.

### 1. Extensions (`.vscode/extensions.json`)

This file recommends the required VS Code extensions:

```json
{
  "recommendations": [
    "ms-azuretools.vscode-azurefunctions",
    "ms-python.python"
  ]
}
```

**What it does:** When you open this project in VS Code, you'll be prompted to install these extensions if you don't have them already.

### 2. Settings (`.vscode/settings.json`)

Project-specific settings for Azure Functions:

```json
{
    "azureFunctions.deploySubpath": ".",
    "azureFunctions.scmDoBuildDuringDeployment": true,
    "azureFunctions.pythonVenv": ".venv",
    "azureFunctions.projectLanguage": "Python",
    "azureFunctions.projectRuntime": "~4",
    "debug.internalConsoleOptions": "neverOpen",
    "azureFunctions.projectLanguageModel": 2
}
```

**Key settings explained:**
- `azureFunctions.pythonVenv`: `.venv` - Points to the virtual environment
- `azureFunctions.projectRuntime`: `~4` - Uses Azure Functions v4 runtime
- `azureFunctions.scmDoBuildDuringDeployment`: `true` - Builds on Azure during deployment
- `debug.internalConsoleOptions`: `neverOpen` - Keeps debug console hidden

### 3. Launch Configuration (`.vscode/launch.json`)

Debug configuration for attaching to the Functions runtime:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Attach to Python Functions",
      "type": "debugpy",
      "request": "attach",
      "connect": {
        "host": "localhost",
        "port": 9091
      },
      "preLaunchTask": "func: host start"
    }
  ]
}
```

**What it does:**
- Attaches the debugger to the Python Functions runtime
- Uses port `9091` for debugging
- Automatically runs the `func: host start` task before debugging
- Press **F5** to start debugging with this configuration

### 4. Tasks Configuration (`.vscode/tasks.json`)

Automated tasks for building and running the Functions host:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "type": "func",
      "label": "func: host start",
      "command": "host start",
      "problemMatcher": "$func-python-watch",
      "isBackground": true,
      "dependsOn": "pip install (functions)"
    },
    {
      "label": "pip install (functions)",
      "type": "shell",
      "osx": {
        "command": "${config:azureFunctions.pythonVenv}/bin/python -m pip install -r requirements.txt"
      },
      "windows": {
        "command": "${config:azureFunctions.pythonVenv}\\Scripts\\python -m pip install -r requirements.txt"
      },
      "linux": {
        "command": "${config:azureFunctions.pythonVenv}/bin/python -m pip install -r requirements.txt"
      },
      "problemMatcher": []
    }
  ]
}
```

**Tasks explained:**

1. **func: host start** - Starts the Azure Functions host
   - Runs in the background
   - Automatically depends on the pip install task
   - Uses the Functions problem matcher to detect errors

2. **pip install (functions)** - Installs dependencies from `requirements.txt`
   - Cross-platform support (Windows, macOS, Linux)
   - Uses the Python from your virtual environment
   - Runs automatically before starting the host

**How to use:**
- Press `Ctrl+Shift+P` → "Tasks: Run Task" → Select a task
- Or just press **F5** to run everything automatically

## 📁 Project Structure

```
AZ FUNC TEMPLATE/
├── .venv/                      # Python virtual environment (created by you)
├── .vscode/                    # VS Code configuration
│   ├── extensions.json         # Recommended extensions
│   ├── launch.json             # Debug configuration
│   ├── settings.json           # Project settings
│   └── tasks.json              # Build/run tasks
├── TEST_FUNC/                  # Example HTTP trigger function
│   ├── __init__.py             # Function implementation
│   └── function.json           # Function binding configuration
├── custom_error.py             # Custom error handling
├── data_service.py             # Data service utilities
├── package_installer.py        # Package installation utilities
├── host.json                   # Global Functions host configuration
├── local.settings.json         # Local environment settings
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🧪 Testing Your Functions

### Manual Testing

Use tools like:
- **Postman** - GUI for API testing
- **curl** - Command-line HTTP client
- **Thunder Client** - VS Code extension for API testing

### Example Request

```json
POST http://localhost:7071/api/TEST_FUNC
Content-Type: application/json

{
  "data": "test"
}
```

## 🌐 Deploying to Azure

### Prerequisites for Deployment

1. Azure subscription - [Create free account](https://azure.microsoft.com/free/)
2. Azure CLI installed - [Installation Guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)

### Deploy Using VS Code

1. Click the Azure icon in the sidebar
2. Sign in to your Azure account
3. Click **Deploy to Function App**
4. Follow the prompts to:
   - Select or create a Function App
   - Choose your subscription
   - Select a region
5. VS Code will deploy your function

### Deploy Using Azure CLI

```powershell
# Login to Azure
az login

# Create a resource group
az group create --name myResourceGroup --location eastus

# Create a storage account
az storage account create --name mystorageaccount --location eastus --resource-group myResourceGroup --sku Standard_LRS

# Create a Function App
az functionapp create --resource-group myResourceGroup --consumption-plan-location eastus --runtime python --runtime-version 3.9 --functions-version 4 --name myFunctionApp --storage-account mystorageaccount

# Deploy the function
func azure functionapp publish myFunctionApp
```

## 🐛 Troubleshooting

### Virtual Environment Issues

**Problem:** Virtual environment not activating
- **Solution:** Ensure you're using the correct activation script for your shell
- **Windows PowerShell:** `.venv\Scripts\Activate.ps1`
- **Windows CMD:** `.venv\Scripts\activate.bat`

**Problem:** Execution policy error on Windows
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Dependency Installation Issues

**Problem:** Package installation fails
- **Solution:** Upgrade pip first:
  ```powershell
  python -m pip install --upgrade pip
  ```

### Function Runtime Issues

**Problem:** Functions host won't start
- **Solution:** Check that Azure Functions Core Tools is installed:
  ```powershell
  func --version
  ```

**Problem:** Port 7071 already in use
- **Solution:** Stop other Functions instances or change the port in `host.json`

### Import Errors

**Problem:** Module not found errors
- **Solution:** Ensure virtual environment is activated and dependencies are installed:
  ```powershell
  .venv\Scripts\Activate.ps1
  pip install -r requirements.txt
  ```

## 📚 Additional Resources

- [Azure Functions Python Developer Guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Azure Functions Best Practices](https://learn.microsoft.com/en-us/azure/azure-functions/functions-best-practices)
- [Azure Functions HTTP Triggers](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger)
- [Local Development Guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-develop-local)

## 📝 Notes

- The `.venv` directory should not be committed to source control
- `local.settings.json` contains local-only settings and should not be committed if it contains secrets
- The project uses Azure Functions Runtime v4 with Python
- Dependencies are managed via `requirements.txt`

## 🤝 Contributing

When adding new functions:

1. Create a new folder for your function (e.g., `MY_NEW_FUNC/`)
2. Add `__init__.py` with your function logic
3. Add `function.json` with binding configuration
4. Update `requirements.txt` if you need new dependencies
5. Test locally before deploying

## 📄 License

[Add your license information here]
