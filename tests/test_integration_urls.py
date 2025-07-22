import time
import requests


def wait_for_service(url, timeout=30):
    for _ in range(timeout):
        try:
            r = requests.get(url)
            if r.status_code in [200, 302]:
                return True
        except Exception:
            pass
        time.sleep(1)
    return False


def test_admin_url_reachable():
    url = "http://localhost:8000/admin/"
    assert wait_for_service(url), f"{url} nicht erreichbar!"


def test_root_url_reachable():
    url = "http://localhost:8000/"
    assert wait_for_service(url), f"{url} nicht erreichbar!"
