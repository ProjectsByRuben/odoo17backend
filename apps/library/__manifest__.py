# -*- coding: utf-8 -*-
{
    'name': "Library",

    'summary': "Library Management",

    'description': """
    Library Management
    """,

    'author': "Praxya Sol",
    'website': "https://www.praxya.com",
    'category': 'Services',
    'version': '0.1',
    'license': 'AGPL-3',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "views/library_book.xml",
        "views/menus.xml",

    ],
}
