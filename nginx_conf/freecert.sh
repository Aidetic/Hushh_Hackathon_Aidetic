sudo apt-get update
sudo apt-get install certbot
sudo apt-get install python3-certbot-nginx
sudo cp /root/projects/Hushh_Hackathon_Aidetic/nginx_conf/agents.hushh.aidetic.in /etc/nginx/conf.d/agents.hushh.aidetic.in
sudo cp /root/projects/Hushh_Hackathon_Aidetic/nginx_conf/agentsapi.hushh.aidetic.in /etc/nginx/conf.d/agentsapi.hushh.aidetic.in
sudo nginx -t
sudo nginx -s reload
sudo certbot --nginx -d agents.hushh.aidetic.in -d agentsapi.hushh.aidetic.in