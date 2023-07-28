# -*- coding: utf-8 -*-
{
    'name': "Hospital Management",

    'summary': " Hospital Management System ",

    'description': """Hospital Management System""",

    'sequence': -100,

    'author': "Haj Odoo",
    'website': "http://www.haj-odoo.com",

    'category': 'Hospital',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
        'wizard/cancel_appointment_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',

    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
