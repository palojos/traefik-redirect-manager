from typing import Any
from .models import CreateRouteRequest, Route, RouteStatus

def has_certificate_guard(route: Route) -> bool:
    """Checks if route has certificate reference"""
    return route.resources.certificate is not None

def has_tls_credentials_guard(route: Route) -> bool:
    """Checks if route has tls_credentials"""
    return route.resources.tls_credentials_secret is not None

def has_ingress_guard(route: Route) -> bool:
    """Checks if route has ingress defined"""
    return route.resources.ingress_route is not None

def is_active_guard(route: Route) -> bool:
    """Checks if route is active, i.e. all required resources are defined"""
    return route.status == RouteStatus.ACTIVE

def create_route(request: CreateRouteRequest) -> Route:
    """Create new route definition from request"""

def create_certificate(route: Route) -> tuple[Route, dict[str, Any]]:
    """Create certificate resource for route"""

def create_ingress(route: Route) -> tuple[Route, dict[str, Any]]:
    """Create ingress resource for route"""

def make_active(route: Route) -> Route:
    """Makes route active and returns updated definition"""

def to_resource(route: Route) -> dict[str, Any]:
    """Maps route into kubernets custom resource"""

def from_resource(resource: dict[str, Any]) -> Route:
    """Maps kubernetes custom resource into route"""

