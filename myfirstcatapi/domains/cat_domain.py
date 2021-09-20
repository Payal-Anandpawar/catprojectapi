import logging
from typing import Optional

from myfirstcatapi import dto
from myfirstcatapi.libs import dates
from myfirstcatapi.models import cat_model

logger = logging.getLogger(__name__)


async def create_cat(new_cat: dto.UnsavedCat) -> dto.Cat:
    now = dates.get_utcnow()
    return await cat_model.create_cat(new_cat, now=now)


async def find_one(cat_filter: dto.CatFilter) -> Optional[dto.Cat]:
    return await cat_model.find_one(cat_filter=cat_filter)


async def find_many(
    cat_filter: Optional[dto.CatFilter] = None,
    cat_sort_params: Optional[dto.CatSortPredicates] = None,
    page: Optional[dto.Page] = None,
) -> dto.PagedResult[dto.CatSummary]:
    results = await cat_model.find_many(
        cat_filter=cat_filter,
        cat_sort_params=cat_sort_params,
        page=page,
    )
    return results


async def delete_one(cat_id: dto.CatID) -> dto.UpdatedCount:
    return await cat_model.delete_one(cat_id=cat_id)
