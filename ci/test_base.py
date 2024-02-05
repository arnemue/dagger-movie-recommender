"""Execute a command."""

import sys

import anyio
import dagger


async def test():
    async with dagger.Connection(dagger.Config(log_output=sys.stderr)) as client:
        src = client.host().directory(".")
        python = (
            client.container()
            # pull container
            .from_("python:3.10-slim-bullseye")
            # mount source directory
            .with_directory("/ws", src)
            # change working directory
            .with_workdir("/ws")
            # install package and test dependencies
            .with_exec(["pip", "install", "-r", "requirements.txt"])
            .with_exec(["pip", "install", ".[test]"])
            .with_exec(["pytest", "tests"])
        )

        print("Starting tests for Python")

        # execute
        await python.sync()

        print("Tests for Python succeeded!")


if __name__ == "__main__":
    anyio.run(test)
