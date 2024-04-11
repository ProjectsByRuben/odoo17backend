# -*- coding: utf-8 -*-
{
    "name": "Library",
    "summary": "Library Management",
    "description": """
    Library Management
    """,
    "author": "Praxya Soluciones",
    "website": "https://www.praxya.com",
    "category": "Services",
    "version": "1.3",
    "license": "AGPL-3",
    "application": True,
    # any module necessary for this one to work correctly
    "depends": [
        "base",
    ],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "security/groups.xml",
        "views/library_book.xml",
        "views/library_book_filter.xml",
        "views/library_author.xml",
        "views/library_book_category_views.xml",
        "views/library_book_order_views.xml",
        "views/menus.xml",
        "data/stage.xml",
        "data/categories.xml",
    ],
}
