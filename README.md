# NexusBio II Cheminformatics Sandbox (`nexusbio_II`)

NexusBio_II is an automated cheminformatics and bioinformatics sandbox environment designed for scalable containerised processing. This repository (`nexusbio_II`) represents an advanced evolution of the original `nexusbio` project, featuring a fully automated CI/CD pipeline using GitHub Actions migrated to a pure **Microsoft Azure Container Apps and Azure Container Registry (ACR)** architecture.

---

## What's New in `nexusbio_II`?

While the core multi-agent components from the original project—such as **literature mining**, **molecular design**, and **pathway synthesis**—remain foundational, **`nexusbio_II`** introduces several key architectural and structural upgrades:

- **Expanded Multi-Agent Intelligence**: Builds upon the original workflow by integrating specialised new worker nodes for **ADMET toxicity prediction** and **patent/clinical intelligence** under `lambda_orchestrator/agents/`.
- **Enhanced Orchestration & Testing**: Added comprehensive end-to-end multi-agent orchestration testing (`test_orchestrator.py`) to validate complex cross-agent execution chains.
---

## Project Directory Structure

```text
nexusbio/
├── .github/
│   └── workflows/
│       └── ci-cd.yml                # Automated GitHub Actions CI/CD pipeline
├── cheminformatics_sandbox/
│   ├── tests/                       # Python test suite
│   ├── utils/                       # Utility scripts and helpers
│   ├── Dockerfile                   # Application container definition
│   ├── Dockerfile.base              # Base RDKit environment container definition
│   ├── main.py                      # Core sandbox entrypoint
│   └── requirements.txt             # Python dependencies
├── frontend/
│   ├── app.py                       # Frontend web service application
│   ├── Dockerfile                   # Frontend container configuration
│   └── requirements.txt             # Frontend dependencies
├── lambda_orchestrator/             # Serverless orchestrator components & agents
│   ├── agents/                  
│   │   ├── admet_agent.py           # ADMET & toxicity prediction agent
│   │   ├── literature_miner.py      # Literature and research mining agent
│   │   ├── molecular_design.py      # Molecular generation and design agent
│   │   ├── patent_clinical_agent.py # Patent & clinical trials intelligence agent
│   │   └── pathway_synthesizer.py   # Biological pathway synthesis agent
│   ├── handler.py                   # Orchestrator entrypoint
│   └── requirements.txt             # Orchestrator Python dependencies
├── .gitignore
├── docker-compose.yaml              # Local multi-container orchestration
├── Dockerfile                       # Root container configuration
├── README.md
├── requirements.txt
└── test_orchestrator.py             # Multi-agent orchestration test script

```

---

## Architecture & Tech Stack

* **Cloud Provider**: Microsoft Azure (`westus2`)
* **Container Registry**: Azure Container Registry (`nexusbio.azurecr.io`)
* **Infrastructure**: Azure Resource Group (`rg-container-apps`)
* **Core Frameworks**: Python 3.11, Docker, RDKit, Public Biomedical APIs (ChEMBL)

---

## Multi-Agent Pipeline Components

The multi-agent framework features five specialised modular worker nodes:

* **Molecular Design Agent** (`molecular_design.py`): Generates and modifies SMILES structures based on design parameters.
* **ADMET & Toxicity Agent** (`admet_agent.py`): Evaluates molecular structures for Lipinski's Rule of Five, physicochemical properties, and toxicity risks.


* **Patent & Clinical Trials Agent** (`patent_clinical_agent.py`): Cross-references compounds with public patent databases and literature sources.


* **Literature Miner Agent** (`literature_miner.py`): Extracts contextual text and references from published research.
* **Pathway Synthesiser Agent** (`pathway_synthesizer.py`): Analyses downstream pathway impacts and biological target responses.
* **Orchestration Test Suite** (`test_orchestrator.py`): Validates multi-agent interoperability and end-to-end task chains.



---

## CI/CD Pipeline (`ci-cd.yml`)

The automated pipeline handles two core stages on every push to `main`:

1. **Python Testing (`test-python`)**:
* Sets up Python 3.11 with pip caching.
* Runs linting and executes test scripts across the sandbox modules.


2. **Azure Deployment (`deploy-azure`)**:
* Authenticates securely with Azure using service principal credentials (`AZURE_CREDENTIALS`).
* Logs into **Azure Container Registry** (`nexusbio.azurecr.io`).
* Builds and pushes container images directly to Azure Container Apps.



---

## Getting Started Locally

### Prerequisites

* Python 3.11+
* Docker & WSL (Ubuntu)
* Azure CLI (`az`)

### Local Setup & Testing

1. **Clone the repository:**
```bash
git clone [https://github.com/articlesmli/nexusbio.git](https://github.com/articlesmli/nexusbio.git)
cd nexusbio

```


2. **Set up a Python virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

```


3. **Run the multi-agent orchestrator test:**
```bash
python3 test_orchestrator.py

```



---

## Azure Secrets Configuration

To enable GitHub Actions deployments, configure the following repository secrets under **Settings > Secrets and variables > Actions**:

* `AZURE_CREDENTIALS`: The full JSON service principal authentication block (`clientId`, `clientSecret`, `subscriptionId`, `tenantId`).
* `AZURE_REGISTRY_NAME`: Set to `nexusbio`.

```
