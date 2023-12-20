#/bin/bash
echo "Make sure to run this as an sudo user"
source venv/bin/activate # We're sourcing our current shell to the virtual environment that was setup by python -m venv venv
# To emulate the same experience: pip install -r requirements.txt
#pip install Flask
#pip install requests
#pip install pymongo
echo "" && echo ""
echo "Lookin' good you're all set to configure port 80 and run \"./run_flask_server.sh\""