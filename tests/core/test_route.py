
from traefik_redirect_manager_core.models import CreateRouteRequest, Resource, Route, RouteChildResources, RouteStatus
from traefik_redirect_manager_core import route as r

route_1 = Route(
    "test-route",
    "test.example.com",
    "some.random.target.com",
    "Test Route",
    status=RouteStatus.ACTIVE,
    resources=RouteChildResources(
        ingress_route=Resource("ingress"),
        tls_credentials_secret=Resource("tls-credentials"),
        certificate=Resource("test-certificate")
    )
)

route_2 = Route(
    "test-route",
    "test.example.com",
    "some.random.target.com",
    "Test Route",
    status=RouteStatus.CREATING,
)

route_3 = Route(
    "test-route",
    "test.example.com",
    "some.random.target.com",
    "Test Route",
    status=RouteStatus.UNKNOWN,
)

route_4 = Route(
    "test-route",
    "test.example.com",
    "some.random.target.com",
    "Test Route",
    status=RouteStatus.REMOVING,
)

def test_has_certificate_guard():
    assert r.has_certificate_guard(route_1)
    assert not r.has_certificate_guard(route_2)


def test_has_tls_credentials_guard():
    assert r.has_tls_credentials_guard(route_1)
    assert not r.has_tls_credentials_guard(route_2)


def test_has_ingress_guard():
    assert r.has_ingress_guard(route_1)
    assert not r.has_ingress_guard(route_2)


def test_is_active_guard():
    assert r.is_active_guard(route_1)
    assert not r.is_active_guard(route_2)
    assert not r.is_active_guard(route_3)
    assert not r.is_active_guard(route_4)


def test_create_route():
    
    request = CreateRouteRequest("Test Route", "test.example.com/hello", "some.random.target.com")

    route = r.create_route(request)

    assert route.display_name == "Test Route"
    assert route.name == "test-route"
    assert route.status == RouteStatus.CREATING
    assert route.source == "test.example.com/hello"
    assert route.target == "some.random.target.com"