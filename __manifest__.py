# -*- coding: utf-8 -*-
{
    'name': 'MÚSICA',
    'version': '1.0',
    'website': 'https://www.driverp.com',
    'author': 'DrivErp',
    'category': 'Extra Tools',
    'sequence': 50,
    'summary': 'Modulo de Música',
    'depends': ['base'],
    'description': '''
        MÚSICA
    ''',
    'data': [
        'views/tsm_music_menu.xml',
        'views/tsm_piece_views.xml',
        'views/tsm_author_views.xml',
        'views/tsm_session_views.xml',
        'views/tsm_count_piece_music.xml',
        'views/tsm_count_piece_author.xml',
        'views/tsm_playlist_views.xml',
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'test': [],
    'application': True,
}
