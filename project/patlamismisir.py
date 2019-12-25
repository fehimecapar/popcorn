
import webbrowser
import os
import re

main_page_head = '''
<head>
    <meta charset="UTF-8">
    <title>Patlamış Mısır!</title>

    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color: Teal;
            color: White;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            right: +12px;
            top: +12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: RosyBrown;
            cursor: pointer;
        }
        .movie-tile img {
            box-shadow: 7px 7px 12px #222;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            right: 0;
            background-color: BurlyWood;
        }
    </style>
    <script type="text/javascript" charset="utf-8">

        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {

            $("#trailer-video-container").empty();
        });

        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });

        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>

    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>


    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Patlamış Mısır Film Fragmanları</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''

movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{resim}" width="220" height="342">
    <div>{baslik}</div>
    <div>{aciklama}</div>
</div>
'''


def create_movie_tiles_content(filmler):
    content = ''
    for movie in filmler:
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailerYoutube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+',
                                                         movie.trailerYoutube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        content += movie_tile_content.format(
            resim= movie.resim,
            baslik= movie.baslik,
            aciklama= movie.aciklama,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(filmler):
    output_file = open('patlamismisir.html', 'w')

    rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(filmler))

    output_file.write(main_page_head + rendered_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)