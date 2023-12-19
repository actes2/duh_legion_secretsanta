echo "starting python server first in it's own seperate thread"
sudo DB_USERNAME=$DB_USERNAME DB_PASSWORD=$DB_PASSWORD python ./app/main.py &

sleep 3s

echo "Login to the ssh Tunnel for routing traffic to our database"
echo "monty's password is: $TUNNEL_PASSWORD"
ssh -L 27017:localhost:27017 montymole@actesco.org

sudo pkill "python"
sudo pkill "python"