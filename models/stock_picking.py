from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Agrega el campo para el Plan Analítico
    analytic_plan_id = fields.Many2one('account.analytic.plan', string="Plan Analítico")
    
    # Agrega el campo para la Cuenta Analítica
    analytic_account_id = fields.Many2one('account.analytic.account', string="Cuenta Analítica")