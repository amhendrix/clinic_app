#!/bin/bash
python3 -m venv venv
source vnv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Setup complete. To run the app:"
echo "source venv/bin/activate"
echo "python3 app.py"

