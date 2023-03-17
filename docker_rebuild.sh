#!/bin/bash
imageName=pet_store_image:my-image
containerName=pet_store_container

echo Delete old container...
docker rm -f $containerName

echo Delete old image...
docker image rm -f $imageName

echo Build new image...
docker build -t $imageName -f Dockerfile  .

echo Run new container...
docker run -d -p 8000:8000 --name $containerName $imageName