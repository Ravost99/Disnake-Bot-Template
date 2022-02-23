
- [ ] Moderations commands
  - [X] [Kick](https://docs.disnake.dev/en/latest/api.html?highlight=kick#disnake.Member.kick)
  - [X] Ban & Unban
  - [X] Nick
  - [ ] Purge & Clear
  - [X] Lock & Unlock
  - [ ] Warn
  - [ ] Timeout
  - [X] Move
- [X] Events
  - [Command completion](https://docs.disnake.dev/en/latest/ext/commands/api.html?highlight=completion#disnake.disnake.ext.commands.on_command_completion)
- [ ] Owner commands
- [ ] Auto Updates

- [ ] Music
  - [ ] Play
  - [ ] Pause
  - [ ] Stop
  - [ ] Join / Leave
  - [ ] YT
  

```py
import urllib

def update():
    stuff_to_update = ['main.py', 'config.py']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen("https://raw.githubusercontent.com/Ravost99/Disnake.py-Bot-Template/master/" + fl).read()
        with open(fl, 'wb') as file:
          file.write(dat)
    print('\n\t\tUpdated Successfull !!!!')
    print('\tRun The Script Again...')
    exit()
```