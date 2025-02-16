import yt_dlp
import os

def download_youtube_as_mp3(video_url, output_folder="downloads_youpy"):
    # Configurações para baixar como MP3
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s', #The output file location
          'ffmpeg_location': 'C:/ffmpeg/bin/ffmpeg.exe' # Pass the path to the ffmpeg executable
    }
    
    try:
        # Cria a pasta de saída se não existir
        os.makedirs(output_folder, exist_ok=True)
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
            print("Download concluído e convertido para MP3!")
    except Exception as e:
        print(f"Erro ao processar o vídeo: {e}")

# Exemplo de uso

# if __name__ == "__main__":
#     while True:
#         video_url = input("Digite a URL: \n")  # Substitua pelo link do vídeo
#         download_youtube_as_mp3(video_url)
