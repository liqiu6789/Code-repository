import pyttsx3


def speak_with_properties(text, rate=300, volume=1.0, voice=''):
    # 初始化引擎
    engine = pyttsx3.init()

    # 设置语速 (范围通常在 50-400 之间)
    engine.setProperty('rate', rate)

    # 设置音量 (范围在 0.0-1.0 之间)
    engine.setProperty('volume', volume)

    # 如果有特定的语音设置，设置它
    if voice:
        voices = engine.getProperty('voices')
        for v in voices:
            if v.id == voice:
                engine.setProperty('voice', v)
                break

                # 设置要说的文本
    engine.say(text)

    # 运行并等待直到完成
    engine.runAndWait()


# 使用函数
speak_with_properties("欢迎来到赛博朋克的世界!", rate=120, volume=0.8)