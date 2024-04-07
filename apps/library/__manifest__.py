# -*- coding: utf-8 -*-
{
    'name': "Library",

    'summary': "Library Management",

    'description': """
    Library Management
    """,

    'author': "Praxya Sol.",
    'website': "https://www.praxya.com",
    'category': 'Services',
    'version': '0.9',
    'license': 'AGPL-3',
    'application': True, 

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/library_book.xml",
        "views/library_book_filter.xml",
        "views/library_author.xml",
        "views/library_book_category_views.xml",
        "views/menus.xml",
        "data/stage.xml",
        "data/categories.xml",
    ],
}
