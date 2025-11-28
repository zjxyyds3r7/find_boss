# from pydub import AudioSegment
# from pydub.playback import play
from fastapi import FastAPI
import pygame
app = FastAPI()

playing = False
def play_audio_with_volume(path, volume_percentage):
    """
    播放音频文件，并在播放时调整音量。
    
    :param path: 音频文件的路径
    :param volume_percentage: 音量大小的百分比（例如：50 表示 50%）
    """

    # 初始化音频模块
    pygame.mixer.init()
    # 加载音频文件
    pygame.mixer.music.load(path)
    # 设置音量
    pygame.mixer.music.set_volume(volume_percentage / 100)
    # 播放音频
    pygame.mixer.music.play()

# 示例用法

play_audio_with_volume("happy.mp3", 100)

@app.get("/warning")
async def root():
    global playing
    if playing:
        return {"message": "Warning is playing"}
    playing = True
    play_audio_with_volume("happy.mp3", 100)
    playing = False
    return {"message": "OK"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)