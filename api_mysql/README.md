#### Generate Secret Key

docker exec projet_sante-app_mysql-1 python secret_key.py

##### add this key in .env

#### Generate Faker

docker exec projet_sante-app_mysql-1 python faker/generate_all_data.py