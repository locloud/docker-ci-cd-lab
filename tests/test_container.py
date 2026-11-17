import subprocess
import time
import unittest
import urllib.request


IMAGE = "docker-ci-cd-lab:test"
CONTAINER = "docker-ci-cd-lab-test"
PORT = 8088


class TestDockerContainer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run(
            ["docker", "build", "-t", IMAGE, "."],
            check=True
        )

        subprocess.run(
            [
                "docker", "run", "-d",
                "--name", CONTAINER,
                "-p", f"{PORT}:80",
                IMAGE
            ],
            check=True,
            capture_output=True
        )

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        subprocess.run(
            ["docker", "rm", "-f", CONTAINER],
            check=False,
            capture_output=True
        )

    def test_nginx_returns_http_200(self):
        with urllib.request.urlopen(
            f"http://127.0.0.1:{PORT}"
        ) as response:
            self.assertEqual(response.status, 200)

    def test_nginx_returns_expected_html(self):
        with urllib.request.urlopen(
            f"http://127.0.0.1:{PORT}"
        ) as response:
            html = response.read().decode()

        self.assertIn(
            "<h1>Hello from Docker CI/CD!</h1>",
            html
        )


if __name__ == "__main__":
    unittest.main()
