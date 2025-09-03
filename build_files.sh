#!/bin/bash
echo "Checking Python binaries..."
which python
which python3
echo "Python version output:"
python3 --version

echo "Running collectstatic..."
pip install -r requirements.txt
python3 manage.py collectstatic --noinput