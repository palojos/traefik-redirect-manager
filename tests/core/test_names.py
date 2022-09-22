
from traefik_redirect_manager_core.names import display_name_to_kube_name, add_kube_name_prefix

def test_display_name_to_kube_name():
    assert display_name_to_kube_name("Test") == "test"
    assert display_name_to_kube_name("Hello world") == "hello-world"
    assert display_name_to_kube_name(" HELlo woRld ") == "hello-world"
    assert display_name_to_kube_name("_HelloWorld") == "_helloworld"
    assert display_name_to_kube_name("hello world again") == "hello-world-again"

def test_add_kube_name_prefix():
    assert add_kube_name_prefix("hello-world", "traefik-redirect-manager") == "traefik-redirect-manager-hello-world"
