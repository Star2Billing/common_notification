#
# Common Notification License
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2012 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from django.utils.translation import ugettext_lazy as _
from common.utils import Choice


class NOTICE_COLUMN_NAME(Choice):
    message = _('Message')
    notice_type = _('Notice type')
    sender = _('Sender')
    date_field = _('Date')
