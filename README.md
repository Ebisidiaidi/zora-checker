# zora-rewards-checker

A Python script to check Zora rewards eligibility and amounts for a list of Ethereum addresses.  It connects to the Base network, retrieves claim amounts from the Zora Rewards contract, and saves the results to a file.

## Installation

1.  **Prerequisites:**

    *   [Python 3.7+](https://www.python.org/downloads/)
    *   [pip](https://pip.pypa.io/en/stable/installation/) (usually included with Python)

2.  **Clone the repository:**

    ```bash
    git clone https://github.com/Ebisidiaidi/zora-checker.git
    cd zora-rewards-checker
    ```

3.  **Install dependencies:**

    ```bash
    pip install tqdm
    ```

## Usage

1.  **Prepare your addresses:**

    *   Create a file named `address.txt` with one Ethereum address per line.

2.  **Run the script:**

    ```bash
    python main.py
    ```

3.  **View the results:**

    *   The script will create a file named `result.txt` containing the claimable Zora amount for each address.

## Configuration

*   **RPC Endpoint:** The script uses a public RPC endpoint for the Base network.  For better performance and reliability, it is highly recommended to use your own private RPC endpoint.  You can modify the `w3` instantiation in `main.py` to use your preferred endpoint.

    ```python
    # main.py
    w3 = Web3(Web3.HTTPProvider("YOUR_PRIVATE_RPC_ENDPOINT"))
    ```

*   **Contract Address and ABI:** The script uses the Zora Rewards contract address and ABI directly in the code.  If the contract address changes, you will need to update the `contract_address` variable in `main.py`.

## `requirements.txt`

Create a `requirements.txt` file with the following content:
