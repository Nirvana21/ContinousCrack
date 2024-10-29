# ContinousCrack

ContinousCrack is a Python implementation of an RSA attack using continued fractions. This project demonstrates how to factor an RSA modulus \( n \) given the public exponent \( e \) using mathematical techniques from number theory.

## Requirements

- Python 3.x
- Libraries:
  - pyyaml
  - sympy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Nirvana21/ContinousCrack.git
   cd ContinousCrack

2. ** Create virtual env **
	python3 -m venv venv
	source venv/bin/activate  

3. ** Install dependencies
	pip install -r requirements.txt

## Usage
	To perform an RSA Wiener attack, place the hexadecimal values of 
	𝑛
	n and 
	𝑒
	e in a YAML configuration file located at data/config.yaml. The format should be:
	n: "<hexadecimal modulus n>"
	e: "<hexadecimal public exponent e>"
	
## Running the Attack
	python src/rsa_attack.py data/config.yaml
