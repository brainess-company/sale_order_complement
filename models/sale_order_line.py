from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    brand_id = fields.Many2one(
        comodel_name='product.brand',
        string='Brand',
        related='product_id.product_tmpl_id.brand_id',
        store=True,
    )

    ncm_id = fields.Many2one(
        comodel_name='l10n_br_fiscal.ncm',
        string='NCM'
    )

    ncm_code = fields.Char(
        related='ncm_id.code',
        string='NCM Cod',
        store=True,
    )


