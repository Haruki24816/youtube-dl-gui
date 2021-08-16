OPTION_DICT = {

    "mp3(192kbps)": {
        "format": "bestaudio",
        "postprocessors": [{"key":"FFmpegExtractAudio","preferredcodec":"mp3","preferredquality":"192"}]
    },

    "mp3(64kbps)": {
        "format": "bestaudio",
        "postprocessors": [{"key":"FFmpegExtractAudio","preferredcodec":"mp3","preferredquality":"64"}]
    },

    "mp4": {
        "format": "best[ext=mp4]"
    },

    "mp4(最高品質)": {
        "format": "bestvideo+bestaudio",
        "merge_output_format": "mp4"
    }

}
