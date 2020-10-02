

# Build

```bash
docker build --tag notifier:latest --output type=tar,dest=notifier.tar .
```

or (for older docker version)

```bash
docker build --tag notifier:latest . && docker save -o notifier.tar notifier:latest
```


# Deploy

```bash
docker load --input notifier.tar
docker run -d -p 5001:5000 -e BOT_API='your-bot-api-key' -e CHAT_ID='your-chat-id' --restart unless-stopped --name notifier notifier
```