from .settings import PORTAL_URL
from .urls import urlpatterns
import os


def students_proc(request):
    return {'PORTAL_URL' : PORTAL_URL}

# def absoluteStudentsUrl(request):
#     '''Returns absolute site root '''
#     separ = os.sep
#     domen_url_list = request.build_absolute_uri().split(separ)
#     domen_url = domen_url_list[0] + separ + separ + domen_url_list[2]
#     return {'DOMEN_URL': domen_url}

# def pagePathTrue(request):
#     on_homepage = False
#     on_journal = False
#     on_groups = False
#     page_path = request.get_full_path()
#     # print "PAGE_PATH: ", page_path
#     if page_path == '/':
#         on_homepage = True
#     elif page_path == '/groups/':
#         on_groups = True
#     elif page_path == '/journal/':
#         on_journal = True
#     return {'HOMEPAGE': on_homepage,
#         'GROUPS': on_groups,
#         'JOURNAL': on_journal}
