class MyfirstcatapiError(Exception):
    pass


class EventException(MyfirstcatapiError):
    pass


class DuplicateEntityError(MyfirstcatapiError):
    pass


class DuplicateCatError(DuplicateEntityError):
    pass


class EmptyResultsFilter(MyfirstcatapiError):
    pass


class EntityNotFoundError(MyfirstcatapiError):
    pass


class CatNotFoundError(EntityNotFoundError):
    pass
