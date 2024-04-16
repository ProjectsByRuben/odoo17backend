# -*- coding: utf-8 -*-
{
    'name': "Sale Order Custom Report",

    'summary': "Custom report for sales",

    'description': """
    Practice Custom Report for Sales
    """,

    'author': "Praxya Soluciones.",
    'website': "https://www.praxya.com",
    'category': 'Sales',
    'version': '0.1',
    'license': 'AGPL-3',

    'depends': ['sale', 'web'],

    # always loaded
    'data': [
        "report/sale_report_templates.xml",
        "report/sale_report.xml",
    ],
}
