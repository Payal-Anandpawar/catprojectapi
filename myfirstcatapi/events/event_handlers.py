import asyncio
import logging
from typing import Callable, Mapping

from myfirstcatapi import dto
from myfirstcatapi.domains import cat_domain
from myfirstcatapi.exceptions import EventException

logger = logging.getLogger(__name__)


def handle_ping(data: dto.JSON) -> None:
    """
    All consumers listen to `ping` event.

    Event payload schema is:

    {
        "event_id": <event correlation id>
    }
    """
    event_id = data.get("event_id")

    logger.info(f"[{event_id}] pong")


def handle_cat_created(data: dto.JSON) -> None:
    event_id = data.get("event_id")
    cat_id = data.get("cat_id")
    required_keys = {"cat_id"}
    cat_id_str = str(cat_id)

    if not all(key in data for key in required_keys):
        exception_message = (
            f"Cannot process event: missing required keys. "
            f"Got: {', '.join(data.keys())}. Expected: {', '.join(required_keys)}"
        )
        logger.exception(f"[{event_id}] {exception_message}")
        raise EventException(exception_message)

    logger.info(f"[{event_id}] Cat {cat_id} has been created")

    # TODO: Handle the async postprocessing of a created Cat here.
    try:
        url = "http://placekitten.com/200/300"
    except ValueError:
        exception_message = f"Cannot process event: invalid partial update. Got: {url}"
        logger.exception(f"[{event_id}] {exception_message}")
        raise EventException(exception_message)

    loop = asyncio.get_event_loop()
    coroutine = cat_domain.update_cat_metadata(cat_id=dto.CatID(cat_id_str), url=dto.CatURL(url))
    loop.run_until_complete(coroutine)


EVENT_HANDLERS: Mapping[str, Callable] = {
    "ping": handle_ping,
    "myfirstcatapi-ping": handle_ping,
    "cat.created": handle_cat_created,
}
