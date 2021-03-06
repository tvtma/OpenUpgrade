# Copyright 2018 Othmane Ghandi <https://github.com/OthmaneGhandi>
# Copyright 2019 TVTMA - David Tran <https://www.tvtmarine.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


def remove_action_window(env):
    """Remove action windows that may cause error: for now action_view_account_move_line_reconcile"""
    openupgrade.logged_query(
        env.cr,
        """DELETE FROM ir_act_window
            WHERE res_model = 'account.move.line.reconcile'
        """)


def enable_digest_kpi(env):
    digest_digest_default = env.ref('digest.digest_digest_default')
    digest_digest_default.write({
        'kpi_account_total_revenue': True
        })


@openupgrade.migrate()
def migrate(env, version):
    remove_action_window(env)
    enable_digest_kpi(env)
