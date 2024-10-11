**Disclaimer: This project is for educational purposes only. The techniques demonstrated here should not be used on any devices or systems that you do not own or have explicit permission to access. Unauthorized access, hacking, or attempts to bypass security systems is illegal and unethical. Always respect privacy and the law.**

# PIN Cracking Simulations

This repository contains two Python scripts (`my_pin.py` and `pin_finder.py`) that simulate cracking a 6-digit PIN under different conditions. 

- `my_pin.py` is designed to simulate the process of guessing a correct PIN within 10 attempts.
- `pin_finder.py` simulates an extensive brute-force approach that attempts to find the correct PIN using up to 1 million chances.

## Table of Contents
- [Introduction](#introduction)
- [Files](#files)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [Disclaimer](#disclaimer)

## Introduction

PIN codes are often used to secure devices, and this project explores two different approaches for cracking a 6-digit PIN:
- The first script attempts to guess a random PIN within a limited number of 10 tries.
- The second script simulates a brute-force attack where a random PIN is guessed out of 1 million possible combinations, highlighting the challenges in securing devices using short numeric PINs.

This project is for **educational purposes** only and demonstrates the basic logic behind brute-force attacks. 

## Files

1. **my_pin.py**: 
    - Simulates the process of guessing a 6-digit PIN within 10 attempts.
    - Randomly generates a 6-digit PIN and attempts to guess it within a maximum of 10 tries.
    
    ![my_pin.py output](C:\Users\HP\OneDrive\Drive~diSk #D`\OneDrive\Desktop\pin.png)

2. **pin_finder.py**: 
    - Simulates an exhaustive brute-force attempt to find the correct PIN.
    - Randomly generates a 6-digit PIN and guesses it from 1 million possible combinations.
    
    ![pin_finder.py output](path_to_image/pin_finder_output.png)

## How to Run

### 1. Clone the Repository
To use these scripts, first clone the repository to your local machine using the following command:

```bash
git clone https://github.com/youganshmalik/pin-cracker-challenge.git

### 2. Run the Scripts

To run the 10-attempts simulation:

```bashCopy code
python my_pin.py

To run the brute-force simulation:

```bash

python pin_finder.py
