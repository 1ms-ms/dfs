#DFS - Docker, Flask, SQLite3
## Docker
```docker run --rm -p 9000:5000 <name_of_the_image>``` 
```docker run -p 9000:5000 -v=$(pwd)/notes.sqlite:/app/notes.sqlite <name_of_the_image>```
## Docker-compose 
Use ```docker-compose build``` and then ```docker-compose up```
