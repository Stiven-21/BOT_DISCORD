import re

#VALIDAR URL DE YOUTUBE
def Val_url_youtube(url):
    regex = re.compile(
        r'(?:https?://)?'
        r'(?:www\.)?'
        r'(?:youtube\.com|youtu\.be)'
        r'/watch\?v=([^&]+)',
        re.IGNORECASE
    )
    return re.match(regex, url) is not None
