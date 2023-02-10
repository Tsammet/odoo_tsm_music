# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

TYPE_PIECE = [
    ('BALADA', 'BALADA'),
    ('NOCTURNE', 'NOCTURNE'),
    ('FUGA', 'FUGA')
]

class TsmPiece(models.Model):
    _name = "tsm.piece"
    _description = "Obra músical"
    _rec_name = 'name'

    name = fields.Char('Nombre de la obra')
    author = fields.Many2one('tsm.music.author', 'Autor')
    duration = fields.Char('Duración')
    type = fields.Selection(TYPE_PIECE, 'Tipo de obra')


MUSIC_PERIOD = [
    ('BARROCO','BARROCO'),
    ('ROMANTICO','ROMANTICO'),
    ('CLASICO','CLASICO'),
    ('CONTEMPORANEO','CONTEMPORANEO')
]

class TsmMusicAuthor(models.Model):
    _name = "tsm.music.author"
    _description = "Autor Musical"
    _rec_name = 'name'

    name = fields.Char('Nombre del Autor')
    country = fields.Many2one('res.country', 'Pais del Autoor')
    period = fields.Selection(MUSIC_PERIOD, 'PERIODO MUSICAL')


class TsmSession(models.Model):
    _name = 'tsm.session'
    _description = 'Sesión de estudio'

    date = fields.Date('Fecha' , default = fields.date.today(), readonly = True)
    playlist_id = fields.Many2one('tsm.playlist', 'Playlist')
    session_items = fields.One2many('tsm.session.line', 'session_id', 'Items de la playlist')

    def load_playlist_button(self):

        data = self.playlist_id.playlist_line

        playlist_line_data = []

        for item in data:
            playlist_line_data.append(
                {
                    'obra' : item.obra,
                    'time' : item.time
                }
            )

        load_playlist = [(0,0,x) for x in playlist_line_data ]
        self.session_items = load_playlist

class TsmSessionLine(models.Model):
    _name = "tsm.session.line"
    _description = "Items de la sesión"
    _rec_name = 'obra'

    obra = fields.Char('Nombre Obra')
    time = fields.Char('Tiempo')
    estudiado = fields.Float('tiempo estudiado')
    session_id = fields.Many2one('tsm.session', 'Items de la sesión')
    



class TsmPlaylist(models.Model):
    _name = 'tsm.playlist'
    _description = 'Playlist'
    _rec_name  = "name"

    name = fields.Char('Nombre de la playlist')
    playlist_line = fields.One2many('tsm.playlist.line', 'playlist_id' ,'items de la playlist')
    session_id = fields.Many2one('tsm.session', 'Sesión')




class TsmPlaylistLine(models.Model):
    _name = 'tsm.playlist.line'
    _description = 'items de la playlist'

    obra = fields.Many2one('tsm.piece', 'Obra a estudiar')
    time = fields.Char('Tiempo de estudio')
    playlist_id = fields.Many2one('tsm.playlist', 'Playlist')




class TsmTypePieceCount(models.Model):
    _name = 'tsm.type.piece.count'
    _description = "Contador Tipos de obras"

    type_piece_count = fields.One2many('tsm.type.piece.count.line', 'piece_count_id' , 'DETALLE')

    def count_genre_button(self):

        genre = [x[0] for x in TYPE_PIECE]

        self.type_piece_count.unlink()

        genre_lines = []

        for g in genre:
            type_music = self.env['tsm.piece'].search([('type', '=', g)])

            if type_music:

                data = {
                    'type_piece' : g,
                    'qty' : len(type_music)
                }
                genre_lines.append(data)

        self.type_piece_count = [(0,0,x) for x in genre_lines]
        
    


class TsmTypePieceCountLine(models.Model):
    _name = 'tsm.type.piece.count.line'
    _description = "Contador Line"

    qty = fields.Integer('Cantidad')
    type_piece = fields.Selection(TYPE_PIECE, 'Tipo Musica')

    piece_count_id = fields.Many2one('type_piece_count')


class TsmCountPiecexAuthor(models.Model):
    _name = "tsm.count.piecex.author"
    _description = "Contador de piezas por author"

    piecex_author_line = fields.One2many('tsm.count.piecex.author.line', 'count_piecexauthor', 'Detalles')


    def count_piece_author_button(self):
        author = self.env['tsm.music.author'].search([])

        self.piecex_author_line.unlink()

        author_music_lines = []

        for a in author:
            pieces = self.env['tsm.piece'].search([('author' , "=", a.id)])
            data = {
                'author_music' : a.id,
                'qty' : len(pieces)
            }
            author_music_lines.append(data)

        self.piecex_author_line = [(0,0,x) for x in author_music_lines]



class TsmCountPiecexAuthorLine(models.Model):
    _name = "tsm.count.piecex.author.line"

    author_music = fields.Many2one('tsm.music.author', 'Autor')
    qty = fields.Integer('Cantidad')

    count_piecexauthor = fields.Many2one('tsm.count.piecex.author')



