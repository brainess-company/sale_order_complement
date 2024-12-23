from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand_id = fields.Many2one(
        comodel_name='product.brand',
        string='Brand',
        related='product_id.product_tmpl_id.brand_id',
        store=True,
    )

    print("Modelo 'sale.order.line' carregado com sucesso!")


