###############################################################################################
#
# Luis Felipe Paternina
# Ing.Sistemas                                
# Odoo Dev
#
# E-mail: lfpaternina93@gmail.com 
# Cel: +573215062353
#
# Bogotá,Colombia
#
#
###############################################################################################

{
    'name': 'Introdoo channel',

    'version': '13.1',

    'author': "Luis Felipe Paternina",

    'contributors': ['Luis Felipe Paternina'],

    'website': "",

    'category': 'Test',

    'depends': [

        'purchase',
        'sale_management',
        'base',
    ],

    'data': [
       
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_company.xml',
        'views/res_partner_patient.xml',
        'views/res_partner_town.xml',
        'views/website_form.xml',             
    ],
    'installable': True
}

