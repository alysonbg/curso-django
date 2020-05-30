from django.shortcuts import render


def video(request, slug):
    video = {'titulo': 'Video Aperitivo: Motivacão', 'vimeo_id': 423820751}
    return render(request, 'aperitivos/video.html', context={'video': video})
