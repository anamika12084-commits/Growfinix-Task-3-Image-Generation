# Growfinix Task 3 – Automated High-End Image Generation

## Project Overview

This project automates image generation using Python and the Pollinations API. It reads prompts from a text file, generates images automatically, and saves them in the output folder.

## Technologies Used

- Python
- Pollinations API
- aiohttp
- asyncio
- python-dotenv

## Features

- Reads prompts from `prompts.txt`
- Generates images automatically
- Uses asynchronous requests
- Saves generated images in the `output` folder
- Handles API errors

## Project Structure

- `main.py` – Main Python script
- `prompts.txt` – Image prompts
- `requirements.txt` – Required Python packages
- `.gitignore` – Files excluded from GitHub
- `output/` – Generated images

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
