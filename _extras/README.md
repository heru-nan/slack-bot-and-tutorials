## Slack de Bot y Tutoriales

### Comandos importantes

Para construir la imagen, en la carpeta contenedora del archivo **Dockerfile**: 
	`docker build -t bot-app .`

Para ejecutar la imagen: 
	`docker run --rm -e SLACK_TOKEN -e SLACK_EVENTS_TOKEN -p 3000:3000 bot-app`

Tambien es necesario agregar ngrok de manera local.	
