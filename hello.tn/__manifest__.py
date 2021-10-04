# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'hello.tn',
    'version': '2.1',
    'category': 'TUTOS',
    'summary': 'hello.tnhello.tnhello.tn',
    'description': """
This module FOR A TEST UPLOAD ON ODOO
----------------------------------------------------
""",
    'author': 'ghali',
    'depends': [
        'base',
        'iap_mail',
        'mail',
        'phone_validation'
    ],
    'data': [
        'data/ir_cron_data.xml',
        'wizard/sms_cancel_views.xml',
        'wizard/sms_composer_views.xml',
        'wizard/sms_template_preview_views.xml',
        'wizard/sms_resend_views.xml',
        'views/ir_actions_views.xml',
        'views/mail_notification_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'views/assets.xml',
        'views/sms_sms_views.xml',
        'views/sms_template_views.xml',
        'security/ir.model.access.csv',
        'security/sms_security.xml',
    ],
    'demo': [
        'data/sms_demo.xml',
        'data/mail_demo.xml',
    ],
    'qweb': [
        'static/src/bugfix/bugfix.xml',
        'static/src/components/notification_group/notification_group.xml',
        'static/src/components/message/message.xml',
    ],
    'images':['static/img/sms_failure.svg'],
    'installable': True,
    'auto_install': True,
    'license': 'LGPL-3',
}
