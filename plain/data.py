# -*- coding: utf-8 -*-

# fake database
data = {
    'products': {
        1: {'id': 1, 'name': 'Linterna', 'description': 'Linterna frontal...', 'detail': '300 watts...', 'image': 'http://example.image.com/1'},
        2: {'id': 2, 'name': 'Armario vino', 'description': 'Armario vino lack...', 'detail': '300 x 200...', 'image': 'http://example.image.com/2'},
        3: {'id': 3, 'name': 'Cepillos maquillaje', 'description': 'Set de cepillos maquillaje...', 'detail': '30 piezas...', 'image': 'http://example.image.com/3'},
    },
    'reviews': {
        1: {'id': 1, 'product_id': 1, 'stars': 3, 'title': 'Muy luminosa', 'body': 'Lorem ipsum...', 'user_id': 1},
        2: {'id': 2, 'product_id': 1, 'stars': 1, 'title': 'Se me rompió enseguida', 'body': 'Pinky winky...', 'user_id': 2}
    },
    'users': {
        1: {'id': 1, 'name': 'John Doe', 'email': 'john@doe.com'},
        2: {'id': 2, 'name': 'Gordon Freeman', 'email': 'gordon@freeman.cat'},
    }
}
