one-line-json
=============

It is used to turn a formated json to One line json

used to turn following

```json
{
    "id": 0,
    "name": "admin",
    "users": [
        {
            "id": 2,
            "name": "guest"
        },
        {
            "id": 3,
            "name": "root"
        }
    ]
}
```
to
```json
"{\"id\":0,\"name\":\"admin\",\"users\":[{\"id\":2,\"name\":\"guest\"},{\"id\":3,\"name\":\"root\"}]}"
```

#### how to use
`command(ctrl)+shift+p` then choose `oneline-JSON`

because it's so simple so i have not submit it to package control, you can install with following

1. Click the Preferences > Browse Packages… menu
2. copy it to the Packages floder

