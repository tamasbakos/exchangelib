from ..util import create_element
from .common import EWSAccountService, EWSPooledMixIn, create_item_ids_element


class MarkAsJunk(EWSAccountService, EWSPooledMixIn):
    """MSDN: https://docs.microsoft.com/en-us/exchange/client-developer/web-service-reference/markasjunk"""
    SERVICE_NAME = 'MarkAsJunk'

    def call(self, items, is_junk, move_item):
        return self._pool_requests(payload_func=self.get_payload, **dict(
            items=items, is_junk=is_junk, move_item=move_item
        ))

    @staticmethod
    def _get_elements_in_container(container):
        from ..properties import MovedItemId
        return container.findall(MovedItemId.response_tag())

    def get_payload(self, items, is_junk, move_item):
        # Takes a list of items and returns either success or raises an error message
        mark_as_junk = create_element(
            'm:%s' % self.SERVICE_NAME,
            attrs=dict(IsJunk='true' if is_junk else 'false', MoveItem='true' if move_item else 'false')
        )
        item_ids = create_item_ids_element(items=items, version=self.account.version)
        mark_as_junk.append(item_ids)
        return mark_as_junk