# -*- coding: utf-8 -*-
# IMPORTS
from typing import Dict, List, Union, Tuple, Optional

# LOCAL IMPORTS
from .core import Resource
from .exceptions import WalmartAuthenticationError

class Report(Resource):
  """
  Get report
  """

  path = 'getReport'

  @property
  def available(self):
    url = '/report/reconreport/availableReconFiles'
    return self.connection.send_request(
        method='GET',
        url=self.connection.base_url + url,
    )

  def recon_report(self, date):
    url = '/report/reconreport/reconFile'
    return self.connection.send_request(
        method='GET',
        url=self.connection.base_url + url,
        params={"reportDate": date},
    )

  def get_report(self, type):
    """
    Types:
      - "item"
      - "buybox"
      - "cpa"
      - "shippingProgram"
      - "shippingConfiguration"
      - "itemPerformance"
      - "returnOverrides"
      - "promo"
    """
    return self.connection.send_request(
        method='GET',
        url=self.url,
        params={"type": type},
    )
