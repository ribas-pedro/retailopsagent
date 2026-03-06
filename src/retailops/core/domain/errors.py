"""Domain-level custom exceptions."""


class DomainError(Exception):
    """Base exception for domain and core errors."""


class ValidationError(DomainError):
    """Raised when a domain entity violates invariants."""


class UseCaseError(DomainError):
    """Raised when a use case cannot complete."""
