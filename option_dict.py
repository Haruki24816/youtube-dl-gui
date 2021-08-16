OPTION_DICT = {

    "mp3(192kbps)": {
        "retries": 4,
        "format": "bestaudio",
        "postprocessors": [{"key":"FFmpegExtractAudio","preferredcodec":"mp3","preferredquality":"192"}]
    },

    "mp3(64kbps)": {
        "retries": 4,
        "format": "bestaudio",
        "postprocessors": [{"key":"FFmpegExtractAudio","preferredcodec":"mp3","preferredquality":"64"}]
    },

    "mp4": {
        "retries": 4,
        "format": "best[ext=mp4]"
    },

    "mp4(最高品質)": {
        "retries": 4,
        "format": "bestvideo+bestaudio",
        "merge_output_format": "mp4"
    }

}
