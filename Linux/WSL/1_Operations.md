# WSL Basic Operations

## Installing WSL on windows (in cmd)
1. Install Ubantu(Default): `wsl --install`
2. Get Linux System List: `wsl --list --online`
3. Install wanted system: `wsl --install Debian`
4. Get installed system: `wsl -l -v`
5. Start the default linux system(with * in front): `wsl`
6. Want to start the specific linux ststem: `wsl -d Debian`
7. Set another linux system as default: `wsl --set-default Debian`

## Operations in wsl(after starting the linnux ststem)
1. Open the explorer: `exeplorer.exe`
2. Open the linux ststem file virtually in windows: can find a file in explorer called `Linux` on the right side or at the top of the explorer, type `\\wsl$` and press enter.
3. Access the files in windows in WSL(for example, Volumn C): `cd /mnt/c`

## Operations in cmd
1. Backup wsl: `wsl --export (linux system) (backup place)`, for example, `wsl --export ubantu C:\users\henry\desktop\backup.tar`
2. Import wsl(Same as import a linux system not on the list): `wsl --import `

