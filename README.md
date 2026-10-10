# NexusBio_II Cheminformatics Sandbox (`nexusbio_II`)

NexusBio_II is an automated cheminformatics and bioinformatics sandbox environment designed for scalable containerised processing. This repository represents an advanced evolution of the original project, featuring a fully automated CI/CD pipeline using GitHub Actions deployed to **Microsoft Azure Container Apps and Azure Container Registry (ACR)**, powered by a local-first AI architecture.

---

## What's New in `nexusbio_II`?

* **Local-First BioGPT Integration**: Replaced external cloud dependencies (such as AWS Bedrock) with Microsoft's open-source `microsoft/biogpt` model for local, secure biomedical literature mining and text generation.


* **Expanded Multi-Agent Intelligence**: Integrates specialised worker nodes for **ADMET toxicity prediction**, **patent/clinical intelligence**, **molecular design**, and **pathway synthesis** under `lambda_orchestrator/agents/`.


* **Robust End-to-End Testing**: Includes comprehensive test suites covering molecular metrics (`test_descriptors.py`), BioGPT initialisation (`test_biogpt.py`), and multi-agent workflow orchestration (`test_orchestrator.py`).



---

## Project Directory Structure

```text
nexusbio_II/
├── .github/
│   └── workflows/
│       └── ci-cd.yml                   # Automated GitHub Actions CI/CD pipeline[cite: 5]
├── cheminformatics_sandbox/
│   ├── utils/                          # Utility scripts (e.g., RDKit descriptors)[cite: 5, 8]
│   ├── Dockerfile                      # Application container definition[cite: 5]
│   ├── Dockerfile.base                 # Base RDKit environment container definition[cite: 5]
│   ├── main.py                         # Core sandbox entrypoint[cite: 5]
│   └── requirements.txt                # Sandbox Python dependencies[cite: 5]
├── frontend/
│   ├── app.py                          # Frontend web service application[cite: 5]
│   ├── Dockerfile                      # Frontend container configuration[cite: 5]
│   └── requirements.txt                # Frontend dependencies[cite: 5]
├── lambda_orchestrator/                # Serverless orchestrator components & agents[cite: 5]
│   ├── agents/                         
│   │   ├── admet_agent.py              # ADMET & toxicity prediction agent[cite: 5, 7]
│   │   ├── literature_miner.py         # Literature and research mining agent[cite: 5]
│   │   ├── molecular_design.py         # Molecular generation and design agent[cite: 5]
│   │   ├── patent_clinical_agent.py    # Patent & clinical trials intelligence agent[cite: 5, 7]
│   │   └── pathway_synthesizer.py      # Biological pathway synthesis agent[cite: 5]
│   ├── handler.py                      # Orchestrator entrypoint[cite: 5]
│   └── requirements.txt                # Orchestrator Python dependencies[cite: 5]
├── tests/                              # Root test suite[cite: 5]
│   ├── test_biogpt.py                  # Local BioGPT model & generation tests[cite: 5, 6]
│   ├── test_descriptors.py             # RDKit molecular metrics tests[cite: 5, 8]
│   └── test_orchestrator.py            # Multi-agent end-to-end pipeline tests[cite: 5, 7]
├── .gitignore
├── docker-compose.yaml                 # Local multi-container orchestration[cite: 5]
├── Dockerfile                          # Root container configuration[cite: 5]
├── README.md
└── requirements.txt                    # Unified project dependencies

```

---

## Architecture & Tech Stack

* **Cloud Provider**: Microsoft Azure (`westus2`)
* **Container Registry**: Azure Container Registry (`nexusbio.azurecr.io`)
* **Infrastructure**: Azure Resource Group (`rg-container-apps`)
* **Core Frameworks**: Python 3.11, PyTorch, Hugging Face Transformers (`BioGPT`), Docker, RDKit, ChEMBL APIs

---

## Multi-Agent Pipeline Components

The multi-agent framework features modular worker nodes designed to handle specific biochemical evaluation tasks:

* **Molecular Design Agent** (`molecular_design.py`): Generates and modifies SMILES structures based on specified design parameters.


* **ADMET & Toxicity Agent** (`admet_agent.py`): Evaluates molecular structures for Lipinski's Rule of Five, physicochemical properties, and toxicity risks.


* **Patent & Clinical Trials Agent** (`patent_clinical_agent.py`): Cross-references compounds with public patent databases and literature sources.


* **Literature Miner Agent** (`literature_miner.py`): Leverages local **BioGPT** (`microsoft/biogpt`) to extract contextual insights and synthesise research text natively.


* **Pathway Synthesiser Agent** (`pathway_synthesizer.py`): Analyses downstream pathway impacts and biological target responses.


* **Orchestration Test Suite** (`test_orchestrator.py`): Validates multi-agent interoperability and end-to-end task chains.



---

## CI/CD Pipeline (`ci-cd.yml`)

The automated pipeline handles two core stages on every push to `main`:

1. **Python Testing (`test-python`)**:
* Sets up Python 3.11 with pip caching.
* Installs standardised dependencies (`torch`, `transformers`, `sacremoses`, `pytest`).
* Runs linting and executes the full root-level test suite (`pytest tests/`).


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
git clone https://github.com/articlesmli/nexusbio.git
cd nexusbio_II

```


2. **Set up a Python virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

```


3. **Run the test suite (including BioGPT verification):**
```bash
PYTHONPATH=. pytest tests/

```


4. **Run the multi-agent orchestrator test:**
```bash
python3 tests/test_orchestrator.py

```



---

## Azure Secrets Configuration

To enable GitHub Actions deployments, configure the following repository secrets under **Settings > Secrets and variables > Actions**:

* `AZURE_CREDENTIALS`: The full JSON service principal authentication block (`clientId`, `clientSecret`, `subscriptionId`, `tenantId`).
* `AZURE_REGISTRY_NAME`: Set to `nexusbio`.