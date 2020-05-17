# terriblehack

To run the app:

In on tab do:
```
cd api/

# Activate Python virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Install files to run nltk - natural language toolkit
python download.py
# This should open up a window
# Navigate to 'All Packages' and install punkt, words, wordnet, wordnet_ic 

# Run Flask app to serve the API
flask run
```

In another tab
```
cd /frontend

# To start the React App
yarn start
```

Enjoy!
