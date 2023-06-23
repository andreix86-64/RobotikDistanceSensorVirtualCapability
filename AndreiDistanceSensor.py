import sys
from abc import ABC

from AbstractVirtualCapability import AbstractVirtualCapability, VirtualCapabilityServer


class DistanceSensorVirtualCapability(AbstractVirtualCapability, ABC):
    """ Simple calculator to test virtual capabilities """

    def __init__(self, server):
        super().__init__(server)
        self.current_operation = None
        self.a = None
        self.b = None

    def _result(self, value) -> dict:
        return {"AndreiResult": value}

    def _error(self, message) -> dict:
        return self._result(f"[ERROR] {message}")

    def andrei_measure_distance(self, args: dict):
        try:
            distance = self.invoke_sync("MeasureDistance")["SimpleDoubleParameter"]
            return self._result(distance)
        except Exception:
            return self._error("Could not measure the distance")

    def loop(self):
        pass


if __name__ == "__main__":
    try:
        port = None
        if len(sys.argv[1:]) > 0:
            port = int(sys.argv[1])
        server = VirtualCapabilityServer(port)
        tf = DistanceSensorVirtualCapability(server)
        tf.start()
        while server.running:
            pass
    except KeyboardInterrupt:
        print("[Main] Received KeyboardInterrupt")
