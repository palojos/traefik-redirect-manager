from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

@dataclass
class CreateRouteRequest:
    """Request to create redirect to target when source is accessed"""
    display_name: str
    source: str
    target: str

@dataclass
class RemoveRouteRequest:
    """Request to remove redirect route"""
    name: str
    

class RouteStatus(Enum):
    """Status of route, only active routes works as expected"""
    UNKNOWN = 0
    CREATING = 1
    ACTIVE = 2
    REMOVING = 3

@dataclass
class Resource:
    """Kubernetes resource, referenced by name as app is operating in single namespace"""
    name: str

@dataclass
class RouteChildResources:
    """Child resources which are required for route to operate"""
    ingress_route: Optional[Resource] = None
    tls_credentials_secret: Optional[Resource] = None
    certificate: Optional[Resource] = None

@dataclass
class Route(Resource):
    """Established route which redirects requests to source into target"""
    source: str
    target: str
    display_name: str
    status: RouteStatus = RouteStatus.UNKNOWN
    resources: RouteChildResources = field(default_factory=RouteChildResources)
