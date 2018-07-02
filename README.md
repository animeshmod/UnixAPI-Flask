# UnixAPI-Flask
Rest API to execute unix commands and get the results.

# Installation
After cloning the repository, create the virtualenv and install requirements.

```sh
$ virtualenv UnixAPI-Flask
$ source UnixAPI-Flask/bin/activate
(UnixAPI-Flask) $ pip install -r requirement.txt
```

# Usage

By default the api will listen on port 5000. The /commands endpoint will provide all the commands the api can execute along with the aid number. Run /commands/aid to execute specific command and get the output.


```sh
$ curl -i http://localhost:5000/commands
```

```sh
{
    "Commands": [
        {
            "aid": 1,
            "command": "DiskSpace",
            "syntax": "df -h"
        },
        {
            "aid": 2,
            "command": "DirectoryList",
            "syntax": "ls -ltr"
        },
        {
            "aid": 3,
            "command": "Processes",
            "syntax": "ps -ef | grep process"
        }
    ]
}
```

