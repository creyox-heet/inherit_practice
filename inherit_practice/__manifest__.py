# -*- coding: utf-8 -*-
# Part of Creyox Technologies.
{
    "name": "Inherit Practice",
    "author": "Creyox Technologies",
    "website": "https://www.creyox.com",
    "support": "support@creyox.com",
    "category": "Sales",
    "summary": "Inherit Practice",
    "license": "OPL-1",
    "version": "17.0.0.1",
    "description": "CR Department Management",
        "depends": ["base","sale","sale_management","stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_report_wiz_view.xml",
        "report/ir_report_action.xml",
        "report/sale_report.xml",
        "report/sale_order_report.xml",
        "views/split_sale_wizard_view.xml",
        "views/sale_order_line_view.xml",
        "views/data_storage_wiz_view.xml",
        "views/inventory_stock_report_wizard_view.xml",

    ],
    "installable": True,
    "application": True,
}
