{
    'name': 'Custom NCM and Brand Fields',
    'version': '16.0.1.0.0',
    'summary': 'Add NCM and Brand fields to sale order lines and customer views.',
    'author': 'Brainess Company',
    'license': 'LGPL-3',
    'depends': ['sale',
                'l10n_br_sale',
                'l10n_br_fiscal',
                'product',
                'product_brand_inventory'],  # Adicione os módulos necessários ,
    'data': [
        'views/sale_order_line_views.xml',  # Já configurado
        # 'views/portal_sale_order_template.xml',  # Portal
        'views/product_search.xml',
        'views/report_sale_order.xml',  # Relatório PDF

    ],
    'installable': True,
    'application': False,
}
