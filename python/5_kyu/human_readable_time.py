def make_readable(seconds):
    x = int(seconds%60)
    y = int(((seconds-x)%3600)/60)
    z = int((seconds-((seconds-x)%3600))/3600)
    secs = str(x).zfill(2)
    mins = str(y).zfill(2)
    hrs = str(z).zfill(2)
    return f"{hrs}:{mins}:{secs}"