import ffmpeg_streaming
from ffmpeg_streaming import Representation


def progress(percentage, line, all_media):
    # You can update a field in your database
    # You can also create a socket connection and show the progress to users
    print("{}% is transcoded".format(percentage))


def create_hls_files(_input, _output, __progress=None):
    rep1 = Representation(width=256, height=144, kilo_bitrate=200)
    rep2 = Representation(width=426, height=240, kilo_bitrate=500)
    rep3 = Representation(width=640, height=360, kilo_bitrate=1000)

    (
        ffmpeg_streaming
            .hls(_input, hls_time=10, hls_allow_cache=1)
            .format('libx264')
            .add_rep(rep1, rep2, rep3)
            .package(_output, __progress)
    )


if __name__ == "__main__":
    _input = '/var/www/media/videos/test.mp4'
    _output = '/var/www/media/videos/dash/test.mpd'
    _progress = progress

    create_hls_files(_input, _output, _progress)