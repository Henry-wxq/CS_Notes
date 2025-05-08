# CS_Notes

## Set Up
### Device: Macbook Pro - M3 Max
### Procedure
1. Install 'Homebrew' by using the command on the official [website](https://brew.sh)
    1. Set the path of 'Homebrew' (copy and paste two lines into the terminal):
    
    `(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/henryw/.zprofile`

    `eval "$(/opt/homebrew/bin/brew shellenv)"`

2. Install Software & IDE
    1. Basic Softwares:
        1. Wechat
        2. Tencent Meeting
        3. QQ
        4. Notion
        5. Zoom
        6. Bilibili
        7. Google Chrome
        8. Youdao Translate
        9. slack
        10. discord
        11. Deepl
      
        `brew install --cask wechat tencent-meeting qq notion zoom bilibili google-chrome youdaodict slack discord deepl`
    2. IDEs
        1. Pycharm
        2. IntelliJ
        3. DataSpell
        4. VScode
        5. Rstudio
        6. Webstorm
        7. ollama
        8. docker
      
        `brew install --cask pycharm intellij-idea dataspell visual-studio-code rstudio webstorm`
        `brew install docker`
3. Enviroment Setting
   1. Git

   `brew install git`  \# Set the user.name, user.email, ssh manually

   2. Anaconda

   `brew install --cask anaconda`

   3. R

   `brew install r`
   
       1. Open VSCode, in Extension, Download R
       2. In Terminal, firstly, type `R`
       3. Secondly, type `R.home("bin")` to get the path of where r binary is
       4. Go to extensions in vscode, find R, at the right corner, Entension Setting, copy the path to it and add `/R`, i.e., `path to R/R`
       5. Go the the left corner of vscode, in the command palettes, type selection, to change the running into `shift + enter`
       6. Radian Download: 
       
5. .gitignore
```
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*
replay_pid*
```

---


Computer Science Note Files of Different Languages including Python, Java, R, LaTeX, Linux, Git, Assembly.......


