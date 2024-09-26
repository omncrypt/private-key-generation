#!/usr/bin/env python3

from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import AtomMainnet
from typing import Optional

# Mnemonic seed phrase
MNEMONIC: str = 'notice approve worry west select winner flavor fine forget roast yellow thought'

# Secret passphrase/password for mnemonic
PASSPHRASE: Optional[str] = None

# Initialize ATOM mainnet BIP44HDWallet
bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency=AtomMainnet)

# Get Atom BIP44HDWallet from mnemonic
bip44_hdwallet.from_mnemonic(
    mnemonic=MNEMONIC, passphrase=PASSPHRASE
)

# Clean default BIP44 derivation indexes/paths
bip44_hdwallet.clean_derivation()

# Creating custom derivation path. Example of # "m/44'/118'/100'/1/100"
bip44_hdwallet.from_index(44, hardened=True)
# Atom Coin Type. More details on https://pypi.org/project/hdwallet/
bip44_hdwallet.from_index(118, hardened=True)
bip44_hdwallet.from_index(100, hardened=True)
bip44_hdwallet.from_index(1)
bip44_hdwallet.from_index(100)

print(f"{bip44_hdwallet.path()} 0x{bip44_hdwallet.private_key()}")

# Clean derivation indexes/paths
bip44_hdwallet.clean_derivation()
