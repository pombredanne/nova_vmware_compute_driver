# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 Justin Santa Barbara
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# Import extensions to pull in osapi_compute_extension CONF option used below.
from nova.api.openstack.compute import extensions
from nova.openstack.common import cfg
from nova.openstack.common.log import logging
from nova.tests.integrated import integrated_helpers

CONF = cfg.CONF
CONF.import_opt('osapi_compute_extension', 'nova.config')
LOG = logging.getLogger(__name__)


class ExtensionsTest(integrated_helpers._IntegratedTestBase):
    def _get_flags(self):
        f = super(ExtensionsTest, self)._get_flags()
        f['osapi_compute_extension'] = CONF.osapi_compute_extension[:]
        f['osapi_compute_extension'].append(
            'nova.tests.api.openstack.compute.extensions.'
            'foxinsocks.Foxinsocks')
        return f

    def test_get_foxnsocks(self):
        """Simple check that fox-n-socks works."""
        response = self.api.api_request('/foxnsocks')
        foxnsocks = response.read()
        LOG.debug("foxnsocks: %s" % foxnsocks)
        self.assertEqual('Try to say this Mr. Knox, sir...', foxnsocks)
