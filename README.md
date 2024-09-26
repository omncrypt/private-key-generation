# Private key generator

This is example of generating private key from seed phrase for Atom chain.

## Installation

```
# Clone and create Python virtual environment
git clone https://github.com/omncrypt/private-key-generation.git
cd private-key-generation
python3 -m venv venv
source venv/bin/activate

# Install hdwallet
pip install hdwallet Python package

# Change mnemonic and pass phrase
nano private-key.py

# Run script
python private-key.py
```

Copy private key from generated output and import to another wallet.


