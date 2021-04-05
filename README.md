# Mobiquity
Test cases to vlaidate the email id of the user
Automated Testing Framework for Mobiquity project
This repo contains the framework and tests for automated end-to-end testing of the Mobiquity project deliverables.

Architecture overview and description can be found here here

Setting up the environment
Dependencies :

git
git-lfs
python3
pip
virtualenv
If needed, create your virtualenv

python3 -m venv /path/to/new/repo/venv

Activate your local virtualenv

source /venv/bin/activate

Install the needed python modules (only once)

pip install -r requirements.txt

Start a test session.

a. run the whole test suite : python -m pytest TestCases/

b. run the tests from a single file : python -m pytest TestCases/test_FetchUser.py
