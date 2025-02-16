# youpy
Youpy youtube Downloader for MP3
![image](https://github.com/user-attachments/assets/c5546675-6f0c-4621-a9fd-e97638901876)


Repositorio do Youpy, ferramenta de download de videos do youtube para MP3, para conseguir rodar o youpy, primeiro você precisa instalar as dependencias com os seguintes comandos:

```pip install -r requirements.txt```

após isso caso você queira rodar diretamente no terminal precisa apenas rodar o comando:

```python screen.py``` ou ```python3 screen.py``` no linux

Para transformar em executavél você precisa compilar com o seguinte comando:

```pyinstaller --onefile screen.py```


## OBS:
para conseguir rodar o programa veja se você possui o ffmpeg instalado no seu sistema operacional:

no windows vá para o CMD e digite:

```ffmpeg -version```

caso haja um output de error acesse o link do ffmpeg:
Recomendo baixar desse link: https://www.gyan.dev/ffmpeg/builds/

após isso precisa apenas adiconar o ffmpeg nas variavéis de ambiente do windows.

